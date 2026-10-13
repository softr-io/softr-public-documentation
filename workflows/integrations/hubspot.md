# HubSpot integration

Connect HubSpot with your Softr applications to keep your CRM in sync with everything happening inside your no-code app. Capture leads from forms, sync member sign-ups to Contacts, push deals from your sales tools, build member dashboards backed by live HubSpot data, and start workflows when a record is created or updated in HubSpot — all without writing a line of code.

## Overview

The Softr HubSpot integration links your Softr app directly to your HubSpot account so customer data flows both ways. Whenever someone signs up, fills out a form, updates a record, or takes an action in your app, you can create or update Contacts, Companies, Deals, or Tickets in HubSpot automatically — and pull HubSpot records back into Softr lists and detail pages just as easily. It also works the other way round: the **Record created** and **Record updated** triggers start a workflow when something changes in HubSpot, so your app, your team's Slack channel, or your Softr database can follow the CRM.

This makes HubSpot a natural fit for Softr customer portals, lead capture sites, internal sales tools, and member dashboards. Use it to turn your Softr forms into a CRM intake funnel, give your sales team a self-serve dashboard of HubSpot deals, or let members see and update their own CRM record from inside your app.

## Available Actions

### Add record

Create a HubSpot record (Contact, Company, Deal, Ticket, or any custom object) from a Softr form submission, sign-up, or workflow step.

### Get record

Look up a single HubSpot record by ID and pull its fields into your Softr app — perfect for showing a member their own profile or surfacing a deal on a detail page.

### Get records

Fetch a list of HubSpot records with optional filters and sorting, ready to display in a Softr list block, table, or kanban.

### Update record

Update the fields on a HubSpot record when something changes in Softr — a form edit, a status change, or a member updating their own profile.

### Update records

Update multiple HubSpot records in one workflow step — useful for bulk status changes, segment tagging, or syncing edits made across a Softr table.

### Delete record

Remove a HubSpot record when it's no longer needed — for example, cleaning up a lead a member has dismissed or a duplicate flagged in your admin tool.

### Delete records

Delete multiple HubSpot records at once, ideal for bulk clean-up workflows triggered from your Softr admin dashboard.

## Available Triggers

HubSpot triggers use background polling: Softr checks HubSpot for changes at a regular interval, so a workflow starts shortly after the change rather than the moment it happens. The interval depends on your plan (every minute on Professional plans and above) and is shown on the trigger in the workflow builder. Each trigger watches one object — Contacts, Companies, Deals, Tickets, or any other object the integration supports, including your custom objects.

### Record created

Starts a workflow when a new record is created in the selected HubSpot object — a new Contact from a HubSpot form, a Deal your sales team opened, a Ticket logged by support. Run a test on the trigger to pull a recent record and see the properties available to later steps.

### Record updated

Starts a workflow when a record in the selected HubSpot object is edited — a deal stage moves, a contact's lifecycle stage changes, a ticket is closed. Add a [Filter](/workflows/advanced-concepts#filter) step after the trigger to act only on the changes you care about.

## Key Benefits

- **No-code CRM automation:** Wire your Softr forms, sign-ups, and record actions to HubSpot visually — no developers, no Zapier zaps to maintain.
- **Two-way data flow:** Push new records into HubSpot and pull existing ones back into Softr lists and detail pages, all from the same workflow builder.
- **Built for customer portals:** Give members a branded Softr experience while your team continues to work in HubSpot — both sides stay in sync.
- **Works across every HubSpot object:** Contacts, Companies, Deals, Tickets, Notes, Tasks, Leads, Projects, Products, Line Items, Invoices, Subscriptions, Listings, Appointments, and your custom objects are all supported with the same simple actions.
- **Bulk operations included:** Update or delete many records in a single step when you need to act on a whole segment at once.
- **React to CRM changes:** Start a workflow when a record is created or updated in HubSpot, so the rest of your stack keeps up without anyone copying data by hand.

## Example Use Cases

| Use Case                              | Description                                                                                                          |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| **Lead capture forms**                | Turn Softr form submissions into new HubSpot Contacts and Deals, complete with source attribution and custom fields. |
| **Member sign-up sync**               | When a new user signs up to your Softr portal, automatically create a matching Contact in HubSpot.                   |
| **Self-serve customer portal**        | Let members view and update their own HubSpot Contact record from inside a Softr app.                                |
| **Internal sales dashboard**          | Build a Softr admin tool that lists open Deals from HubSpot, with one-click updates back to the CRM.                 |
| **Support ticket intake**             | Convert Softr support form submissions into HubSpot Tickets and route them to the right pipeline.                    |
| **Bulk segment management**           | Update or delete groups of Contacts at once from a Softr admin view — perfect for list cleanup or bulk re-tagging.   |
| **New lead alerts**                   | When a Contact or Deal is created in HubSpot, notify your team in Slack or add the record to your Softr database.    |
| **Act on a stage change**             | When a Deal is updated in HubSpot, check its stage and start the hand-off or onboarding workflow when it moves.      |

## How to Connect Softr with HubSpot

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a HubSpot trigger, such as Record created, or a HubSpot action, such as Add record.
3. Click **Connect to HubSpot** and sign in to authorize Softr to access your HubSpot account.
4. Pick the HubSpot account or portal you want to connect if you manage more than one.
5. Choose the object you want to work with — Contact, Company, Deal, Ticket, or a custom object.
6. For an action, map fields from your Softr forms, records, or earlier workflow steps to the matching HubSpot properties. For a trigger, run a test to pull a sample record.
7. Save and activate your workflow.
