# Push Notifications

Send web push notifications to your app users directly from a Softr Workflow. Notify users about new messages, status changes, task assignments, or any other event — right in their browser, even when they're not actively using your app.

## Overview

The **Send Push Notification** action is a native Softr feature that lets you deliver real-time notifications to one or more specific users of your published app. Unlike email or Slack, push notifications appear directly in the user's browser or device notification center, making them ideal for time-sensitive updates.

Each notification includes a **title**, **body**, and an optional **URL** to open when the user clicks it.

## Prerequisites

Before using the Send Push Notification action in a Workflow, push notifications must be enabled in your app:

1. Open your Softr app and go to **Users → Notifications**.
2. Enable push notifications for the device type(s) you want to support — **Mobile**, **Desktop**, or both.
3. Publish your app.

Once enabled, users who visit your published app will be prompted to allow notifications in their browser. Only users who have granted permission will receive push notifications from your workflows.

## Available Actions

### Send Push Notification

Send a push notification to one or more users of your published app.

**Settings:**

| Field        | Description                                                                 |
| :----------- | :-------------------------------------------------------------------------- |
| **Recipient(s)** | One or more users to notify. Map a user email from an earlier workflow step, or provide multiple emails for targeted delivery. |
| **Title**    | The notification heading (displayed in bold). Keep it short and clear.      |
| **Body**     | The notification message text. Describe what happened or what action is needed. |
| **URL** *(optional)* | The page to open when the user clicks the notification. Defaults to your app's home page if left empty. |

## Key Benefits

- **Instant delivery:** Notifications appear in the user's browser or OS notification center in real time.
- **No email required:** Reach specific users directly without sending an email or requiring them to be inside the app.
- **Clickable deep links:** Drive users to a specific page or record by setting a URL in the notification.
- **Native to Softr:** No third-party service or API key required — push notifications are built into every published Softr app.

## Example Use Cases

| Use Case                         | Description                                                                                   |
| :------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Task assignment**              | Notify a user when a new task is assigned to them in your project management app.             |
| **Status change alert**          | Alert a customer when their order or support ticket status is updated.                        |
| **New message or comment**       | Let users know when someone replies to their post or leaves a comment.                        |
| **Approval required**            | Prompt a manager to review and approve a pending request.                                     |
| **Deadline reminder**            | Send a reminder before a due date using a scheduled workflow trigger.                         |

## How to Add a Push Notification Action to a Workflow

1. Open your Softr workspace and go to **Workflows**.
2. Create a new workflow or open an existing one.
3. Add an action step, select **Softr Apps**, then choose **Send Push Notification**.
4. In the **Settings** panel on the right, configure the **Recipient(s)**, **Title**, **Body**, and optionally a **URL**.
5. Map dynamic values from earlier steps (e.g., use the triggered user's email as the recipient, or the record name in the notification body).
6. Test the action using the **Testing** tab — make sure at least one user has subscribed to notifications in your published app.
7. Turn on your workflow.

<Tip>
  To test push notifications, open your published app in a browser, allow notifications when prompted, then trigger the workflow. The notification will appear in your browser's notification center.
</Tip>
