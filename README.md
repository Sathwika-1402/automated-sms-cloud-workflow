# 📱 Cloud SMS Notification Workflow

## Overview

This project started with a simple business requirement:

**How can a business send text notifications to customers from an application?**

The project was completed in stages:

1. Compare Twilio and AWS SMS
2. Choose Twilio for SMS delivery
3. Test SMS locally using Python
4. Move the Python process to AWS Lambda
5. Test SMS delivery from the cloud
6. Automate Lambda using Amazon EventBridge Scheduler
7. Successfully send SMS without manual execution

---

## 📌 Project Flow

**Business Requirement → Select Twilio → Build Python Integration → Test in VS Code → Move to AWS Lambda → Test in Cloud → Add EventBridge Scheduler → Automated SMS**

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

**AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

The Lambda function was manually executed using the **Test** option in AWS.

This confirmed that the SMS process could run successfully from the cloud.

---

## ⚡ Stage 3: Automating the SMS Workflow

After confirming that the Lambda function worked manually, the next step was to remove the need to click **Test** every time.

Amazon EventBridge Scheduler was used to automatically trigger the Lambda function at a scheduled time.

A one-time schedule was created for the first automation test.

### Automated Flow

**EventBridge Scheduler → AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

When the scheduled time arrived:

- EventBridge automatically triggered Lambda
- Lambda ran the Python code
- Python called the Twilio API
- Twilio sent the SMS
- The message was successfully received on the test phone

No manual Lambda test was required.

This confirmed that the SMS workflow could run automatically from the cloud.

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
- Amazon EventBridge Scheduler
- AWS Environment Variables
- AWS IAM
- GitHub

---

## ✅ Current Project Status

The project has successfully demonstrated:

- Twilio vs AWS SMS comparison
- Cost-conscious testing using a Twilio trial account
- Python integration with Twilio
- Manual SMS testing from Visual Studio Code
- Successful local SMS delivery
- Running Python code in AWS Lambda
- Successful cloud-based SMS delivery
- Creating an EventBridge Scheduler trigger
- Automatically invoking AWS Lambda
- Automatically sending an SMS without manually clicking Test

---

## 📚 What I Learned

Through this project, I gained hands-on experience with:

- Understanding a business messaging requirement
- Comparing SMS providers
- Considering cost before production deployment
- Python programming
- REST API integration
- API authentication
- Twilio SMS
- Troubleshooting API errors
- Environment variables
- AWS Lambda
- AWS IAM permissions
- Amazon EventBridge Scheduler
- Local vs cloud execution
- Event-driven cloud automation
