# Common errors: PDF, email and pictures

**When to use this:** The site works, but one feature fails.
**Time it takes:** 10 minutes
**You need:** [SSH access](../connect.md), in the Quota folder.

| You see | Meaning | Do this |
|---|---|---|
| `503 pdf_unavailable` when opening a PDF | The backend lacks a library for PDFs | Rebuild without the cache: `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env build --no-cache backend` then `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d`. Test: `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env exec backend python -c "import weasyprint"` |
| `503 mail_unavailable` when sending an offer | The email settings are wrong | Check the `SMTP_*` values in `deploy/.env`, then `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env up -d` |
| `503 media_unavailable` on a picture upload | The pictures folder is missing or not writable | Check `MEDIA_ROOT` in `deploy/.env` points at a real folder the server can write to |
| Offers show no pictures | The pictures folder is empty or wrong | Same check as above |
| Mailbox search finds words but not meanings | The search helper (Ollama) is not running | [The office Mac](../maintenance/office-mac.md) |
| Staff get no new-mail pop-ups | They did not allow notifications in the browser, or `VAPID_*` is empty in `deploy/.env` | Allow notifications for Quota's address in the browser |
| A staff e-mail "sent" from Quota (password reset, reminder) never arrives | System e-mail still goes to the test mail catcher on the Mac, not out | Known; a real sending mailbox is still to be set up. Tell the developer. |
| "locked" at sign-in | Five wrong attempts | Wait 15 minutes, or an administrator resets the password in **Administration → Users** |

## Check it worked

Repeat what failed: open the PDF, send a test offer, upload a picture.

## If it is still wrong

Copy the last 50 lines of `docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env logs --tail=50 backend` and send them to the developer.

_Last checked: 2026-11-11_
