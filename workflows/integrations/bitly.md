# Bitly integration

Connect Bitly with your Softr applications to create short, branded, trackable links automatically. Build workflows that shorten URLs the moment they're needed — when a record is added, a form is submitted, or a new member signs up — so every link you share is clean, on-brand, and measurable.

## Overview

The Softr Bitly integration links your no-code apps directly to your Bitly account. Whenever your workflow produces a URL worth sharing — a referral link, a campaign page, a document, a personalized signup link — you can automatically shorten it into a Bitlink with a title, tags, and the right Bitly group, then store or send the short link anywhere in your app.

Whether you're building a marketing dashboard, a partner portal, or a referral program, the Bitly integration turns long, unwieldy URLs into short links your users can actually share — with Bitly's click tracking behind every one of them.

## Available Actions

### Create link

Shorten any URL into a Bitlink with an optional title, tags, and Bitly group — all set dynamically from your Softr workflow. Groups are chosen from a live dropdown pulled straight from your connected Bitly account, and the short link comes back ready to store in a record, send in an email, or show to your users.

### Get link

Retrieve an existing Bitlink — its destination URL, title, tags, and archived state — so later workflow steps can reuse or display it.

### Update link

Rename a Bitlink, replace its tags, or archive and unarchive it, keeping your link library tidy as your Softr data changes.

### List links

Pull the Bitlinks in a group, optionally filtered by a search term — perfect for finding an existing short link before creating a new one, or for showing a campaign's links inside your app.

## Key Benefits

- **No-code simplicity:** Configure Bitly actions visually in Softr — no code required beyond the one-time access token setup.
- **Short links on autopilot:** Shorten URLs the moment your workflow runs, instead of pasting them into Bitly by hand.
- **Organized from the start:** File every link under the right Bitly group and tag it consistently, so campaigns stay tidy.
- **Trackable by default:** Every link created through your workflow is a Bitlink, so clicks are tracked in your Bitly dashboard automatically.
- **Share-ready output:** Use the short link immediately in the next workflow step — save it to a record, send it via email or Slack, or display it in your app.

## Example Use Cases

| Use Case | Description |
| :------- | :---------- |
| **Referral link generator** | Create a personalized short link for each new member who signs up to your Softr app, and save it to their profile. |
| **Campaign link intake** | Let your marketing team submit long campaign URLs through a Softr form that returns a branded, tagged Bitlink. |
| **Record-based link shortening** | Shorten the URL field of every new record — listings, articles, products — and store the Bitlink alongside it. |
| **Event promotion** | When a new event is added in your Softr app, generate a short registration link ready for social media and email. |
| **Partner portal links** | Give partners tidy, trackable short links to share, generated automatically when their record is approved. |
| **Document sharing** | Shorten long file or page URLs before emailing them to clients, so messages stay clean and clicks stay measurable. |

## How to Connect Softr with Bitly

1. Open your Softr workspace and go to **Workflows**.
2. Create a new workflow or open an existing one, then add a Bitly action.
3. In the **Account** field, click **Add another account** and paste your Bitly **access token**.
4. To generate an access token, open Bitly and go to **Settings → Developer settings → API**, enter your password, and click **Generate token**.
5. Click **Save** — Softr verifies your token and connects the account.
6. Map the **Destination URL** from your Softr forms, records, or previous workflow steps, optionally pick a group and add a title or tags, then activate your workflow.
