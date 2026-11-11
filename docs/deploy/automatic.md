# How a change reaches the office (the pipeline)

**When to use this:** You want to know what the green ticks and red crosses on GitHub mean, and how a change reaches the office.
**Time it takes:** 5 minutes to read

## The short version

```
push to main ─► CI: style check + tests ─► builds the new version
                Security: secrets, libraries, known holes
you press "Release to production" ─► the office server installs it within minutes
   (backup first, then update, then checks; if anything is wrong it goes back by itself)
```

Nothing goes live in the office until someone presses **Release to production**.

!!! note "The staging copy is switched off"
    Since 8 November 2026 a tested version goes straight to Release. See [The staging copy](staging.md) to bring it back.

## The robots on GitHub

Open the repository on GitHub and click the **Actions** tab at the top. Each run shows a green tick, a red cross or a yellow dot.

| Robot | When | What it does |
|---|---|---|
| **CI** | Every push and pull request | Checks the code style and runs the tests. On `main`, when they pass, builds the new version. |
| **Security** | Every push, and every Monday | Looks for passwords committed by mistake, libraries with known security holes, and holes in the built version. |
| **Release to production** | Only when someone presses it | Marks the newest tested version as the one the office server should run. |

| You see | Meaning |
|---|---|
| Green tick on CI | Tests passed; the new version is built and waiting for Release. |
| Red cross on CI | A test or style check failed. Nothing was built; the office stays as it was. Tell the developer. |
| Red cross on Security | A library needs updating or something looks like a password. Not urgent for the site, but tell the developer this week. |
| Yellow dot | Still running. Wait. |

## Next

- Try a change before it goes live: [The staging copy](staging.md)
- Put it live: [Release a new version](update.md)

_Last checked: 2026-11-11_
