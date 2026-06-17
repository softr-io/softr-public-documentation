# DocuSign integration

Connect DocuSign with your Softr applications to automate your e-signature process end to end — send documents and templates for signature the moment something happens in your app, look up the status of an envelope on demand, cancel agreements that are no longer needed, and react instantly when a document is signed or declined. Build contract, onboarding, and approval workflows on top of live signature data, all without code.

## Overview

The Softr DocuSign integration lets you connect your no-code apps with your DocuSign account. Create envelopes from a document or a DocuSign template, send them for signature, void agreements, and fetch envelopes, recipients, and the data signers entered into form fields — all driven by the forms, sign-ups, and record actions you already build with in Softr. Every action returns the envelope or its details so you can use them in any downstream workflow step.

With Softr, you can turn a form submission into a signature request, send a contract automatically when a deal is marked won, surface the status of pending agreements in a member portal, and kick off follow-up automations the moment an envelope is completed or declined — keeping your app and your signing process in sync.

## Available Actions

### Create envelope

Create an envelope from a document you provide (via a file URL), add a signer and a signature field, and optionally send it for signature right away. Use it to turn a generated document or an uploaded file into a signature request without leaving Softr.

### Create envelope from template

Create and send an envelope from an existing DocuSign template — assign a recipient to a template role and pre-fill the template's merge fields with values from your app. Ideal for standardized contracts, NDAs, and agreements you send repeatedly.

### Send envelope

Send a draft (created-but-not-yet-sent) envelope to its recipients, for example after a review or approval step has passed in your workflow.

### Void envelope

Cancel an envelope with a reason, for instance when an agreement is superseded, a deal falls through, or the wrong document was sent.

### Get envelope

Fetch a single envelope by ID — including its recipients and documents — to read its status and details in a later workflow step or surface them inside Softr.

### List envelopes

Retrieve a page of envelopes filtered by date range, status, or search text — to show in a list block, sync to a Softr database, or loop over in a workflow.

### Get envelope recipients

Fetch the recipients of an envelope along with their signing status and routing order, so you can see who has signed and who is still pending.

### Get envelope form data

Fetch the data signers entered into an envelope's form fields, ready to save to a Softr database, route into another tool, or use in a follow-up step.

## Available Triggers

### Envelope event

Fires when an envelope or recipient reaches a key milestone in DocuSign. Choose which event to listen to — or react to all of them:

- **Envelope completed** — every recipient has signed and the envelope is complete.
- **Envelope declined** — a recipient declined to sign and the envelope is declined.
- **Recipient completed** — an individual recipient finished signing.
- **Recipient declined** — an individual recipient declined to sign.

The trigger hands you the envelope's details — status, subject, sender, recipients, documents, and key timestamps — so you can update records, notify your team, or start a follow-up workflow the moment the event happens.

## Key Benefits

- **No-code e-signatures:** Send documents for signature and react to signing events from your Softr app — no API setup, no scripts.
- **Two-way automation:** Push envelopes into DocuSign and react to completed or declined events coming back out, so your app and your agreements stay aligned.
- **Templates and merge fields:** Send standardized agreements from DocuSign templates with fields pre-filled from your Softr data.
- **Live signature status in your app:** Pull envelopes, recipients, and form data into list and detail blocks to build contract and onboarding dashboards.
- **End-to-end workflows:** Tie signing to the rest of your app — provision access, update records, send emails, and notify your team in the same workflow.

## Example Use Cases

| Use Case                          | Description                                                                                       |
| :-------------------------------- | :------------------------------------------------------------------------------------------------ |
| **Contract on deal won**          | Send an agreement from a DocuSign template when a deal is marked won, with the client's details pre-filled. |
| **Form to signature request**     | Turn a Softr form submission into an envelope and send it to the submitter for signature automatically. |
| **Onboarding paperwork**          | Send NDAs or onboarding documents when a new member signs up, then unlock access once they're signed. |
| **Signing status portal**         | Use **List envelopes** and **Get envelope recipients** to show members and admins which agreements are pending or complete. |
| **Auto-update on completion**     | Trigger on **Envelope completed** to mark a record as signed, store the form data, and notify your team. |
| **Cancel stale agreements**       | Void envelopes that are no longer valid from a Softr admin view when a deal falls through or terms change. |

## How to Connect Softr with DocuSign

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a DocuSign action (or the **Envelope event** trigger).
3. Click **Connect to DocuSign** and sign in with your DocuSign account, then review and authorize the requested permissions.
4. Pick the operation you need — create an envelope, send it, void it, list envelopes, and so on.
5. For template-based sends, choose the **template**, assign the **role**, and map your data to the template's merge fields.
6. Map fields from your Softr forms, records, or previous workflow steps to the action's inputs (such as signer email and name, document, or envelope ID).
7. Save and activate your workflow.
