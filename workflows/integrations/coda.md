# Coda integration

Connect Coda with your Softr applications to bring your docs and tables to life inside the tools you build. Pull rows from any Coda table into Softr lists, dashboards, and member portals — and keep your no-code app and your Coda workspace working from the same source of truth, without writing a single line of code.

## Overview

The Softr Coda integration lets you read rows from your Coda tables directly inside your no-code app. Form submissions, member actions, scheduled runs, and other workflow triggers can fetch the right rows from Coda so your app always reflects what your team is tracking.

This fits naturally with the kinds of apps Softr customers build every day: client portals that surface project status from a Coda tracker, internal dashboards that show live operational data to teammates who don't have a Coda seat, and member-facing views powered by the tables your team already maintains in Coda.

## Available Actions

### List rows

Pull rows from a Coda table into a Softr list block, dashboard, or admin view — ideal for showing project status, inventory, or any tracked data to clients and teammates. Pick the doc and table, optionally filter to just the rows you need, and map the columns into your Softr app.

### Get row

Look up a single Coda row by its ID to display its details inside your Softr app or use its values later in the workflow.

### Create or update row

Add a new row to a Coda table from a form submission or workflow step — or, by setting key columns, update the matching row when one already exists so you never create duplicates.

### Update row

Change the column values of an existing Coda row when something happens in your Softr app, such as a status change or an approval.

### Delete row

Remove a row from a Coda table as part of a workflow — for example when a request is cancelled or a record is archived in your Softr app.

## Key Benefits

- **No-code data access:** Bring Coda tables into your Softr app visually — no scripts, no API calls to manage.
- **Always up to date:** Each workflow run fetches the latest rows, so your dashboards and portals reflect what's in Coda right now.
- **Client-friendly views:** Give customers a polished Softr portal backed by the Coda tables your team already maintains, without handing out Coda seats.
- **Targeted results:** Filter rows by column value so each view shows exactly the data that matters.
- **Built for the apps you ship:** Power member portals, admin tools, and dashboards from a single Coda source of truth.

## Example Use Cases

| Use Case                          | Description                                                                                              |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Project status dashboard**      | Surface live rows from a Coda project tracker inside a Softr list block so non-Coda users can follow progress. |
| **Client-facing portal**          | Show each client only their rows from a shared Coda table, filtered by company or account.               |
| **Internal operations view**      | Pull inventory, orders, or requests from Coda into an admin dashboard your team can scan at a glance.     |
| **Member directory**              | Power a member portal from a Coda table of people, surfacing names, roles, and details in Softr.          |
| **Scheduled data digest**         | On a recurring workflow, fetch the latest rows from Coda to feed a report or summary view.                |

## How to Connect Softr with Coda

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Coda action.
3. Click **Connect to Coda** and paste your Coda API token. You can generate one in your Coda account settings at [coda.io/account](https://coda.io/account).
4. Pick the doc and table you want to work with.
5. Map the columns from your Coda table to your Softr list, records, or later workflow steps — and optionally add a filter to narrow the rows returned.
6. Save and activate your workflow.
