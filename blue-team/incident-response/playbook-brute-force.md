# IR Playbook: Suspected SSH Brute Force

**Trigger:** [`ssh_bruteforce.yml`](../detection-rules/ssh_bruteforce.yml) fires, or `analyze_auth_log.py` flags an IP over threshold.

## 1. Triage

- [ ] Identify the source IP and affected host(s).
- [ ] Check attempted usernames — generic (`admin`, `root`, `test`) suggests automated/opportunistic scanning; specific valid usernames suggest targeted reconnaissance.
- [ ] Check whether any attempt from that IP **succeeded** (correlate failed attempts with an `Accepted` line for the same IP shortly after).

## 2. Scope

- [ ] Search for the same source IP across other hosts in the environment — is this isolated or part of a wider sweep?
- [ ] Check if the source IP has any prior history (internal threat intel notes, previous alerts).
- [ ] If a login succeeded: what did that account do afterward? (auth log + shell history + any EDR/process logs available)

## 3. Contain

- [ ] If no successful login: block the source IP at the firewall (temporary rule), and note when it was applied.
- [ ] If a login succeeded: disable/reset the compromised account's credentials immediately, and treat as a confirmed incident (escalate — this is no longer just "suspected").

## 4. Eradicate & Recover

- [ ] Confirm no persistence was established (new SSH keys added to `~/.ssh/authorized_keys`, new cron jobs, new user accounts).
- [ ] Rotate credentials for the affected account and any accounts that share the password.
- [ ] Remove the temporary firewall block once confirmed safe, or make it permanent if the IP is confirmed malicious.

## 5. Lessons Learned

- [ ] Was SSH exposed to the internet unnecessarily? Consider restricting to VPN/jump host.
- [ ] Was key-based auth enforced, or was password auth still allowed?
- [ ] Update the detection threshold/rule if this incident revealed a gap (e.g., attacker stayed under the alert threshold).

---
*Template based on standard IR lifecycle (Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned, per NIST SP 800-61). Adapt as you run this against real home-lab scenarios.*
