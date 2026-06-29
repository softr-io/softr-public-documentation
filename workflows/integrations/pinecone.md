# Pinecone integration

Connect Pinecone with your Softr applications to power semantic search, retrieval-augmented generation (RAG), and other AI features. Build workflows that create indexes, store text records, and search for semantically similar content — all without code.

## Overview

The Softr Pinecone integration allows you to connect your no-code apps with the Pinecone vector database using **integrated embedding**. Create serverless indexes backed by a built-in embedding model, upsert raw text records (Pinecone embeds them server-side), and search with natural-language query text. Use the results to ground LLM prompts, build smart search experiences, or recommend related content.

With Softr, you can configure end-to-end semantic workflows: index your knowledge base whenever new content is added, then search Pinecone whenever a user asks a question — all without writing a single line of code, and without managing embeddings yourself.

## Available Actions

### Create index

Create a new serverless Pinecone index with integrated embedding. Choose an embedding model — `multilingual-e5-large` (dense), `llama-text-embed-v2` (dense), or `pinecone-sparse-english-v0` (sparse) — a cloud (AWS, GCP, or Azure), and a region. Optionally set deletion protection and tags. The index name is normalized to lowercase alphanumeric and hyphens (max 45 characters). The distance metric is determined automatically by the embedding model.

Indexes created here are automatically configured so that records use the **`chunk_text`** field for embedding — which is what the **Upsert records** action expects.

### List indexes

List every index in the connected Pinecone project.

### Describe index

Get full details for a single index — including its data-plane host. Useful for checking readiness or confirming an index's configuration.

### Delete index

Delete a Pinecone index permanently. Pinecone rejects the deletion when the index has deletion protection enabled (set at creation time).

### Upsert records

Insert or update raw text records into an index. Pinecone embeds the text server-side, so you don't supply vectors yourself. Up to **96 records** per request.

Each record must include:

- **`_id`** — a unique string identifier for the record.
- **`chunk_text`** — the text to embed. This field is **required** and must be non-blank.
- Any other keys (e.g. `category`) — stored as **metadata**, which you can filter and return in the **Search records** action.

```json
[
  { "_id": "rec1", "chunk_text": "Hello world", "category": "greeting" }
]
```

> **Important — the text field must be named `chunk_text`.** If you created your index with Softr's **Create index** action, it's already configured for `chunk_text` and there's nothing to do. If you created the index in the Pinecone console or via the SDK, its field map defaults to `text` — you must set the field map's text field to **`chunk_text`**, otherwise upserts will fail validation.

### Search records

Search an index using natural-language query text — Pinecone embeds it server-side. Request top-K results (1–10,000, default 10), optionally filter by metadata, and optionally restrict which record fields are returned. The metadata `filter` and `fields` inputs operate on the extra keys you stored on each record at upsert time (anything beyond `_id` and `chunk_text`).

## Key Benefits

- **No-code simplicity:** Create Pinecone indexes and manage text records from Softr's visual workflow builder — no SDK or scripting required.
- **Integrated embedding:** Skip the embedding step entirely — let Pinecone embed your text records and search queries server-side using its built-in models.
- **Real-time semantic search:** Surface relevant content to your users instantly based on meaning, not keywords.
- **AI workflow ready:** Combine Pinecone with the OpenAI, Anthropic, or other AI actions to build retrieval-augmented generation pipelines.

## Example Use Cases

| Use Case                              | Description                                                                                            |
| :------------------------------------ | :----------------------------------------------------------------------------------------------------- |
| **RAG over your knowledge base**      | Upsert document text into Pinecone, then search for relevant context to ground an AI assistant's answers. |
| **Semantic search for help articles** | Index support content and surface the closest matches when a user submits a support form.             |
| **Personalized recommendations**      | Upsert profile or item text and search Pinecone to find the most similar items, products, or other users. |
| **Duplicate detection**               | Search for near-duplicate records before adding new ones to a database.                                |
| **AI-powered tagging**                | Search records by similarity to known categories and assign tags automatically.                        |

## How to Connect Softr with Pinecone

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Pinecone action.
3. In the **Account** field, connect your Pinecone account and enter **Your Pinecone API key** (it starts with `pcsk_`).
4. Your API key can be found in the [Pinecone console](https://app.pinecone.io) under **Project → API Keys**.
5. Configure your inputs (index, records, query text, etc.) and save.
6. Activate your workflow.
