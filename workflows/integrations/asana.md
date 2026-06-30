# Asana integration

Connect Asana with your Softr applications to automate work management — create and update tasks, manage projects, post comments, and look up users without writing code.

## Overview

The Softr Asana integration lets you connect your no-code apps with your Asana workspace. Automatically create tasks when forms are submitted, update task status as records change, post comments to keep conversations in sync, and pull in users or projects to enrich your automations.

Whether you're building a client portal, an internal task tracker, or a project-status dashboard, you can wire Softr records and user actions directly to Asana to remove manual data entry and keep both systems aligned in real time.

## Credentials Required

Connect Softr to Asana with one of two methods.

### OAuth 2.0 (recommended for multi-user accounts)

Click **Connect with Asana** in the Softr workflow builder; you'll be redirected to Asana to authorize Softr. Softr requests the following scopes (or their bundled `default` scope):

| Scope | Purpose |
| :---- | :------ |
| `tasks:read`, `tasks:write` | Read and modify tasks and subtasks |
| `projects:read`, `projects:write` | Read and modify projects |
| `users:read` | Look up workspace members |
| `workspaces:read` | List workspaces |

### Personal Access Token (single-user / scripts)

Generate a Personal Access Token in the Asana developer console under **My Apps → Personal access tokens**. Paste it into the **Personal Access Token** field when configuring an Asana action in Softr.

| Field | Description |
| :---- | :---------- |
| **Personal Access Token** | A long-lived token from your Asana developer console; inherits your account's permissions and never expires. |

## Available Actions

### Task: Create

Create a new task in a workspace. Set name, description (notes), assignee, due date, projects, tags, followers, and custom fields.

**Key inputs:** workspace (required), name (required), projects, parent, assignee, assignee status, notes, html notes, due on, due at, start on, start at, tags, followers, custom fields, completed, liked, resource subtype

**Output fields:** gid, name, notes, html_notes, completed, completed_at, due_on, due_at, start_on, start_at, assignee, assignee_status, projects, workspace, parent, tags, followers, num_subtasks, liked, num_likes, created_at, modified_at, permalink_url, custom_fields, resource_subtype

### Task: Get

Retrieve a single task by its GID.

**Key inputs:** task_gid (required)

**Output fields:** Same as Task: Create.

### Task: Update

Update any combination of fields on an existing task. Only fields you provide are changed.

**Key inputs:** task_gid (required), name, notes, html_notes, assignee, assignee_status, due_on, due_at, start_on, start_at, completed, liked, projects, custom_fields, resource_subtype

**Output fields:** Same as Task: Create.

### Task: Delete

Soft-delete a task. The task moves to Asana's trash and is recoverable for 30 days.

**Key inputs:** task_gid (required)

**Output fields:** success (boolean), task_gid

### Task: List

List tasks scoped to a project, section, or assignee. Filter by completion or modification time. Cursor-paginated; pass `next_offset` from one call as `offset` on the next.

**Key inputs:** project, section, assignee + workspace, completed_since, modified_since, limit (1–100), offset

**Output fields:** `records` — array of task objects (same fields as Task: Get); `next_offset` — pagination cursor

### Task: Search

Full-text search for tasks within a workspace, with rich filters for assignees, projects, tags, and date ranges.

> **Rate limit notice:** Asana's search endpoint is hard-limited to **60 requests per minute** regardless of plan tier. Design workflows accordingly.

**Key inputs:** workspace (required), text, completed, assignee_any, projects_any, tags_any, created_on_after, created_on_before, due_on_after, due_on_before, sort_by, sort_ascending, limit

**Output fields:** `records` — array of matching tasks

### Subtask: Create

Add a subtask to an existing task.

**Key inputs:** parent_task_gid (required), name (required), assignee, notes, html_notes, due_on, due_at, completed

**Output fields:** Same as Task: Get.

### Subtask: List

List subtasks of a parent task. Cursor-paginated.

**Key inputs:** parent_task_gid (required), limit, offset

**Output fields:** `records` — array of subtasks; `next_offset` cursor.

### Comment: Add to Task

Post a plain-text or rich-text comment on a task. Optionally pin it.

**Key inputs:** task_gid (required), text **or** html_text (one required), is_pinned

**Output fields:** gid, resource_subtype (`comment_added`), created_at, created_by, text, html_text, is_pinned

### Tag: Add to Task

Apply an existing tag to a task.

**Key inputs:** task_gid (required), tag_gid (required)

**Output fields:** success, task_gid, tag_gid

### Tag: Remove from Task

Remove a tag from a task.

**Key inputs:** task_gid (required), tag_gid (required)

**Output fields:** success, task_gid, tag_gid

### Project: Create

Create a project in a workspace. Required fields differ between personal workspaces and organizations (organizations require a team).

**Key inputs:** workspace (required), team (required for organizations), name (required), notes, html_notes, color, due_on, start_on, privacy_setting, owner, default_view, archived

**Output fields:** gid, name, notes, html_notes, color, due_on, start_on, owner, team, workspace, privacy_setting, default_view, archived, created_at, modified_at, permalink_url

### Project: Get

Retrieve a project by its GID.

**Key inputs:** project_gid (required)

**Output fields:** Same as Project: Create.

### Project: Update

Update fields on an existing project.

**Key inputs:** project_gid (required), name, notes, html_notes, color, due_on, start_on, owner, default_view, archived

**Output fields:** Same as Project: Create.

### Project: Delete

Delete a project.

**Key inputs:** project_gid (required)

**Output fields:** success, project_gid

### Project: List

List projects in a workspace, optionally filtered by team or archived state. Cursor-paginated.

**Key inputs:** workspace (required), team, archived, limit (1–100), offset

**Output fields:** `records` — array of projects; `next_offset` cursor.

### User: Get

Retrieve a user by GID, email, or the literal `me`.

**Key inputs:** user (required)

**Output fields:** gid, name, email, photo (URLs at multiple sizes), workspaces

### User: List

List all users in a workspace. Cursor-paginated.

**Key inputs:** workspace (required), limit, offset

**Output fields:** `records` — array of users; `next_offset` cursor.

## Key Benefits

- **No-code simplicity:** Configure Asana actions visually in the Softr workflow builder — no scripting required.
- **End-to-end task lifecycle:** Create, update, complete, comment on, and delete tasks driven by Softr events.
- **Dynamic dropdowns:** Workspaces, projects, users, tags, teams, and sections are loaded live from the connected account so options stay current.
- **Rich filtering and search:** Use Asana's native search to find tasks by assignee, project, tag, or date range.
- **Custom fields supported:** Pass a key/value map to set custom field values on Task: Create and Task: Update.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Form-to-task** | A Softr form submission creates an Asana task with the submission details and assigns it to the on-duty agent. |
| **Status sync** | When a Softr database record moves to "In progress", flip the linked Asana task's `completed` flag and post a comment. |
| **Onboarding tracker** | Auto-create a checklist of subtasks (Subtask: Create) when a new client signs up. |
| **Internal portal** | Build a Softr page that lists open Asana tasks for a project (Task: List), with a quick-update form per row. |
| **Daily digest** | Use Task: Search with `due_on_before: today` and `completed: false` to surface overdue tasks for a Slack or email digest. |

## How to Connect Softr with Asana

1. Open your Softr workspace and go to **Integrations**.
2. Find **Asana** and click **Connect**.
3. Choose **OAuth 2.0** (recommended) or **Personal Access Token**.
   - For OAuth: click **Continue**, authorize Softr in Asana, and you'll be returned to Softr.
   - For PAT: paste the token from Asana's developer console.
4. Click **Save**. Softr will verify the credentials.
5. In the **Workflow** builder, add an Asana action to any workflow.
6. Pick the connected account, select the workspace, and configure the action inputs.
7. Test the step and activate your workflow.
