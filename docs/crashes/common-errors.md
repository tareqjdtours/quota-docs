# Common errors: PDF, e-mail, pictures, search

**When to use this:** Quota works, but one thing fails.
**Time it takes:** 10 minutes
**You need:** The Terminal on the office Mac for some fixes ([connect](../connect.md) if you are not at it).

Find what you see in the first column. If a fix says "restart the backend", type this in the Quota folder:

```bash
cd ~/quota
docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env restart backend
```

| You see | What it means | Do this |
|---|---|---|
| `503 pdf_unavailable` when opening a PDF | The PDF maker inside the backend failed | Restart the backend. If it comes back, tell the developer: the version needs fixing, then [go back](../deploy/rollback.md). |
| `503 mail_unavailable` when sending an offer | The e-mail settings are wrong or the mail server is down | Tell the developer. Staff can still send offers from their own mailbox in Compose. |
| `503 media_unavailable` on a picture upload | The pictures folder cannot be reached | Restart the backend. If it repeats, tell the developer (the `MEDIA_ROOT` setting). |
| Offers show no pictures | Same as above | Same as above. |
| Mailbox search finds words but not meanings | The search helper (Ollama) is not running | [The office Mac](../maintenance/office-mac.md), step 4. |
| Staff get no new-mail pop-ups | Their browser does not allow notifications | In the browser: the padlock left of the address → **Notifications** → **Allow**. |
| A password-reset or reminder e-mail from Quota never arrives | Quota's own e-mails still go to a test mail catcher on the Mac | Known: a real sending mailbox is still to be set up. An administrator resets the password instead (next line). |
| "locked" at sign-in | Five wrong passwords in fifteen minutes | Wait fifteen minutes, or an administrator sets a new password in **Administration → Users**. |

## If it is still wrong

Copy the last 50 lines of the backend's messages and send them to the developer:

```bash
docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env logs --tail=50 backend
```

_Last checked: 2026-11-11_
