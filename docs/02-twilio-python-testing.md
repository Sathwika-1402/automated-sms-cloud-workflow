# Twilio Python API Testing

## Goal

The goal was to send an SMS using Python and the Twilio API.

## Tools Used

- Python
- Visual Studio Code
- Twilio Python SDK
- Twilio Trial Account

## Setup

Installed the required packages:

```bash
python -m pip install twilio
python -m pip install python-dotenv
```

## Environment Variables

Twilio credentials were stored in a `.env` file instead of directly in the Python code.

Example:

```text
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_number_here
```

No real credentials are included in this repository.

## Testing

A Python program was created to connect to Twilio and send an SMS.

The first test failed because the Twilio trial account required a predefined SMS template.

After using an approved trial template, the SMS was successfully sent.

## Result

The test was successful.

**Flow:**

Python → Twilio API → SMS → Mobile Phone

## What I Learned

- How Python connects to Twilio
- How API authentication works
- How to store credentials safely
- How to troubleshoot a Twilio API error
