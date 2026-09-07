---
title: "Zoho CRM"
sidebarTitle: "Zoho CRM"
description: "Connect Zoho CRM with your Softr workflows to create, update, and look up CRM records."
---

# Zoho CRM integration

Connect Zoho CRM with your Softr applications to capture leads, keep contacts current, and move deals forward automatically. Push data from your forms and portals into Zoho CRM, or pull records back into your app — all without writing code.

## Overview

The Softr Zoho CRM integration links your no-code app to your Zoho CRM organization so records stay in sync on both sides. When someone signs up, submits a form, or updates a record in Softr, your workflow can create, update, or look up records in the Leads, Contacts, Accounts, and Deals modules.

Every action works across those four modules and includes your custom fields, so you can build lead capture sites, customer portals, and internal sales tools on top of the CRM your team already uses.

## Available Actions

### Create record

Add a new record to the Leads, Contacts, Accounts, or Deals module. Pick the module, then map values from your Softr form, record, or an earlier workflow step onto the module fields, including custom fields.

### Update record

Change an existing record by ID. Fields you leave out keep their current values, so you can update a single phone number or deal stage without touching the rest of the record.

### Create or update record

Create a record, or update the matching one if it already exists. Zoho matches on each module's own duplicate-check field — Email for Leads and Contacts, Account Name for Accounts, and Deal Name for Deals. Include that field in your values so Zoho can find the match.

### Get record

Retrieve one record by ID with every field the module defines. Use it to show a member their own CRM record, or to read current values before you decide what to do next.

### List records

List records from a module. Zoho requires an explicit field selection, so you choose which fields come back. You can also set the page size (up to 200), sort by any field in ascending or descending order, and page through results with the page token from the previous run.

### Search records

Find records in a module by email, phone, keyword, or a Zoho criteria expression such as `((Last_Name:equals:Doe)and(Company:starts_with:Acme))`. Fill in exactly one of the four search inputs per step, and page through the results by page number.

## Key Benefits

- **No-code CRM automation:** Set up Zoho CRM steps visually in the Softr workflow builder — no developer and no third-party automation tool needed.
- **Works with your custom fields:** Field pickers load live from your Zoho CRM organization, so custom fields are available next to the standard ones.
- **Two-way data flow:** Write new records into Zoho CRM and read existing ones back into your app from the same workflow.
- **No duplicates:** Use Create or update record, or search first, so repeat form submissions update the right record instead of creating a second one.
- **Built for portals:** Give members a branded Softr experience while your team keeps working in Zoho CRM.
- **Multi-step workflows:** Chain Zoho CRM actions with other integrations — post to Slack after a new lead, or send an email after a deal changes.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Lead capture from forms** | When a visitor submits a form in your Softr app, create a Lead in Zoho CRM with their details and source. |
| **Member sign-up sync** | When a new user signs up to your portal, create or update the matching Contact so the CRM always has the current record. |
| **Self-serve customer portal** | Let members view and edit their own Contact record from inside your Softr app. |
| **Deal pipeline updates** | When a status changes in Softr, update the linked Deal so your pipeline stays current. |
| **Duplicate check before outreach** | Search by email or phone before you create a record, then update the existing one instead of adding a copy. |
| **Internal sales dashboard** | List Deals or Accounts from Zoho CRM in a Softr table, and let your team update them without a full CRM seat. |
| **Account enrichment** | Get a record by ID mid-workflow to read current field values, then branch on them in later steps. |

## How to Connect Softr with Zoho CRM

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Zoho CRM action, such as Create record.
3. Click **Connect** and sign in to Zoho to give Softr permission to access your Zoho CRM account.
4. Select the **Module** you want to work with — Leads, Contacts, Accounts, or Deals.
5. Configure the action inputs — map your workflow data to the module fields, or set the record ID, filters, and sorting.
6. Test the step to confirm the data reaches Zoho CRM.
7. Save and activate your workflow.

<Note>
Softr connects to Zoho CRM with OAuth, and your data center is detected automatically. Connect with a Zoho user whose profile can see the modules and fields you plan to use — records and fields that user cannot access do not appear in Softr.
</Note>
