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

## Workflow action pages carry versions

Softr workflow actions are versioned (`1.0.0`, `1.1.0`, `1.2.0`, ...). A step keeps the version it was created with,
so several versions run in production at the same time, and a page must say which version(s) a statement applies
to. The pattern follows GitLab's version history notes.

- **One page per action** under `workflows/actions/<action>.mdx`, covering every version the service still runs. A
  new version extends the page; it never gets a page of its own.
- **Page scope**: a quote line right under the H1: `> **Applies to:** Run Custom Code 1.0.0, 1.1.0`. Every action
  page has this line, also when the action has a single version (`> **Applies to:** Send Email 1.0.0`). A reader,
  including a model trained on these docs or reading them later, must be able to tell which versions the text was
  written for and to recognise a version the page does not list as newer than the docs.
- **Section scope**: a quote line right under the heading: `> **Applies to:** 1.2.0 and later`, or an explicit list
  such as `1.0.0, 1.1.0`. No line means the section applies to every version of the page.
- **Item scope**: plain text in tables, lists and sentences: `` `fetch` (1.2.0 and later)``,
  `` `http`, `https` (1.0.0, 1.1.0)``.
- **Version history**: a quote block right under the heading (after the "Applies to" line when both exist), oldest
  entry first, one verb per line:

  ```markdown
  > **Version history**
  > - Introduced in 1.2.0.
  > - Changed in 1.3.0: the response is now ...
  > - Removed in 1.3.0.
  ```

  A change inside an existing version, with no version bump, names the month instead:
  `Added to 1.0.0 and 1.1.0 in September 2026.`
- **Versions table**: every action page ends with `## Versions`, newest first, one row per version on what changed.
- **Removal**: when the service stops running a version, delete its history lines and drop it from every "Applies
  to" line. A section or item marker that then lists every remaining version is dropped; the page line stays.

Working rules:

- Every change to an action page carries the version(s) it applies to, in the scope that fits: page, section, item
  or history entry.
- The versions come from the Studio's action specifications and the workflows service, never from memory.
- A page describes what is live in production. Docs for a change wait for that change to be deployed before they
  merge, because merging deploys.
