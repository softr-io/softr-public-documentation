# Zendesk integration

Connect Zendesk with your Softr applications to automate support operations and eliminate manual ticket work. Build workflows that create and update tickets, log comments, and look up users and organizations — all triggered by events in your Softr app.

## Overview

The Softr Zendesk integration links your no-code apps directly to your Zendesk support account. Whenever something happens in Softr — a form submission, a record status change, a new user sign-up — you can automatically create tickets, update their details, post comments, or retrieve customer and organization data to drive the next step in your workflow.

Whether you're building a client portal, an internal help desk tool, or an operations dashboard, the Zendesk integration removes the gap between what's happening in your Softr app and what your support team sees in Zendesk.

## Available Actions

### Create ticket

Open a new support ticket in Zendesk with a subject, description, priority, assignee, and tags — all set dynamically from your Softr workflow.

### Get ticket

Retrieve the full details of a specific ticket by its ID, so you can use ticket data in later workflow steps.

### Update ticket

Change a ticket's status, priority, assignee, group, or tags to keep Zendesk in sync with what's happening in your Softr app.

### Delete ticket

Remove a ticket from your Zendesk queue — useful for cleanup workflows or voided requests.

### List tickets

Fetch a filtered list of tickets by status, group, organization, or Zendesk search query to power reports, dashboards, or conditional logic.

### Add comment to ticket

Post a public reply or internal agent note to any ticket — ideal for logging Softr form responses or escalation details directly inside Zendesk.

### Get user

Look up a Zendesk user by ID to retrieve their name, email, role, and organization for use in downstream workflow steps.

### List users

Search and return a set of Zendesk users based on any query criteria, such as role or organization.

### Get organization

Retrieve the full details of a Zendesk organization by ID, including domain names, notes, and tags.

### List organizations

Search and return a list of Zendesk organizations to drive lookups, filters, or conditional branching in your workflow.

## Key Benefits

- **No-code simplicity:** Configure every Zendesk action visually in Softr — no coding required beyond the initial API token setup.
- **Instant ticket creation:** Turn any Softr form submission or record event into a Zendesk ticket automatically, the moment it happens.
- **Full ticket lifecycle:** Create, update, comment on, and close tickets without leaving your workflow canvas.
- **Richer automation with lookups:** Pull user and organization data mid-workflow to personalize messages, route tickets, or update other systems.
- **Support-ready portals:** Build client-facing forms and internal help desks in Softr that feed directly into Zendesk — giving your support team everything they need, where they already work.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Support request form** | Create a Zendesk ticket automatically when a user submits a help request form in your Softr portal. |
| **Status sync** | Update the linked Zendesk ticket to `solved` when a record's status field changes to "Resolved" in your Softr database. |
| **Agent notes from forms** | Post an internal note to a ticket when a customer fills in a follow-up form, keeping all context in one place. |
| **Escalation alerts** | When a high-priority record is flagged in Softr, create an urgent Zendesk ticket and notify your team in Slack. |
| **Client portal ticket feed** | Display a filtered list of open tickets for each logged-in user by querying Zendesk with their email inside a Softr list block. |
| **New user onboarding ticket** | Auto-create a welcome or setup ticket in Zendesk when a new member signs up to your Softr app. |

## How to Connect Softr with Zendesk

1. Open your Softr workspace and go to **Workflows**.
2. Create a new workflow or open an existing one, then add a Zendesk action.
3. In the **Account** field, click **Add another account** and enter your Zendesk **subdomain**, **email address**, and **API token**.
4. To generate an API token, log into Zendesk and go to **Admin Center → Apps & Integrations → Zendesk API → API Tokens**, then click **Add API token**.
5. Click **Save** — Softr verifies your credentials and connects the account.
6. Configure the action inputs, click **Continue**, and activate your workflow.
