# Supabase integration

Connect Supabase with your Softr applications to read and write database records directly from your workflows — no SQL scripting required. Turn form submissions, sign-ups, and record changes into rows in your Supabase database, and pull that data back into your app in real time.

## Overview

The Softr Supabase integration lets your app create, find, update, and delete records in your Supabase database as part of a workflow. Trigger a new row from a form submission, update records when a status changes, or look up existing data to display or use in the next step — all driven by what your users do in Softr.

Whether you're building a customer portal, an internal admin tool, or a member dashboard, Supabase becomes the backend your Softr app writes to and reads from, so your existing database stays the single source of truth while Softr handles the front end and the automations. Supabase connects to your workflows through Softr's SQL / Database action, using your project's PostgreSQL credentials.

## Available Actions

### Find record

Look up the first record that matches your conditions — perfect for fetching a customer, order, or profile to display in your app or use in a later step.

### Find multiple records

Return every record that meets your criteria, so you can power a live list, dashboard, or digest from your Supabase data.

### Add record

Create a new record whenever a workflow runs — turn a form submission or sign-up into a row in your database instantly.

### Update record

Change a single record automatically as things happen in your app, such as updating a status or contact detail.

### Update multiple records

Update many records at once — ideal for bulk status changes or applying the same update across a set of rows.

### Delete record

Remove a single record that's no longer needed as work is cancelled or cleaned up.

### Delete multiple records

Clear out a batch of records at once to keep your database tidy.

## Key Benefits

- **No-code database access:** Read from and write to your Supabase database visually inside Softr — no SQL or backend code required.
- **Your data stays the source of truth:** Keep your existing Supabase backend and let Softr handle the front end and automations on top of it.
- **Always-current pickers:** Databases, schemas, tables, and fields load live from your connected project, so your options stay up to date.
- **Real-time two-way sync:** New submissions become rows the moment they arrive, and record changes flow back into your app instantly.
- **Custom queries when you need them:** Drop in a custom SQL query for anything the standard actions don't cover.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Form-to-database intake** | A Softr form submission adds a new record to your Supabase table with all the submitted details. |
| **User provisioning on sign-up** | When a new member signs up, create their record in Supabase so their data is ready across your app. |
| **Status sync** | When a record moves to "In progress" in your Softr app, update the matching Supabase row automatically. |
| **Live data dashboard** | Use Find multiple records to power a Softr list block that always reflects your latest Supabase data. |
| **Bulk updates** | Update multiple records at once — for example, mark a batch of orders as shipped from an admin action. |
| **Automated cleanup** | Delete records that are cancelled or expired to keep your database tidy without manual work. |

## How to Connect Softr with Supabase

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a **SQL / Database** action — add, find, update, or delete a record.
3. Under **Account**, connect your Supabase database as a data source using your Supabase PostgreSQL (PSQL) credentials. See the [Supabase data source guide](/data-sources/supabase) for the exact steps. (Supabase is available on Professional plans and higher.)
4. Pick the **database**, **schema**, and **table** the action should work with.
5. Map fields from your Softr forms, records, or previous workflow steps to the action's inputs — or write a custom **SQL Query** for advanced cases.
6. Save and activate your workflow.
