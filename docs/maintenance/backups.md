# Backups

**When to use this:** Before every update, and to make sure copies exist off the server.
**Time it takes:** 5 minutes
**You need:** [SSH access](../connect.md), in the Quota folder.

## What is already automatic

A helper box called **backup** saves a copy of the database **every night** (at
the hour set in the settings, 02:00 by default), plus once each time it starts.
Copies are kept 30 days by default and older ones are deleted. They live in the
**backups** volume, **on the same server as the database**.

!!! danger "A copy on the same machine is not enough"
    If the server dies, those copies die with it. Copy them elsewhere regularly.

## Copy the nightly backups off the server

```bash
docker compose -f deploy/compose.yml --env-file deploy/.env cp backup:/backups ./backups-copy
```

Then move the `backups-copy` folder to another computer or a cloud drive.

## Take a backup by hand (before an update)

```bash
docker compose -f deploy/compose.yml --env-file deploy/.env exec -T db pg_dump -U postgres quota | gzip > quota_manual.sql.gz
```

Use a clear name if you keep several, for example `quota_before-update-2026-11-01.sql.gz`.

## The pictures are not in the database

The pictures offers show are in the `MEDIA_ROOT` folder on the server. Back that
folder up with the server's normal file backups. The generated PDFs are only a
cache and are made again when needed.

## Check it worked

- The file exists and is not tiny: `ls -lh quota_manual.sql.gz`.
- A backup you have never restored is a hope. Once, on a spare machine, try [Restore the database](../crashes/restore-database.md).

## If something goes wrong

| You see | Do this |
|---|---|
| `service "db" is not running` | The database is stopped: [Site is down](../crashes/site-down.md) |
| An empty or very small file | The command failed; check the disk with `df -h` and retry |
| "pg_dump failed" in the backup log | Check the disk and the database password in the settings |

_Last checked: YYYY-MM-DD_
