# Google Sheets integration

Connect Google Sheets with your Softr applications to turn any spreadsheet into a live backend for your no-code app. Capture form submissions, sync member data, build internal dashboards, and keep an audit trail of user activity — all without leaving Softr.

## Overview

The Softr Google Sheets integration lets your app read from and write to any Google Sheet you own or have access to. Add new rows when users submit forms, look up records to display in member dashboards, update data when statuses change, and clean up stale entries automatically — every change happens in real time as people use your Softr app.

Google Sheets fits naturally into Softr workflows wherever you'd otherwise need a database: lightweight CRMs, signup logs, internal request trackers, exportable reports, and member-facing portals backed by a sheet your team already maintains.

## Available Actions

### Add row

Append a new row to a Google Sheet whenever a user submits a form, signs up, or triggers a workflow in your Softr app.

### Get row

Look up a single row by a matching value to display its data in a Softr block or use it in the next workflow step.

### Get rows

Retrieve multiple rows from a sheet — filtered or in full — to power lists, dashboards, and reports inside your app.

### Update row

Find a row by a matching value and update its fields when a record changes, a status moves forward, or a member edits their profile.

### Update rows

Apply the same update across multiple matching rows in one step, ideal for bulk status changes or batch corrections.

### Delete row

Remove a single row from a sheet when a user cancels, a request is resolved, or stale data needs to go.

### Delete rows

Clear out multiple matching rows at once to keep your sheet tidy after bulk actions or scheduled clean-ups.

## Key Benefits

- **No-code simplicity:** Use any spreadsheet as a backend for your Softr app with a few clicks — no databases, no SQL, no setup.
- **Real-time sync:** Every form submission, profile update, or record change in Softr is reflected in your sheet instantly.
- **Familiar to your team:** Keep working in the tool your team already knows while powering rich, dynamic Softr apps on top of it.
- **Read and write in both directions:** Push data into sheets and pull it back into Softr lists, profile blocks, or dashboards.
- **Bulk-friendly:** Update or clean up many rows at once to keep large datasets manageable without manual work.

## Example Use Cases

| Use Case                          | Description                                                                                          |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Form submissions to a sheet**   | Capture every Softr form entry — leads, applications, support requests — as a new row in Google Sheets. |
| **Member portal backed by a sheet** | Power a members-only directory, course catalog, or resource hub with data your team manages in a spreadsheet. |
| **Internal dashboards**           | Pull rows from an operations sheet into a Softr admin dashboard so your team can review and act on the latest data. |
| **Status updates and edits**      | When a user changes a record in Softr, update the matching row in your sheet to keep both in sync.    |
| **Audit trail of user actions**   | Log every key action — sign-ups, purchases, approvals — to a Google Sheet for reporting and compliance. |
| **Exports and weekly reports**    | Build scheduled workflows that gather data from your app and write clean reports to a shared sheet your team can review. |

## How to Connect Softr with Google Sheets

1. Open your Softr app and go to **Integrations → Google Sheets**.
2. Click **Connect Google Sheets** and sign in with your Google account.
3. Authorize Softr to access the sheets you want to use in your workflows.
4. Add a Google Sheets action to a workflow and pick the spreadsheet and worksheet you want to read from or write to.
5. Map fields from your Softr forms, records, or previous workflow steps to the columns in your sheet.
6. Save and activate your workflow.
