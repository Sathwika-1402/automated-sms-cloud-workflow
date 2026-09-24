# SMS Automation with Amazon EventBridge Scheduler

## Goal

The AWS Lambda SMS function was working successfully, but it still had to be started manually using the **Test** button.

The goal of this stage was to automate the process.

---

## Before Automation

The workflow required manual execution:

**Click Test → AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

---

## Automation Setup

Amazon EventBridge Scheduler was used to automatically trigger the Lambda function.

For the first test, a **one-time schedule** was created.

The schedule used the **America/Chicago** time zone.

An empty JSON payload was used:

```json
{}
```

The Lambda function did not require additional input for this test.

---

## Execution Role

EventBridge Scheduler needs permission to run the Lambda function.

A new execution role was created so EventBridge could invoke the Lambda function automatically.

In simple terms:

**EventBridge Scheduler → Permission Role → AWS Lambda**

---

## Automated Flow

**EventBridge Scheduler → AWS Lambda → Python → Twilio API → SMS → Mobile Phone**

---

## Testing

A one-time schedule was created a few minutes in the future.

After creating the schedule, the Lambda **Test** button was not used.

At the scheduled time:

- EventBridge automatically triggered Lambda
- Lambda ran the Python code
- Python called the Twilio API
- Twilio sent the SMS
- The SMS was successfully received

---

## Result

The automation test was successful.

The project progressed from:

**Manual Local Test → Manual Cloud Test → Automated Cloud Test**

This confirmed that AWS could automatically run the SMS workflow without manual execution.

---

## Key Learning

This stage showed the difference between manual execution and automated execution.

**Manual execution:** a person starts the process.

**Automated execution:** an event starts the process automatically.

Amazon EventBridge Scheduler acted as the trigger that automatically started the AWS Lambda function.
