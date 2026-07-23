# Typeform integration

Connect Typeform with your Softr applications to put your form submissions to work automatically. Build workflows that fire the moment someone submits one of your Typeform forms — then notify your team, create records, and sync the answers wherever they need to go, all without code.

## Overview

The Softr Typeform integration lets you connect your no-code apps with Typeform, the online form and survey builder. When a new submission is received on a form you choose, Softr starts a workflow and hands you the submitted answers — so you can route the data into the rest of your app and tools.

With Softr, you can turn every Typeform submission into action: save it to a Softr database, send a confirmation email, post a Slack message, create a CRM contact, or kick off any other workflow built on top of the response.

## Available Triggers

### New Submission

Fires when a new response is received on the Typeform form you select. The trigger payload includes the response token (a unique ID you can use to deduplicate submissions), the submission and landed timestamps, any hidden fields passed to the form, and an `answers` object keyed by each question's title. Softr resolves the question titles and types for the form you pick — including text, email, number, date, yes/no, single- and multiple-choice, and file upload URL answers — so you can reference each answer directly in later workflow steps.

## Key Benefits

- **No-code form automation:** Connect a Typeform form and act on every submission visually in Softr — no webhooks to wire up by hand.
- **Instant reactions:** Workflows fire the moment a form is submitted — no polling, no delay.
- **Works with any form:** Pick any form on your Typeform account, including hidden fields, file uploads, and multiple-choice questions.
- **Secure connection:** Authorize once with OAuth — no API keys to copy or rotate.

## Example Use Cases

| Use Case                          | Description                                                                                      |
| :-------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Submissions to a database**     | Save every Typeform response to a Softr database to power a list, portal, or admin dashboard.     |
| **Lead routing to CRM**           | Create or update a contact in HubSpot, Salesforce, or Xero when a lead form is submitted.         |
| **Instant team notifications**    | Post new submissions to a Slack channel or send an email so the right person responds fast.       |
| **Application intake**            | Kick off an onboarding or review workflow whenever an application or registration form comes in.  |
| **File collection**               | Capture uploaded files from a submission and archive their URLs to a database or storage tool.    |
| **Confirmation follow-ups**       | Send a personalized confirmation email to the submitter using the answers from their submission.  |

## How to Connect Softr with Typeform

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the Typeform **New Submission** trigger.
3. Click **Connect Typeform** and authorize Softr to access your Typeform account.
4. Pick the **form** you want to watch for new submissions.
5. Map the submission's answers to the inputs of your downstream actions (database records, emails, Slack messages, and more).
6. Save and activate your workflow — Softr registers the webhook with Typeform automatically.
