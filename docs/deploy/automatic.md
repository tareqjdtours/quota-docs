# How a change reaches the office (the pipeline)

**When to use this:** You want to know what the ticks on GitHub mean and how a change goes live.
**Time it takes:** 5 minutes to read

## The short version

```
push to main ─► CI: style check + tests ─► builds the new version ─► the staging copy installs it
                Security: secrets, libraries, known holes                        │
                                                       you try it on staging ◄───┘
you press "Release to production" ─► the office server installs it within minutes
   (backup first, then update, then checks; if anything is wrong it goes back by itself)
```

Nothing goes live in the office until someone presses **Release to production**.

## The robots on GitHub

Open the repository on GitHub → **Actions** tab.

| Robot | When | What it does |
|---|---|---|
| **CI** | Every push and pull request | Checks the code style and runs the tests. On `main`, when they pass, builds the new version. |
| **Security** | Every push, and every Monday | Looks for passwords committed by mistake, libraries with known security holes, and holes in the built version. |
| **Release to production** | Only when someone presses it | Marks the version staging runs as the one the office server should run. |

| You see | Meaning |
|---|---|
| Green tick on CI | Tests passed; staging gets it within minutes. |
| Red cross on CI | A test or style check failed. Nothing was built; staging and the office stay as they were. Tell the developer. |
| Red cross on Security | A library needs updating or something looks like a password. Not urgent for the site, but tell the developer this week. |
| Yellow dot | Still running. Wait. |

## Next

- Try a change before it goes live: [The staging copy](staging.md)
- Put it live: [Release a new version](update.md)

_Last checked: 2026-11-08_
