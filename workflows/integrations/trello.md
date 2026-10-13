# Trello integration

Connect Trello with your Softr applications to turn form submissions, sign-ups, and record changes into Trello cards automatically — no code required.

## Overview

The Softr Trello integration links your no-code apps to your Trello boards. When something happens in your app — a form is submitted, a member signs up, a record is updated — Softr can create a Trello card on the right list, assign members, apply labels, and set a due date, keeping your team's board in sync without manual data entry.

Whether you're running an intake pipeline, a support queue, or a content calendar, you can wire Softr forms and record actions straight into Trello so work lands where your team already tracks it.

## Available Actions

### Card: Create

Create a new card on any Trello list. Set the card name and description, place it at the top or bottom of the list, assign board members, apply labels, and set start and due dates — all mapped from your Softr form fields, records, or earlier workflow steps. Boards, lists, members, and labels are loaded live from your connected account, so you always pick from real, up-to-date options.

### Card: Get

Look up a single card by its ID and pull its details — name, description, list, due date, members, and labels — into your workflow to use in later steps.

### Card: Update

Change an existing card: rename it, edit the description, move it to another list or board, update members, labels, position, and dates, or archive and restore it. Only the fields you set are changed.

### Card: Delete

Permanently delete a card by its ID. To keep the card but hide it, use Card: Update to archive it instead.

### Card: List

Return all cards in a chosen list — perfect for building dashboards, digests, or driving follow-up steps for each card in a list.

## Key Benefits

- **No-code simplicity:** Configure the Trello action visually in the Softr workflow builder — no scripting required.
- **Live board data:** Boards, lists, members, and labels are fetched from your connected Trello account so dropdowns stay current.
- **Right card, right place:** Send each card to the exact list and position, with members, labels, and due dates set automatically.
- **Real-time sync:** Cards appear on your board the moment the triggering event happens in your Softr app.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Form-to-card** | A Softr form submission creates a Trello card on your intake list with the submission details in the description. |
| **Support queue** | When a customer submits a request through your portal, create a card on the "New" list and assign the on-duty agent. |
| **Content calendar** | A new record in your Softr content database creates a card with a due date so writers see deadlines on the board. |
| **Sign-up onboarding** | When a new member signs up, create a Trello card to kick off your onboarding checklist for that customer. |

## How to Connect Softr with Trello

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the **Trello** action (Card: Create).
3. Click **Connect to Trello**. Generate an API key at [trello.com/power-ups/admin](https://trello.com/power-ups/admin), then use the token link on that page to generate an API token, and paste both into Softr.
4. Choose the **board** the card should be created on.
5. Pick the **list** and map your Softr form fields, records, or previous steps to the card's name, description, members, labels, and dates.
6. Save and activate your workflow.
