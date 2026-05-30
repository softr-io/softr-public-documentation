# Pinecone integration

Connect Pinecone with your Softr applications to power semantic search, retrieval-augmented generation (RAG), and other vector-based AI features. Build workflows that manage indexes, store embeddings, and query for semantically similar content — all without code.

## Overview

The Softr Pinecone integration allows you to connect your no-code apps with the Pinecone vector database. Automatically create and manage serverless indexes, upsert pre-computed vectors or text records (using Pinecone's integrated embedding models), and query for the most similar items at runtime. Use the results to ground LLM prompts, build smart search experiences, or recommend related content.

With Softr, you can configure end-to-end vector workflows: index your knowledge base whenever new content is added, then query Pinecone whenever a user asks a question — all without writing a single line of code.

## Available Actions

### Create index

Create a new serverless Pinecone index. Choose a cloud (AWS, GCP, Azure), region, vector type (dense or sparse), distance metric, and optional integrated embedding model.

### List indexes

List every index in the connected Pinecone project, including each index's host, dimension, metric, and status.

### Describe index

Get full details for a single index — including its data-plane host. Useful for resolving the host for downstream actions or checking readiness.

### Delete index

Delete a Pinecone index permanently. Fails when the index has deletion protection enabled.

### Upsert vectors

Insert or update pre-computed vectors (with values, optional sparse values, and optional metadata) into a chosen namespace.

### Query vectors

Find the most similar vectors to a query vector, vector ID, or sparse vector. Filter by metadata, request top-K results, and optionally include the matched vectors' values and metadata.

### Fetch vectors

Look up vectors by ID — useful when you already know which records you want to retrieve.

### Delete vectors

Delete vectors by ID, by metadata filter, or all vectors in a namespace. Exactly one mode must be selected.

### Upsert records (integrated embedding)

For indexes configured with an integrated embedding model, upsert raw text records — Pinecone embeds them server-side. Up to 96 records per request.

### Search records (integrated embedding)

Search an index with integrated embedding using natural-language query text, an existing record ID, or a pre-computed vector. Optional reranker support for higher-quality results.

### List namespaces

List the namespaces in an index, with cursor-based pagination.

### Delete namespace

Delete a namespace and all vectors it contains. The default namespace cannot be deleted by name.

## Key Benefits

- **No-code simplicity:** Manage Pinecone indexes, vectors, and namespaces from Softr's visual workflow builder — no SDK or scripting required.
- **Integrated embedding:** Skip the embedding step entirely — let Pinecone embed text records server-side using its built-in models.
- **Real-time semantic search:** Surface relevant content to your users instantly based on meaning, not keywords.
- **AI workflow ready:** Combine Pinecone with the OpenAI, Anthropic, or other AI actions to build retrieval-augmented generation pipelines.

## Example Use Cases

| Use Case                              | Description                                                                                            |
| :------------------------------------ | :----------------------------------------------------------------------------------------------------- |
| **RAG over your knowledge base**      | Upsert documents into Pinecone, then query for relevant context to ground an AI assistant's answers.   |
| **Semantic search for help articles** | Index support content and surface the closest matches when a user submits a support form.             |
| **Personalized recommendations**      | Embed user profiles and query Pinecone to find the most similar items, products, or other users.       |
| **Duplicate detection**               | Search for near-duplicate records before adding new ones to a database.                                |
| **AI-powered tagging**                | Search records by similarity to known categories and assign tags automatically.                        |

## How to Connect Softr with Pinecone

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Pinecone action.
3. Click **Connect Pinecone** and enter your Pinecone API key.
4. Your API key can be generated in the Pinecone console under **Project → API Keys**. Use a key with ReadWrite access to your project.
5. Configure your inputs (index name, namespace, vectors, query, etc.) and save.
6. Activate your workflow.
