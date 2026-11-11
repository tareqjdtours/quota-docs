# The site is down: first five minutes

**When to use this:** Staff cannot open the Quota Dashboard, or every page shows errors.
**Time it takes:** 5 minutes to find the cause
**You need:** [SSH access](../connect.md), in the Quota folder.

!!! tip "Stay calm, change one thing at a time"
    Your data is safe in the database volume. Most problems are fixed by a restart. Do **not** delete anything.

## Steps

1. **What is running?**

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env ps
   ```

   Any box that is exited, restarting or unhealthy is the suspect.

2. **Is the computer OK?**

   ```bash
   df -h
   ```

   100% full stops the database. Tell the developer; do not delete volumes.

3. **Read the last messages:**

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env logs --tail=100 backend
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env logs --tail=50 db
   ```

4. **Match what you see** with the table below.

5. **If unsure, restart.** It keeps all data.

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env restart
   ```

   If that does not help:

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env down
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d
   ```

   Never add `-v` to `down`: it erases the database.

## What you see and what to do

| You see | Meaning | Do this |
|---|---|---|
| Site will not load, `frontend` not running | The web box stopped | `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d` |
| Page loads, actions give **502** | The web box cannot reach the backend | `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env restart backend frontend` |
| `backend` keeps restarting | Often the database is down, or a setting is wrong | Read the backend logs; check `db` |
| `db` not running | Database stopped | Check disk (step 2), then `up -d`. If it will not start: [Restore](restore-database.md) |
| Errors about a missing column or table | New code, old database shape | Run `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec backend alembic upgrade head` |
| "locked" at sign-in | Too many wrong passwords | Wait 15 minutes |
| A PDF, email or picture error | A single feature, not the whole site | [Common errors](common-errors.md) |
| Office address works, `quota.selectdmc.com` does not | A tunnel, not Quota | [How staff and clients reach it](../reach.md) |
| Staff see a plain **403** | A test server took port 5190 | Tell the developer; do not stop the live boxes |
| Nothing at all, `Cannot connect to the Docker daemon` | OrbStack is not running | [The office Mac](../maintenance/office-mac.md) |
| Whole server does not answer | Off or network down | [The server is gone](server-lost.md) |
| Just updated | New version problem | [Go back](../deploy/rollback.md) |

## Check it worked

```bash
curl http://localhost/health
curl http://localhost/api/v1/health/db
```

Then sign in and open a quote.

## After it is fixed

- Write down what happened, what you did, and the times.
- Tell the team it is back.
- Take a fresh [backup](../maintenance/backups.md).

_Last checked: 2026-11-11_
