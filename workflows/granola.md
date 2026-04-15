# Granola integration

Connect Granola with your Softr applications to automate meeting workflows, access AI-powered meeting summaries, and keep your team aligned. Build workflows that react to new or updated meeting notes — all without code.

## Overview

The Softr Granola integration allows you to connect your no-code apps with your Granola meeting notes. Automatically retrieve meeting summaries, attendee lists, and calendar event details whenever a new meeting is recorded or an existing note is updated. Keep your team informed and your records up to date without manual effort.

With Softr, you can list and retrieve meeting notes, access AI-generated summaries, and trigger workflows when new meetings are captured or notes are modified in Granola.

## Available Actions

### List Notes

Retrieve a paginated list of meeting notes with optional date filters. Only notes with completed AI summaries are returned. Supports cursor-based pagination for large result sets.

### Get Note

Retrieve full details of a single meeting note, including the AI-generated summary, attendees, calendar event metadata, folder memberships, and optionally the full transcript.

## Available Triggers

### Note Created

Fires whenever a new meeting note with a completed AI summary appears in Granola. Use this to send notifications, update records, or trigger follow-up workflows.

### Note Updated

Fires when an existing meeting note is updated (summary regeneration, title edits, folder changes, etc.). Use this to keep downstream records in sync.

## Key Benefits

- **No-code simplicity:** Set up and manage your Granola workflows visually in Softr, without any technical setup.
- **AI-powered summaries:** Access Granola's AI-generated meeting summaries directly in your workflows.
- **Event-driven automation:** React to new or updated meeting notes with custom workflows.
- **Team alignment:** Automatically share meeting outcomes, action items, and attendee details with your team.

## Example Use Cases

| Use Case                            | Description                                                                                   |
| :---------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Meeting summary to Slack**        | Automatically post a meeting summary to a Slack channel when a new note is created.           |
| **CRM update after meetings**       | Update a CRM record with meeting notes and attendees when a note is created or updated.       |
| **Action item tracking**            | Create tasks in your project management tool based on meeting summaries.                      |
| **Meeting log database**            | Automatically add new meeting notes to a Softr database for searchable records.               |
| **Follow-up email automation**      | Send follow-up emails to meeting attendees after a note is created.                           |

## How to Connect Softr with Granola

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Granola action or trigger.
3. Click **Connect Granola** and enter your Granola API key.
4. Your API key can be found in your Granola workspace settings (Business or Enterprise plan required). Keys are prefixed with `grn_`.
5. Configure your inputs (date filters, note ID, etc.) and save.
6. Activate your workflow.
