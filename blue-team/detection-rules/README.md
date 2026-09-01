# Detection Rules

[Sigma](https://sigmahq.io/) rules — a generic, SIEM-agnostic format for detection logic. Each rule here maps to a detection idea also implemented as a script under [`../log-analysis-101/`](../log-analysis-101/), so you can see the same logic expressed both ways: as ad-hoc analysis and as a rule you'd deploy in a real SIEM (Splunk, Elastic, Wazuh, etc. can all consume or translate Sigma rules).

| Rule | Detects | MITRE ATT&CK |
|---|---|---|
| [`ssh_bruteforce.yml`](ssh_bruteforce.yml) | 5+ failed SSH logins from one source IP in 5 minutes | [T1110 - Brute Force](https://attack.mitre.org/techniques/T1110/) |
