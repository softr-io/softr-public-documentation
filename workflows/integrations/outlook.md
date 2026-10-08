# Outlook integration

Connect Outlook with your Softr applications to send transactional emails, customer confirmations, and internal alerts straight from your no-code app. Keep your members, your team, and your shared inboxes in sync — without leaving Softr.

## Overview

The Softr Outlook integration lets you send emails from your Microsoft 365 account whenever something happens in your Softr app. Trigger emails from form submissions, new member sign-ups, status changes, or scheduled workflows, and deliver them straight from the Outlook address your customers already know and trust.

Whether you're confirming a booking from a member portal, alerting a shared support inbox about a new request, or sending a personalized follow-up after a form submission, Outlook fits naturally into the apps your team and customers already rely on every day.

## Available Actions

### Send email

Send an email from your connected Outlook account to one or more recipients, with a custom subject, body, and optional CC, BCC, and attachments — all triggered by events inside your Softr app.

**Send as** (optional) — send the email from a shared mailbox or an alias instead of the connected account, for example `support@yourcompany.com`. Leave it empty to send from the connected account's own address. The connected account needs **Send As** permission on that mailbox in Microsoft 365; your Microsoft 365 administrator grants it in the Exchange admin center, and it can take up to an hour to apply. The sender's display name comes from the mailbox itself, not from the workflow.

If the connected account is not allowed to send as that mailbox, Outlook rejects the email and the step fails with `Failed to send email. Status code: 403` followed by Microsoft's `ErrorSendAsDenied` response.

## Key Benefits

- **No-code simplicity:** Build email automations visually in Softr — no SMTP setup, no developer required.
- **Send from your real address:** Emails go out from your Microsoft 365 mailbox — or from a shared mailbox such as `support@` with **Send as** — so customers see a sender they recognize.
- **Personalized at scale:** Pull form fields, member details, and record data into every message automatically.
- **Team-ready inboxes:** Route notifications to shared Outlook inboxes so the whole team can pick up replies.
- **Reliable delivery:** Lean on Microsoft 365 deliverability for transactional and member-facing email.

## Example Use Cases

| Use Case                          | Description                                                                                                   |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **Form submission confirmations** | Send a personalized thank-you email to anyone who submits a contact, booking, or application form in Softr.   |
| **New member welcome emails**     | Email new sign-ups from a member portal with onboarding instructions, login links, or next-step resources.    |
| **Internal team alerts**          | Notify a shared Outlook inbox whenever a new lead, support ticket, or high-priority record lands in your app. |
| **Status change notifications**   | Email a customer when their order, application, or request moves to a new status in your Softr database.      |
| **Approval and review requests**  | Send an approver an email with the relevant record details whenever a member submits something for review.    |
| **Scheduled digests and reports** | Email weekly or daily summaries of new records, sign-ups, or activity to managers and stakeholders.           |

## How to Connect Softr with Outlook

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the **Send email** Outlook action.
3. Click **Connect to Outlook** and sign in with your Microsoft 365 account.
4. Approve the requested permissions so Softr can send email on your behalf.
5. Choose the trigger that should send it (form submission, sign-up, record update, schedule).
6. Fill in recipients, subject, and body — using fields from your Softr forms, records, or previous workflow steps to personalize the message. To send from a shared mailbox, enter its address in **Send as**.
7. Save and activate your workflow.
