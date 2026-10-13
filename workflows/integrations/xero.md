# Xero integration

Connect Xero with your Softr applications to automate your accounting busywork — create invoices and contacts the moment something happens in your app, look up financial records on demand, and react instantly when invoices or customers change in Xero. Build billing and CRM-style workflows on top of your live accounting data, all without code.

## Overview

The Softr Xero integration lets you connect your no-code apps with your Xero organization. Create and update contacts (customers and suppliers) and sales invoices or bills, fetch a single record by ID, or pull a page of contacts and invoices to display and act on inside Softr. Every action returns the created or updated record so you can use it in any downstream workflow step.

With Softr, you can turn a form submission into a Xero contact, raise an invoice when a deal is marked won, surface outstanding invoices in a member portal, and kick off follow-up automations the moment a contact or invoice changes in Xero — keeping your app and your books in sync both ways.

## Available Actions

### Create contact

Create a new contact (customer or supplier) in your Xero organization, for example when someone signs up or submits a form in your Softr app.

### Update contact

Update an existing Xero contact — refresh their details, addresses, or status when records change in Softr.

### Get contact

Fetch a single contact by ID so you can display or reuse their details in a later workflow step.

### List contacts

Retrieve a page of contacts from your organization to show in a list block, sync to a Softr database, or loop over in a workflow.

### Create invoice

Create a new sales invoice (ACCREC) or bill (ACCPAY), including line items, due date, currency, branding theme, and status — for example, billing a customer automatically after a booking or order.

### Update invoice

Update an existing invoice to change its line items, status, dates, or reference as records change in your app.

### Get invoice

Fetch a single invoice by ID or invoice number to read its amount, status, and details downstream.

### List invoices

Retrieve a page of invoices — for example, to surface outstanding or paid invoices to members or to drive a reminder workflow.

## Available Triggers

### Resource changed

Fires when a contact, invoice, or credit note is created or updated in Xero. Choose which resource to listen to and, optionally, limit it to create or update events only. Use it to keep Softr records in sync with your books and to start follow-up automations the moment something changes in Xero.

## Key Benefits

- **No-code accounting automation:** Configure Xero actions and triggers visually in Softr — no API setup, no scripts.
- **Two-way sync:** Push contacts and invoices into Xero and react to changes coming back out, so your app and your books stay aligned.
- **Live financial data in your app:** Pull contacts and invoices into list and detail blocks to build billing portals and finance dashboards.
- **Multi-organization ready:** Pick which Xero organization each action uses, so agencies and multi-entity businesses can automate every set of books.
- **Reusable outputs:** Every action returns the full record, ready to drop into emails, database records, Slack messages, or any other workflow step.

## Example Use Cases

| Use Case                          | Description                                                                                       |
| :-------------------------------- | :------------------------------------------------------------------------------------------------ |
| **New customer to Xero**          | Create a Xero contact automatically when someone signs up or submits a form in your Softr app.    |
| **Invoice on order or booking**   | Raise a sales invoice when a customer places an order or confirms a booking, then email the link. |
| **Billing portal**                | Use **List invoices** to show members their outstanding and paid invoices inside a Softr portal.  |
| **Keep CRM contacts in sync**     | Update a Xero contact whenever the matching record changes in your Softr database.                |
| **Payment follow-ups**            | Trigger on a changed invoice and send a reminder or update a record when its status changes.      |
| **Finance dashboard**            | Pull contacts and invoices into a Softr admin dashboard for a real-time view of your accounts.    |

## How to Connect Softr with Xero

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Xero action (or the **Resource changed** trigger).
3. Click **Connect to Xero** and sign in with your Xero account, then review and authorize the requested permissions.
4. Select the **Organization** you want the action or trigger to use (Softr supports connecting more than one Xero organization).
5. Map fields from your Softr forms, records, or previous workflow steps to the action's inputs (for example, contact details or invoice line items).
6. Save and activate your workflow.
