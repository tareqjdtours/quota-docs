# What happens when code is pushed (CI)

**When to use this:** You want to know what the green or red tick on GitHub means.
**Time it takes:** 3 minutes to read

## The short version

Every push to the `main` branch and every pull request starts a robot called **CI**
on GitHub. It:

1. starts a temporary database,
2. checks the code style,
3. runs the automatic tests.

That is **all** it does. **It does not update the server.** A green tick means
"the code passed its tests", not "it is live".

## To put a new version live

Follow [Update to a new version](update.md).

## Reading the result

Open the repository on GitHub → **Actions** tab.

| You see | Meaning |
|---|---|
| Green tick | Tests passed. Safe to [update](update.md). |
| Red cross | A test or style check failed. **Do not update.** Tell the developer. |
| Yellow dot | Still running. Wait. |

_Last checked: YYYY-MM-DD_
