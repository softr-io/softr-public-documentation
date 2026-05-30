# Firecrawl integration

Connect Firecrawl with your Softr applications to pull content from the web without writing any scraping code. Build workflows that scrape specific URLs, run web searches, and feed the results into the rest of your Softr app.

## Overview

The Softr Firecrawl integration allows you to connect your no-code apps with Firecrawl's scraping and search API. Convert any webpage into clean markdown, HTML, or structured data, run natural-language searches across the web, news, and images, and use the results to enrich records, trigger follow-ups, or populate content — all without managing a headless browser or proxy fleet.

With Softr, you can scrape single URLs, search the web, and wire the responses into every downstream action in your workflow.

## Available Actions

### Scrape URL

Scrape a webpage and return its content in one or more formats: `markdown`, `html`, `rawHtml`, `screenshot`, or `summary`. You can choose to keep only the main content (strip nav, headers, footers, sidebars) or keep the full page. The response includes the requested formats plus page metadata (title, description, language, Open Graph tags, source URL, status code, content type).

### Search web

Run a natural-language query across the web, news articles, or image results. Pick one or more sources (`web`, `news`, `images`) and a per-source result limit. Each web result returns URL, title, and description; news results include snippet, date, and source; image results include image URL, dimensions, and title.

## Key Benefits

- **No-code simplicity:** Configure scraping and search actions visually in Softr — no browser automation or API plumbing.
- **Clean, LLM-ready output:** Markdown and structured JSON responses plug straight into downstream AI actions.
- **Multi-format scraping:** Ask for markdown, HTML, screenshots, or summaries from the same call.
- **Web, news and images in one action:** Search across multiple content types with a single query.
- **Automatic retries:** Firecrawl API calls are retried with exponential backoff on transient failures.

## Example Use Cases

| Use Case                          | Description                                                                                                  |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Enrich new leads with website content** | When a lead is created in your Softr app, scrape their company URL and save the summary alongside the record. |
| **AI-generated competitor briefs** | Scrape a competitor's pricing page daily and pipe the markdown into an AI summarization action.              |
| **Knowledge base from search**    | Run a Firecrawl search, scrape the top results, and store them in a Softr database as a searchable corpus.   |
| **Automated news digest**         | Search the news source for a topic and email a daily round-up to internal users.                             |
| **Link preview on form submission** | When a user submits a URL through a form, scrape it and display title/description back to them.             |

## How to Connect Softr with Firecrawl

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Firecrawl action (**Scrape URL** or **Search web**).
3. Click **Connect Firecrawl** and enter your Firecrawl API key.
4. Your API key can be found in your Firecrawl account under [API Keys](https://www.firecrawl.dev/app/api-keys). Keys are prefixed with `fc-` and do not expire.
5. Configure your inputs (target URL or search query, formats, limits) and save.
6. Activate your workflow.

## Usage and Billing Notes

- Each Firecrawl action consumes **5 workflow credits** per run.
- Firecrawl enforces per-team rate limits that vary by plan. If you hit a 429, Softr retries the call with exponential backoff before failing the action.
- Screenshot URLs returned by the scrape action expire 24 hours after generation — download or re-host them if you need to keep them long-term.
