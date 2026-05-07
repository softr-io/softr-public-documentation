# DocsAutomator integration

Connect DocsAutomator with your Softr applications to turn form submissions, member sign-ups, and record updates into polished, branded PDFs — contracts, invoices, certificates, and reports — generated automatically from your own Google Docs templates.

## Overview

The Softr DocsAutomator integration lets you generate professional documents on demand from inside your no-code app. Design a template once in Google Docs, drop in `{placeholder}` tags wherever data should appear, and let Softr fill it in with values from form submissions, list records, or any earlier step in your workflow. The finished PDF is produced automatically — no manual copy-paste, no formatting drift.

This is the missing piece for any Softr app where users expect a real document at the end of a process: client portals that hand off signed agreements, booking tools that issue invoices, course platforms that award completion certificates, and internal tools that fire off branded reports straight from your data.

## Available Actions

### Create document

Generate a PDF from a Google Docs template by passing in the values that fill its placeholders — kicked off by a form submission, a button click, or any other workflow trigger.

## Key Benefits

- **No-code document automation:** Design templates visually in Google Docs and wire them into Softr workflows without writing a line of code.
- **Use the editor you already know:** Templates live in Google Docs, so anyone on your team can update wording, branding, or layout without touching your app.
- **Polished PDF output:** Every document comes out as a clean, share-ready PDF — consistent typography, logos, and structure on every run.
- **Personalized at scale:** Pull names, dates, line items, and any other dynamic data from your Softr records or forms straight into the document.
- **Member-facing or internal:** Deliver documents to your customers automatically, or generate them quietly in the background for your team.

## Example Use Cases

| Use Case                          | Description                                                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Contracts and agreements**      | Generate a tailored contract PDF the moment a client submits a form, ready to send for signature.                    |
| **Invoices after a booking**      | Fire off a branded invoice automatically when a member books a service or completes a checkout in your Softr app.    |
| **Certificates of completion**    | Issue personalized course-completion certificates to members the second they finish a program or pass a milestone.   |
| **Custom client reports**         | Let internal teams produce on-demand reports — pulled live from app data — straight from a button in a Softr dashboard. |
| **Branded sales proposals**       | Turn a CRM-style internal tool into a one-click proposal generator, with deal data dropped into a polished template. |
| **Quotes and order confirmations**| Email a formatted quote or order confirmation as soon as a lead requests pricing or a customer places an order.      |

## How to Connect Softr with DocsAutomator

1. In Google Docs, create the template you want to use and add `{placeholder}` tags wherever dynamic data should appear (for example `{client_name}`, `{invoice_total}`).
2. In your DocsAutomator account, register the template and copy your API key from the account settings.
3. Open your Softr app and go to **Integrations → DocsAutomator**.
4. Click **Connect DocsAutomator** and paste your API key.
5. Add the **Create document** action to a workflow and pick the template you want to fill.
6. Map fields from your Softr forms, records, or earlier workflow steps to the template's placeholders, then save and activate your workflow.
