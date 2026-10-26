# Dropbox integration

Connect Dropbox with your Softr applications to store, organize, and share files straight from your workflows — upload documents from your app, keep a folder per client, hand out download and shared links, and collect files from your customers with file requests.

## Overview

The Softr Dropbox integration lets your workflows work with the files in a connected Dropbox account. Upload a file attached to a record, create the folder structure your app needs, find, copy, move, or delete files, and pass Dropbox files on to other steps — a table file field, an email, or an AI step.

It fits the way Softr apps are built: client portals, intake forms, and internal tools. Give every new client their own folder, send them a link to upload their documents, and share finished files back with a link — all from your Softr data, without leaving the workflow builder.

On Dropbox team accounts, your workflows also see the team folders you have access to.

## Available Actions

### Upload file

Upload a file of up to 150 MB to a Dropbox folder, keeping its name or giving it a new one. Choose what happens when a file with the same name already exists: rename the new file, replace the existing one, or fail.

### Create folder

Create a folder in Dropbox. When a folder with the same name already exists, the step can use the existing folder, which makes it easy to keep one folder per client, rename the new folder, or fail.

### Get file or folder

Get the details of a file or folder by its path or ID — its name, path, size, and when it last changed.

### Get folder contents

List the files and folders in a folder, optionally including its subfolders and only files or only folders. Use a loop to go through the items, for example to process each file. If `hasMore` is true, the folder holds more items than were returned: raise **Max items** or narrow the item type.

### Find file or folder

Search your Dropbox, or one folder of it, by name, optionally by file category and extension. Finding nothing is not an error: `count` is 0 and `firstItem` is empty. If `hasMore` is true, Dropbox had more matches than were returned.

Dropbox search can take a few minutes to include newly added files. To look up a file you know the path of, use **Get file or folder** instead.

### Copy file or folder

Copy a file or folder into another folder, optionally under a new name.

### Move or rename file or folder

Move a file or folder into another folder, rename it, or both. Set a destination folder, a new name, or both; leave the destination empty to rename in place.

### Delete file or folder

Delete a file or folder. Deleting a folder also deletes everything in it. Deleted items can be restored from Dropbox for as long as your Dropbox plan keeps them.

### Get temporary download link

Get a direct download link to a file, valid for 4 hours. Use the link to put the file in a table file field, attach it to an email, or pass it to an AI step. Folders and files that can only be exported, such as Paper docs, have no download link.

### Create shared link

Create a link to share a file or folder, and choose who can open it, whether it is view-only or editable, whether downloads are allowed, a password, and an expiry.

- If the item already has a link with the same settings, that link is returned and `isExisting` is true.
- If the item already has a link with other settings, or you set a password and the item is already shared, the step fails.
- A team audience, a password, an expiry, and turning off downloads need a paid Dropbox plan.

### Create file request

Create a link people can use to upload files into a Dropbox folder — send it in the `url` output to a client, for example in an email. Add a description for the uploaders, a deadline, and how long late uploads are still accepted. Deadlines and late uploads need a paid Dropbox plan.

## Key Benefits

- **No-code file automation:** Upload, organize, and share Dropbox files from your Softr workflows — no scripts or developer help required.
- **A folder per client:** Create folders from your records and reuse them on every run, so each client's files stay in one place.
- **Share without manual steps:** Hand out download links, shared links, and file request links straight from your app's data.
- **Collect files from anyone:** Let clients and partners upload documents into the right folder, even if they don't use Dropbox.
- **Works with team accounts:** Reach the team folders your Dropbox team account has access to.

## Example Use Cases

| Use Case                       | Description                                                                                              |
| :----------------------------- | :------------------------------------------------------------------------------------------------------- |
| **Client onboarding folders**  | Create a Dropbox folder for every new client record and store their files in it.                         |
| **Document collection**        | Send a new client a file request link so they can upload their contracts and IDs into their own folder.  |
| **Form attachments to Dropbox** | Upload files submitted through a Softr form to the right Dropbox folder automatically.                  |
| **Sharing finished work**      | Create a shared link to a finished report and email it to the client when its record is marked as done.  |
| **Files in your app**          | Get a temporary download link and save the file to a table file field so members can open it in the app. |
| **Archiving**                  | Move or rename files when a project closes, or delete them when a record is removed.                     |

## How to Connect Softr with Dropbox

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Dropbox action, for example **Upload file**.
3. Click **Connect to Dropbox** and sign in with your Dropbox account.
4. Approve the requested permissions so Softr can work with your Dropbox files on your behalf.
5. Choose the trigger that should run the workflow (form submission, sign-up, record update, schedule).
6. Fill in the action's settings — using fields from your Softr forms, records, or previous workflow steps.
7. Save and activate your workflow.

To remove Softr's access, delete the connection in Softr. Dropbox may still list Softr under **Settings → Apps** in your Dropbox account; disconnect it there to remove it from the list.
