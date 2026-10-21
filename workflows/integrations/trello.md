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

## Available Triggers

Both triggers are **Instant**: when you publish the workflow, Softr registers a webhook on the board you pick, and Trello notifies Softr as soon as something changes. Unpublishing the workflow removes the webhook. The connected Trello account must have access to the board.

When you click **Test**, Softr loads the most recent matching event from the board's activity, so you can map real values into later steps before the trigger has ever run. If the board has no matching activity yet, make a change on the board and test again.

### On card event

Start a workflow when a card on the board is created, changed, moved, archived, deleted, or commented on.

| Input | Description |
| :---- | :---------- |
| **Account** | Your connected Trello account. |
| **Board** | The board to watch. Required. |
| **Events** | Which card events start the workflow: **Card created**, **Card updated**, **Card moved to another list**, **Card archived**, **Card deleted**, **Comment added**. Leave empty to listen to all of them. |

A move and an archive also count as **Card updated**, so a workflow listening to updates runs for those too. Copying a card, creating a card by email, and converting a checklist item into a card all count as **Card created**.

Outputs:

| Output | Description |
| :----- | :---------- |
| `id` | The ID of the Trello action (the event). |
| `type` | Trello's action type, for example `createCard`, `updateCard`, `deleteCard`, or `commentCard`. |
| `date` | When the event happened. |
| `memberCreator` | The member who made the change (`id`, `fullName`, `username`). |
| `card` | The card (`id`, `name`, `shortLink`, and the fields the change touched). |
| `list` | The card's list. Empty when the card moved — see `listBefore` and `listAfter`. |
| `listBefore`, `listAfter` | The lists the card moved from and to. Only set when the card moved. |
| `board` | The board (`id`, `name`). |
| `old` | The previous values of the fields an update changed, for example `{ "idList": "..." }` or `{ "closed": false }`. |
| `text` | The comment text. Only set for **Comment added**. |

Trello only sends the card fields that changed. To read the full card — description, due date, members, labels — add a **Card: Get** step with the card's `id`.

### On checklist item event

Start a workflow when a checklist item (a task on a card) is created, completed, marked incomplete, updated, or deleted.

| Input | Description |
| :---- | :---------- |
| **Account** | Your connected Trello account. |
| **Board** | The board to watch. Required. |
| **Events** | Which checklist item events start the workflow: **Item created**, **Item completed**, **Item marked incomplete**, **Item updated**, **Item deleted**. Leave empty to listen to all of them. |

**Item updated** covers edits to an item, such as renaming it. Checking or unchecking an item is reported as **Item completed** or **Item marked incomplete**, not as an update.

Outputs:

| Output | Description |
| :----- | :---------- |
| `id` | The ID of the Trello action (the event). |
| `type` | Trello's action type, for example `createCheckItem`, `updateCheckItemStateOnCard`, `updateCheckItem`, or `deleteCheckItem`. |
| `date` | When the event happened. |
| `memberCreator` | The member who made the change (`id`, `fullName`, `username`). |
| `checkItem` | The checklist item (`id`, `name`, `state`). `state` is `complete` or `incomplete`. |
| `checklist` | The checklist the item belongs to (`id`, `name`). |
| `card` | The card the checklist is on (`id`, `name`). |
| `board` | The board (`id`, `name`). |
| `old` | The previous values of the fields an update changed, for example `{ "name": "..." }`. Only set for **Item updated**. |

If publishing fails with an error from Trello, check that the connected account can still open the board and reconnect the account if its token was revoked.

## Key Benefits

- **No-code simplicity:** Configure the Trello action visually in the Softr workflow builder — no scripting required.
- **Live board data:** Boards, lists, members, and labels are fetched from your connected Trello account so dropdowns stay current.
- **Right card, right place:** Send each card to the exact list and position, with members, labels, and due dates set automatically.
- **Real-time sync:** Cards appear on your board the moment the triggering event happens in your Softr app.
- **Two-way automation:** Card and checklist item triggers start workflows the moment something changes on your board, so Softr can react to work your team does in Trello.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Form-to-card** | A Softr form submission creates a Trello card on your intake list with the submission details in the description. |
| **Support queue** | When a customer submits a request through your portal, create a card on the "New" list and assign the on-duty agent. |
| **Content calendar** | A new record in your Softr content database creates a card with a due date so writers see deadlines on the board. |
| **Sign-up onboarding** | When a new member signs up, create a Trello card to kick off your onboarding checklist for that customer. |
| **Status sync** | When a card moves to the "Done" list, update the matching record in your Softr database and notify the requester. |
| **Task progress** | When a checklist item is completed on an onboarding card, mark the step as done in your Softr client portal. |

## How to Connect Softr with Trello

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the **Trello** action (Card: Create).
3. Click **Connect to Trello**. Generate an API key at [trello.com/power-ups/admin](https://trello.com/power-ups/admin), then use the token link on that page to generate an API token, and paste both into Softr.
4. Choose the **board** the card should be created on.
5. Pick the **list** and map your Softr form fields, records, or previous steps to the card's name, description, members, labels, and dates.
6. Save and activate your workflow.
