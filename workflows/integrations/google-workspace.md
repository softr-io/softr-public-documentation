# Google Workspace integration

Connect Google Workspace with your Softr applications to automate user lifecycle management, group provisioning, and identity workflows. Build automations that create accounts when someone signs up, suspend access when employees leave, and keep distribution lists in sync — all without code.

## Overview

The Softr Google Workspace integration connects your no-code apps with the Google Workspace Admin Directory. Provision new accounts, update profiles, manage suspensions, and control group membership directly from form submissions, member sign-ups, or status changes inside your Softr app. The connection requires a Google Workspace administrator to authenticate, so you can run sensitive directory operations safely from a workflow.

A typical Softr use case: a form-driven onboarding portal where a new contractor record automatically creates a Workspace user, adds them to the right team distribution list, and forces a password change at first sign-in. When their record is archived, suspension and group removal happen the same way — no IT ticket required.

## Available Actions

### Create user

Provision a new Google Workspace user with first name, last name, username, domain, and an initial password. Optionally require a password change on first sign-in (recommended).

### Update user

Update an existing user's name, primary email, password, or org unit assignment. Only the fields you supply are modified.

### Suspend user

Suspend a user account immediately and record an optional reason. Use this for offboarding without permanently deleting the account.

### Delete user

Permanently delete a Google Workspace user. Deletion is irreversible after the ~20-day account-purge window, so reserve this for confirmed offboarding.

### Get user

Retrieve a single user's full profile, including name, email aliases, org unit, last login time, and any custom schema fields.

### List users

List users in the workspace with optional filters by domain, query string, sort order, and pagination. Returns the page of results plus a cursor for the next page.

### Find user by email

Look up a user by primary email or alias. Returns whether the user was found and the user resource if so — handy for checking whether a record-driven account already exists before creating one.

### Create group

Create a new group (distribution list, mailing list, or team alias) with an email address, display name, and description.

### Update group

Update an existing group's name, email, or description.

### Delete group

Delete a Google Workspace group.

### Get group

Retrieve a single group's profile, including aliases.

### List groups

List groups in the workspace with optional filters by domain, user membership, or query string.

### Find group by email

Look up a group by email or alias.

### Add user to group

Add a user to an existing group with a specified role (Owner, Manager, or Member) and delivery setting.

### Remove user from group

Remove a user from a group's membership.

## Triggers

### User created

Triggers when a new Google Workspace user is created. The integration polls the Directory API at a regular interval and emits the full user resource for each new account.

### User updated

Triggers when an existing user's profile is modified. Useful for syncing identity changes back into your Softr app or downstream systems.

## Key Benefits

- **No-code simplicity:** Wire identity automations directly to forms, sign-ups, or record updates in Softr — no scripts, no scheduled jobs.
- **Lifecycle automation:** Provision, update, suspend, and delete accounts as a natural side-effect of business events, not a manual checklist.
- **Group hygiene at scale:** Keep mailing lists and team groups aligned with org changes without IT support tickets.
- **Admin-only safety:** All operations run as a Workspace administrator authorized once, so end users never see or handle credentials.
- **Real-time visibility:** Trigger downstream workflows the moment a user is created or updated, instead of polling on cron.

## Example Use Cases

| Use Case                              | Description                                                                                         |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| **Onboarding new hires**              | A form submission in Softr provisions a Workspace account and adds the hire to the right groups.   |
| **Contractor offboarding**            | Marking a contractor record as inactive suspends their Workspace user and removes them from groups. |
| **Self-service mailing list sign-up** | Members in a Softr portal opt into team distribution lists; the workflow toggles their group membership. |
| **Promotion / role change**           | Changing a user's role in your Softr app updates their org unit and group memberships in Workspace. |
| **Account audit dashboard**           | A list-users action populates a Softr dashboard so admins can see all active accounts at a glance. |
| **New-user welcome flow**             | The User Created trigger fires a downstream workflow — sending a welcome email, posting to Slack, or creating a CRM contact. |

## How to Connect Softr with Google Workspace

1. Open your Softr app and go to **Integrations → Google Workspace**.
2. Click **Connect Google Workspace**. You'll be redirected to Google to sign in with a Workspace administrator account.
3. Review and approve the requested admin scopes (user, group, group member, domain, schema, and org unit access).
4. Once redirected back to Softr, choose the Google Workspace actions or triggers you want to add to your workflow.
5. Configure each step (e.g. select the domain for new users, set the role for group additions) and connect it to a trigger.
6. Save and activate your workflow.
