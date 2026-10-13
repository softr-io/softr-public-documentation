# ActiveCampaign integration

Connect ActiveCampaign with your Softr applications to keep your CRM, lists, and deals in sync with everything happening inside your no-code app. Capture leads from forms, push sign-ups to contacts, tag subscribers based on user actions, and build member dashboards backed by live ActiveCampaign data — all without writing a line of code.

## Overview

The Softr ActiveCampaign integration links your Softr app directly to your ActiveCampaign account so customer data flows both ways. Whenever someone signs up, fills out a form, updates a record, or takes an action in your app, you can create or update contacts, deals, accounts, and tags in ActiveCampaign automatically — and pull ActiveCampaign records back into Softr lists and detail pages just as easily.

This makes ActiveCampaign a natural fit for Softr customer portals, lead capture sites, marketing automation triggers, and member dashboards. Use it to turn your Softr forms into a marketing funnel, give your team a self-serve dashboard of open deals, or let members see and update their own CRM record from inside your app.

## Available Actions

### Contact

- **Create contact** — add a new contact in ActiveCampaign, optionally upserting if the email already exists. Supports first/last name, phone, and custom fields.
- **Update contact** — update an existing contact by ID.
- **Get contact** — retrieve a single contact by ID and pull their fields into your Softr app.
- **Delete contact** — delete a contact by ID.
- **List contacts** — search and list contacts with filters for email, name, list, tag, status, and creation date.
- **Add contact to list** — subscribe a contact to a list.
- **Remove contact from list** — unsubscribe a contact from a list.
- **Add tag to contact** — apply a tag to a contact.
- **Remove tag from contact** — remove a tag using the contact-tag link ID returned by Add tag.

### Deal

- **Create deal** — add a new deal with title, value, currency, contact, pipeline, stage, and owner.
- **Update deal** — change any field on an existing deal.
- **Get deal** — retrieve a deal by ID.
- **Delete deal** — delete a deal by ID.
- **List deals** — search and list deals with filters for pipeline, stage, owner, and status.
- **Add deal note** — append a note to a deal.

### Account

- **Create account** — add a new account with name, website URL, and custom fields.
- **Update account** — update an existing account by ID.
- **Get account** — retrieve an account by ID.
- **Delete account** — delete an account by ID.
- **List accounts** — search and list accounts.

### Tag & List

- **Create tag** — create a new contact or template tag.
- **List tags** — search and list available tags.
- **List lists** — list the lists in your ActiveCampaign account.

## Key Benefits

- **No-code CRM and marketing automation:** Wire your Softr forms, sign-ups, and record actions to ActiveCampaign visually — no developers, no Zapier zaps to maintain.
- **Two-way data flow:** Push new contacts and deals into ActiveCampaign and pull them back into Softr lists and detail pages, all from the same workflow builder.
- **Built for customer portals:** Give members a branded Softr experience while your team continues to run automations in ActiveCampaign — both sides stay in sync.
- **Granular segmentation:** Apply and remove tags, subscribe and unsubscribe from lists, and update custom fields based on actions inside your Softr app.
- **Built-in rate limiting:** Softr respects ActiveCampaign's 5 requests/second limit so your automations stay reliable as you scale.

## Example Use Cases

| Use Case                              | Description                                                                                                                       |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Lead capture forms**                | Turn Softr form submissions into new ActiveCampaign contacts and deals, complete with source attribution and custom fields.       |
| **Member sign-up sync**               | When a new user signs up to your Softr portal, automatically create a matching contact in ActiveCampaign and subscribe to a list. |
| **Self-serve customer portal**        | Let members view and update their own ActiveCampaign contact record from inside a Softr app.                                      |
| **Tag-based segmentation**            | Tag contacts in ActiveCampaign based on Softr actions — clicking a CTA, completing onboarding, upgrading a plan.                  |
| **Internal sales dashboard**          | Build a Softr admin tool that lists open deals from ActiveCampaign, with one-click updates back to the CRM.                       |
| **Account-based selling**             | Sync companies as ActiveCampaign accounts and link them to contacts and deals for full account-based workflows.                   |

## How to Connect Softr with ActiveCampaign

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add an ActiveCampaign action.
3. Click **Connect to ActiveCampaign** to open the credentials form.
4. In a separate tab, log in to your ActiveCampaign account, go to **Settings → Developer**, and copy your **API URL** (looks like `https://your-account.api-us1.com`) and your **API Key**.
5. Paste both values into the Softr credentials form and save.
6. Choose the action you want to run — Create contact, Add deal note, List contacts, etc.
7. Map fields from your Softr forms, records, or earlier workflow steps to the matching ActiveCampaign fields. Dynamic dropdowns let you pick lists, tags, pipelines, stages, and owners from your account.
8. Save and activate your workflow.
