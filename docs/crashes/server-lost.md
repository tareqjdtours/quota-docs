# The server is gone

**When to use this:** The machine died, was stolen, or its disk is destroyed.
**Time it takes:** About an hour, plus downloads
**You need:** GitHub access to both repositories, a new Linux machine with Docker, the settings file (`deploy/.env`) from the team password manager, the newest backup copy stored **off** the server, and the pictures folder.

!!! tip "This is why copies must be kept off the server"
    If every backup was on the dead machine, the data may be gone. Check laptops, cloud drives, and colleagues first.

## Steps

1. **Prepare a new machine** with Linux, Docker and the compose plugin.
2. **Install it** by following [First install](../deploy/first-install.md) steps 1 to 3. Use the saved `deploy/.env` instead of writing a new one. If you must make a new one, the password must match whatever the restored database expects (ask the developer).
3. **Put the pictures folder back** and point `MEDIA_ROOT` at it.
4. **Restore the data** with [Restore the database](restore-database.md), using your newest backup.
5. **Tell staff the new address** if it changed, and update `PUBLIC_BASE_URL` if so.

## Check it worked

- You can sign in, open a recent quote, and view an offer with pictures.
- A fresh [backup](../maintenance/backups.md) exists and is copied off the machine.

## If something goes wrong

| You see | Do this |
|---|---|
| No backup can be found | Check every device and cloud account the team uses. Tell the developer immediately. |
| The newest backup is old | Restore it anyway, then have staff re-enter newer work. |

_Last checked: YYYY-MM-DD_
