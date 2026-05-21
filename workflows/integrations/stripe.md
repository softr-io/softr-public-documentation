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

## Key Benefits

- **No-code payments:** Take payments from your Softr app without writing backend code or stitching together a separate checkout tool.
- **Paid member portals:** Charge users on signup, gate content behind a successful payment, and manage subscribers inside Softr.
- **Real-time billing data:** Surface customers, charges, and account balance live inside your member views and admin dashboards.
- **End-to-end workflows:** Tie payments to the rest of your app — trigger emails, update records, notify your team, and provision access in the same workflow.
- **Customer data in sync:** Keep Stripe and your Softr database aligned automatically as users sign up, update their profile, or churn.

## Example Use Cases

| Use Case                           | Description                                                                                                       |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **Charge on signup**               | When a new member signs up to your Softr app, create a Stripe customer and a payment intent to charge them immediately. |
| **Form-based checkout**            | Turn any Softr form into a checkout page — collect order details, create a payment intent, and confirm the charge in one workflow. |
| **Admin customer manager**         | Build an internal tool where your team can search Stripe customers, view their charges, and update their details without leaving Softr. |
| **Live revenue dashboard**         | Pull the current Stripe balance and a list of recent charges into a Softr dashboard so founders and ops teams can monitor revenue at a glance. |
| **Targeted coupon distribution**   | Generate coupons on the fly and email them to a specific user group — VIPs, churning members, or campaign signups — straight from a workflow. |
| **Refund and receipt portal**      | Let members look up their past charges from inside their account page, and let admins issue updates or annotate transactions internally. |

## How to Connect Softr with Stripe

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Stripe action.
3. Click **Connect to Stripe** and paste your Secret API key.
4. Your Secret API key can be found in your Stripe Dashboard under **Developers → API keys**.
5. Pick the operation you need — create a customer, charge a payment, list charges, and so on.
6. Map fields from your Softr forms, records, or previous workflow steps to the Stripe action's inputs.
7. Save and activate your workflow.
