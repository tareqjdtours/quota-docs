# Go back to an earlier version

**When to use this:** A released version works but something in it is wrong, and you want the one before.
**Time it takes:** 5 minutes
**You need:** A GitHub account with write access. No server access.

!!! warning "Going back does not undo database changes"
    Database updates only move forward. They are written so the earlier version keeps working. If it ever does not, [restore the backup](../crashes/restore-database.md) the server took just before the update (`pre-update_...` in the backups folder).

## Steps

1. GitHub → the repository (backend or frontend) → **Packages** → `quota-backend` (or `quota-frontend`).
2. Find the release you want: each one is kept as `prod-<date>-<time>`.
3. **Actions** → **Release to production** → **Run workflow**, type that name instead of `main`, press the green button.
4. Wait about 5 minutes.

## Check it worked

- Sign in and open an order.
- The release run's summary names the version you typed.

!!! tip "Back to normal"
    The next time you press Release to production with `main`, the office follows the latest again.

## If something goes wrong

| You see | Do this |
|---|---|
| Errors about missing columns | The database is ahead of the code. [Restore the backup](../crashes/restore-database.md). |
| The release run is red: "not a tag" or "not found" | The name is wrong. Copy it again from Packages. |

_Last checked: 2026-11-08_
