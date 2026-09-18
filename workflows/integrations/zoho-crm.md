---
title: "Zoho CRM"
sidebarTitle: "Zoho CRM"
description: "Connect Zoho CRM with your Softr workflows to create, update, and look up CRM records, and start workflows the moment a record changes."
---

# Zoho CRM integration

Connect Zoho CRM with your Softr applications to capture leads, keep contacts current, and move deals forward automatically. Push data from your forms and portals into Zoho CRM, pull records back into your app, or start a workflow the moment a record is created, updated, or deleted in the CRM — all without writing code.

## Overview

The Softr Zoho CRM integration links your no-code app to your Zoho CRM organization so records stay in sync on both sides. When someone signs up, submits a form, or updates a record in Softr, your workflow can create, update, or look up records in the Leads, Contacts, Accounts, and Deals modules.

Every action works across those four modules and includes your custom fields, so you can build lead capture sites, customer portals, and internal sales tools on top of the CRM your team already uses. Triggers work the other way round: when a record is created, updated, or deleted in one of those modules, Zoho notifies Softr instantly and your workflow runs.

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

Find records in a module with the same condition builder the other look-up actions use. The field list comes from the module's own schema, so your custom fields are there to filter on and a field the module does not have cannot be asked for. Set the page size (up to 200) and page through the results by page number.

Zoho's search is a single flat chain of comparisons, which sets a few limits. One filter uses either **all** or **any**, not both, and holds at most 10 comparisons — "is none of" and conditions on dates each expand to more than one. "Is any of" matches up to 100 values. The conditions that translate are is, is not, starts with, greater or less than (or equal to), is between, is not between, is any of, is all of and is none of; contains, ends with and is empty have no equivalent in Zoho's search. Anything Zoho cannot express is reported before the search runs, naming the condition at fault, and Zoho's own message is shown when it rejects a request.

On date and date-time fields a condition covers whole days, so "is" on a date matches every record from that day rather than one exact timestamp, and relative ranges such as the last 7 days resolve when the workflow runs.

## Available Triggers

Zoho CRM triggers are **Instant**: Zoho notifies Softr as soon as a record changes, and the workflow runs right away. Each trigger watches one module — Leads, Contacts, Accounts, or Deals.

### Record created

Starts a workflow when a record is created in the selected module. The output carries the record ID; chain **Get record** to read its fields.

### Record updated

Starts a workflow when a record in the selected module is edited. The output carries the record ID, the names of the fields that changed, and their new values, so a workflow can branch on what changed without an extra call. Only edits to the record itself count — adding a note or changing a related record does not fire this trigger.

### Record deleted

Starts a workflow when a record is deleted from the selected module. The output carries the ID of the deleted record.

Every trigger run is about a single record. When many records change at once — a bulk edit or an import — Softr starts one workflow run per record. Softr registers the notification with Zoho when you turn the workflow on, keeps it active for as long as the workflow stays on, and removes it when you turn the workflow off.

## Key Benefits

- **No-code CRM automation:** Set up Zoho CRM steps visually in the Softr workflow builder — no developer and no third-party automation tool needed.
- **Works with your custom fields:** Field pickers load live from your Zoho CRM organization, so custom fields are available next to the standard ones.
- **Two-way data flow:** Write new records into Zoho CRM and read existing ones back into your app from the same workflow.
- **Real-time:** Changes in Zoho CRM start your workflows the moment they happen — no polling and no delay.
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
| **Duplicate check before outreach** | Search for a matching record by email, name, or any other field before you create one, then update the existing record instead of adding a copy. |
| **Internal sales dashboard** | List Deals or Accounts from Zoho CRM in a Softr table, and let your team update them without a full CRM seat. |
| **Account enrichment** | Get a record by ID mid-workflow to read current field values, then branch on them in later steps. |
| **React to CRM changes** | When a Lead is created or a Deal is updated in Zoho CRM, notify your team in Slack or update the matching record in your Softr database. |
| **Act on a stage change** | When a Deal is updated, check whether the stage is among the changed fields and start the hand-off workflow only when it is. |
| **Keep your app in sync on deletion** | When a record is deleted in Zoho CRM, remove or archive the matching record in your Softr app. |

## How to Connect Softr with Zoho CRM

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Zoho CRM trigger, such as Record updated, or a Zoho CRM action, such as Create record.
3. Click **Connect** and sign in to Zoho to give Softr permission to access your Zoho CRM account.
4. Select the **Module** you want to work with — Leads, Contacts, Accounts, or Deals.
5. Configure the inputs — for an action, map your workflow data to the module fields, or set the record ID, filters, and sorting.
6. Test the step to confirm the data reaches Zoho CRM, or that a sample record comes back for a trigger.
7. Save and activate your workflow. Activating a workflow with a Zoho CRM trigger registers the notification with Zoho.

<Note>
Softr connects to Zoho CRM with OAuth, and your data center is detected automatically. Connect with a Zoho user whose profile can see the modules and fields you plan to use — records and fields that user cannot access do not appear in Softr. Triggers also need permission to receive notifications from Zoho; if you connected Zoho CRM before triggers were available and a trigger cannot be turned on, reconnect the account.
</Note>
