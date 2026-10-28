# Connect to the server (SSH)

**When to use this:** Any page that says "open a terminal on the server".
**Time it takes:** 5 minutes (first time: 15)
**You need:** The server address and your username from the person who manages access, and to be on the office network (or VPN).

SSH lets you type commands on the server from your own computer, securely.

!!! warning "The address and username are not on this site"
    This site is public. Ask the developer, or look in the team password manager.
    Replace `<username>`, `<server-address>` and `<quota-folder>` below.

## Steps: the first time

1. Open a terminal (**Mac**: Terminal. **Windows**: PowerShell). SSH is already installed.
2. Create your own key (skip if you have one). Choose a passphrase and remember it.

   ```bash
   ssh-keygen -t ed25519 -C "your-name-laptop"
   ```

3. Show your **public** key and send the whole line to the person managing the server:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

   !!! danger "Never share the private key"
       The file **without** `.pub` stays on your computer. Never send it or paste it anywhere.

4. After they add it, connect:

   ```bash
   ssh <username>@<server-address>
   ```

5. The first time it asks `Are you sure you want to continue connecting (yes/no)?` Type `yes`.
6. Go to the Quota folder (the one that contains the `deploy` and `backend` folders):

   ```bash
   cd <quota-folder>
   ls
   ```

   You should see `backend`, `frontend` and `deploy`. **Run every command on this site from this folder.**

## Check it worked

```bash
hostname
docker compose version
```

The first shows the server's name, not your computer's.

## Leaving

```bash
exit
```

## Safety

- Use only your own key. Do not run commands you do not understand.
- Never run `docker compose down -v` or `docker volume prune`.
- If your laptop is lost, tell the server manager at once so your key is removed.

## If something goes wrong

| You see | Do this |
|---|---|
| `Connection timed out` | Not on the office network or VPN, or the server is off. |
| `Connection refused` | Server on, SSH not running, or wrong address. Ask the developer. |
| `Permission denied (publickey)` | Your key was not added, or wrong username. |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | **Stop** and ask the developer. |

_Last checked: YYYY-MM-DD_
