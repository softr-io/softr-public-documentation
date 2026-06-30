# Attio integration

Connect Attio with your Softr applications to keep your CRM in sync with everything happening in your app — and to react instantly when something changes in Attio. Capture leads from forms, sync member sign-ups, create follow-up tasks, and kick off workflows the moment a record or task changes, all without code.

## Overview

The Softr Attio integration moves data both ways. From your Softr app into Attio: whenever a form is submitted, a user signs up, or a record changes, your workflow can create, update, or find records, add notes, and create or update tasks. From Attio back into Softr: webhook triggers fire your workflows the moment a record is created, updated, or deleted, or a task is created.

You choose which Attio object to work with — People, Companies, Deals, or any custom object — and map fields from your Softr forms, records, or previous workflow steps to Attio attributes. Softr automatically picks up your workspace's objects and attributes, including custom ones, so the setup matches your CRM exactly.

## Available Actions

### Create or update record

Add a new record to any Attio object, or update the existing one when a match is found — for example, by email address for people or by domain for companies. No duplicate checks needed: if the record exists, it's updated; if not, it's created.

### Create record

Add a brand-new record to any Attio object, with the attribute values you map from your app.

### Update record

Update an existing record by its ID — change only the attributes you choose, leaving the rest untouched.

### Find records

Search any Attio object for records that match the conditions you set, and use the results in later workflow steps.

### Get record

Retrieve a single record by its ID and use its attributes in later steps — for example, to pull the full details of the record that fired a trigger.

### Create note

Attach a note to a record in Attio — great for logging form answers, call summaries, or activity from your Softr app.

### Create task

Create a task in Attio, optionally with a deadline, an assignee, and a linked record, so follow-ups never slip.

### Update task

Update a task's deadline, completion status, assignee, or linked record by its ID.

## Available Triggers

### Record created

Starts a workflow when a new record is created in Attio. Optionally scope it to a single object.

### Record updated

Starts a workflow when a record is updated. Optionally scope it to a single object.

### Record deleted

Starts a workflow when a record is deleted. Optionally scope it to a single object.

### Task created

Starts a workflow when a new task is created in Attio.

## Key Benefits

- **No-code CRM automation:** Keep Attio up to date from your Softr app visually, without writing any code or touching an API.
- **Two-way sync:** Push data into Attio with actions, and react to changes in Attio with triggers — in one workflow builder.
- **No duplicates:** Create-or-update logic matches records by a unique attribute, so the same lead or customer is never added twice.
- **Works with your setup:** Standard and custom objects, custom attributes, selects, and statuses from your workspace all show up automatically.
- **Real-time:** Records, notes, and tasks land in Attio the moment something happens in your app — and Attio changes start your workflows instantly.

## Example Use Cases

| Use Case                       | Description                                                                                                  |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Lead capture forms**         | Turn every Softr form submission into a person or company record in Attio, enriched with the form answers.   |
| **Member sign-up sync**        | Add new app users to Attio the moment they sign up, so sales and success teams see them right away.          |
| **Client portal updates**      | When a client updates their details in your portal, sync the changes to their Attio record automatically.    |
| **Deal intake**                | Create or update a deal in Attio when a request is submitted through your client-facing intake form.         |
| **Log activity as notes**      | Attach a note to the matching Attio record whenever a customer submits feedback or completes a step.         |
| **Automatic follow-up tasks**  | Create an assigned task in Attio when a new lead comes in, so someone always owns the next step.             |
| **React to CRM changes**       | When a record is created or updated in Attio, trigger a Softr workflow to notify a team or update your app.  |
| **Enrich on trigger**          | When a trigger fires, fetch the full record by its ID to read every attribute before notifying or updating.  |

## How to Connect Softr with Attio

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add an **Attio** action (or trigger, if you want the workflow to start from an Attio event).
3. Click **Connect to Attio** and paste your access token. You can create one in Attio under **Workspace Settings → Developers → Access tokens**.
4. Pick the object you want to work with — People, Companies, Deals, or a custom object (and, for triggers, optionally scope to a single object).
5. Map fields from your Softr forms, records, or previous workflow steps to the action's inputs.
6. Save and activate your workflow.
