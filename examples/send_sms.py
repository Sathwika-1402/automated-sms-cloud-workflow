import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="sample_message",
    from_=twilio_number,
    to="+1XXXXXXXXXX"
)

print("Message sent!")
print("Message SID:", message.sid)
