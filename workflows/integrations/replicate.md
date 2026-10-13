# Replicate integration

Generate AI images directly from your Softr workflows. The Replicate integration gives your no-code app access to a curated set of image-generation models — pick the one that fits your need, drop in a text prompt, and get back a finished image as part of any automation.

## Overview

The Softr Replicate integration runs image-generation models hosted on Replicate from your workflows. Two actions ship today: **Pruna via Replicate** (a model selector covering several optimized variants like Z-Image Turbo, Flux Fast, P-Image, and SDXL Lightning) and **Flux Schnell via Replicate** (Black Forest Labs' 4-step distilled image model). One Replicate API token covers them all, and the same token will cover any future Replicate actions you add.

Inside a Softr app, this means form submissions can produce hero images for membership cards, list rows can spawn personalized illustrations, AI assistants can generate visuals on demand, and onboarding flows can hand new users an avatar built from their bio. The action returns an image URL you can drop into a Files field, attach to an email, or hand off to any downstream workflow step.

## Available Actions

### Pruna via Replicate

Generate an image with one of Pruna AI's optimized models — fast, production-ready, and tuned for quality at speed. Pick the model that matches your style preference; the rest of the inputs (prompt, aspect ratio, output format) stay the same regardless of which model you choose.

### Flux Schnell via Replicate

Generate up to four images at a time with Black Forest Labs' Flux Schnell — a 4-step distilled model designed for cinematic output in under three seconds. Pass an optional seed for reproducible results, or leave it empty to get fresh variations on every run.

## Key Benefits

- **No-code image generation:** Drop a prompt into a workflow step and get back a usable image URL — no API plumbing, no token juggling.
- **One credential, every model:** A single Replicate API token works for every action under the Replicate provider, so adding new image actions later doesn't mean reconnecting.
- **Reproducible when you need it:** Pass an optional seed to regenerate the same image deterministically — useful for template previews and A/B tests.
- **Fast by default:** Both actions ship with Replicate's accelerated inference paths enabled, so most generations finish inside a few seconds.

## Example Use Cases

| Use Case                              | Description                                                                                          |
| :------------------------------------ | :--------------------------------------------------------------------------------------------------- |
| **Personalized hero images**          | When a user signs up, generate a custom banner from their bio and store the URL on their profile.    |
| **Per-record illustrations**          | For every new record in a listing, generate a thumbnail from the record's prompt or description.     |
| **Form-driven creative briefs**       | Turn a form submission into four image variations Flux Schnell renders in parallel for review.       |
| **AI-assistant visuals**              | Let a Softr AI assistant call the action mid-conversation when a user asks for a visual.             |
| **Marketing asset batches**           | Loop over a list of campaign briefs to produce a gallery of generated images for the marketing team. |

## How to Connect Softr with Replicate

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add the **Replicate → Pruna via Replicate** or **Replicate → Flux Schnell via Replicate** action.
3. Click **Connect Replicate** and paste your Replicate API token.
4. To create a token, sign in to [Replicate](https://replicate.com/account/api-tokens) and generate a new token (must start with `r8_`). The same token works for every Replicate action, current and future.
5. Choose a model (for the Pruna action) or accept the Flux Schnell defaults, write your prompt, and configure aspect ratio and output options.
6. Save and activate your workflow.
