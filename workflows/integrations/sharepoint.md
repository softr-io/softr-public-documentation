# SharePoint integration

Connect SharePoint with your Softr applications to put the sites your team already works in behind your no-code app. Turn form submissions into list items, keep request trackers current, and upload member documents straight into the right document library — without anyone opening SharePoint to do it by hand.

## Overview

The Softr SharePoint integration lets your workflows work with two parts of a SharePoint site: **lists** and **document libraries**. Read and write list items to use SharePoint lists as a backend for trackers, registers, and intake logs — and create folders, upload files, and browse libraries to keep documents organised as your app is used.

Once you connect your Microsoft account, Softr reads your sites, lists, document libraries, and list columns live. You pick them from dropdowns rather than typing IDs, and the column choices always reflect the list you selected — so a column added in SharePoint shows up in your workflow without any re-configuration.

## Available Actions

### List items

#### Find list items

Search a list and return the items you need. Filter by a single column value — for example every request whose `Status` is `Open` — or leave the filter blank to return the first items in the list. **Max items** caps how many come back (100 by default).

#### Get list item by ID

Fetch one item and use its column values in later steps. Identify it either by an item ID from an earlier step, or by a search condition — a column and value, which returns the first matching item.

#### Create list item

Add a new item to a list, setting the column values from your form fields, records, or earlier workflow steps.

#### Update list item

Change the column values on an existing item. As with **Get list item by ID**, you can point at the item by ID from a previous step, or find it by a column and value.

#### Delete list item

Remove an item from a list — again by ID from an earlier step, or by the first item matching a column and value.

#### Create list

Create a new list on a site, with a name and an optional description.

### Files & folders

#### Find file or folder

Search a document library by file or folder name — a partial name works. Scope the search to a single folder, or leave the folder blank to search the whole library. Returns up to **Max items** results (25 by default).

#### Get file or folder by ID

Fetch a single file or folder by its ID to use its details in later steps — name, path, link, size, and when it was created and last modified.

#### Get folder contents

List the files and folders inside a folder. Leave the folder blank to list the document library root. **Max items** caps the result (100 by default).

#### Upload file

Upload a file into a document library — for example a document a member submitted through a Softr form. Choose a destination folder or leave it blank to upload to the library root, optionally override the file name, and decide what happens if a file with that name already exists: **rename** the new file, **replace** the existing one, or **fail** the step.

#### Create folder

Create a folder in a document library — inside a parent folder, or at the library root. Same-name handling matches uploads: rename, replace, or fail.

#### Delete file or folder

Delete a file or folder from a document library by its ID.

## Key Benefits

- **Your SharePoint site as a backend:** Power Softr apps from the lists and libraries your team already maintains — no migration, no duplicate source of truth.
- **Always in sync with your lists:** Sites, lists, libraries, and columns are read live from SharePoint, so dropdowns never drift out of date when someone adds a column or a library.
- **Right value, right column type:** Filter values are matched against the column's real type — text, number, date, or yes/no — so filtering works the way it does inside SharePoint.
- **Work by ID or by condition:** Get, update, and delete items either by an ID carried from an earlier step or by a column value, so workflows work even when nothing upstream knows the item's ID.
- **Documents where they belong:** Files uploaded through your app land in the correct library and folder, with predictable handling when a name is already taken.

## Example Use Cases

| Use Case                             | Description                                                                                                       |
| :----------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **Form submissions to a list**       | Capture every Softr form entry — requests, applications, incident reports — as a new item in a SharePoint list.     |
| **Request tracker in a portal**      | Find list items for the signed-in member and show them in your Softr app, then update the item when a status moves. |
| **Document intake**                  | Upload files members submit through your app straight into the right document library and folder.                   |
| **Per-client folders**               | Create a folder for each new client record so their documents have a home from day one.                             |
| **Client-facing document list**      | List a folder's contents, or search a library by name, to show clients only the documents that concern them.        |
| **Clean-up after cancellation**      | When a request is withdrawn, find the matching list item by reference and delete it, along with its uploaded files. |

## How to Connect Softr with SharePoint

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a SharePoint action.
3. Click **Connect SharePoint** and sign in with the Microsoft account that has access to the site you want to use.
4. Authorize Softr to access your SharePoint sites.
5. Pick the **Site**, then the **List** or **Document library** the action should work with.
6. Map fields from your Softr forms, records, or previous workflow steps to the list columns — or choose the file to upload.
7. Save and activate your workflow.
