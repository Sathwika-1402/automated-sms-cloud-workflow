# Automated SMS Cloud Workflow

## Overview

This project started with a simple business requirement:

**How can a business send automated SMS messages to customers?**

The project began by comparing **Twilio** and **AWS SMS** based on cost, ease of use, scalability, and setup.

After the comparison, **Twilio was selected for the initial SMS implementation** because it was easier to set up, beginner-friendly, and straightforward to integrate with Python.

The project then moved from local Python testing to cloud-based execution using **AWS Lambda**.

---

## Project Journey

1. Compared Twilio and AWS SMS
2. Reviewed pricing, advantages, and disadvantages
3. Selected Twilio for SMS testing
4. Built a Python program using the Twilio API
5. Successfully sent an SMS from a local computer
6. Moved the Python process to AWS Lambda
7. Successfully sent an SMS from the cloud
8. Next step: automate the workflow using an event trigger

---

## Twilio vs AWS SMS

| Feature | Twilio | AWS SMS |
|---|---|---|
| Ease of setup | Easier | More configuration |
| Beginner friendly | Yes | Moderate |
| SMS cost | Usually higher | Can be lower |
| High-volume messaging | Good | Very good |
| Communication features | SMS, Voice, WhatsApp, Verification | AWS-based messaging |
| Best fit | Simple communication integrations | High-volume or AWS-based environments |

### Approximate U.S. SMS Cost

- **Twilio:** around **$0.0118–$0.0133 per SMS**
- **AWS SMS:** around **$0.00883 per SMS** in a common U.S. pricing example

Actual pricing can vary depending on carrier, destination, message length, number type, and usage volume.

---

## Why Twilio Was Selected

Twilio was selected for the first implementation because it provides:

- Simple SMS API integration
- Good documentation
- Easy Python support
- Quick setup for testing
- Support for additional communication services such as Voice, WhatsApp, and Verification

AWS SMS may be more cost-effective at higher volumes, but Twilio was simpler for the initial implementation and testing.

---

## Local Python Implementation

The first version of the project was created using:

- Python
- Visual Studio Code
- Twilio Messaging API
- Twilio Python SDK

The Python application connected to Twilio and successfully sent an SMS to a test phone number.

### Initial Flow

**Python Application → Twilio API → SMS → Mobile Phone**

---

## Twilio Trial Testing

The first implementation used a Twilio trial account.

During testing, the trial account required:

- A verified recipient phone number
- A predefined SMS template

The first test failed because a custom message was used.

After changing to an approved trial template, the SMS was successfully sent.

This was also the first troubleshooting step completed in the project.

---

## Moving the Workflow to AWS

After the local Python test was successful, the next goal was to run the same process in the cloud.

**AWS Lambda** was selected to run the Python code without depending on a local computer.

The Lambda function was first tested with a simple Python response to confirm that the cloud function was working correctly.

After that, the SMS logic was added and connected to Twilio.

---

## Cloud Workflow

The current working flow is:

**AWS Lambda → Python → Twilio API → Mobile Phone**

AWS Lambda runs the Python code in the cloud.

The Python code sends a request to Twilio.

Twilio processes the request and delivers the SMS.

The cloud-based SMS test was completed successfully.

---

## Security

Sensitive credentials are kept separate from the source code.

Authentication tokens, account information, real phone numbers, company information, and other private details are not included in this public repository.

Only sample code and general implementation details are documented.

---

## Current Status

The project can currently:

- Send an SMS using Python
- Connect Python to the Twilio API
- Run Python code using AWS Lambda
- Send an SMS from AWS Lambda through Twilio
- Store credentials separately from the application code

---

## Next Step: Automation

Currently, the Lambda function is manually started using the **Test** option in AWS.

The next phase is to automate the workflow so that Lambda runs when a specific event happens.

Example:

**Customer books an appointment → Event occurs → AWS Lambda runs → Twilio sends SMS**

Other possible triggers could include:

- Appointment confirmation
- Appointment reminder
- Order confirmation
- Shipping update
- Payment confirmation
- Account alert
- Support ticket update

The goal is to remove the need for someone to manually start the Lambda function.

---

## Technologies Used

- Python
- REST API
- Twilio Messaging API
- Twilio Python SDK
- AWS Lambda
- Visual Studio Code
- GitHub

---

## What I Learned

Through this project, I learned:

- How businesses can send automated SMS messages
- How to compare two messaging providers
- How APIs connect applications to external services
- How Python communicates with the Twilio API
- How API authentication works
- How to keep credentials separate from source code
- How to troubleshoot API errors
- How AWS Lambda runs Python code in the cloud
- How a local Python application can be moved to a cloud environment
- How event-based automation can remove manual steps

---

## Future Improvements

- Add an automatic event trigger
- Add error handling
- Track message delivery status
- Test different SMS use cases
- Support multiple recipients
- Compare production costs at different message volumes
