# Attio integration

Connect Attio with your Softr applications to keep your CRM in sync with everything happening in your app. Capture leads from forms, sync member sign-ups, and keep customer records up to date in Attio — all without code.

## Overview

The Softr Attio integration lets you send data from your no-code apps straight into your Attio workspace. Whenever something happens in your Softr app — a form is submitted, a user signs up, a record changes — your workflow can create or update the matching record in Attio, so your CRM always reflects the latest state of your business.

You choose which Attio object to work with — People, Companies, Deals, or any custom object — and map fields from your Softr forms, records, or previous workflow steps to Attio attributes. Softr automatically picks up your workspace's objects and attributes, including custom ones, so the setup matches your CRM exactly.

## Available Actions

### Create or update record

Add a new record to any Attio object, or update the existing one when a match is found — for example, by email address for people or by domain for companies. No duplicate checks needed: if the record exists, it's updated; if not, it's created.

## Key Benefits

- **No-code CRM automation:** Keep Attio up to date from your Softr app visually, without writing any code or touching an API.
- **No duplicates:** The create-or-update logic matches records by a unique attribute, so the same lead or customer is never added twice.
- **Works with your setup:** Standard and custom objects, custom attributes, selects, and statuses from your workspace all show up automatically.
- **Real-time sync:** Records land in Attio the moment something happens in your app — no manual exports or copy-pasting.

## Example Use Cases

| Use Case                       | Description                                                                                                 |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Lead capture forms**         | Turn every Softr form submission into a person or company record in Attio, enriched with the form answers.  |
| **Member sign-up sync**        | Add new app users to Attio the moment they sign up, so sales and success teams see them right away.         |
| **Client portal updates**      | When a client updates their details in your portal, sync the changes to their Attio record automatically.   |
| **Deal intake**                | Create or update a deal in Attio when a request is submitted through your client-facing intake form.        |
| **Onboarding status tracking** | Update a status attribute in Attio as customers complete onboarding steps inside your Softr app.            |

## How to Connect Softr with Attio

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add an **Attio** action.
3. Click **Connect to Attio** and paste your access token. You can create one in Attio under **Workspace Settings → Developers → Access tokens**.
4. Pick the object you want to work with — People, Companies, Deals, or a custom object — and the matching attribute used to find existing records.
5. Map fields from your Softr forms, records, or previous workflow steps to the record's attributes.
6. Save and activate your workflow.
