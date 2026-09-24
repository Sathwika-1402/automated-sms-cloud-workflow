# AWS Lambda SMS Testing

## Goal

The goal was to move the working SMS process from a local Python environment to AWS Lambda and test it from the cloud.

---

## Why AWS Lambda?

The first SMS test was run manually from Visual Studio Code.

The local flow was:

**VS Code → Python → Twilio API → SMS → Mobile Phone**

AWS Lambda was then used so the Python code could run in the cloud instead of depending on a local computer.

---

## Step 1: Create Lambda Function

A new AWS Lambda function was created using a Python runtime.

The first test used a simple function:

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello from AWS Lambda!"
    }
```

The function was deployed and tested successfully.

This confirmed that Python code could run in AWS Lambda.

---

## Step 2: Add Twilio Credentials

Twilio credentials were added using AWS Lambda environment variables.

This allowed the function to access the required Twilio account information without hard-coding sensitive values directly in the Python code.

---

## Step 3: Add SMS Logic

The Lambda function was updated to send an SMS through the Twilio API.

The function reads the Twilio credentials, prepares the SMS request, authenticates with Twilio, and sends the message.

---

## Sample Lambda Code

```python
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
```

No real credentials or phone numbers are included in this sample code.

---

## Step 4: Deploy and Test

After updating the Lambda function:

1. The function was deployed.
2. The **Test** option was used to execute the function.
3. AWS Lambda ran the Python code.
4. The Python code called the Twilio API.
5. Twilio processed the request and sent the SMS.

---

## Result

The SMS was successfully received on the test phone.

The cloud flow was:

**AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

---

## Deploy vs Test

During this process, an important difference was learned:

**Deploy** saves and updates the Lambda function code.

**Test** actually runs the Lambda function.

The SMS was only sent after the function was executed using **Test**.

---

## What I Learned

- How to create a Python function in AWS Lambda
- How to test Python code in the cloud
- How to use AWS environment variables
- How Lambda can call an external API
- How Twilio authentication works from AWS
- The difference between deploying and executing a Lambda function
- How to move a working local Python process into the cloud
