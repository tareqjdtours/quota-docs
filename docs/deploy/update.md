# Update to a new version

**When to use this:** The developers pushed new code and you want it live.
**Time it takes:** 10 minutes
**You need:** [SSH access](../connect.md). Nothing updates automatically, so someone has to do this.

!!! warning "Staff may see a short pause"
    The site restarts. Do it outside office hours when you can.

## Before you start

- [ ] Be in the Quota folder on the server.
- [ ] [Take a backup](../maintenance/backups.md).
- [ ] Check GitHub: the latest push on `main` should have a green tick (its tests passed).
- [ ] Write down the version you are on, so you can go back:

  ```bash
  git rev-parse --short HEAD
  git -C frontend rev-parse --short HEAD
  ```

## Steps

1. Download the new code for both repositories:

   ```bash
   git pull
   git -C frontend pull
   ```

2. Rebuild and restart:

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env up -d --build
   ```

3. **Update the database.** This is not automatic. Skipping it causes errors.

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env exec backend alembic upgrade head
   ```

## Check it worked

```bash
docker compose -f deploy/compose.yml --env-file deploy/.env ps
curl http://localhost/health
```

- `db`, `backend`, `frontend` and `backup` are running.
- Open the site, sign in, open a quote, and open its offer.

## If something goes wrong

| You see | Do this |
|---|---|
| `git pull` says local changes would be overwritten | Someone edited files on the server. Do not force it; ask the developer. |
| Pages show errors about a missing column or table | Step 3 was not run, or failed. Run it and read the message. |
| The database update step fails | [Go back](rollback.md), then tell the developer the error. |
| Site is down after the update | [Site is down](../crashes/site-down.md) |

_Last checked: YYYY-MM-DD_
