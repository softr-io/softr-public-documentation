# Jotform integration

Connect Jotform with your Softr applications to put your form submissions to work automatically. Build workflows that fire the moment someone submits one of your Jotform forms — then notify your team, create records, and sync the answers wherever they need to go, all without code.

## Overview

The Softr Jotform integration lets you connect your no-code apps with Jotform, the online form builder. When a new submission is received on a form you choose, Softr starts a workflow and hands you the submitted answers — already mapped to human-readable question labels — so you can route the data into the rest of your app and tools.

With Softr, you can turn every Jotform submission into action: save it to a Softr database, send a confirmation email, post a Slack message, create a CRM contact, or kick off any other workflow built on top of the response.

## Available Triggers

### New Submission

Fires when a new submission is received on the Jotform form you select. The trigger payload includes the submission ID, form ID, submitter IP, creation time, and an `answers` object keyed by your form's question labels — including multi-part fields like full name and address, and uploaded file URLs. Softr resolves the field labels and types for the form you pick, so you can reference each answer directly in later workflow steps.

## Key Benefits

- **No-code form automation:** Connect a Jotform form and act on every submission visually in Softr — no webhooks to wire up by hand.
- **Readable answers:** Submitted data arrives keyed by your actual question labels, not cryptic field IDs, so mapping is effortless.
- **Instant reactions:** Workflows fire the moment a form is submitted — no polling, no delay.
- **Works with any form:** Pick any form on your Jotform account, including multi-part fields, file uploads, and multi-select questions.

## Example Use Cases

| Use Case                          | Description                                                                                      |
| :-------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Submissions to a database**     | Save every Jotform response to a Softr database to power a list, portal, or admin dashboard.      |
| **Lead routing to CRM**           | Create or update a contact in HubSpot, Salesforce, or Xero when a lead form is submitted.         |
| **Instant team notifications**    | Post new submissions to a Slack channel or send an email so the right person responds fast.       |
| **Application intake**            | Kick off an onboarding or review workflow whenever an application or registration form comes in.  |
| **File collection**               | Capture uploaded files from a submission and archive their URLs to a database or storage tool.    |
| **Confirmation follow-ups**       | Send a personalized confirmation email to the submitter using the answers from their submission.  |

## How to Connect Softr with Jotform

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the Jotform **New Submission** trigger.
3. Click **Connect Jotform** and paste your Jotform API key. To generate one, sign in to Jotform and go to **Settings → API**, then create a new API key. Select your account region (US/global, EU, or HIPAA) if prompted.
4. Pick the **form** you want to watch for new submissions.
5. Map the submission's answers to the inputs of your downstream actions (database records, emails, Slack messages, and more).
6. Save and activate your workflow — Softr registers the webhook with Jotform automatically.
