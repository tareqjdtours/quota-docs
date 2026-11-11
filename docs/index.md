# Quota Dashboard Runbook

How to look after the Quota Dashboard (the quoting tool for Jordan Select Tours and Jordan Direct Tours), and
what to do when something goes wrong. Written so that anyone on duty can follow it, step by step, even if they
have never done it before.

!!! danger "Something is broken right now?"
    Go straight to **[The site is down: first five minutes](crashes/site-down.md)**.

## Pick what you need

| I want to... | Go to |
|---|---|
| Check that Quota is healthy | [Daily health check](maintenance/health-checks.md) |
| Fix Quota when staff cannot open it | [The site is down](crashes/site-down.md) |
| Fix one thing that fails (a PDF, an e-mail, a picture) | [Common errors](crashes/common-errors.md) |
| Put a new version live | [Release a new version](deploy/update.md) |
| Undo a bad version | [Go back to an earlier version](deploy/rollback.md) |
| Check the backups | [Backups](maintenance/backups.md) |
| Know how staff and clients get in | [How staff and clients reach it](reach.md) |
| Look after the office Mac itself | [The office Mac](maintenance/office-mac.md) |
| Type commands on the Mac from my own computer | [Connect to the server](connect.md) |
| Change a password or key | [Passwords and keys](maintenance/secrets.md) |
| Bring the data back from a backup | [Restore the database](crashes/restore-database.md) |

## How to use these pages

- **Do the steps in order**, one at a time. Do not skip a step because it looks done.
- Grey boxes are **commands**. Click the copy button at the box's top right, paste it into the Terminal with
  **⌘ V**, and press **Return**.
- After most steps there is a picture of a Terminal window. It shows what you type (marked **you type this**)
  and what comes back. **Green** is what you want to see. **Red** means something is wrong: look at the table
  *If you see something else* at the bottom of the page.
- The pictures are examples. Dates, times and numbers on your screen will be different. That is normal.

## Words used on these pages

| Word | What it means |
|---|---|
| **The office Mac** | The Mac mini in the office that runs Quota. Every command on this site is typed on it. |
| **Terminal** | The Mac app where you type commands. Open it with **⌘ Space**, type `Terminal`, press **Return**. |
| **The Quota folder** | The folder `~/quota` on the office Mac. Every command on this site is typed there. |
| **Box (container)** | One part of Quota running on the Mac: `frontend` (the website), `backend` (the brain), `db` (the database), `backup` (nightly copies), `mail` (a test mail catcher). |
| **Release** | Putting a new version of Quota live, with a button on GitHub. |
| **Tunnel** | A safe link from the office Mac to Cloudflare, so people can reach Quota from outside without opening the router. |

## Typing the commands

The live copy of Quota is called **quota** and uses two settings files, so many commands start like this:

```bash
docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env
```

Always copy the **whole** command from the page. If you leave out a part, the command talks to an empty copy
and shows nothing.

## How a new version arrives

Code changes are tested by robots on GitHub, but **nothing reaches the office until someone presses Release to
production**. The office Mac then installs it by itself within minutes: it takes a backup first, updates, checks
itself, and goes back to the old version on its own if anything fails. See
[How a change goes live](deploy/automatic.md).

## How people reach it

| Who | Address | What protects it |
|---|---|---|
| Staff, office and home | `https://quota.selectdmc.com` | A one-time code sent to a work e-mail, then the Quota sign-in |
| Clients | `trip.jordanselect.com` (JST) and `trip.jdtours.com` (JDT) | Only the map, the online offer and pictures; nothing else answers |

See [How staff and clients reach it](reach.md).

## The golden rules

1. **Never delete a Docker volume.** Never run `docker compose down -v` or `docker volume prune`. That erases the database.
2. **Never start or stop other servers on ports 80, 5190 or 8010.** They belong to the live Quota.
3. **Read the message before you act.** Change one thing at a time.
4. **Write down what you did**, with the times.
5. **When unsure, stop and ask.** Waiting is safer than guessing.

## Who to contact

_(Name, phone, role. Fill this in.)_

!!! warning "Keep this site free of secrets"
    This site is public. Never write passwords, keys, IP addresses or customer data here. The pictures on it
    are made-up examples.
