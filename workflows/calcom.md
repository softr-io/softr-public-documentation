# Cal.com integration

Connect Cal.com with your Softr applications to automate scheduling, manage bookings, and keep your team updated in real time. Build workflows that create, reschedule, or cancel bookings and react to scheduling events — all without code.

## Overview

The Softr Cal.com integration allows you to connect your no-code apps with your Cal.com scheduling account. Automatically manage bookings from your Softr app whenever key events occur, such as form submissions, user sign-ups, or data changes. Keep your calendar organized and your attendees informed without manual effort.

With Softr, you can create new bookings, look up existing ones, cancel or reschedule meetings, and trigger workflows when booking events happen in Cal.com.

## Available Actions

### Create Booking

Create a new booking for a specific event type. Specify the attendee's name, email, time zone, and preferred start time. Optionally include a custom location, guest emails, and metadata.

### Get Booking

Retrieve the full details of an existing booking by its unique identifier, including status, attendees, hosts, and meeting URL.

### List Bookings

Search and filter your bookings by status, event type, attendee email, date range, and more. Supports pagination for large result sets.

### Cancel Booking

Cancel an existing booking with an optional cancellation reason. All attendees are automatically notified.

### Reschedule Booking

Move an existing booking to a new time. The original booking is cancelled and a new one is created with the updated schedule.

## Available Triggers

### Booking Created

Fires whenever a new booking is created in Cal.com. Use this to send confirmations, update records, or notify your team.

### Booking Cancelled

Fires when a booking is cancelled. Use this to trigger follow-up actions, update your CRM, or reassign resources.

### Booking Rescheduled

Fires when a booking is rescheduled to a new time. Use this to update calendars, notify stakeholders, or adjust related records.

### Meeting Ended

Fires when a meeting ends. Use this to trigger post-meeting workflows such as sending follow-up emails or creating summary records.

## Key Benefits

- **No-code simplicity:** Set up and manage your Cal.com workflows visually in Softr, without any technical setup.
- **Real-time scheduling:** Create and manage bookings instantly from your Softr app.
- **Event-driven automation:** React to booking events (created, cancelled, rescheduled, ended) with custom workflows.
- **Team coordination:** Keep your team aligned with automated notifications and record updates.

## Example Use Cases

| Use Case                            | Description                                                                             |
| :---------------------------------- | :-------------------------------------------------------------------------------------- |
| **Automated booking from forms**    | Create a Cal.com booking when a visitor submits a scheduling request form in Softr.     |
| **Cancellation follow-up**          | Send a follow-up email or update your CRM when a booking is cancelled.                  |
| **Rescheduling notifications**      | Notify a Slack channel or update a record when a meeting is rescheduled.                |
| **Post-meeting actions**            | Automatically create a summary record or send a feedback request after a meeting ends.  |
| **Booking lookup in client portal** | Let users view their booking details by entering a booking ID in your Softr app.        |

## How to Connect Softr with Cal.com

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Cal.com action or trigger.
3. Click **Connect Cal.com** and authorize your Cal.com account.
4. Select the actions or triggers you want to include in your workflow.
5. Configure your inputs (event type, attendee details, etc.) and save.
6. Activate your workflow.
