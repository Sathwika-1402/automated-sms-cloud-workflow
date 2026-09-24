# 📱 Cloud SMS Notification Workflow

## Overview

This project started with a simple business requirement:

**How can a business send text notifications to customers from an application?**

The project was completed in stages:

1. Compare Twilio and AWS SMS
2. Choose an SMS provider
3. Test SMS locally using Python
4. Move the Python process to AWS Lambda
5. Test SMS delivery from the cloud

---

## 📌 Project Flow

**Business SMS Requirement**
↓
**Compare Twilio and AWS SMS**
↓
**Select Twilio for SMS Delivery**
↓
**Test with Twilio Trial**
↓
**Build Python Integration**
↓
**Test Manually from VS Code**
↓
**Move Python Process to AWS Lambda**
↓
**Test Manually from AWS Cloud**

---

## 🔍 Twilio vs AWS SMS

The first step was deciding which service should be used to send SMS messages.

| Feature | Twilio | AWS SMS |
|---|---|---|
| Ease of setup | Easier | More configuration |
| Beginner friendly | Yes | Moderate |
| SMS cost | Usually higher | Can be lower |
| High-volume messaging | Good | Very good |
| Communication features | SMS, Voice, WhatsApp, Verification | AWS-based messaging |
| Best fit | Quick communication integrations | High-volume or AWS-based systems |

### Approximate U.S. SMS Cost

- **Twilio:** approximately **$0.0118–$0.0133 per SMS**
- **AWS SMS:** approximately **$0.00883 per SMS** in a common U.S. pricing example

Actual pricing can vary depending on carrier, destination, number type, message length, and usage volume.

---

## ✅ Why Twilio Was Selected

Twilio was selected for the initial SMS implementation because it offered:

- Simple setup
- Easy-to-understand documentation
- Python support
- Straightforward API integration
- Quick testing
- Additional communication services such as Voice, WhatsApp, and Verification

AWS SMS may offer lower costs at higher volumes, but Twilio provided a simpler starting point for development and testing.

---

## 💰 Cost-Conscious Testing Approach

Before purchasing credits or moving to a production setup, the integration was first tested using a **Twilio trial account and trial phone number**.

This allowed the basic workflow to be validated before spending money on production usage.

The trial was used to confirm that:

- Python could connect to Twilio
- Authentication worked
- SMS requests were processed
- Messages could reach a test phone
- The overall workflow worked correctly

The trial account had some limitations, such as verified recipient numbers and predefined message templates, but it was sufficient for basic testing.

---

## 🐍 Stage 1: Local Python Testing

The first working version was built locally using:

- Python
- Visual Studio Code
- Twilio Messaging API
- Twilio Python SDK

A Python program was created to connect to Twilio and send an SMS.

The program was manually started from Visual Studio Code.

### Local Testing Flow

**VS Code → Python → Twilio API → SMS → Mobile Phone**

This confirmed that the Python application could successfully communicate with Twilio and send a message.

---

## 🧪 Trial Testing and Troubleshooting

The first SMS test failed because the Twilio trial account did not allow a custom message.

The trial account required a predefined SMS template.

After changing the message to an approved trial template, the SMS was successfully sent and received.

This was the first troubleshooting step completed during the project.

---

## ☁️ Stage 2: Moving the Process to AWS Lambda

After the local Python test worked, the next goal was to run the same process from the cloud instead of depending on a local computer.

AWS Lambda was used for this purpose.

### Why AWS Lambda?

Twilio and AWS Lambda have different roles:

- **AWS Lambda runs the Python code**
- **Twilio sends the SMS**

This allows the Python process to run in the cloud instead of only on a developer's computer.

---

## 🧪 Testing AWS Lambda

Before connecting Twilio, a simple Python Lambda function was created and tested.

The function returned:

```text
Hello from AWS Lambda!
```
This confirmed that Python code could run successfully in AWS.

After that:

- Twilio credentials were stored using AWS environment variables
- The SMS logic was added to the Lambda function
- The function was deployed
- The function was manually tested from AWS

The SMS was successfully received on the test phone.

---

## ☁️ Cloud Testing Flow

The current working cloud flow is:

**AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

The Lambda function was manually executed using the **Test** option in AWS.

This confirmed that the SMS process could run successfully from the cloud.

---

## 🔐 Security

Sensitive information is kept separate from the public source code.

The repository does not contain:

- Authentication tokens
- Real Account SID values
- Real phone numbers
- Company information
- Customer information

Only sample code and general implementation details are included.

---

## 🛠 Technologies Used

- Python
- Visual Studio Code
- REST APIs
- Twilio Messaging API
- Twilio Python SDK
- AWS Lambda
- AWS Environment Variables
- GitHub
