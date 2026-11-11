# Go back to an earlier version

**When to use this:** A new version is live, but something in it is wrong, and you want the one before.
**Time it takes:** 5 minutes
**You need:** A GitHub account with write access. No Terminal needed.

!!! warning "Going back does not undo database changes"
    Database changes only move forward, and they are written so the earlier version keeps working. If it ever
    does not, the developer can [restore the backup](../crashes/restore-database.md) the Mac took just before the
    update (`pre-update_...` in the backups folder).

## 1. Find the name of the version you want

Every release is kept under a name like `prod-20261111-1302` (the date, then the time in UTC, which is
Amman time minus 3 hours).

1. Open GitHub, go to the **quota-dashboard-backend** repository.
2. On the right side of its main page, under **Packages**, click **quota-backend**.
3. Find the version from before the bad release. Copy its name that starts with `prod-` and is **not** just `prod`.

## 2. Release that version

1. In the same repository, click **Actions** → **Release to production** (left list) → **Run workflow** (right).
2. In the box that says `main`, delete `main` and paste the name you copied, for example `prod-20261110-0915`.
3. Click the green **Run workflow** button.
4. If the screens were also changed in the bad release, do the same in **quota-dashboard-frontend**, with the
   name from its **quota-frontend** package.
5. Wait about 5 minutes.

## Check it worked

- The release run on GitHub shows a **green tick**.
- Sign in to Quota and check the problem is gone.

!!! tip "Back to normal later"
    The next time someone releases with `main`, the office gets the latest version again. Tell the developer
    what was wrong so it is fixed first.

## If something goes wrong

| You see | Do this |
|---|---|
| The release run is red: "not a tag" or "not found" | The name is wrong. Copy it again from Packages. |
| Errors about missing columns | The database is ahead of the code. Tell the developer. |

_Last checked: 2026-11-11_
