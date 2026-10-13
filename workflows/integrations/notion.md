# Notion integration

Connect Notion with your Softr applications to turn your Notion databases into a living backend for forms, member portals, and lightweight CMSes. Capture submissions, surface records to your users, start workflows when a page is added or edited in Notion, and keep everything in sync — without leaving the tools your team already loves.

## Overview

The Softr Notion integration lets your no-code apps read from and write to Notion databases in real time. Whenever a user submits a form, signs up, or updates a record in Softr, you can create, fetch, edit, or remove the matching page in Notion — keeping your operations team working in their familiar workspace while your customers interact with a polished Softr front end. It also works the other way round: the **Record created** and **Record updated** triggers start a workflow when a page is added or edited in a Notion database, so your app can follow what your team does in Notion.

This pairing fits naturally wherever Notion is already the source of truth: applicant trackers, content calendars, customer directories, project boards, internal wikis, and client intake systems. Your team manages the data in Notion; your members and visitors see and act on it through Softr blocks, forms, and member dashboards.

## Available Actions

### Add record

Create a new page in a Notion database — perfect for capturing form submissions, new sign-ups, or any record your Softr app generates.

### Get record

Fetch a single page from a Notion database by its ID, ready to display in a detail view or pass to the next workflow step.

### Get records

Retrieve multiple pages from a Notion database at once, with optional filters, so you can power Softr lists with live Notion data.

### Update record

Modify the properties of an existing page in a Notion database whenever a status changes, an admin reviews a submission, or a member edits their own profile.

### Update records

Update several pages in a Notion database in a single workflow step — ideal for bulk status changes, batch approvals, or recurring clean-up jobs.

### Delete record

Remove a single page from a Notion database when an item is archived, rejected, or no longer relevant.

### Delete records

Remove multiple pages from a Notion database in one go, keeping your workspace tidy without manual housekeeping.

## Available Triggers

Notion triggers use background polling: Softr checks the database for changes at a regular interval, so a workflow starts shortly after the change rather than the moment it happens. The interval depends on your plan (every minute on Professional plans and above) and is shown on the trigger in the workflow builder. Each trigger watches one Notion database.

### Record created

Starts a workflow when a new page is added to the selected Notion database — a new applicant, a new content entry, a new row your team typed in. Run a test on the trigger to pull a recent page and see the properties available to later steps.

### Record updated

Starts a workflow when a page in the selected Notion database is edited — a status changes, an owner is assigned, a date is set. Add a [Filter](/workflows/advanced-concepts#filter) step after the trigger to act only on the changes you care about.

## Key Benefits

- **No-code Notion backend:** Use any Notion database as the data layer behind your Softr app, with no scripts or third-party glue tools.
- **Real-time sync:** Form submissions, profile edits, and status changes flow into Notion the moment they happen.
- **Familiar workspace for your team:** Your operators, editors, and admins keep working in Notion while customers interact through Softr.
- **Bidirectional workflows:** Read from Notion to power lists and dashboards, or write to Notion to capture activity from your app.
- **Bulk-friendly automations:** Update or clean up many records at once with the multi-record actions.
- **React to changes in Notion:** Start a workflow when a page is added or edited in a Notion database, so notifications, syncs, and follow-ups happen without anyone leaving Notion.

## Example Use Cases

| Use Case                       | Description                                                                                                            |
| :----------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| **Form-to-Notion intake**      | Capture Softr form submissions — applications, contact requests, feedback — as new pages in a Notion database.         |
| **Member portal on Notion**    | Power a member dashboard with Notion data: each member sees and edits only the rows linked to their account.           |
| **Lightweight CMS for content**| Let editors manage articles, listings, or events in Notion and surface them to visitors through Softr list blocks.     |
| **Applicant or lead tracker**  | Push new leads into a Notion CRM database, then update their stage as your team moves them through the pipeline.       |
| **Status-driven notifications**| Update a Notion page when a record changes in Softr, so your operations team always sees the latest state in context.  |
| **Admin clean-up workflows**   | Bulk-archive or delete outdated Notion pages on a schedule or when a record is closed in your Softr admin tool.        |
| **New entry alerts**           | When a page is added to a Notion database, notify your team in Slack or send a confirmation email to the submitter.  |
| **Notion-to-Softr sync**       | When a page is edited in Notion, update the matching record in your Softr database so your app shows the latest state. |

## How to Connect Softr with Notion

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Notion trigger, such as Record created, or a Notion action, such as Add record.
3. Click **Connect to Notion** and sign in to authorize Softr to access your Notion workspace.
4. Choose which pages and databases Softr should be able to read from and write to.
5. Pick the database you want to use.
6. For an action, map your Softr form fields, record properties, or previous workflow outputs to the matching Notion database properties. For a trigger, run a test to pull a sample page.
7. Save and activate your workflow.
