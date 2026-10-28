# First install

**When to use this:** Setting up Quota Dashboard on a new machine.
**Time it takes:** 45 minutes
**You need:** A Linux machine with Docker and the compose plugin (about 2 GB of disk), [SSH access](../connect.md), GitHub access to both repositories, and the legacy `images/` folder somewhere on the machine.

## Before you start

- [ ] Decide the web address staff will use.
- [ ] Have these values ready (never write them on this site): a database password, a signing key (long random text), mail (SMTP) settings, and the path to the pictures folder.

## Steps

1. **Get both repositories.** The front end goes inside the backend's folder.

   ```bash
   git clone git@github.com:AbuEnzo/quota-dashboard-backend.git quota
   git clone git@github.com:AbuEnzo/quota-dashboard-frontend.git quota/frontend
   cd quota
   ```

2. **Create the settings file** and fill it in.

   ```bash
   cp deploy/.env.example deploy/.env
   nano deploy/.env
   ```

   Set `PUBLIC_BASE_URL`, `MEDIA_ROOT` (the pictures folder), `POSTGRES_PASSWORD`, `JWT_SECRET` and the `SMTP_*` values. Save with Ctrl+O, Enter, Ctrl+X.

3. **Build and start.**

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env up -d --build
   ```

4. **Create the database tables.**

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env exec backend alembic upgrade head
   ```

5. **Load the catalogue** from the old system (it must be reachable from the server):

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env exec backend python scripts/import_legacy.py
   ```

6. **Create the first administrator.** Choose a strong password in place of `choose-one`.

   ```bash
   docker compose -f deploy/compose.yml --env-file deploy/.env exec -e SEED_ADMIN_PASSWORD='choose-one' backend python scripts/seed_admin.py admin@example.com "Administrator"
   ```

7. **Add https.** Put the office's TLS proxy (Caddy, Traefik, or the existing nginx) in front of the web port, and set `PUBLIC_BASE_URL` to the https address. Then `COOKIE_SECURE=true` applies. Run step 3 again after changing the settings.

## Check it worked

```bash
curl http://localhost/health
curl http://localhost/api/v1/health/db
```

The first answers `{"status":"ok"}`. The second shows the database and its version. Then open the address in a browser and sign in as the administrator.

## If something goes wrong

| You see | Do this |
|---|---|
| `set POSTGRES_PASSWORD in deploy/.env` | The settings file is missing a value. Edit `deploy/.env`. |
| `set MEDIA_ROOT in deploy/.env` | Point it at the pictures folder. |
| Import cannot reach the legacy database | The old database address is wrong or not reachable from the container. Ask the developer. |
| Anything else | [Site is down](../crashes/site-down.md) |

_Last checked: YYYY-MM-DD_
