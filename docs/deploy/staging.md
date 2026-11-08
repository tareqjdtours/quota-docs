# The staging copy

**When to use this:** You want to try a change on real data before it reaches the office.
**Time it takes:** however long you need to try it

## What it is

A second Quota on the same server, on **port 8080** of the server's office address. Every change that passes
the tests is installed there automatically within minutes. Its data is a copy of the real Quota.

## What is switched off on staging

So nothing you do there reaches a client, a hotel or another system:

- **No e-mail leaves.** Everything "sent" lands in a mail catcher on the server instead.
- **Mailboxes are not read** and cannot be opened from staging.
- **No reminders** go to clients, and no daily digest.
- **Nothing is written** to the CRM or the old Access system.
- **Pictures are read-only.** Uploading a picture fails on staging; that is expected.

## Refresh its data

Its data does not follow the real Quota by itself. The developer refreshes it from the real one when needed
(the commands are in `deploy/README.md`, "The staging copy").

## Next

When it works: [Release a new version](update.md).

_Last checked: 2026-11-08_
