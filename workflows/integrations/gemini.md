# Gemini integration

Connect Gemini with your Softr applications to use Google's AI models for writing, summarizing, categorizing, and image generation inside your workflows. Turn form submissions and records into polished content and visuals — no code required.

## Overview

The Softr Gemini integration sends text from your workflows to Google's Gemini models and returns the result for use in any later step. Draft copy, condense long submissions, sort records into categories, run any custom prompt, or generate images with Google's Nano Banana image model — then write the output to a database, an email, or the next action in the chain.

In a typical Softr app, Gemini reacts to what your users do: a client uploads a request through a form block, a member updates their profile, a new record lands in a table — and the workflow answers with generated text, a summary for your team, a routing label, or a brand-new image.

## Available Actions

### Custom prompt

Send your own prompt to Gemini — with data mapped in from forms, records, or earlier steps — and use the response anywhere in your workflow.

### Write

Generate original text such as email drafts, descriptions, announcements, or personalized messages.

### Summarize Text

Condense long text — briefs, feedback, meeting notes — into a short summary your team can scan.

### Categorize

Assign text to one of your predefined categories so submissions and records get routed automatically.

### Nano Banana 2 (image)

Generate an image from a text prompt with Google's Nano Banana image model and use it in your app — as a record attachment, listing visual, or email asset.

## Key Benefits

- **Google's AI, no code:** Use Gemini's text and image models from a visual workflow editor — no scripts or API plumbing.
- **Text and images together:** Write copy and generate matching visuals for records, listings, and emails in one workflow.
- **Your own Google AI account:** Connect with your API key and use your own models, quotas, and billing.
- **Routing-ready output:** Use Categorize to produce clean labels you can branch on, filter with, or store in a record.

## Example Use Cases

| Use Case                          | Description                                                                                                 |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Visuals for every listing**     | When a member adds a product or event through your portal, generate an image and attach it to the record.     |
| **Summarize incoming requests**   | Condense long form submissions into short summaries your admin dashboard can display at a glance.             |
| **Sort and route submissions**    | Categorize new entries — support, sales, feedback — and branch the workflow to the right follow-up.            |
| **Content on autopilot**          | Draft descriptions, announcements, or member updates from record data whenever something changes.              |
| **Personalized onboarding**       | When a user signs up, write a tailored welcome message from their answers and send it automatically.           |

## How to Connect Softr with Gemini

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Gemini action.
3. Click **Connect Gemini** and paste your Gemini API key. You can create one for free in [Google AI Studio](https://aistudio.google.com) under **Get API key**.
4. Choose the model and write your instructions or prompt.
5. Map fields from your Softr forms, records, or previous workflow steps into the prompt inputs.
6. Save and activate your workflow.
