# Tally integration

Connect Tally with your Softr applications to put your form submissions to work automatically. Build workflows that fire the moment someone completes one of your Tally forms — then notify your team, create records, and sync the answers wherever they need to go, all without code.

## Overview

The Softr Tally integration lets you connect your no-code apps with Tally, the free-to-use form and survey builder. When a new submission is received on a form you choose, Softr starts a workflow and hands you the submitted answers — so you can route the data into the rest of your app and tools in real time.

With Softr, you can turn every Tally submission into action: save it to a Softr database, send a confirmation email, post a Slack message, create a CRM contact, or kick off any other workflow built on top of the response.

## Available Triggers

### New Submission

Fires when a new submission is received on the Tally form you select. The trigger payload includes a unique event ID you can use to deduplicate submissions, the form ID and name, the response and respondent IDs, the submission timestamp, a link to download the response as a PDF, and an `answers` object keyed by each question's label. Softr resolves the question labels and types for the form you pick — including text, email, phone, link, number, date, rating, single- and multiple-choice, ranking, and file upload answers — and turns multiple-choice selections into their readable labels, so you can reference each answer directly in later workflow steps.

## Key Benefits

- **No-code form automation:** Connect a Tally form and act on every submission visually in Softr — no webhooks to wire up by hand.
- **Instant reactions:** Workflows fire the moment a form is submitted — no polling, no delay.
- **Readable answers:** Multiple-choice and dropdown selections come through as their labels, not internal IDs, so your workflows stay easy to read and map.
- **Works with any form:** Pick any published form on your Tally account, including multiple-choice questions and file uploads.
- **Secure connection:** Authorize once with OAuth — no API keys to copy or rotate.

## Example Use Cases

| Use Case                          | Description                                                                                      |
| :-------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Submissions to a database**     | Save every Tally response to a Softr database to power a list, portal, or admin dashboard.        |
| **Lead routing to CRM**           | Create or update a contact in HubSpot, Salesforce, or Xero when a lead form is submitted.         |
| **Instant team notifications**    | Post new submissions to a Slack channel or send an email so the right person responds fast.       |
| **Application intake**            | Kick off an onboarding or review workflow whenever an application or registration form comes in.  |
| **File collection**               | Capture uploaded files from a submission and archive their URLs to a database or storage tool.    |
| **Confirmation follow-ups**       | Send a personalized confirmation email to the submitter using the answers from their submission.  |

## How to Connect Softr with Tally

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the Tally **New Submission** trigger.
3. Click **Connect Tally** and authorize Softr to access your Tally account.
4. Pick the **form** you want to watch for new submissions.
5. Map the submission's answers to the inputs of your downstream actions (database records, emails, Slack messages, and more).
6. Save and activate your workflow — Softr registers the webhook with Tally automatically.
