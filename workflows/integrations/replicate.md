# Replicate integration

Connect Replicate with your Softr applications to generate AI images on demand inside your workflows. Create product shots, listing visuals, and marketing images with state-of-the-art models like Flux — straight from the data in your app, no code required.

## Overview

The Softr Replicate integration runs image-generation models hosted on Replicate and hands the resulting image back to your workflow. Write a prompt — or build one from form answers and record fields — and get an image you can attach to a record, embed in an email, or display in your app.

In a typical Softr app, Replicate turns user input into visuals: a member lists a product in your marketplace, a client submits a creative brief through a form block, a new event record is added — and the workflow generates matching imagery automatically, so every record ships with a picture.

## Available Actions

### Flux via Replicate

Generate high-quality images from a text prompt using the Flux family of models — great for realistic scenes, product visuals, and marketing assets.

### Pruna via Replicate

Generate images with Pruna-optimized models for faster, more cost-efficient results — ideal for high-volume image workflows.

## Key Benefits

- **Images from your app's data:** Build prompts from form answers, record fields, and previous steps, and attach the results right back to your records.
- **State-of-the-art models:** Use Flux for top-tier quality or Pruna-optimized models when speed and cost matter most.
- **No-code image pipeline:** No GPUs, SDKs, or scripts — configure the prompt visually and let the workflow do the rest.
- **Pay-as-you-go:** Replicate bills only for what you run, so occasional and bursty workloads stay affordable.

## Example Use Cases

| Use Case                            | Description                                                                                                  |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **Marketplace listing images**      | When a member adds a product without a photo, generate one from the title and description automatically.       |
| **Event and community visuals**     | Create a unique cover image for each new event or community post added to your app.                            |
| **Creative request portal**         | Let clients order visuals through a form block — the workflow generates the image and saves it to their record. |
| **Marketing assets on demand**      | Generate campaign or social images from a content calendar stored in your database.                             |
| **Personalized member graphics**    | Create welcome banners or profile artwork from each new member's sign-up details.                               |

## How to Connect Softr with Replicate

1. Open your Softr app and go to **Workflows**.
2. Create a new workflow and add a Replicate action.
3. Click **Connect Replicate** and paste your Replicate API token. You can create one at [replicate.com](https://replicate.com) under **Account settings → API tokens**.
4. Pick the model action you want — Flux or Pruna — and write your image prompt.
5. Map fields from your Softr forms, records, or previous workflow steps into the prompt.
6. Save and activate your workflow.
