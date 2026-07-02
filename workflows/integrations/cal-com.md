# Cal.com integration

Connect Cal.com with your Softr applications to turn scheduling into a fully automated part of your app — create, reschedule, and cancel bookings from your workflows, and start workflows the moment a meeting is booked, moved, cancelled, or ends. Build booking flows for onboarding, sales, and support without any manual back-and-forth.

## Overview

The Softr Cal.com integration moves data both ways. From your Softr app into Cal.com: whenever a form is submitted, a member signs up, or a record changes, your workflow can create a booking on the right event type, reschedule or cancel an existing one, or look bookings up to use in later steps. From Cal.com back into Softr: webhook triggers fire your workflows the moment a booking is created, rescheduled, or cancelled, or a meeting ends.

This pairs naturally with the way Softr apps are built — booking forms, member portals, and client-facing dashboards. Map fields from your Softr forms, records, or previous workflow steps to the booking's details, and react to real scheduling events to send follow-ups, update records, or notify your team.

## Available Actions

### Create booking

Create a booking on a Cal.com event type, using the attendee details and time you map from your app — great for turning a form submission into a confirmed meeting.

### Reschedule booking

Move an existing booking to a new time by its unique reference, with an optional reason that's shared with the attendee and host.

### Cancel booking

Cancel a booking by its unique reference, with an optional cancellation reason shown to the attendee and host.

### Get booking

Retrieve a single booking by its unique reference and use its details in later workflow steps — for example, to read the attendee and time of the booking that fired a trigger.

### List bookings

List bookings from Cal.com with optional filters, and use the results in the rest of your workflow.

## Available Triggers

### Booking created

Starts a workflow when a new booking is created in Cal.com.

### Booking rescheduled

Starts a workflow when a booking is moved to a new time in Cal.com.

### Booking cancelled

Starts a workflow when a booking is cancelled in Cal.com.

### Meeting ended

Starts a workflow when a Cal.com meeting has ended — perfect for post-call follow-ups.

## Key Benefits

- **No-code scheduling automation:** Create, move, and cancel bookings straight from your Softr workflows — no Zaps, scripts, or developer help required.
- **Two-way sync:** Push bookings into Cal.com with actions, and react to real scheduling events with triggers, all in one workflow builder.
- **Real-time follow-ups:** Kick off a workflow the instant a meeting is booked, rescheduled, cancelled, or ends — send confirmations, reminders, or thank-you messages automatically.
- **Personalized member experiences:** Turn form submissions, sign-ups, and record changes into confirmed meetings tied to the right event type and person.
- **Everything in one place:** Keep your bookings and your app's records in step, so your team always sees the latest scheduling activity.

## Example Use Cases

| Use Case                          | Description                                                                                                                          |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Booking from form submissions** | When a prospect submits a "Book a call" form, create a Cal.com booking on the right event type with the details they provided.      |
| **Onboarding calls for new members** | Automatically book a kickoff meeting when someone signs up in your member portal, so onboarding starts without any manual steps.  |
| **Post-meeting follow-ups**       | When a meeting ends, trigger a workflow to send a thank-you email, log the call, or ask for feedback inside your app.               |
| **Sync bookings to your records** | When a booking is created or rescheduled in Cal.com, update the matching record in your Softr app so your team always sees the latest time. |
| **No-show and cancellation handling** | When a booking is cancelled, trigger a workflow to notify the owner, free up the slot, or offer the attendee a new time.       |
| **Reschedule from your app**      | Let members move an existing meeting from their dashboard — reschedule the Cal.com booking and confirm the new time back to them.   |

## How to Connect Softr with Cal.com

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a **Cal.com** action (or trigger, if you want the workflow to start from a Cal.com event).
3. Click **Connect to Cal.com** and give Softr permission to access your Cal.com account.
4. For an action, choose the event type and map the attendee details and time from your Softr form, record, or a previous workflow step.
5. For a trigger, pick the booking event you want to start the workflow — booking created, rescheduled, cancelled, or meeting ended.
6. Save and activate your workflow.
