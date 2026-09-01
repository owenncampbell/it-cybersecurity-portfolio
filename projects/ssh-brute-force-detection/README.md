# SSH Brute-Force Detection

A small end-to-end detection project: a Python script that parses an `auth.log`-style file and flags source IPs with excessive failed SSH login attempts, a [Sigma rule](ssh_bruteforce.yml) expressing the same logic for a real SIEM, and an [incident response playbook](playbook-brute-force.md) for what to do when it fires.

`sample_auth.log` is **synthetic data** (IPs are from the RFC 5737 documentation ranges, `203.0.113.0/24` and `198.51.100.0/24` — not real hosts) so it's safe to commit and run as-is.

## Run it

```bash
python3 analyze_auth_log.py sample_auth.log --threshold 5
```

## Output

```
=== Failed login attempts by source IP ===
203.0.113.45: 9 attempts, usernames tried: ['admin', 'root', 'test'] <-- possible brute force
198.51.100.9: 3 attempts, usernames tried: ['oracle', 'postgres']

=== Successful logins ===
192.168.1.50: owen
192.168.1.51: deploy

[!] 1 IP(s) exceeded threshold (5 failures): ['203.0.113.45']
```

## What this demonstrates

- Parsing unstructured log text with regex
- Aggregating events by source (IP) to spot a pattern a single line wouldn't show
- A tunable detection threshold (real SOC tooling exposes this as a config value, not a hardcoded number)
- Exit code reflects detection result (`1` if suspects found) so it could be wired into a cron job or CI-style check

## The Sigma rule

[`ssh_bruteforce.yml`](ssh_bruteforce.yml) expresses the same detection logic in [Sigma](https://sigmahq.io/) — a generic, SIEM-agnostic rule format (Splunk, Elastic, Wazuh, etc. can all consume or translate it). It maps to [MITRE ATT&CK T1110 - Brute Force](https://attack.mitre.org/techniques/T1110/).

## The playbook

[`playbook-brute-force.md`](playbook-brute-force.md) is the incident response playbook for when this detection fires — triage, scope, contain, eradicate/recover, lessons learned (NIST SP 800-61 lifecycle).

## Next steps (ideas to extend this)

- Correlate failed attempts *followed by* a success from the same IP (a brute force that succeeded)
- Add a sliding time window instead of counting the whole file (e.g. "5 failures in 60 seconds")
- Feed real logs from the [home lab](https://github.com/owenncampbell/cybersecurity-home-lab) once it's built
