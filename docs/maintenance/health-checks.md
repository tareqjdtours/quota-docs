# Daily health check

**When to use this:** Every morning, or whenever you want to be sure it is OK.
**Time it takes:** 3 minutes
**You need:** A browser; for the full check, [SSH access](../connect.md).

## Quick check

1. Open the Quota Dashboard and sign in.
2. Open a recent quote and its offer.
3. Open `http://<server>/health` in a browser. It should answer `{"status":"ok"}`.

## Full check (on the server, in the Quota folder)

1. See every box:

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env ps
   ```

   Good looks like: `db`, `backend`, `frontend` and `backup` all running.

2. Check the database answers:

   ```bash
   curl http://localhost/api/v1/health/db
   ```

3. Look at the latest backend messages:

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env logs --tail=50 backend
   ```

4. Check the last backup was made:

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env logs --tail=5 backup
   ```

   You should see a line like `backup: wrote /backups/quota_<date>.sql.gz`.

5. Check disk space (a full disk stops the database):

   ```bash
   df -h
   ```

   Worry above about 85% used.

## If something goes wrong

| You see | Do this |
|---|---|
| A box is restarting or exited | [Site is down](../crashes/site-down.md) |
| No recent backup line, or "pg_dump failed" | Check the disk, then take a [manual backup](backups.md) |
| Disk above 85% | Tell the developer. Never delete Docker volumes. |

_Last checked: YYYY-MM-DD_
