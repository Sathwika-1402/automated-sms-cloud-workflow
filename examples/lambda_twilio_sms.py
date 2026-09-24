import os
import urllib.parse
import urllib.request
import base64
import json


def lambda_handler(event, context):

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_number = os.environ.get("TWILIO_PHONE_NUMBER")

    to_number = "+1XXXXXXXXXX"

    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"

    data = urllib.parse.urlencode({
        "From": twilio_number,
        "To": to_number,
        "Body": "sample_message"
    }).encode("utf-8")

    credentials = f"{account_sid}:{auth_token}"

    encoded_credentials = base64.b64encode(
        credentials.encode("utf-8")
    ).decode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        method="POST"
    )

    request.add_header(
        "Authorization",
        f"Basic {encoded_credentials}"
    )

    request.add_header(
        "Content-Type",
        "application/x-www-form-urlencoded"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return {
        "statusCode": 200,
        "body": f"Message sent! SID: {result['sid']}"
    }
