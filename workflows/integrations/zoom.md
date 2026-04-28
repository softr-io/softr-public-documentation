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

## How to Connect Softr with Zoom

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Zoom action.
3. Click the Account field and choose **Add another account** to start the OAuth flow.
4. Sign in to Zoom if prompted, review the requested permissions, and click **Allow**.
5. You are redirected back to Softr and the connected Zoom account appears in the Account field.
6. Configure your inputs (topic, start time, duration, etc.) and save.
7. Activate your workflow.
