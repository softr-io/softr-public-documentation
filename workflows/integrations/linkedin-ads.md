# LinkedIn Ads integration

Connect LinkedIn Ads with your Softr workflows to bring your campaign performance into your own tables — spend, impressions, clicks, leads, and conversions for every ad account and campaign. Build marketing dashboards, client reports, and budget trackers in Softr that stay up to date without exporting a single CSV.

## Overview

The Softr LinkedIn Ads integration pulls reporting data from LinkedIn into your workflows. Pick an ad account and a date range, choose whether you want one row per account or per campaign, and whether each row covers a day, a month, or the whole range. Every row comes back with the campaign and campaign group names, the currency, and the main metrics — ready to write into a Softr table with a loop.

This fits the way Softr apps are built for marketing teams and agencies: a scheduled workflow keeps a performance table fresh, and list, chart, and table blocks turn it into a demand-gen dashboard, a client-facing report in a portal, or a spend overview next to your CRM data.

## Available Actions

### Get performance report

Get LinkedIn Ads account or campaign metrics for a date range, as rows to write into a table — impressions, reach, clicks, landing page clicks, spend, CTR, CPC, CPM, conversions, conversion value, and leads.

- **Days are in UTC.** LinkedIn reports each day in UTC, not in the ad account's time zone, so a day's numbers can differ slightly from what you see in Campaign Manager when your account uses another time zone.
- **Keep it fresh on a schedule.** Conversions keep arriving for weeks after a click. Run the workflow on a schedule that re-pulls the last 7 to 30 days, and update existing rows by `date_start` and `campaign_id` (or `date_start` and `ad_account_id` for account-level reports) instead of adding duplicates.
- **Row limit.** Returns up to 500 rows. If `truncated` is true, shorten the date range, use a coarser granularity or filter to one campaign.
- **Approximate metrics.** LinkedIn rounds metrics for member privacy, so daily rows can add up to slightly more or less than a total for the same range. Reach and frequency are empty for ranges longer than 92 days.

## Key Benefits

- **Campaign data in your own tables:** Store LinkedIn Ads performance next to your CRM and app data, and report on it with Softr blocks.
- **No exports, no scripts:** Replace weekly CSV downloads with a scheduled workflow that keeps every number current.
- **One shape for every report:** Each row has the same columns, so the same table works for daily, monthly, and total reports.
- **Client-ready reporting:** Show each client their own campaign results in a Softr portal, with permissions deciding who sees what.
- **Budget visibility:** Track spend in the account currency and in USD to watch budgets across accounts and campaigns.

## Example Use Cases

| Use Case                          | Description                                                                                                                             |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Demand-gen dashboard**          | Every morning, pull the last 30 days of campaign metrics into a Softr table and chart spend, leads, and cost per lead on a dashboard page. |
| **Agency client portal**          | Keep one performance table per client ad account and show each client their own campaigns in a member portal.                          |
| **Weekly performance digest**     | On a weekly schedule, fetch the past week's totals and email the marketing team a summary of spend, clicks, and conversions.            |
| **Budget pacing alerts**          | Pull month-to-date spend per campaign and notify the owner in Slack when a campaign runs ahead of its planned budget.                   |
| **Pipeline attribution**          | Store LinkedIn leads and conversions by campaign next to your CRM deals, so the team can see which campaigns bring in pipeline.         |

## How to Connect Softr with LinkedIn Ads

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow — for a report, start it with a **Recurring schedule** trigger — and add the **LinkedIn Ads** action **Get performance report**.
3. Click **Connect to LinkedIn Ads**, sign in to LinkedIn, and give Softr permission to access your ad accounts. The LinkedIn user you sign in with needs a role on the ad accounts you want to report on.
4. Choose the ad account, the date range, the level (account or campaign), and the granularity (daily, monthly, or total). Optionally pick one campaign.
5. Add a loop over the report's `rows` and write each row to your Softr table.
6. Save and activate your workflow.

## Calling the LinkedIn API directly

Your LinkedIn Ads connection also works with the **Call API** action, for LinkedIn Marketing API endpoints that no built-in action covers yet. Choose your LinkedIn Ads connection as the authentication and Softr adds the access token for you.

Calls to `https://api.linkedin.com/rest/...` endpoints also need these two headers, which you add yourself in the Call API action:

| Header                      | Value    |
| :-------------------------- | :------- |
| `Linkedin-Version`          | `202609` |
| `X-Restli-Protocol-Version` | `2.0.0`  |
