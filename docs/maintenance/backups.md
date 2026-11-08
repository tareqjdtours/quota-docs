# Backups

**When to use this:** To know where the copies are, and to check they are being made.
**Time it takes:** 5 minutes
**You need:** [Access to the server](../connect.md) for the checks.

## What is automatic

| When | What | Where |
|---|---|---|
| Every night, 02:00 | The database (about 120 MB) and Quota's own files (offer PDFs, mail attachments) | The server's backups folder (30 days of database copies, 7 of files) |
| Every night, 03:15 | The database copies, Quota's files and the offer pictures | The **backup SSD** plugged into the server, and **Cloudflare R2** (online, encrypted on the server first) |
| Before every update | The database | The server's backups folder |
| Every Sunday, 03:30 | A test: the newest copy is restored into a scratch database and checked | Nothing kept; a "fail" e-mail if it does not work |

Only what changed is sent each night. A file changed or deleted is kept 30 days, so a mistake is never copied
over the only good copy.

!!! danger "Keep the two keys safe"
    The server's settings file and the **backup encryption password** are not in the backups. Keep both in the
    password manager. Without the password, the online copy can never be read, not even by you.

## You are told when something is wrong

The monitor e-mails if a night is missed, the SSD is unplugged or full, the online copy fails, or the Sunday
test fails. No e-mail means it worked.

## Check it by hand

On the server:

```bash
tail -5 ~/Library/Logs/quota-offsite.log     # last nights: "SSD: done", "R2: done"
tail -3 ~/Library/Logs/quota-restore.log     # last Sunday: "restore-check: ok"
```

## Take a backup by hand

In the deploy folder on the server:

```bash
docker compose -p quota -f compose.yml --env-file .env exec -T db pg_dump -U postgres quota | gzip > quota_manual.sql.gz
```

## If something goes wrong

| You see | Do this |
|---|---|
| "SSD is not there (drive unplugged?)" | Plug the SSD back in; it is checked again the next night. |
| "only N GB free" on the SSD | Tell the developer; older copies can be kept for fewer days. |
| "the newest dump is N hours old" | The nightly backup stopped: [Site is down](../crashes/site-down.md) and check the `backup` box is running. |
| "R2: copying ... failed" | Internet down that night, or the R2 key expired. Tell the developer if it repeats. |

_Last checked: 2026-11-08_
