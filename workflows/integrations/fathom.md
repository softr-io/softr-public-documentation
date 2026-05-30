# Fathom integration

Connect Fathom with your Softr applications to automate meeting follow-ups, route AI-generated meeting content into your tools, and keep your team aligned. Build workflows that react to newly processed Fathom meetings — all without code.

## Overview

The Softr Fathom integration lets you connect your no-code apps with Fathom, the AI meeting assistant that records, transcribes, and summarizes calls. List recent meetings, fetch summaries and transcripts on demand, and trigger workflows the moment Fathom finishes processing a recording.

With Softr, you can fan out meeting summaries to Slack or email, push action items into a CRM or project tool, archive transcripts to a database, and any other automation built on top of meeting outcomes.

## Available Actions

### List Meetings

Retrieve up to 30 most-recent Fathom meetings, with optional filters by created-date range, recorder email, team, and invitee email domain. You can opt-in to include the AI summary, transcript, action items, and CRM matches per meeting. Pagination across Fathom's cursor pages is handled internally.

### Get Recording Summary

Fetch the AI-generated summary (Markdown) for a single recording by its ID.

### Get Recording Transcript

Fetch the full speaker-tagged transcript for a single recording by its ID. Long meetings can produce large payloads.

## Available Triggers

### New Meeting Content Ready

Fires when Fathom finishes processing a meeting and its content (summary, transcript, action items, CRM matches) becomes available. You choose:
- **Recording scope** — which meetings should trigger this workflow (your recordings, recordings shared with you, team-shared recordings).
- **Content blocks** — which content fields to include in the trigger payload (summary, transcript, action items, CRM matches). At least one must be enabled.

The trigger payload mirrors the Meeting object returned by **List Meetings**, plus a `type` discriminator. Webhook deliveries are signed using the [Standard Webhooks](https://www.standardwebhooks.com/) scheme; Softr verifies the signature on every delivery.

## Key Benefits

- **No-code simplicity:** Configure Fathom actions and triggers visually in Softr, no API plumbing required.
- **End-to-end meeting automation:** From "meeting recorded" to "Slack message + CRM update + task created" — all in one workflow.
- **Selective payloads:** Only fetch what you need (summary, transcript, action items, CRM matches) to keep workflows fast.
- **Secure by default:** Standard Webhooks signature verification ensures only genuine Fathom deliveries trigger your workflow.

## Example Use Cases

| Use Case                              | Description                                                                                   |
| :------------------------------------ | :-------------------------------------------------------------------------------------------- |
| **Meeting summary to Slack**          | Post the AI summary of every new meeting to a Slack channel.                                  |
| **CRM update after sales calls**      | Update HubSpot or Stripe records with action items and notes from sales calls.                |
| **Action item tracking**              | Create tasks in monday.com or ClickUp based on the action items extracted by Fathom.          |
| **Transcript archive**                | Save full transcripts to a Softr database or Notion page for searchable records.              |
| **Follow-up email automation**        | Send a recap email to invitees after every customer meeting.                                  |
| **Meeting digest**                    | Aggregate the day's recordings into a single end-of-day summary using **List Meetings**.      |

## How to Connect Softr with Fathom

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Fathom action or trigger.
3. Click **Connect Fathom** and enter your Fathom API key.
4. To generate an API key, sign in to Fathom and navigate to **User Settings → API Access**. The key grants access to meetings recorded by you or shared to your team.
5. For triggers, choose the recording scope and content blocks you want to receive in the payload.
6. Configure inputs (date filters, recording ID, etc.) and save.
7. Activate your workflow — Softr will register the webhook with Fathom automatically when needed.

## Rate Limits

Fathom enforces a rate limit of **60 requests per 60-second rolling window** per user, shared across all of a user's API keys. Softr's Fathom client respects this limit and backs off automatically when throttled.
