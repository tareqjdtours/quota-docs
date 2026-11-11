# Quota Dashboard Runbook

How to deploy, look after and fix the Quota Dashboard (the quoting tool for
Jordan Select Tours and Jordan Direct Tours). Written for whoever is on duty,
including when the usual person is away. Every page is a short list of steps.

!!! danger "Something is broken right now?"
    Go straight to **[The site is down: first five minutes](crashes/site-down.md)**.

## Pick what you need

| I want to... | Go to |
|---|---|
| Open a terminal on the server | [Connect with SSH](connect.md) |
| Install it on a new machine | [First install](deploy/first-install.md) |
| Put a new version live | [Update to a new version](deploy/update.md) |
| Undo a bad version | [Go back](deploy/rollback.md) |
| Check it is healthy | [Daily health check](maintenance/health-checks.md) |
| Back up or copy backups | [Backups](maintenance/backups.md) |
| Change a password or key | [Passwords and keys](maintenance/secrets.md) |
| Bring the data back | [Restore the database](crashes/restore-database.md) |
| Fix a PDF, email or picture error | [Common errors](crashes/common-errors.md) |
| Look after the office Mac itself | [The office Mac](maintenance/office-mac.md) |
| Know how staff and clients get in | [How staff and clients reach it](reach.md) |

## What it is made of

| Box | What it does |
|---|---|
| **frontend** | The website staff open (nginx). It also passes requests to the backend. |
| **backend** | The brain: prices quotes, builds offers and PDFs, sends email, hands booked quotes to the CRM. |
| **db** | The database (PostgreSQL). All quotes and the catalogue live here. |
| **backup** | A helper that saves a copy of the database every night. |
| **tunnels** | Two small boxes outside the stack, `quota-staff-tunnel` and `quota-tunnel`, that carry staff and client traffic from Cloudflare. |

All run together with **Docker Compose**. A **volume** is the folder Docker
keeps data in, so data survives restarts. The ones that matter: **pgdata** (the
database) and **backups** (the nightly copies). The pictures offers show are in a
separate folder on the server (`MEDIA_ROOT`), **not** in the database.

## How a new version arrives

Code pushed to GitHub is tested and built by robots, but **nothing reaches the office until someone presses
Release to production** on GitHub. The office Mac then installs it by itself within minutes: backup first,
database update, health checks, and it goes back to the old version on its own if anything fails.
See [How a change goes live](deploy/automatic.md).

## How people reach it

| Who | Address | What protects it |
|---|---|---|
| Staff, office and home | `https://quota.selectdmc.com` | Cloudflare Access: a one-time code to a work e-mail, then the Quota sign-in |
| Clients | `trip.jordanselect.com` (JST) and `trip.jdtours.com` (JDT) | Only the map, the online offer and pictures; nothing else answers |

Both come through Cloudflare tunnels, so no router port is open. See [How staff and clients reach it](reach.md).

## Typing the commands

Every command on this site is typed in the Quota folder on the office Mac (`~/quota`). The production copy is
called **quota** and uses two compose files, so every command starts:

```bash
docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env
```

Leaving out `-p quota` or the office file talks to a *different*, empty copy. If `ps` shows nothing, check you
typed the whole start.

## The golden rules

1. **Back up before any update.** See [Backups](maintenance/backups.md).
2. **Never delete a Docker volume.** Never run `docker compose down -v` or `docker volume prune`.
3. **Never start or stop other servers on ports 80, 5190 or 8010.** They belong to the live copy. A test server started there takes staff's traffic away.
4. **Read the error before you act.** Start at the [site-down page](crashes/site-down.md).
5. **Write down what you did**, with times.

## Who to contact

_(Name, phone, role. Fill this in.)_

!!! warning "Keep this site free of secrets"
    GitHub Pages sites are public. Never write passwords, keys, IP addresses or customer data here.
