# Stripe integration

Connect Stripe with your Softr applications to take payments, manage customers, and run paid member portals — all from inside your no-code app. Build checkout flows on top of Softr forms, charge users on signup, distribute coupons to specific groups, and surface live billing data in admin dashboards.

## Overview

The Softr Stripe integration lets your app create and manage Stripe customers, kick off payments, look up charges, and pull live balance data — driven by the same forms, sign-ups, and record actions you already build with in Softr. Whether a member submits a checkout form, signs up for a paid tier, or an admin needs to issue a refund, the workflow runs end-to-end without leaving Softr.

This unlocks the patterns most Softr customers reach for first: paid member portals that charge on signup, client-facing checkout pages backed by a Softr form, internal admin tools for managing customers and payments, and finance dashboards that show charges and account balance in real time.

## Available Actions

### Customers

#### Create customer

Add a new customer to Stripe — typically from a Softr signup form, a checkout page, or a "new client" record action — capturing email, name, and any custom metadata you want to keep linked to the user.

#### Get customer

Look up a single Stripe customer by ID. Use this to surface a member's billing details inside their account page or in an admin record view.

#### List customers

Pull a list of customers from Stripe to power admin dashboards, member directories, or filtered views (for example, all customers created in the last 30 days).

#### Update customer

Keep Stripe in sync with your Softr app — update a customer's email, name, address, or metadata when the corresponding record changes in your data source.

#### Delete customer

Remove a customer from Stripe when they're deleted from your app or request account closure, keeping your billing data clean.

### Payment intents

#### Create payment intent

Start a new payment for a given amount and currency — the building block for charging members on signup, processing one-off purchases from a Softr form, or accepting payment on a custom checkout page.

#### Confirm payment intent

Confirm a payment intent to actually move the funds, completing the charge once the customer has provided their payment details.

### Charges

#### Get charge

Retrieve the details of a single charge by ID. Useful for displaying receipts, surfacing transaction details on a member's account page, or powering an admin "view payment" screen.

#### List charges

Fetch a list of charges from Stripe — by customer, by date range, or across the whole account — to feed transaction tables, revenue dashboards, or finance reports inside Softr.

#### Update charge

Update metadata or descriptions on an existing charge, for example to tag a payment with the related Softr record ID or attach internal notes.

### Coupons

#### Create coupon

Generate a new Stripe coupon — fixed amount or percentage off — directly from a Softr workflow. Perfect for spinning up promo codes for a campaign or rewarding specific user segments.

#### List coupons

Pull all available coupons from Stripe to display in a member portal, an admin discount manager, or a dropdown on your checkout form.

### Balance

#### Get balance

Fetch your current Stripe account balance, including available and pending funds, to power live finance dashboards for your team or owner-facing reports.

### Products

A **product** is the *what* you sell — a membership tier, an event, a course, or a physical item. In Stripe, a product holds one or more **prices** (see below).

#### Create product

Add a catalog product to Stripe — set its name, description, images, and any metadata — for example when an admin publishes a new membership tier or event from a Softr form.

#### Get product

Look up a single product by ID to surface its details on a public product page or an admin edit screen.

#### Get many products

Retrieve a list of products, optionally filtered to only active or only archived ones, to power a catalog, an admin product manager, or a picker on a checkout form.

#### Update product

Update a product's mutable fields — name, description, images, default price, or metadata. Set the product to inactive to **archive** it (hide it from new purchases without affecting existing subscriptions).

#### Delete product

Permanently delete a product. Stripe only allows deleting a product that has never had a price attached; for the common case, use **Update product** and set it to inactive to archive instead.

### Prices

A **price** is the *how much / how often* — `$10/month`, `$120/year`, or `$25 one-time`. One product can have many prices. Prices are largely immutable: to change an amount, create a new price and archive the old one.

#### Create price

Create a one-time or recurring price for a product. Set the amount (in the smallest currency unit — e.g. cents), currency, and, for recurring prices, the billing interval (day, week, month, or year) and interval count.

#### Get price

Retrieve a single price by ID — for example to show the amount and billing cadence on a checkout or account page.

#### Get many prices

List prices, optionally filtered to a single product, to power "show all price options for this membership / event" experiences on a native Softr page.

#### Archive price

Deactivate a price so it can no longer be used for new purchases (existing subscriptions on it are unaffected), or re-activate a previously archived price. This replaces a general "update price," which Stripe does not allow.

### Subscriptions

#### Create subscription

Subscribe a customer to one or more recurring prices — the core action for launching paid memberships. Optionally add a free trial, apply a coupon, or set the subscription to cancel at the end of the period.

#### Get subscription

Retrieve a single subscription by ID, including its status, items, and current period, to display on a member's account page.

#### Get many subscriptions

List subscriptions, filtered by customer, status, or price — for example to let a member see their own subscriptions or to power an admin churn dashboard.

#### Update subscription

Change a subscription: swap the price (upgrade / downgrade), change quantity, apply a coupon, update the payment method, or schedule cancellation at period end.

#### Cancel subscription

Cancel a subscription **immediately**. To let a member keep access until the end of the period they've already paid for — the more common membership flow — use **Update subscription** with *cancel at period end* instead.

### Invoice items

#### Create invoice item

Add a one-off line item (a custom amount or an existing price) to a customer. Pending invoice items are automatically pulled into the customer's next invoice, or into a specific draft invoice — the first step of the manual invoicing flow.

### Invoices

Invoices follow Stripe's lifecycle: **draft → open → paid / uncollectible / void**.

#### Create invoice

Create a draft invoice for a customer. Pending invoice items are pulled in automatically. Choose whether Stripe charges the saved card automatically or emails the customer a payable invoice.

#### Get invoice

Retrieve a single invoice by ID, including its status, totals, and hosted invoice URL / PDF links.

#### Get many invoices

List invoices, filtered by customer, subscription, or status — for example to show a member their invoice history.

#### Finalize invoice

Move a draft invoice to **open**, locking its line items and generating the hosted invoice page and PDF. Required before an invoice can be paid or sent.

#### Pay invoice

Attempt to collect payment on an open invoice using the customer's default (or a specified) payment method.

#### Send invoice

Email an open invoice to the customer so they can pay via the hosted invoice page (for the "send invoice" collection method).

#### Void invoice

Void an open invoice that should not be paid. Voiding is final and cannot be undone.

## Key Benefits

- **No-code payments:** Take payments from your Softr app without writing backend code or stitching together a separate checkout tool.
- **Paid member portals:** Charge users on signup, gate content behind a successful payment, and manage subscribers inside Softr.
- **Real-time billing data:** Surface customers, charges, and account balance live inside your member views and admin dashboards.
- **End-to-end workflows:** Tie payments to the rest of your app — trigger emails, update records, notify your team, and provision access in the same workflow.
- **Customer data in sync:** Keep Stripe and your Softr database aligned automatically as users sign up, update their profile, or churn.
- **Recurring billing & memberships:** Build a catalog of products and prices, subscribe members to recurring plans, and let them upgrade, downgrade, or cancel — all from inside Softr.
- **Manual invoicing:** Assemble invoices from custom line items or subscriptions, then finalize, send, or collect payment as part of an automated workflow.

## Example Use Cases

| Use Case                           | Description                                                                                                       |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **Charge on signup**               | When a new member signs up to your Softr app, create a Stripe customer and a payment intent to charge them immediately. |
| **Form-based checkout**            | Turn any Softr form into a checkout page — collect order details, create a payment intent, and confirm the charge in one workflow. |
| **Admin customer manager**         | Build an internal tool where your team can search Stripe customers, view their charges, and update their details without leaving Softr. |
| **Live revenue dashboard**         | Pull the current Stripe balance and a list of recent charges into a Softr dashboard so founders and ops teams can monitor revenue at a glance. |
| **Targeted coupon distribution**   | Generate coupons on the fly and email them to a specific user group — VIPs, churning members, or campaign signups — straight from a workflow. |
| **Refund and receipt portal**      | Let members look up their past charges from inside their account page, and let admins issue updates or annotate transactions internally. |
| **Sell memberships at multiple price points** | Publish a product with monthly and yearly prices, show both options on a Softr page, and subscribe the member to the price they pick. |
| **Self-serve subscription management** | Let members view their subscription, upgrade or downgrade the plan, or cancel at period end — without contacting support. |
| **Automated invoicing**            | Add line items to a customer, create and finalize an invoice, then email it or charge it automatically — all triggered from a Softr record action. |

## How to Connect Softr with Stripe

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Stripe action.
3. Click **Connect to Stripe** and paste your Secret API key.
4. Your Secret API key can be found in your Stripe Dashboard under **Developers → API keys**.
5. Pick the operation you need — create a customer, charge a payment, list charges, and so on.
6. Map fields from your Softr forms, records, or previous workflow steps to the Stripe action's inputs.
7. Save and activate your workflow.
