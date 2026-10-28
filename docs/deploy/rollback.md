# Go back to the last working version

**When to use this:** A new version broke something and you need the old one.
**Time it takes:** 15 minutes
**You need:** [SSH access](../connect.md) and the version codes you wrote down before the update.

!!! warning "Going back does not undo database changes"
    The database update (step 3 of [Update](update.md)) only moves forward. If the new version changed the database and the old code cannot work with it, [restore the backup](../crashes/restore-database.md) taken before the update.

## Before you start

- [ ] Take a [backup](../maintenance/backups.md) of the current state.
- [ ] Have the two old version codes (backend and frontend).

## Steps

1. In the Quota folder, check out the old versions:

   ```bash
   git checkout <old-backend-code>
   git -C frontend checkout <old-frontend-code>
   ```

2. Rebuild and restart:

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env up -d --build
   ```

## Check it worked

- `docker compose -f deploy/compose.yml --env-file deploy/.env ps` shows all boxes running.
- Sign in and open a quote.

!!! danger "Remember to return to the latest later"
    The server is now parked on an old version. When the fix is ready, run `git checkout main && git pull` (and the same with `git -C frontend`) before following [Update](update.md), or future updates will not work.

## If something goes wrong

| You see | Do this |
|---|---|
| Errors about missing columns | The database is ahead of the code. [Restore the backup](../crashes/restore-database.md). |
| `error: pathspec ... did not match` | The version code is wrong. Check it with `git log --oneline`. |

_Last checked: YYYY-MM-DD_
