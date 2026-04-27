# Zendesk integration

Connect Zendesk with your Softr applications to automate support operations and manage tickets — all without code. Build workflows that create, update, and comment on tickets, and look up users and organizations to enrich your automation logic.

## Overview

The Softr Zendesk integration allows you to connect your no-code apps with your Zendesk support account. Automatically create support tickets, update their status, add comments, and retrieve user or organization details — all triggered by events in your Softr app.

Whether you're building a customer portal, an internal help desk, or an operations tool, you can wire Softr records and form submissions directly to Zendesk to eliminate manual data entry and speed up response times.

## Credentials Required

To connect Softr with Zendesk you need three pieces of information from your Zendesk account:

| Field | Description |
| :---- | :---------- |
| **Subdomain** | The prefix of your Zendesk URL, e.g. `acme` from `acme.zendesk.com` |
| **Email** | The email address of the Zendesk agent or admin used for API access |
| **API Token** | A token generated in Zendesk Admin → Apps & Integrations → Zendesk API → API Tokens |

To generate an API token, log into Zendesk, go to **Admin Center → Apps & Integrations → Zendesk API**, enable token access, and click **Add API token**.

## Available Actions

### Ticket: Create

Create a new support ticket in Zendesk. Set the description, subject, status, priority, type, assignee, group, tags, and more.

**Key inputs:** description (required), subject, status, priority, type, requester email, assignee email, group, organization, tags, external ID, recipient

**Output fields:** id, subject, description, status, priority, type, requester\_id, assignee\_id, group\_id, organization\_id, tags, external\_id, created\_at, updated\_at, url

### Ticket: Get

Retrieve a single ticket by its numeric ID.

**Key inputs:** ticket\_id (required)

**Output fields:** id, subject, description, status, priority, type, requester\_id, assignee\_id, group\_id, organization\_id, tags, custom\_fields, created\_at, updated\_at, url

### Ticket: Update

Update an existing ticket. Change its status, priority, assignee, group, organization, or tags.

**Key inputs:** ticket\_id (required), subject, status, priority, type, assignee email, group, organization, tags, external ID

**Output fields:** same as Ticket: Get

### Ticket: Delete

Soft-delete a ticket by ID. Deleted tickets move to the Deleted view and are permanently removed after 30 days.

**Key inputs:** ticket\_id (required)

**Output fields:** success (boolean)

### Ticket: List

Search and list tickets. Filter by status, group, organization, or a full Zendesk search query. Control sort order and the number of results returned.

**Key inputs:** status, group, organization, query, sort by, sort order, limit

**Output fields:** array of ticket objects (same fields as Ticket: Get)

### Add Comment to Ticket

Add a public reply or an internal note to an existing ticket.

**Key inputs:** ticket\_id (required), body (required), visibility (public or internal note)

**Output fields:** id, ticket\_id, body, public, author\_id, created\_at

### User: Get

Retrieve a user by their numeric Zendesk user ID.

**Key inputs:** user\_id (required)

**Output fields:** id, name, email, role, organization\_id, phone, time\_zone, locale, verified, suspended, external\_id, tags, created\_at, updated\_at, url

### Organization: Get

Retrieve an organization by its numeric Zendesk ID.

**Key inputs:** organization\_id (required)

**Output fields:** id, name, domain\_names, details, notes, tags, external\_id, group\_id, shared\_tickets, shared\_comments, created\_at, updated\_at, url

## Key Benefits

- **No-code simplicity:** Set up and manage your Zendesk workflows visually in Softr, without any coding.
- **End-to-end ticket lifecycle:** Create, update, comment on, and close tickets automatically based on events in your Softr app.
- **Dynamic fields:** Groups, statuses, and organizations are loaded from your live Zendesk account so you always see up-to-date options.
- **Flexible filtering:** Use Zendesk's native search syntax to query tickets with any combination of conditions.
- **Enriched automation:** Look up user and organization details mid-workflow to branch logic or populate other systems.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Support ticket from form** | Automatically create a Zendesk ticket when a user submits a contact or support form in Softr. |
| **Status sync** | When a Softr database record moves to "Resolved", update the linked Zendesk ticket status to `solved`. |
| **Agent reply** | Post an internal note or public reply to a ticket from a Softr workflow step. |
| **Escalation alerts** | When a ticket priority is set to `urgent`, look it up and post its details to Slack or send an email via a multi-step workflow. |
| **Agent dashboard** | Build an internal Softr portal that lists open tickets for a team, fetching them by group or query filter. |

## How to Connect Softr with Zendesk

1. Open your Softr workspace and go to **Integrations**.
2. Find **Zendesk** and click **Connect**.
3. Enter your **subdomain**, **email**, and **API token** (see Credentials Required above).
4. Click **Save**. Softr will verify the credentials against your Zendesk account.
5. Open the **Workflow** builder and add a Zendesk action to any workflow.
6. Select the connected account, configure the action inputs, and save.
7. Test the step and activate your workflow.
