# Passwords and keys

**When to use this:** A password was shared by mistake, someone left, or a user is locked out.
**Time it takes:** 10 minutes
**You need:** An administrator login for a locked-out user. For the keys: the Terminal on the office Mac ([connect](../connect.md)).

## A user is locked out

Five wrong sign-in attempts in fifteen minutes lock the account for fifteen
minutes. **Wait fifteen minutes**, or an administrator can reset the password in
the app: **Administration → Users**.

## Sign everyone out and replace the signing key

The signing key (`JWT_SECRET`) proves a sign-in is genuine. Changing it signs
**everyone** out.

1. Make a new random key and copy what it prints (one long line of letters and numbers):

   ```bash
   openssl rand -hex 32
   ```

2. Open the settings file:

   ```bash
   cd ~/quota
   nano deploy/.env
   ```

3. With the arrow keys, go to the line that starts with `JWT_SECRET=`. Delete what is after the `=` and paste
   the new key. Change **nothing else**.
4. Save and close: press **Ctrl O**, then **Return**, then **Ctrl X**.
5. Restart:

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
