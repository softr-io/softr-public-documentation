# GoHighLevel integration

Connect GoHighLevel with your Softr applications to keep your CRM in step with your app — capture leads from forms, move deals through your pipelines, assign follow-up tasks, and book appointments, all without code. Workflows can also start the moment a contact is created or an opportunity changes stage in GoHighLevel.

## Overview

The Softr GoHighLevel integration moves data both ways. From your Softr app into GoHighLevel: when a form is submitted, a user signs up, or a record changes, your workflow can create or update contacts, create and update opportunities, manage a contact's tasks, and book appointments on a calendar. From GoHighLevel back into Softr: instant triggers start your workflows when a contact is created or an opportunity moves to another stage.

Each connection is linked to one GoHighLevel business account (sub-account). Softr picks up that account's pipelines, stages, calendars, users, and custom fields, so the fields you see in the workflow builder match your CRM.

## Available Actions

### Contacts

#### Create or update contact

Create a contact, or update the existing one when a contact with the same email address or phone number already exists — no duplicate checks needed. Set the contact's name, company, address, website, source, timezone, tags, assigned user, custom fields, and whether they should receive messages (**Do not disturb**).

Setting **Tags** replaces all of the contact's current tags.

#### Update contact

Update an existing contact by its ID. Only the fields you fill in are changed; the rest stay as they are.

#### Get contact

Retrieve a contact by its ID and use its details in later steps — for example, the full details of the contact that started the workflow.

#### Search contacts

Search contacts by name, phone, email, tags, or company. Leave the search query empty to list all contacts. Results come in pages of up to 100 contacts, sorted by date added or date updated.

#### Delete contact

Delete a contact by its ID.

### Opportunities

#### Create opportunity

Create an opportunity in a pipeline stage for a contact, with its name, status, value, assigned user, expected close date, win probability, and custom fields.

#### Update opportunity

Update an opportunity by its ID — move it to another stage, change its status, value, or assigned user. The new stage must belong to the opportunity's pipeline. When you set the status to lost, you can also give a lost reason.

#### Get opportunity

Retrieve an opportunity by its ID.

#### Search opportunities

Search opportunities, optionally filtered by pipeline, stage, status, assigned user, and creation date. Results come in pages of up to 100 opportunities.

### Tasks

#### Create task

Create a task for a contact, with a title, description, due date, and assigned user.

#### Update task

Update a contact's task — change its title, description, due date, or assigned user, or mark it as completed or not completed.

#### List tasks

List all tasks of a contact.

#### Delete task

Delete a task from a contact.

### Calendars

#### Book appointment

Book an appointment on a GoHighLevel calendar for a contact. Set the start time, and optionally the end time, title, description, status, assigned user, and meeting location (Zoom, Google Meet, Microsoft Teams, phone, address, or a custom location).

- If you leave the end time empty, the calendar's slot duration is used.
- If you leave the meeting location empty, the calendar's default location is used.
- By default, the booking follows the calendar's availability and scheduling rules. Turn on **Skip free-slot validation** to book a slot that is already taken, or **Ignore date range** to book outside the calendar's scheduling window.
- Turn on **Send notifications** to run the calendar's automations and send its notifications for this booking.

## Available Triggers

### Contact created

Starts a workflow when a new contact is created in GoHighLevel.

### Opportunity stage changed

Starts a workflow when an opportunity moves to a different stage in GoHighLevel.

To test a trigger, create a contact or move an opportunity to another stage in GoHighLevel, then load the event in the workflow builder.

## Key Benefits

- **No-code CRM automation:** Keep GoHighLevel contacts, opportunities, and tasks up to date from your Softr app — no scripts or developer help required.
- **No duplicate contacts:** Create or update contacts by email address or phone number.
- **Pipelines that move themselves:** Create opportunities and move them between stages as things happen in your app.
- **Real-time triggers:** React instantly when a contact is created or an opportunity changes stage in GoHighLevel.
- **Matches your account:** Pipelines, stages, calendars, users, and custom fields are loaded from your GoHighLevel business account.

## Example Use Cases

| Use Case                     | Description                                                                                               |
| :--------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Lead capture**             | Create or update a GoHighLevel contact whenever someone submits a form in your Softr app.                 |
| **Deal tracking**            | Create an opportunity in your sales pipeline when a member requests a quote, and move it when they accept. |
| **Follow-up tasks**          | Create a task for your team when a client submits a request in your client portal.                        |
| **Appointment booking**      | Book a GoHighLevel appointment from a booking form in your Softr app.                                     |
| **Client onboarding**        | When an opportunity moves to "Won", create the client's records and give them access to your Softr portal. |
| **CRM to app sync**          | When a contact is created in GoHighLevel, add them to a Softr table.                                      |

## How to Connect Softr with GoHighLevel

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a GoHighLevel action or trigger, for example **Create or update contact**.
3. Click **Connect to GoHighLevel** and sign in to your GoHighLevel account.
4. Choose the business account (sub-account) to connect, and approve the requested permissions. If you sign in with an agency account, choose one of its sub-accounts.
5. Choose the trigger that should run the workflow (form submission, sign-up, record update, schedule).
6. Fill in the action's settings — using fields from your Softr forms, records, or previous workflow steps.
7. Save and activate your workflow.

To connect several business accounts, add a connection for each one.

To remove Softr's access, delete the connection in Softr. This also uninstalls the Softr app from that GoHighLevel business account, so any other Softr connections to the same business account stop working too.
