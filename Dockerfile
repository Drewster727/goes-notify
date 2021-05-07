FROM python:2.7.16-alpine
RUN pip install requests twilio
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "goes-notify.py", "--config=/app/config.json"]