# Passwords and keys

**When to use this:** A password was shared by mistake, someone left, or a user is locked out.
**Time it takes:** 10 minutes
**You need:** [SSH access](../connect.md), in the Quota folder; or an administrator login.

## A user is locked out

Five wrong sign-in attempts in fifteen minutes lock the account for fifteen
minutes. **Wait fifteen minutes**, or an administrator can reset the password in
the app: **Administration → Users**.

## Sign everyone out and replace the signing key

The signing key (`JWT_SECRET`) proves a sign-in is genuine. Changing it signs
**everyone** out.

1. Edit the settings file:

   ```bash
   nano deploy/.env
   ```

2. Replace the `JWT_SECRET` value with a new long random text. Save (Ctrl+O, Enter, Ctrl+X).
3. Restart:

   ```bash
   docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d
   ```

!!! danger "Never change MAIL_SECRET_KEY"
    `MAIL_SECRET_KEY` in `deploy/.env` locks the staff mailboxes' passwords inside the database. If it changes,
    or is lost, every connected mailbox has to be connected again by its owner. Changing `JWT_SECRET` is safe
    as long as `MAIL_SECRET_KEY` stays as it is.

## Other keys on the Mac

| Key | Where | If it leaks |
|---|---|---|
| Tunnel tokens | A `token` file next to each tunnel's start script | Make a new token in Cloudflare and restart that tunnel. See [How staff and clients reach it](../reach.md). |
| GitHub download token | `~/quota/deploy/.docker` | Delete it on GitHub, make a new read-only one. See [The office Mac](office-mac.md). |
| New-mail pop-up keys (`VAPID_*`) | `deploy/.env` | Make a new pair; staff then allow the pop-ups again once. |

## Change the database password

Do not do this alone: the password is stored in two places (the database and the settings file). Ask the developer.

## The settings file

`deploy/.env` holds every secret. It is never in git. Keep a copy in the team password manager, because if the server is lost the file is lost too.

## Check it worked

- After a key change, you are asked to sign in again.
- A new password lets the user in.

_Last checked: 2026-11-11_
