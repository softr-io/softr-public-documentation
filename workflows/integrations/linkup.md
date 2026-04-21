# Linkup integration

Connect Linkup with your Softr applications to add grounded, real-time web search and page fetching to your workflows. Use Linkup to feed up-to-date context into AI prompts, power research automations, or extract content from any webpage on demand.

## Overview

The Softr Linkup integration allows you to call Linkup's web search and page fetch APIs directly from your workflows. Ask a natural-language question and get a synthesized answer with citations, or fetch a single URL and receive clean markdown that's ready to plug into an AI prompt or a database record.

With Softr, you can search the web, retrieve page content, and combine the results with any other action — send to Slack, store in a tablespace, or enrich a CRM record — all without code.

## Available Actions

### Search the web

Runs a natural-language web search and returns a synthesized answer backed by a list of sources. Supports standard (1 credit) and deep (10 credits) search modes, domain include/exclude filters, and publication-date filters.

### Fetch page

Fetches a single URL and returns a cleaned markdown representation of the page. Optionally extracts images and includes the raw HTML. Supports JavaScript rendering for SPAs and client-rendered pages.

## Key Benefits

- **Grounded AI context:** Give your AI actions up-to-date, source-cited information instead of relying on model training data.
- **No-code simplicity:** Configure searches and fetches visually in Softr — no external scripts or scraping setup.
- **Credit-metered:** Pay only for what you use; choose standard or deep search per call based on the precision you need.
- **Composable:** Pipe Linkup results straight into AI prompts, databases, Slack messages, or any other workflow action.

## Example Use Cases

| Use Case                              | Description                                                                                          |
| :------------------------------------ | :--------------------------------------------------------------------------------------------------- |
| **Research briefs**                   | Search the web on a topic and post a sourced summary to Slack every morning.                         |
| **Real-time AI answers**              | Feed Linkup search results into an AI prompt to answer user questions with fresh, cited information. |
| **Lead enrichment**                   | Fetch a prospect's website and extract markdown to enrich a CRM record.                              |
| **Competitor monitoring**             | Run scheduled deep searches restricted to competitor domains and log changes to a database.          |
| **Page-to-database**                  | Fetch a news article, extract markdown, and add a new record with the content in a Softr table.      |

## How to Connect Softr with Linkup

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Linkup action.
3. Click **Connect Linkup** and paste your Linkup API key.
4. Your API key can be found on the Linkup dashboard at [app.linkup.so](https://app.linkup.so).
5. Configure your inputs (query, URL, filters, toggles) and save.
6. Activate your workflow.
