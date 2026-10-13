# QuickBooks integration

Connect QuickBooks Online with your Softr applications to keep your books in sync with your app — create customers and invoices the moment something happens in Softr, look up financial records on demand, record payments and vendor bills, and react instantly when anything changes in QuickBooks. Build billing portals and finance workflows on top of your live accounting data, without code.

## Overview

The Softr QuickBooks integration lets your app read and write the records your accounting runs on: customers, invoices, vendors, bills, items, and payments. Create or update a record, fetch a single one by ID, or pull a filtered list to display and act on inside Softr. Every action returns the record it created, updated, or fetched, so you can use it in any downstream workflow step.

This unlocks the patterns Softr customers reach for first: turning a form submission into a QuickBooks customer, raising and emailing an invoice when a booking is confirmed, surfacing outstanding invoices in a client portal, recording payments from an app, and kicking off follow-up automations the moment an invoice or customer changes in QuickBooks — keeping your app and your books aligned both ways.

## Available Actions

### Customers

#### Create customer

Add a new customer to QuickBooks — typically from a Softr signup form, an onboarding flow, or a "new client" record action. Set the display name (required), contact name and company, email, phone, billing address, preferred delivery method, and whether the customer is taxable.

#### Get customer

Look up a single customer by ID to surface their billing details on a member's account page or an admin record view.

#### List customers

Retrieve customers to power admin dashboards, client directories, or a picker on a form. Set a limit and, optionally, a filter to narrow the results (for example, only active customers).

#### Update customer

Keep QuickBooks in sync with your app — refresh a customer's name, contact details, billing address, or status when the matching record changes in Softr. Updates are sparse: only the fields you fill in are changed, and everything else is left untouched.

### Invoices

#### Create invoice

Raise a sales invoice for a customer, with one or more line items (amount, item, quantity, description, tax code), transaction and due dates, document number, billing email, customer memo, and billing address — for example, billing a client automatically after an order or a confirmed booking.

#### Get invoice

Fetch a single invoice by ID to read its amount, balance, status, and line items downstream.

#### List invoices

Retrieve invoices — for example, to show a client their invoice history in a portal, or to drive a payment-reminder workflow. Supports a limit and an optional filter.

#### Update invoice

Change an existing invoice's transaction or due date, document number, billing email, or customer memo as records change in your app.

#### Send invoice

Email an invoice to a customer through QuickBooks. Provide the invoice ID and the recipient address, and QuickBooks delivers the invoice and marks it as sent.

#### Void invoice

Void an invoice that should not be paid. The invoice stays in QuickBooks for your audit trail with its amounts zeroed out.

#### Delete invoice

Permanently remove an invoice from QuickBooks. Use **Void invoice** instead when you need to keep a record of the transaction.

### Vendors

#### Create vendor

Add a supplier to QuickBooks with their display name (required), contact details, company, account number, billing address, and 1099 status.

#### Get vendor

Fetch a single vendor by ID to reuse their details in a later workflow step.

#### List vendors

Retrieve vendors to display in Softr, sync to a Softr database, or loop over in a workflow. Supports a limit and an optional filter.

#### Update vendor

Update a vendor's details or deactivate them when the matching record changes in your app. Like customer updates, only the fields you provide are changed.

### Bills

#### Create bill

Record a vendor bill with one or more expense lines. Each line can be item-based (linked to a product or service) or account-based (linked to an expense account), with an amount and description, plus transaction and due dates, a document number, and a private note.

#### Get bill

Fetch a single bill by ID to read its vendor, amount, balance, and lines.

#### List bills

Retrieve bills — for example, to build an accounts-payable view or an approval queue inside Softr. Supports a limit and an optional filter.

### Items

#### Get item

Look up a single product or service item by ID, for example to read its name, price, or type before adding it to an invoice.

#### List items

Retrieve your products and services to display in Softr or to populate a selection on a form. Supports a limit and an optional filter.

### Payments

#### Create payment

Record a customer payment in QuickBooks with the amount, transaction date, reference number, and a private note — for example after a member pays through your app.

#### Get payment

Fetch a single payment by ID to display or reconcile it downstream.

#### List payments

Retrieve payments to build reconciliation views, a client's payment history, or a finance dashboard. Supports a limit and an optional filter.

## Available Triggers

### Entity changed

Fires when a record is created or updated in QuickBooks. Choose the entity to listen to — customer, invoice, vendor, bill, item, or payment — and whether the trigger runs on **created**, **updated**, or **both**. Voiding a transaction counts as an update.

QuickBooks delivers only the change details — the realm (company) ID, entity name, entity ID, operation, and the time it was last updated — not the full record. Chain the matching **Get** action (for example **Get invoice**) after the trigger, using the entity ID, to fetch the record's current state and use it in the rest of your workflow.

## Key Benefits

- **No-code accounting automation:** Configure QuickBooks actions and triggers visually in Softr — no API setup, no scripts.
- **Two-way sync:** Push customers, invoices, bills, and payments into QuickBooks and react to changes coming back out, so your app and your books stay aligned.
- **Live financial data in your app:** Pull customers, invoices, and payments into list and detail blocks to build billing portals and finance dashboards.
- **Pick records from dropdowns:** Customers, items, vendors, accounts, and tax codes load straight from your QuickBooks company, so you select them instead of hunting for IDs.
- **Safe updates:** Update actions only change the fields you fill in, so partial updates from a Softr form never wipe the rest of the record.
- **Reusable outputs:** Every action returns the full record, ready to drop into emails, database records, Slack messages, or any other workflow step.

## Example Use Cases

| Use Case                            | Description                                                                                                        |
| :---------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **New customer to QuickBooks**      | Create a QuickBooks customer automatically when someone signs up or submits an onboarding form in your Softr app.  |
| **Invoice on order or booking**     | Raise an invoice when a customer places an order or confirms a booking, then email it with **Send invoice**.       |
| **Client billing portal**           | Use **List invoices** and **List payments** to show clients their invoices and payment history inside Softr.       |
| **Accounts payable queue**          | Create vendor bills from a Softr form and surface open bills in an internal approval dashboard.                    |
| **Payment follow-ups**              | Trigger on a changed invoice, fetch it with **Get invoice**, and send a reminder or update a record when it's paid.|
| **Keep records in sync**            | Update a QuickBooks customer or vendor whenever the matching record changes in your Softr database.                |
| **Finance dashboard**               | Pull invoices, bills, and payments into a Softr admin dashboard for a real-time view of your books.                |

## How to Connect Softr with QuickBooks

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a QuickBooks action (or the **Entity changed** trigger).
3. Click **Connect to QuickBooks** and sign in with your Intuit account, then select the company you want to connect and authorize the requested permissions.
4. Pick the connected QuickBooks account on the action or trigger (you can connect more than one company).
5. Map fields from your Softr forms, records, or previous workflow steps to the action's inputs — for example, customer details or invoice line items. Fields like customer, item, vendor, account, and tax code are offered as dropdowns loaded from your QuickBooks company.
6. Save and activate your workflow.
