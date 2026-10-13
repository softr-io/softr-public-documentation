# Agent instructions for this repository

Shared entry point for every AI agent working on these docs. `CLAUDE.md` is just an `@AGENTS.md` import, so add
rules here and never duplicate them there.

## What this is

Softr's public documentation, https://docs.softr.io, built with [Mintlify](https://www.mintlify.com/docs). Pages are
MDX files under topic folders; the navigation lives in `docs.json`. Merging to `main` deploys to production.

## Previewing a change

- Every pull request gets a preview deployment: the `mintlify` bot comments the preview URL on the PR and a
  "Mintlify Deployment" check reports the build. The URL stays the same for the life of the branch.
- Locally: `npx --yes mint@latest dev` (or `npm i -g mint` and `mint dev`) from the repo root.
- Every page is also served as Markdown at `<page URL>.md`, indexed by `llms.txt`. AI clients (the Softr Workflows
  CLI catalog, assistants) read that form. A custom snippet component (JSX under `snippets/`) shows up there as raw
  source, so prefer plain Markdown and Mintlify's built-in components.

## Writing conventions

`CONVENTIONS.md` is the source of the writing conventions — read it before editing any page. The rules that matter most
for an agent:

- Workflow action pages carry versions: a `> **Applies to:** ...` line under the H1 of every action page (also with a
  single version), one under any section that does not apply to every version of the page, a `> **Removed in:** ...`
  line for a section later versions dropped, plain-text versions next to items in tables and lists, and a `## Versions`
  table at the end. A `> **Version history**` block only for a change inside the versions a section applies to.
- Every change to an action page carries the version(s) it applies to, in the scope that fits. A new version extends
  the existing page; it never gets a page of its own.
- The versions come from the Studio's action specifications and the workflows service, never from memory.
- A page describes what is live in production. Docs for a change wait for that change to be deployed before they
  merge, because merging deploys.
