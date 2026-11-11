# Release a new version

**When to use this:** The developer says a change is ready and tested, and asks for it to go live.
**Time it takes:** 5 minutes
**You need:** A GitHub account with write access to the two Quota repositories. No Terminal needed.

!!! note "Staff may see a pause of under a minute"
    Quota restarts while the new version starts. Release outside busy hours when you can.

## Before you start

- [ ] The developer says the change is ready.
- [ ] On GitHub, the repository's **Actions** tab shows a **green tick** on the latest **CI** run on `main`.
  A red cross means it is not ready: stop and tell the developer.

## Steps

1. Open GitHub and go to the **quota-dashboard-backend** repository.
2. Click the **Actions** tab (at the top, next to *Pull requests*).
3. In the list on the left, click **Release to production**.
4. On the right, click the grey **Run workflow** button. A small box opens.
5. Leave **Branch: main** and leave the box under it saying `main`. Click the green **Run workflow** button.
6. If the developer says **the screens changed too**, do steps 1 to 5 again in the **quota-dashboard-frontend**
   repository.
7. Wait about 5 minutes. The office Mac checks every 2 minutes, takes a backup, updates and starts the new version.

## Check it worked

- On GitHub, the new **Release to production** run shows a **green tick**.
- Open Quota, sign in, open an order and its offer.
- If you are at the office Mac: `tail -3 ~/Library/Logs/quota-update.log` ends with `done:`
  (see the picture on [The office Mac](../maintenance/office-mac.md)).

## If something goes wrong

The Mac checks the new version itself. If it does not start properly, it **puts the previous version back on
its own**.

| You see | Do this |
|---|---|
| The release run has a red cross | Nothing changed in the office. Check you left `main` in the box, and try again once. Then tell the developer. |
| Green tick, but after 10 minutes Quota still has the old version | The Mac could not download it. See [Quota's GitHub sign-in](../maintenance/office-mac.md#quotas-github-sign-in). |
| The new version runs but something is wrong in it | [Go back to an earlier version](rollback.md). |

_Last checked: 2026-11-11_
