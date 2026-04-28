# Zoom integration

Connect Zoom with your Softr applications to automate meeting scheduling, share join links instantly, and keep your team aligned. Build workflows that create Zoom meetings on demand and push the details to the people and tools that need them — all without code.

## Overview

The Softr Zoom integration allows you to connect your no-code apps with your Zoom account. Automatically schedule Zoom meetings whenever key events occur in your Softr app — such as form submissions, booking confirmations, or status changes — and use the returned meeting details (join URL, meeting ID, password) in any downstream step of your workflow.

With Softr, you can spin up scheduled Zoom meetings on the fly and feed the details into emails, database records, Slack messages, or any other workflow action.

## Available Actions

### Create meeting

Schedule a new Zoom meeting on the connected user's account. Configure the topic, start time, duration, timezone, password, agenda, and meeting options such as host video, participant video, mute upon entry, waiting room, join before host, and automatic recording. The action returns the meeting ID, join URL, start time, password, and topic so they can be used by subsequent workflow steps.

## Key Benefits

- **No-code simplicity:** Set up and manage your Zoom workflows visually in Softr, without any technical setup.
- **Instant scheduling:** Create Zoom meetings automatically the moment a trigger fires, with no manual setup.
- **Customizable meeting options:** Control video, audio, recording, and waiting room behavior on every meeting.
- **Seamless handoff:** Pass meeting details into any downstream action — email, database, Slack, and more.

## Example Use Cases

| Use Case                          | Description                                                                                       |
| :-------------------------------- | :------------------------------------------------------------------------------------------------ |
| **Booking confirmation**          | Create a Zoom meeting when a customer books a session and email them the join link automatically. |
| **Sales call automation**         | Schedule a Zoom call when a new lead reaches a qualified stage in your CRM.                       |
| **Interview scheduling**          | Generate a Zoom meeting for each candidate and send the link to both interviewer and candidate.   |
| **Office hours and consultations**| Spin up a Zoom meeting per submission and store the join URL in a Softr database.                 |
| **Internal team syncs**           | Auto-create a Zoom meeting and post the join link to a Slack channel when a workflow runs.        |

## Prerequisites

- An active Softr account with access to **Workflows**.
- A Zoom account with permission to create meetings (any paid or free Zoom plan that allows scheduling meetings via the Zoom Web Portal).
- Permission to authorize third-party apps on your Zoom account. If your Zoom account is managed by an admin, the admin may need to pre-approve the Softr app on the Zoom Marketplace.

## Adding the Softr Zoom integration

Follow these steps to install and authorize the Zoom integration inside Softr.

1. Sign in to your Softr workspace and open the application where you want to use the integration.
2. In the left sidebar, click **Workflows** and either open an existing workflow or click **New workflow**.
3. Choose a trigger for your workflow (for example, a one-time schedule, a form submission, or a record creation).
4. On the workflow canvas, click the **+** below the trigger and select **Add a new action**.
5. In the **Select an action** modal, search for `Zoom` and pick **Zoom → Create meeting**.
6. The action panel opens on the **Settings** tab. In the **Account** field, click the dropdown and choose **Add another account**.
7. A confirmation dialog appears. Click **Continue** to be redirected to Zoom's OAuth consent screen.
8. Sign in to your Zoom account if prompted, review the requested permissions, and click **Allow**.
9. You are redirected back to Softr. The connected Zoom account now appears in the **Account** field, formatted as `Zoom — <Display Name> (<email>) #N`.
10. Fill in the action inputs (topic, start time, duration, etc.), click **Continue**, and turn on the workflow.

If anything goes wrong during installation, see the [Troubleshooting](#troubleshooting) section below.

## Using the Softr Zoom integration

Once the integration is connected, you can use the **Create meeting** action in any Softr workflow.

### Create meeting

Schedules a new meeting on the connected Zoom account.

**Inputs**

- **Account** — the connected Zoom account that will own the meeting.
- **Topic** (required) — the meeting title shown in Zoom and in the join page.
- **Start time** — the date and time the meeting is scheduled to begin. Supports static values, dynamic values from previous workflow steps, and the **Current date & time** chip.
- **Duration** — meeting length in minutes.
- **Timezone** — the IANA timezone for the start time (for example, `Europe/Paris`).
- **Password** — optional 6+ character meeting password.
- **Agenda** — optional description shown in the meeting details and calendar invites.
- **Host video / Participant video** — whether host and participant cameras are on when joining.
- **Mute upon entry** — automatically mute participants as they join.
- **Waiting room** — require participants to be admitted from a waiting room.
- **Join before host** — allow participants to join before the host arrives.
- **Auto recording** — record the meeting automatically (`none`, `local`, or `cloud`).

**Outputs**

The action returns the meeting details so they can be used in any subsequent workflow step:

- `meetingId` — the Zoom meeting ID.
- `joinUrl` — the URL participants use to join the meeting.
- `startTime` — the scheduled start time returned by Zoom.
- `password` — the meeting password.
- `topic` — the meeting topic.

**Tips**

- Use the **Test** button on the action's **Testing** tab to create a real meeting on your Zoom account and inspect the response before turning the workflow on.
- Reference the action's outputs in later steps using `${actionId.field}` (for example, send `${createMeeting.joinUrl}` by email).
- Sensitive fields like the meeting password are obfuscated in workflow logs.

## Removing the Softr Zoom integration

To remove the Zoom integration, disconnect it from Softr. This fully deauthorizes the app and revokes the OAuth tokens.

1. Open your Softr workspace and navigate to the workflow that uses Zoom.
2. Open the Zoom action and click the **Account** dropdown.
3. Remove the connected Zoom account from the list (or disconnect it from your workspace's connected accounts under **Settings → Integrations**).
4. Softr automatically calls Zoom's token revocation endpoint to invalidate the OAuth tokens for that account.

After removal, Softr deletes the stored OAuth tokens and any cached account metadata associated with that Zoom user. The connected account no longer appears in the **Account** dropdown, and workflows that referenced it will fail with an authentication error on their next run until a new Zoom account is connected. No data from your Zoom account (other than the basic profile fields used to label the connected account) is stored by Softr, so no additional data deletion steps are required.

## Troubleshooting

**The OAuth popup closes without connecting my account.**
- Make sure third-party cookies and popups are enabled for `softr.io` in your browser.
- If your Zoom account is managed by an organization, an admin may need to pre-approve the Softr app on the Zoom Marketplace before users can install it.

**The Account dropdown is empty after authorization.**
- Refresh the workflow editor and reopen the action panel.
- If the connected account still doesn't appear, remove the integration (see above) and reconnect.

**The Create meeting action fails with an authentication error.**
- The connected Zoom account may have been removed from the Zoom Marketplace, or the OAuth tokens may have been revoked. Reconnect the account from the action's **Account** field.

**The meeting is created but the start time is wrong.**
- Check the **Timezone** input. The start time is interpreted in the timezone you select on the action.

**Scheduling meetings on behalf of another user fails.**
- Scheduling for another user requires that the other user has granted scheduling privileges on Zoom and that your Zoom plan supports scheduling privileges.

If your issue isn't covered here, please reach out using the [Contact support](#contact-support) section below.

## FAQ

**Which Zoom permissions does Softr request?**

Softr requests two scopes: `meeting:write:meeting` (to create scheduled meetings on your account) and `user:read:user` (to read your basic profile so the connected account can be labeled in Softr's UI). No other scopes are requested.

**Does Softr store my Zoom password or meeting recordings?**

No. Softr never sees your Zoom password — authorization happens through Zoom's OAuth flow. Softr does not access, download, or store Zoom recordings.

**Can multiple Zoom accounts be connected to the same Softr workspace?**

Yes. You can connect multiple Zoom accounts and pick which one each action uses via the **Account** dropdown.

**Will Softr send me email updates about the integration?**

Softr only sends transactional emails related to your workspace. You can manage email preferences from your Softr account settings.

**What happens to scheduled meetings if I disconnect the integration?**

Meetings that were already created on Zoom remain on the Zoom account — they are not deleted. Future workflow runs that reference the disconnected account will fail until a new Zoom account is connected.
