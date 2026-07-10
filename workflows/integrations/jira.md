# Jira integration

Connect Jira with your Softr applications to turn app activity into tracked work. Build workflows that open Jira issues automatically — from form submissions, new sign-ups, or record changes — so nothing your team needs to act on gets lost.

## Overview

The Softr Jira integration links your no-code apps directly to your Jira Cloud site. Whenever something happens in Softr — a customer submits a bug report, a record is flagged, a new request comes in — you can automatically create a Jira issue in the right project, with the right type, assignee, priority, and details filled in from your workflow.

Whether you're building a client portal, an internal operations tool, or a support dashboard, the Jira integration closes the gap between what happens in your Softr app and the work your team tracks in Jira.

## Available Actions

### Create issue

Open a new issue in a Jira project with a summary, description, issue type, assignee, priority, labels, and due date — all set dynamically from your Softr workflow. Project, issue type, assignee, and priority are chosen from live dropdowns pulled straight from your connected Jira site.

### Get issue

Retrieve the full details of a specific issue by its key — summary, status, assignee, priority, and timestamps — so you can use live Jira data in later workflow steps.

### Update issue

Change an existing issue's summary, description, assignee, priority, labels, or due date to keep Jira in sync with what's happening in your Softr app.

### Delete issue

Remove an issue from Jira by its key — with the option to delete its subtasks too — for cleanup or voided-request workflows.

### Search issues

Find issues with a JQL query and return the matching set, so you can power lists, dashboards, reports, or conditional logic inside your Softr app.

### Add comment

Post a comment to an issue — ideal for logging Softr form responses, status updates, or context straight onto the relevant Jira issue.

### List comments

Retrieve the comments on an issue to display an activity feed, drive follow-ups, or surface the latest discussion inside your Softr app.

## Key Benefits

- **No-code simplicity:** Configure every Jira action visually in Softr — no code required beyond the one-time API token setup.
- **Instant issue creation:** Turn any Softr form submission or record event into a Jira issue the moment it happens.
- **Always-current options:** Projects, issue types, assignees, and priorities load directly from your Jira account, so you never hardcode IDs.
- **Right work, right place:** Route each issue to the correct project and assignee automatically, based on your Softr data.
- **Ops-ready portals:** Build intake forms and internal tools in Softr that feed work straight into Jira, where your team already plans and ships.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Bug report intake** | Create a Jira issue automatically when a user submits a bug report form in your Softr portal. |
| **Feature request tracking** | Turn feature-request form submissions into Jira stories in your product backlog, tagged and assigned. |
| **Escalation from records** | When a record is flagged as high priority in your Softr database, open an urgent Jira issue for the responsible team. |
| **New client onboarding** | Auto-create an onboarding issue in Jira when a new member signs up to your Softr app. |
| **Internal request desk** | Let employees file IT or ops requests through a Softr form that creates a Jira issue in the right project. |

## How to Connect Softr with Jira

1. Open your Softr workspace and go to **Workflows**.
2. Create a new workflow or open an existing one, then add a Jira action.
3. In the **Account** field, click **Add another account** and enter your Jira **domain** (e.g. `https://your-team.atlassian.net`), your **email address**, and an **API token**.
4. To generate an API token, log into [id.atlassian.com](https://id.atlassian.com), go to **Security → API tokens**, and click **Create API token**.
5. Click **Save** — Softr verifies your credentials and connects the account.
6. Pick the **project** and **issue type**, map the remaining fields from your Softr forms or previous workflow steps, then activate your workflow.
