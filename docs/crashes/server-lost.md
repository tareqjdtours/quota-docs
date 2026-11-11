# The server is gone

**When to use this:** The machine died, was stolen, or its disk is destroyed.
**Time it takes:** About an hour, plus downloads
**You need:** GitHub access to both repositories, a new Mac with OrbStack (or a Linux machine with Docker), the settings file (`deploy/.env`) from the team password manager, the newest backup copy stored **off** the server, and the pictures folder.

!!! tip "This is why copies must be kept off the server"
    If every backup was on the dead machine, the data may be gone. Check laptops, cloud drives, and colleagues first.

## Steps

1. **Prepare a new machine.** On a Mac, set it up as [The office Mac](../maintenance/office-mac.md) describes.
2. **Install it** by following [First install](../deploy/first-install.md). Use the saved `deploy/.env` instead of writing a new one: it holds `MAIL_SECRET_KEY`, without which every mailbox must be connected again.
3. **Put the pictures folder back** and point `MEDIA_ROOT` at it.
4. **Restore the data** with [Restore the database](restore-database.md), using your newest backup.
5. **Start the two tunnels** on the new machine with their tokens (see [How staff and clients reach it](../reach.md)). Staff and client addresses then work unchanged.

## Check it worked

- You can sign in, open a recent quote, and view an offer with pictures.
- A fresh [backup](../maintenance/backups.md) exists and is copied off the machine.

## If something goes wrong

| You see | Do this |
|---|---|
| No backup can be found | Check every device and cloud account the team uses. Tell the developer immediately. |
| The newest backup is old | Restore it anyway, then have staff re-enter newer work. |

_Last checked: 2026-11-11_
