# Writing conventions

How the pages of docs.softr.io are written. `AGENTS.md` points AI agents here; humans read it directly.

## Pages are plain Markdown first

Every page is also served as Markdown at `<page URL>.md` and indexed by `llms.txt`, and AI clients (the Softr Workflows
CLI catalog, assistants) read that form. Prefer plain Markdown and Mintlify's built-in components (`Note`, `Tip`,
`Warning`, `Frame`, `CodeGroup`, `Steps`). A custom JSX snippet under `snippets/` shows up in that export as raw
source, so it is a last resort.

## Workflow action pages carry versions

Softr workflow actions are versioned (`1.0.0`, `1.1.0`, `1.2.0`, ...). A step keeps the version it was created with, so
several versions run in production at the same time, and a page must say which version(s) a statement applies to. The
docs describe what a version offers, not when it got it.

### One page per action

Each action has one page under `workflows/actions/<action>.mdx` that covers every version the service still runs. A
new version extends the page; it never gets a page of its own.

### Applies to

A quote line, `> **Applies to:** ...`, names the versions a piece of text was written for.

- **Page scope**, right under the H1, on every action page, also when the action has a single version:

  ```markdown
  # Run Custom Code

  > **Applies to:** Run Custom Code 1.0.0, 1.1.0
  ```

  A reader, including a model trained on these docs or reading them later, must be able to tell which versions the
  text was written for and to recognise a version the page does not list as newer than the docs.

- **Section scope**, right under the heading, when a section does not apply to every version of the page:

  ```markdown
  ## Calling APIs with `fetch`

  > **Applies to:** 1.2.0 and later
  ```

  An explicit list (`1.0.0, 1.1.0`) or `X and later`. No line means the section applies to every version of the page.

- **Item scope**, plain text inside tables, lists and sentences: `` `fetch` (1.2.0 and later)``,
  `` `http`, `https` (1.0.0, 1.1.0)``.

### Removed in

A section that later versions dropped gets a second line in the same quote block, with the version and the
replacement:

```markdown
## Calling HTTP APIs with `http` and `https`

> **Applies to:** 1.0.0, 1.1.0
>
> **Removed in:** 1.2.0. Use [`fetch`](#calling-apis-with-fetch) instead.
```

### Version history

A quote block right under the heading (after the lines above when they exist), only for a change inside the versions
the section applies to. Oldest entry first, one verb per line:

```markdown
> **Version history**
> - Changed in 1.3.0: the response is now ...
> - Changed in 1.4.0: ...
```

Not history: "Introduced in 1.2.0" under "Applies to: 1.2.0 and later", a removal entry next to a "Removed in" line,
and a capability added to versions that already exist — the section just carries the "Applies to" line of those
versions.

### Versions table

Every action page ends with a `## Versions` section: a sentence on how the reader recognises the lines above, then a
table, newest first, one row per version on what changed.

### Retiring a version

When the service stops running a version, delete its history lines and drop it from every "Applies to" line. A
section or item marker that then lists every remaining version is dropped; the page line stays.

### Where the versions come from

The Studio's action specifications and the workflows service, never memory. A page describes what is live in
production: docs for a change wait for that change to be deployed before they merge, because merging deploys.
