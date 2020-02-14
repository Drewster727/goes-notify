#!/usr/bin/env python

# Note: for setting up email with sendmail, see: http://linuxconfig.org/configuring-gmail-as-sendmail-email-relay

import argparse
import commands
import json
import logging
import smtplib
import sys
import os
import glob
import requests
import hashlib

from datetime import datetime
from os import path
from subprocess import check_output
from distutils.spawn import find_executable
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from math import log

EMAIL_TEMPLATE = """
<p>Good news! New Global Entry appointment(s) available on the following dates:</p>
%s
<p>Your current appointment is on %s</p>
<p>If this sounds good, please sign in to https://ttp.cbp.dhs.gov/ to reschedule.</p>
"""
GOES_URL_FORMAT = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=3&locationId={0}&minimum=1'

def notify_send_email(dates, current_apt, settings, use_gmail=False):
    sender = settings.get('email_from')
    recipient = settings.get('email_to', sender)  # If recipient isn't provided, send to self.

    try:
        if use_gmail:
            password = settings.get('gmail_password')
            if not password:
                logging.warning('Trying to send from gmail, but password was not provided.')
                return
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
        else:
            username = settings.get('email_username').encode('utf-8')
            password = settings.get('email_password').encode('utf-8')
            server = smtplib.SMTP(settings.get('email_server'), settings.get('email_port'))
            server.ehlo()
            server.starttls()
            server.ehlo()
            if username:
                    server.login(username, password)

        subject = "Alert: Global Entry interview openings are available"

        dateshtml = '<ul>'
        for d in dates:
            dateshtml += "<li>" + d + "</li>"

        dateshtml += "</ul>"

        message = EMAIL_TEMPLATE % (dateshtml, current_apt.strftime('%B %d, %Y'))

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ','.join(recipient)
        msg['mime-version'] = "1.0"
        msg['content-type'] = "text/html"
        msg.attach(MIMEText(message, 'html'))

        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
    except Exception:
        logging.exception('Failed to send succcess e-mail.')
        log(e)

def notify_osx(msg):
    commands.getstatusoutput("osascript -e 'display notification \"%s\" with title \"Global Entry Notifier\"'" % msg)

def notify_sms(settings, dates):
    for avail_apt in dates: 
        try:
            from twilio.rest import Client
        except ImportError:
            logging.warning('Trying to send SMS, but TwilioRestClient not installed. Try \'pip install twilio\'')
            return

        try:
            account_sid = settings['twilio_account_sid']
            auth_token = settings['twilio_auth_token']
            from_number = settings['twilio_from_number']
            to_number = settings['twilio_to_number']
            assert account_sid and auth_token and from_number and to_number
        except (KeyError, AssertionError):
            logging.warning('Trying to send SMS, but one of the required Twilio settings is missing or empty')
            return

        # Twilio logs annoyingly, silence that
        logging.getLogger('twilio').setLevel(logging.WARNING)
        client = Client(account_sid, auth_token)
        body = 'New GOES appointment available on %s' % avail_apt
        logging.info('Sending SMS.')
        client.messages.create(body=body, to=to_number, from_=from_number)

def main(settings):
    try:
        # obtain the json from the web url
        data = requests.get(GOES_URL_FORMAT.format(settings['enrollment_location_id'])).json()

    	# parse the json
        if not data:
            logging.info('No tests available.')
            return

        current_apt = datetime.strptime(settings['current_interview_date_str'], '%B %d, %Y')
        dates = []
        for o in data:
            if o['active']:
                dt = o['startTimestamp'] #2017-12-22T15:15
                dtp = datetime.strptime(dt, '%Y-%m-%dT%H:%M')
                if current_apt > dtp:
                    dates.append(dtp.strftime('%A, %B %d @ %I:%M%p'))

        if not dates:
            return

        hash = hashlib.md5(''.join(dates) + current_apt.strftime('%B %d, %Y @ %I:%M%p')).hexdigest()
        fn = "goes-notify_{0}.txt".format(hash)
        if settings.get('no_spamming') and os.path.exists(fn):
            return
        else:
            for f in glob.glob("goes-notify_*.txt"):
                os.remove(f)
            f = open(fn,"w")
            f.close()

    except OSError:
        logging.critical("Something went wrong when trying to obtain the openings")
        return

    msg = 'Found new appointment(s) in location %s on %s (current is on %s)!' % (settings.get("enrollment_location_id"), dates[0], current_apt.strftime('%B %d, %Y @ %I:%M%p'))
    logging.info(msg + (' Sending email.' if not settings.get('no_email') else ' Not sending email.'))

    if settings.get('notify_osx'):
        notify_osx(msg)
    if not settings.get('no_email'):
        notify_send_email(dates, current_apt, settings, use_gmail=settings.get('use_gmail'))
    if settings.get('twilio_account_sid'):
        notify_sms(settings, dates)

def _check_settings(config):
    required_settings = (
        'current_interview_date_str',
        'enrollment_location_id'
    )

    for setting in required_settings:
        if not config.get(setting):
            raise ValueError('Missing setting %s in config.json file.' % setting)

    if config.get('no_email') == False and not config.get('email_from'): # email_to is not required; will default to email_from if not set
        raise ValueError('email_to and email_from required for sending email. (Run with --no-email or no_email=True to disable email.)')

    if config.get('use_gmail') and not config.get('gmail_password'):
        raise ValueError('gmail_password not found in config but is required when running with use_gmail option')

if __name__ == '__main__':

    # Configure Basic Logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s: %(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        stream=sys.stdout,
    )

    pwd = path.dirname(sys.argv[0])

    # Parse Arguments
    parser = argparse.ArgumentParser(description="Command line script to check for goes openings.")
    parser.add_argument('--config', dest='configfile', default='%s/config.json' % pwd, help='Config file to use (default is config.json)')
    arguments = vars(parser.parse_args())
    logging.info("config file is:" + arguments['configfile'])
    # Load Settings
    try:
        with open(arguments['configfile']) as json_file:
            settings = json.load(json_file)

            # merge args into settings IF they're True
            for key, val in arguments.iteritems():
                if not arguments.get(key): continue
                settings[key] = val

            settings['configfile'] = arguments['configfile']
            _check_settings(settings)
    except Exception as e:
        logging.error('Error loading settings from config.json file: %s' % e)
        sys.exit()

    # Configure File Logging
    if settings.get('logfile'):
        handler = logging.FileHandler('%s/%s' % (pwd, settings.get('logfile')))
        handler.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s %(message)s'))
        handler.setLevel(logging.DEBUG)
        logging.getLogger('').addHandler(handler)

    logging.debug('Running cron with arguments: %s' % arguments)

    main(settings)
