import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv(key="TWILIO_SID")
auth_token = os.getenv(key="TWILIO_AUTH_TOKEN")

def send_message(formatted_msg: str, image_url: str = None):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=formatted_msg,
        to='whatsapp:+255625290997',
        media_url=[image_url]
    )

    return message

# print(message.sid)