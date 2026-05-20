# Salesforce integration

Connect Salesforce with your Softr applications to automate CRM workflows, sync customer data, and keep your sales team's pipeline up to date — all without writing code.

## Overview

The Softr Salesforce integration lets you create, update, retrieve, and delete Salesforce contacts directly from your no-code app workflows. Trigger CRM operations from form submissions, user sign-ups, record changes, or any other event in your Softr app — and have Salesforce reflect those changes instantly.

Use Softr workflows to bridge your customer-facing portals and internal tools with Salesforce, so your sales team always has accurate, up-to-date contact data without manual data entry.

## Available Actions

### Create contact

Add a new contact record to Salesforce. Map fields from your Softr form or data source — including name, email, phone, lead source, and custom fields — directly to the Salesforce contact object.

### Update contact

Update an existing Salesforce contact by ID. Modify any contact field from within a Softr workflow, such as updating a phone number, reassigning an account, or changing a lead source after qualification.

### Get contact

Retrieve a single Salesforce contact record by its ID. Use the returned data in subsequent workflow steps — for example, to personalize a notification or populate a Softr block.

### Get many contacts

Fetch a list of contacts from Salesforce with optional filters by email, last name, or account ID. Useful for syncing data, checking for duplicates before creating a new contact, or powering dynamic list views.

### Delete contact

Permanently remove a contact from Salesforce by ID. Trigger this from a Softr admin action button or a data-cleanup workflow.

## Key Benefits

- **Eliminate manual data entry:** Automatically push customer information from Softr forms and portals into Salesforce without anyone having to copy and paste.
- **Real-time CRM sync:** Keep your Salesforce pipeline current as soon as events happen in your Softr app — new sign-ups, form submissions, or record updates.
- **Seamless customer portals:** Build client-facing portals in Softr that read from and write to Salesforce, giving your team a single source of truth.
- **No Salesforce admin required:** Configure CRM automations visually in Softr, without custom Apex code or complex Salesforce flows.
- **Multi-step workflows:** Chain Salesforce actions with other integrations — send a Slack notification after creating a contact, or email a confirmation after updating a record.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Lead capture from forms** | When a visitor submits a contact form in your Softr app, automatically create a Salesforce contact with their details. |
| **Member portal sync** | When a new user signs up to your Softr portal, create a corresponding Salesforce contact and assign them to the right account. |
| **CRM data enrichment** | Allow customers to update their own profile in a Softr portal, and have those changes flow directly into their Salesforce contact record. |
| **Admin contact management** | Give your team an internal dashboard in Softr to look up, edit, or remove Salesforce contacts without needing Salesforce licenses for every user. |
| **Deduplication before outreach** | Before sending a campaign email, query Salesforce to check whether a contact already exists, and skip or update instead of creating a duplicate. |
| **Offboarding automation** | When a user account is deleted in Softr, automatically delete or update the corresponding Salesforce contact record. |

## How to Connect Softr with Salesforce

1. In your Softr app, open the **Workflows** section and create or edit a workflow.
2. Add a **Salesforce action** step (Create contact, Update contact, etc.).
3. Click **Connect Salesforce** and authorize Softr to access your Salesforce org via OAuth.
4. Configure the action inputs — map fields from your workflow data to the Salesforce contact fields.
5. Save and activate your workflow to start syncing data automatically.
