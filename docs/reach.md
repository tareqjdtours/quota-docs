# How staff and clients reach it

**When to use this:** Staff or clients cannot open Quota from outside, or you want to know how the doors work.
**Time it takes:** 5 minutes to read
**You need:** For changes, the Cloudflare account that holds the domains, and [SSH access](connect.md).

Quota runs on the office Mac. Nobody reaches it through an open router port. Two **Cloudflare tunnels**
run on the Mac and carry the traffic out to Cloudflare, which gives the https address and certificate.

## The two doors

| | Staff | Clients |
|---|---|---|
| Address | `https://quota.selectdmc.com` | `https://trip.jordanselect.com` (JST), `https://trip.jdtours.com` (JDT) |
| Tunnel in Cloudflare | `quota-staff` | `quota-maps` |
| Container on the Mac | `quota-staff-tunnel` | `quota-tunnel` |
| Who gets in | Only people Cloudflare Access lets through: a one-time code sent to a work e-mail address | Anyone with a link |
| What answers | All of Quota, after the Quota sign-in | Only the route map, the online offer and offer pictures. Every other path answers 404. |

Each brand has its own client address so a client never sees the other brand's name. Quota picks the address
from the order's company (`CLIENT_URL_SELECT` and `CLIENT_URL_DIRECT` in `deploy/.env`).

!!! note "The client door serves pictures only"
    The pictures folder also holds old proposal files with client names and prices. The client door answers
    only for picture files (jpg, png, webp and the like) and 404 for anything else in it.

## Check the doors

From a phone on mobile data (not the office Wi-Fi):

- `https://trip.jordanselect.com/health` answers `{"status":"ok"}`.
- `https://trip.jordanselect.com/api/v1/auth/me` answers **404**. That is right: the client door must not reach sign-in.
- `https://quota.selectdmc.com` shows the Cloudflare page asking for an e-mail address, never Quota straight away.

On the Mac:

```bash
docker ps --format '{{.Names}} {{.Status}}' | grep tunnel
```

Both tunnels should say `Up`.

## If something goes wrong

| You see | Do this |
|---|---|
| Both addresses fail, the office address works | A tunnel is down. `docker start quota-staff-tunnel quota-tunnel`. If it stops again, read `docker logs --tail=50 quota-tunnel`. |
| Staff see a plain **403** page from Quota's address | Something else is answering on port 5190 (a test server someone started). Tell the developer; never stop the live boxes. |
| Staff get no code e-mail | Their address is not in the Cloudflare Access policy, or the code went to spam. Check Zero Trust › Access in Cloudflare. |
| A client's map link opens but stays blank | An old copy of the map is stuck in their browser. A hard reload (Shift + reload) clears it. |
| A client link shows the office address | The link was made before the client addresses were set. Copy it again from the order. |

!!! warning "The tunnel tokens"
    Each tunnel has a token in a file next to its start script on the Mac. A token is a password: never put it in
    chat, e-mail or git. To replace one, make a new token in Cloudflare (Zero Trust › Networks › Tunnels) and
    restart the tunnel with it.

_Last checked: 2026-11-11_
