#!/usr/bin/env python

# Note: for setting up email with sendmail, see: http://linuxconfig.org/configuring-gmail-as-sendmail-email-relay

import argparse
import commands
import json
import logging
import smtplib
import sys
import os

from datetime import datetime
from os import path
from subprocess import check_output
from distutils.spawn import find_executable
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

EMAIL_TEMPLATE = "%s"

def notify_send_email(body, settings, use_gmail=False):
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

        subject = "Alert: Globaly Entry interview openings are available"
        message = body

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

def main(settings):
    try:
        # obtain the json from the web url
		
	# parse the json
	
	# determine
	# if it's any different than the previous check OR current date check is different
	# if it's the same, exit, we already notified
		
        if not script_output or script_output == 'None':
            logging.info('No tests available.')
            return

    except OSError:
        logging.critical("Something went wrong when trying to obtain the openings")
        return

    if not settings.get('no_email'):
        notify_send_email("", settings, use_gmail=settings.get('use_gmail'))


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
    parser.add_argument('--no-email', action='store_true', dest='no_email', default=False, help='Don\'t send an e-mail when the script runs.')
    parser.add_argument('--use-gmail', action='store_true', dest='use_gmail', default=False, help='Use the gmail SMTP server instead of sendmail.')
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
