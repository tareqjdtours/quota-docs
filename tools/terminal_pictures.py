"""Draws the Terminal pictures for the runbook: what to type and what comes back.
Every picture is made-up example text (no real names, addresses, keys or accounts).
Run: python3 tools/terminal_pictures.py   (needs Google Chrome)"""
import html, os, subprocess, tempfile

OUT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'img', 'term')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
C = 'docker compose -p quota -f deploy/compose.yml -f deploy/compose.office.yml --env-file deploy/.env'
P = 'office-mac quota %'

# name: list of (kind, text); kind is 'cmd' (typed), 'out' (shown), 'good' / 'bad' (output to notice)
PICS = {
  'cd-quota': [('cmd', 'cd ~/quota'), ('cmd', 'ls'), ('out', 'AGENTS.md   CLAUDE.md   README.md   backend   deploy   docs')],
  'ps': [('cmd', C + ' ps --format "table {{.Service}}\\t{{.Status}}"'),
         ('out', 'SERVICE    STATUS'), ('good', 'backend    Up 4 hours (healthy)'), ('good', 'backup     Up 3 days'),
         ('good', 'db         Up 3 days (healthy)'), ('good', 'frontend   Up 4 hours (healthy)'), ('good', 'mail       Up 3 days (healthy)')],
  'ps-bad': [('cmd', C + ' ps --format "table {{.Service}}\\t{{.Status}}"'),
         ('out', 'SERVICE    STATUS'), ('bad', 'backend    Restarting (1) 8 seconds ago'), ('out', 'backup     Up 3 days'),
         ('out', 'db         Up 3 days (healthy)'), ('out', 'frontend   Up 4 hours (healthy)'), ('out', 'mail       Up 3 days (healthy)')],
  'health': [('cmd', 'curl http://localhost/health'), ('good', '{"status":"ok"}'),
             ('cmd', 'curl http://localhost/api/v1/health/db'), ('good', '{"status":"ok","database":"ok","alembicRevision":"d9e1f3a5b7c9"}')],
  'update-done': [('cmd', 'tail -3 ~/Library/Logs/quota-update.log'),
             ('out', ' Container quota-backend-1 Healthy'), ('out', ' Container quota-frontend-1 Healthy'),
             ('good', '2026-11-11 13:06:37 update[quota]: done: {"status":"ok","database":"ok"}')],
  'update-unauthorized': [('cmd', 'tail -2 ~/Library/Logs/quota-update.log'),
             ('bad', '2026-11-09 10:53:29 update[quota]: could not fetch the images (registry login expired or no internet?): unauthorized'),
             ('bad', '2026-11-09 10:55:30 update[quota]: could not fetch the images (registry login expired or no internet?): unauthorized')],
  'login': [('cmd', 'DOCKER_CONFIG=~/quota/deploy/.docker docker login ghcr.io -u <github-user>'),
            ('out', 'Password: ' + '(paste the token: nothing shows while you paste, that is normal)'), ('good', 'Login Succeeded')],
  'backup-log': [('cmd', C + ' logs --tail=3 backup'),
             ('good', 'backup-1  | backup: wrote /backups/quota_2026-11-11_0200.sql.gz (129M)'),
             ('out', 'backup-1  | backup: wrote /backups/quota_files_2026-11-11_0200.tar.gz (529M)')],
  'offsite-problem': [('cmd', 'tail -2 ~/Library/Logs/quota-offsite.log'),
             ('bad', '2026-11-10 03:15:00 offsite: PROBLEM: no destination set up (BACKUP_SSD_DIR or R2_BUCKET in deploy/.env)'),
             ('bad', '2026-11-11 03:15:02 offsite: PROBLEM: no destination set up (BACKUP_SSD_DIR or R2_BUCKET in deploy/.env)')],
  'backups-list': [('cmd', 'ls deploy/backups | grep sql.gz | tail -3'),
             ('out', 'quota_2026-11-09_0200.sql.gz'), ('out', 'quota_2026-11-10_0200.sql.gz'), ('good', 'quota_2026-11-11_0200.sql.gz')],
  'tunnels': [('cmd', "docker ps --format '{{.Names}}  {{.Status}}' | grep tunnel"),
             ('good', 'quota-staff-tunnel  Up 3 days'), ('good', 'quota-tunnel  Up 6 days')],
  'context': [('cmd', 'docker context ls'),
             ('out', 'NAME            DESCRIPTION'), ('out', 'default         Current DOCKER_HOST based configuration'),
             ('out', 'desktop-linux   Docker Desktop'), ('good', 'orbstack *      OrbStack')],
  'disk': [('cmd', 'df -h /'), ('out', 'Filesystem        Size    Used   Avail Capacity  Mounted on'),
           ('good', '/dev/disk3s1s1   228Gi    12Gi    26Gi    32%    /')],
  'ssh-first': [('cmd', 'ssh <username>@<server-address>', '%'),
             ('out', "The authenticity of host '<server-address>' can't be established."),
             ('out', 'ED25519 key fingerprint is SHA256:(a long code)'),
             ('out', 'Are you sure you want to continue connecting (yes/no/[fingerprint])? yes')],
  'ssh-key': [('cmd', 'ssh-keygen -t ed25519 -C "your-name-laptop"', '%'),
             ('out', 'Enter file in which to save the key (~/.ssh/id_ed25519): (press Enter)'),
             ('out', 'Enter passphrase (empty for no passphrase): (type one, nothing shows)'),
             ('out', 'Your public key has been saved in ~/.ssh/id_ed25519.pub'),
             ('cmd', 'cat ~/.ssh/id_ed25519.pub', '%'),
             ('good', 'ssh-ed25519 AAAAC3Nz...(one long line)... your-name-laptop')],
  'restart': [('cmd', C + ' restart'),
             ('out', '[+] Restarting 5/5'), ('good', ' ✔ Container quota-db-1        Started'), ('good', ' ✔ Container quota-backend-1   Started'),
             ('good', ' ✔ Container quota-frontend-1  Started'), ('out', ' ✔ Container quota-backup-1    Started'), ('out', ' ✔ Container quota-mail-1      Started')],
  'ollama': [('cmd', 'brew services list | grep ollama'), ('good', 'ollama   started   (your user)   ~/Library/LaunchAgents/sh.brew.ollama.plist')],
}

CSS = '''body{margin:0;background:#fff;font:15px/1.5 Menlo,Monaco,monospace}
.w{margin:12px;border-radius:12px;overflow:hidden;box-shadow:0 6px 24px rgba(0,0,0,.18);background:#1e1f24;width:1076px}
.t{background:#33343a;height:34px;display:flex;align-items:center;padding:0 14px;gap:8px}
.d{width:12px;height:12px;border-radius:50%}.r{background:#ff5f57}.y{background:#febc2e}.g{background:#28c840}
.n{color:#bbb;font:13px -apple-system,Helvetica,sans-serif;margin-left:12px}
.b{padding:14px 18px 18px;color:#d6d6d6;white-space:pre-wrap;word-break:break-all}
.p{color:#7fd1ff}.c{color:#fff;font-weight:bold}.ok{color:#8be28b}.bad{color:#ff8c7a}
.tag{font:bold 12px -apple-system,Helvetica,sans-serif;border-radius:6px;padding:1px 7px;margin-left:10px;vertical-align:1px}
.tc{background:#fff3;color:#fff}.tg{background:#2e5e2e;color:#bdf5bd}.tb{background:#6e2a22;color:#ffd0c8}'''

def render(name, lines):
    rows = []
    for item in lines:
        kind, text = item[0], html.escape(item[1])
        if kind == 'cmd':
            prompt = item[2] if len(item) > 2 else P
            rows.append(f'<span class="p">{html.escape(prompt)}</span> <span class="c">{text}</span><span class="tag tc">you type this</span>')
        elif kind == 'good': rows.append(f'<span class="ok">{text}</span>')
        elif kind == 'bad': rows.append(f'<span class="bad">{text}</span>')
        else: rows.append(text)
    body = '\n'.join(rows)
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="w"><div class="t"><span class="d r"></span><span class="d y"></span><span class="d g"></span><span class="n">Terminal (example)</span></div><div class="b">{body}</div></div>'
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(page); src = f.name
    # height: enough for wrapped lines; trimmed afterwards by the window size guess
    chars = sum(max(1, -(-len(item[1]) // 105)) + (1 if item[0] == 'cmd' and len(item[1]) > 80 else 0) for item in lines)
    h = 34 + 32 + 23 * chars + 40
    out = os.path.abspath(os.path.join(OUT, name + '.png'))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=2',
                    f'--window-size=1100,{h}', f'--screenshot={out}', 'file://' + src], capture_output=True)
    os.unlink(src)
    print('drew', name)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for k, v in PICS.items(): render(k, v)
