# Documint integration

Connect Documint with your Softr applications to generate polished PDF documents — invoices, contracts, certificates, and more — directly from your workflows, with zero manual formatting.

## Overview

The Softr Documint integration lets you turn workflow data into finished documents automatically. Design your document once as a template in Documint, then generate a new PDF every time a workflow runs — populated with data from your app, no copy-pasting or manual document creation required.

Once you connect a template, Softr automatically reads its fields, so you always map data to the placeholders your template actually has — including repeating sections like line items, which can be bound to a list from earlier in your workflow.

## Available Actions

### Create document

Generate a document from a Documint template. Pick the template, map its fields to data from your workflow, and get back a link to the finished document — ready to send, store, or share.

## Key Benefits

- **No-code simplicity:** Configure document generation visually in Softr, without any technical setup.
- **Always in sync with your template:** Fields are read live from your chosen Documint template, so the mapping never drifts out of date when you update the template's design.
- **Repeating sections made easy:** Bind a list of records from your workflow (e.g. order line items) directly to a repeating section in your template.
- **Event-driven generation:** Automatically produce a document the moment a form is submitted, a record is created, or any other app event occurs.

## Example Use Cases

| Use Case                                 | Description                                                                                                    |
| :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Invoice generation**                    | Automatically generate an invoice PDF whenever a new order is created in your app.                               |
| **Contract creation**                     | Produce a filled-in contract or agreement the moment a deal or application is approved.                          |
| **Certificates and reports**              | Generate a personalized certificate or report from workflow data, ready to email to the recipient.               |
| **Order confirmations with line items**   | Merge a list of purchased items into a single order confirmation document using a repeating template section.    |

## How to Connect Softr with Documint

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Documint action.
3. Click **Connect Documint** when prompted to configure the connection.
4. Paste your Documint API key. You can find it in your Documint account under **Account → API** (`https://app.documint.me/account/api`).
5. Choose the template to generate documents from — Softr loads its fields automatically — and map each field to data from your workflow.
6. Save your workflow and activate it.