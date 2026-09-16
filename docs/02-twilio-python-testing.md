# Twilio Python API Testing

## Goal

The goal of this test was to send an SMS from a Python program using the Twilio API.

---

## Tools Used

- Python 3
- Visual Studio Code
- Twilio Python SDK
- python-dotenv
- Twilio Trial Account

---

## Setup

A Python project was created in Visual Studio Code.

A virtual environment was created to keep the project packages separate from the rest of the system.

Required packages:

```bash
python -m pip install twilio
python -m pip install python-dotenv

Environment Variables

Twilio credentials were stored in a local .env file instead of writing them directly inside the Python code.

Example:

TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_number_here

No real credentials are included in this repository.
