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
   docker compose -f deploy/compose.yml --env-file deploy/.env up -d
   ```

## Change the database password

Do not do this alone: the password is stored in two places (the database and the settings file). Ask the developer.

## The settings file

`deploy/.env` holds every secret. It is never in git. Keep a copy in the team password manager, because if the server is lost the file is lost too.

## Check it worked

- After a key change, you are asked to sign in again.
- A new password lets the user in.

_Last checked: YYYY-MM-DD_
