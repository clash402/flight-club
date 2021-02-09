from twilio.rest import Client
from decouple import config


class NotificationManager:
    def __init__(self):
        pass

    def send_sms(self, message):
        account_sid = config("TWILIO_ACCOUNT_SID")
        auth_token = config("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        sms_message = client.messages.create(
            body=message,
            from_=config("SENDING_PHONE_NUMBER"),
            to=config("RECEIVING_PHONE_NUMBER")
        )

        print(f"{sms_message.status}: Message sent")

    def send_email(self, user):
        print(f"Emailed to {user}")
