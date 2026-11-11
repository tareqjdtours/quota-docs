# Restore the database from a backup

**When to use this:** Data was lost or damaged, or you are rebuilding a server.
**Time it takes:** 20 minutes
**You need:** [SSH access](../connect.md), in the Quota folder, and a backup file ending in `.sql.gz`. See [Backups](../maintenance/backups.md).

!!! danger "This replaces everything in the live database"
    Anything entered after the backup was taken is **lost**. Tell staff to stop first. If the database still starts, take a fresh [backup](../maintenance/backups.md) before you begin.

## Before you start

- [ ] Staff told to stop using the app.
- [ ] You know which backup file and its date.
- [ ] The file is on the server. To take one from the backup volume:

  ```bash
  docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env cp backup:/backups ./backups-copy
  ls backups-copy
  ```

## Steps

1. Stop everything that uses the database:

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env stop backend backup
   ```

2. Empty the database:

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec -T db psql -U postgres -c 'DROP DATABASE quota' -c 'CREATE DATABASE quota'
   ```

3. Load the backup (change the file name):

   ```bash
   gunzip -c backups-copy/quota_<date>.sql.gz | docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec -T db psql -U postgres quota
   ```

4. Start everything and bring the database shape up to date:

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env start backend backup
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec backend alembic upgrade head
   ```

## Check it worked

- `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env ps` shows all boxes running.
- Sign in and open a **recent quote** and its offer.
- Tell staff which date and time the data goes back to, so they can re-enter anything missing.

## If something goes wrong

| You see | Do this |
|---|---|
| `database "quota" is being accessed by other users` | Step 1 did not stop everything. Run it again and check with `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env ps`. |
| `gzip: not in gzip format` | Wrong or damaged file. Try another backup. |
| `service "db" is not running` | `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d db`, wait a minute, retry from step 2. |
| Errors about missing columns after the restore | Run `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec backend alembic upgrade head` again. |

_Last checked: YYYY-MM-DD_
