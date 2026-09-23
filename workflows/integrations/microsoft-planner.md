# Microsoft Planner integration

Connect Microsoft Planner with your Softr applications to turn what happens in your app into tasks your team actually sees. Build workflows that create Planner tasks the moment work appears — a client request comes in through a form, a record changes status, a new member joins — complete with the right bucket, assignees, due date, labels and checklist, so nothing waits for someone to copy it over by hand.

## Overview

The Softr Microsoft Planner integration links your no-code apps directly to the Planner plans your Microsoft 365 groups already use. Whenever a workflow runs, it can create a task in the plan and bucket you choose, assign it to the right people, set start and due dates, priority and progress, apply the plan's labels, and add a description, checklist items and attachment links — all mapped from your Softr forms, records and previous workflow steps.

This fits anywhere work is requested or tracked inside a Softr app: client portals where requests should become team tasks, internal tools where a status change kicks off follow-up work, or onboarding flows where every new sign-up needs the same set of to-dos.

## Available Actions

### Create task

Create a task in a Planner plan and bucket of your choice. Set the title, description, assignees, start and due dates, priority, progress and labels, add checklist items and attachment links, and get the created task back to use in the next step.

### Get task

Read a task by its id and get everything on it — title, bucket, assignees, dates, priority, progress, labels, description, checklist and attachments — ready to show in your app or use in the next step.

### List tasks

Pull the tasks of a plan, or of one bucket, and narrow them to a status (not started, in progress, completed) or to one person's assignments — to sync a board into a Softr table, build a "my tasks" view, or send a digest.

### Update task

Change a task from your workflow: rename it, move it to another bucket, reassign it, set new dates, priority or progress, swap its labels, replace the description or add checklist items. Fields you leave empty keep their current value.

### Delete task

Remove a task permanently when the request behind it is withdrawn or the work is no longer needed.

### List plans

Get every plan your connected account can see, with the Microsoft 365 group each one belongs to — to let users pick a plan in your app or to loop over plans in a report.

### Get plan

Read a plan and the names of its labels, so your workflow can pick the right label for a task or show the plan's setup in your app.

### List buckets

Get the buckets of a plan in board order, to route a task to the right column by name or mirror the board's stages in a Softr view.

### Create bucket

Add a new bucket to a plan — for example one column per new client, project phase or sprint created in your app.

## Key Benefits

- **No-code simplicity:** Pick your plan, bucket and labels from live dropdowns and map the rest from your app — no scripts, no Power Automate.
- **Tasks where your team works:** Work requested in Softr lands directly in the Planner boards your team already checks in Teams and Microsoft 365.
- **Complete tasks, not stubs:** Assignees, dates, priority, labels, checklist and attachments are set in one step, so the task is ready to work on when it appears.
- **Secure sign-in:** Connect with your Microsoft work account through Microsoft's own sign-in; Softr only asks for permission to manage tasks.
- **Ready for the next step:** Use the task's id and details downstream — save them to a record, notify the assignee, or link back to the request.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Client request intake** | When a client submits a request through your Softr portal, create a Planner task in the delivery team's plan with the request details, a due date and the account owner assigned. |
| **Onboarding checklists** | Each time a new customer or employee is added, create a task with a ready-made checklist of onboarding steps in the right bucket. |
| **Status-driven follow-ups** | When a record moves to "Approved" or "Needs review" in your app, create the follow-up task in the matching bucket with the right label — or move and reassign the existing one. |
| **Bug and feedback triage** | Turn feedback submitted in your app into prioritized tasks, with the submitter's screenshots attached as links. |
| **Content and campaign planning** | When a campaign or article is scheduled in your Softr app, create the production task with its start and due dates in the marketing plan. |
| **Recurring operations** | On a schedule, create the week's recurring tasks — reports, checks, reviews — so they appear in Planner without anyone remembering to add them. |
| **Board per client** | When a new client is added in your app, create a bucket named after them in the delivery plan, so their tasks have a home from day one. |
| **Team task dashboard** | List each plan's open tasks on a schedule and sync them into a Softr table, so clients or managers see progress without a Planner licence. |

## How to Connect Softr with Microsoft Planner

1. Open your Softr workspace and go to **Workflows**.
2. Create a new workflow or open an existing one, then add a Microsoft Planner action — work with tasks (create, get, list, update, delete), plans (list, get) or buckets (list, create).
3. In the **Account** field, click **Add another account** and sign in with your Microsoft work or school account. Grant Softr permission to manage your tasks when Microsoft asks.
4. Pick the **Plan** and **Bucket** the task should be created in — the dropdowns list the plans you have access to.
5. Map the **Title** and any other fields from your Softr forms, records, or previous workflow steps. Assignees can be entered as email addresses.
6. Save and activate your workflow.
