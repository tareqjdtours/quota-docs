# Release a new version

**When to use this:** A change has been tested and you want it in the office.
**Time it takes:** 5 minutes
**You need:** A GitHub account with write access to the two Quota repositories. No server access.

!!! note "Staff may see a pause of under a minute"
    The site restarts while the new version starts. Release outside busy hours when you can.

## Before you start

- [ ] The latest **CI** run on `main` has a green tick.
- [ ] Someone tried the change on a test copy. ([The staging copy](staging.md) is switched off for now.)

## Steps

1. GitHub → the **backend** repository → **Actions** → **Release to production** → **Run workflow**. Leave `main` and press the green button.
2. If the screens changed, do the same in the **frontend** repository.
3. Wait about 5 minutes. The office server checks every 2 minutes, takes a backup, updates the database and starts the new version.

## Check it worked

- The release run on GitHub has a green tick, and its summary names the version.
- Open Quota, sign in, open an order and its offer.
- On the Mac, `tail -3 ~/Library/Logs/quota-update.log` ends with `done:`. (The monitor e-mails are not set up yet, so do not wait for one.)

## If something goes wrong

The server checks the new version itself. If it does not start properly, it **puts the previous version back on its own** and the monitor e-mails "fail".

| You see | Do this |
|---|---|
| A "fail" e-mail after a release | The old version is running again. Tell the developer; the log is on the server in `~/Library/Logs/quota-update.log`. |
| The release run is green but the office still has the old version after 10 minutes | The Mac could not download it. See [Quota's own GitHub sign-in](../maintenance/office-mac.md#quotas-own-github-sign-in). |
| The release run is red | Nothing changed in the office. Check you typed a real version name. |
| The new version runs but something is wrong | [Go back to an earlier version](rollback.md). |

_Last checked: 2026-11-11_
