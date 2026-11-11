# The office Mac

**When to use this:** The Mac was restarted, updated, or someone installed something on it; or updates stopped arriving.
**Time it takes:** 10 minutes
**You need:** A seat at the Mac or [SSH access](../connect.md).

Quota runs on the Mac mini in the office. The live copy is in the folder `~/quota`. **Never run it from any other
folder**: developers change branches in their own folders, and the live copy must stay on released versions.

## What must be true on the Mac

| Setting | Why |
|---|---|
| **OrbStack** is the Docker app, set to *Start at login* | Every Quota box and both tunnels run in it. They come back by themselves when it starts. |
| Docker's context is `orbstack` (`docker context ls` shows a star next to it) | If another Docker app (Docker Desktop) takes over, the boxes and the CRM's test robot cannot be reached. |
| A user is logged in, and the Mac never sleeps | The update, backup and test schedules only run while someone is logged in. |
| The Mac starts by itself after a power cut | So Quota comes back without anyone in the office. |
| **Ollama** runs (it starts when the user logs in) | The mailbox search by meaning uses it. Without it, search still finds words and numbers, but not meanings. |

!!! warning "Do not install Docker Desktop"
    On 9 November 2026 Docker Desktop was opened on this Mac. It took over Docker's settings, which broke the CRM's
    tests and later stopped Quota's updates. If it happens again: `docker context use orbstack`.

## The schedules

Four jobs run on their own. Their logs are in `~/Library/Logs/`:

| Job | When | Log |
|---|---|---|
| Install a released version | Every 2 minutes | `quota-update.log` |
| Copy backups off the Mac | Every night at 03:15 | `quota-offsite.log` |
| Prove the backups restore | Every Sunday | `quota-restore.log` |
| The staging copy | Switched off (see [The staging copy](../deploy/staging.md)) | `quota-staging-update.log` |

Show them: `launchctl list | grep quota`. Put them back after a reinstall: `cd ~/quota/deploy && ./install-macos.sh`.

## Quota's own GitHub sign-in

The Mac downloads new versions from GitHub's package store, signed in with a read-only token. Quota keeps this
sign-in in its own folder, `~/quota/deploy/.docker`, apart from the Mac's usual one, because the CRM's test robot
runs on the same Mac and signs out of the usual one after every run.

If `quota-update.log` says **unauthorized**, the sign-in is gone or the token expired. Make a new token on GitHub
with only **read:packages**, then on the Mac:

```bash
DOCKER_CONFIG=~/quota/deploy/.docker docker login ghcr.io -u <github-user>
```

Paste the token when it asks for the password. The next run (within 2 minutes) installs whatever was released.

## Check it worked

```bash
tail -3 ~/Library/Logs/quota-update.log
```

The last lines say `done:` or that nothing new was released, not `unauthorized` or `FAILED`.

## If something goes wrong

| You see | Do this |
|---|---|
| "I pressed Release but nothing changed" | Read `quota-update.log`. `unauthorized`: the sign-in above. `FAILED ... rolled back`: the new version was refused; tell the developer. |
| `Cannot connect to the Docker daemon` | OrbStack is not running. Open it. Then `docker context use orbstack`. |
| Mail search ignores meanings | `brew services restart ollama` on the Mac, logged in as the usual user. |
| After a power cut nothing came back | Someone must log in at the Mac once. Then check OrbStack started. |

_Last checked: 2026-11-11_
