# Apify integration

Connect Apify with your Softr applications to bring live web data into your no-code apps. Run web scrapers, monitor competitors, enrich leads, and build research dashboards — all triggered by what your users do in Softr.

## Overview

The Softr Apify integration lets you turn any Softr app into a frontend for the web. Trigger Apify Actors and tasks from form submissions, button clicks, or scheduled workflows, then pipe the scraped results straight back into your Softr lists, member dashboards, or admin tools.

Whether you're building a lead-research portal for your sales team, a price-monitoring dashboard for your operations team, or a public directory backed by live web data, Apify gives your Softr app access to thousands of pre-built scrapers and your own custom Actors — without writing a single line of code on the Softr side.

## Available Actions

### Run Actor

Start an Apify Actor — your own or one from the Apify Store — with custom JSON input. Optionally wait for the run to finish before continuing the workflow.

### Run Actor and Get Dataset

Run an Actor end-to-end and return the scraped items in a single step. Ideal when you want the results immediately available to the next workflow step.

### Get Last Actor Run

Fetch the most recent run of an Actor, optionally filtered by status. Useful for surfacing the latest results in a Softr list or for checking whether a recurring scrape has completed.

### Run Task

Trigger a saved Apify task using its preconfigured input. Perfect for canned scrapes you've tuned in the Apify Console.

### Run Task and Get Dataset

Run a saved task and return its output items in one step. The most common pattern for "user clicks a button → see scraped results in Softr" workflows.

### Fetch Dataset Items

Read items from any existing Apify dataset by ID. Use this to pull historical scrape results into a Softr list block or to paginate through large datasets.

### Get Key-Value Store Record

Retrieve a single record from an Apify key-value store. Useful for fetching screenshots, files, or structured payloads an Actor has saved alongside its dataset output.

## Available Triggers

### Actor Run Finished

Kick off a Softr workflow whenever an Apify Actor or task run finishes — succeeds, fails, aborts, or times out. Optionally scope the trigger to a specific Actor or task so unrelated runs don't fire your workflow.

## Key Benefits

- **No-code web data:** Add live web scraping to your Softr app without managing servers, browsers, or proxies.
- **Thousands of ready-made scrapers:** Tap into the Apify Store for pre-built Actors covering Google Maps, LinkedIn, Amazon, Instagram, Zillow, and more.
- **Bring your own Actors:** Run any custom Actor your team has built, with full control over input and output.
- **Real-time and scheduled:** Trigger scrapes on user actions in your app, or react to runs that finish in the background.
- **Member-facing or internal:** Build self-serve research tools for your customers, or back-office dashboards for your team.

## Example Use Cases

| Use Case                          | Description                                                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Lead-research portal**          | Let sales reps submit a Google Maps URL or LinkedIn search in a Softr form, then return enriched leads in a list block. |
| **Competitor price monitoring**   | Run a scheduled scrape of competitor product pages and surface the latest prices in an internal Softr dashboard.        |
| **Self-serve scraping for clients** | Sell scraping as a service through a member portal — clients submit a URL, get charged, and download results.        |
| **Dynamic public directory**      | Power a public-facing Softr directory (jobs, real estate, restaurants) with fresh data scraped on a schedule.          |
| **Review and reputation tracking**| Pull Google Maps or Trustpilot reviews into an admin dashboard so your team can respond from inside Softr.            |
| **AI-enriched lead workflows**    | Chain Apify with an AI action — scrape a company site, then summarize it or draft an outreach email automatically.    |

## How to Connect Softr with Apify

1. In your Apify Console, go to **Settings → API tokens** and copy a token.
2. Open your Softr app and go to **Integrations → Apify**.
3. Click **Connect Apify** and paste your API token.
4. Add an Apify action or trigger to a workflow and pick the Actor, task, dataset, or key-value store you want to use.
5. Map inputs from your Softr forms, records, or previous workflow steps to the Actor's JSON input.
6. Save and activate your workflow.
