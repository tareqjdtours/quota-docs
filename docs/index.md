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

## What it is made of

| Box | What it does |
|---|---|
| **frontend** | The website staff open (nginx). It also passes requests to the backend. |
| **backend** | The brain: prices quotes, builds offers and PDFs, sends email, hands booked quotes to the CRM. |
| **db** | The database (PostgreSQL). All quotes and the catalogue live here. |
| **backup** | A helper that saves a copy of the database every night. |

All run together with **Docker Compose**. A **volume** is the folder Docker
keeps data in, so data survives restarts. The ones that matter: **pgdata** (the
database) and **backups** (the nightly copies). The pictures offers show are in a
separate folder on the server (`MEDIA_ROOT`), **not** in the database.

## Unlike the CRM, nothing deploys by itself

When code is pushed to GitHub, robots only **test** it. They do not update the
server. Someone must log in and run the [update steps](deploy/update.md). That
also means **the database update is a separate step you must run yourself**.

## The golden rules

1. **Back up before any update.** See [Backups](maintenance/backups.md).
2. **Never delete a Docker volume.** Never run `docker compose down -v` or `docker volume prune`.
3. **After every update, run the database update step**, or pages will error.
4. **Read the error before you act.** Start at the [site-down page](crashes/site-down.md).
5. **Write down what you did**, with times.

## Who to contact

_(Name, phone, role. Fill this in.)_

!!! warning "Keep this site free of secrets"
    GitHub Pages sites are public. Never write passwords, keys, IP addresses or customer data here.
