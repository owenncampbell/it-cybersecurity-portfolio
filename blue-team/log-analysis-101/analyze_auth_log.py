#!/usr/bin/env python3
"""Detect potential SSH brute-force activity in an auth.log-style file.

Usage:
    python3 analyze_auth_log.py sample_auth.log
    python3 analyze_auth_log.py sample_auth.log --threshold 5
"""

import argparse
import re
import sys
from collections import defaultdict

FAILED_RE = re.compile(
    r"^(?P<month>\w+\s+\d+)\s+(?P<time>\d+:\d+:\d+).*"
    r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)
ACCEPTED_RE = re.compile(
    r"^(?P<month>\w+\s+\d+)\s+(?P<time>\d+:\d+:\d+).*"
    r"Accepted (password|publickey) for (?P<user>\S+) from (?P<ip>\S+)"
)


def analyze(path: str, threshold: int):
    failures_by_ip = defaultdict(list)
    accepted = []

    with open(path) as f:
        for line in f:
            m = FAILED_RE.search(line)
            if m:
                failures_by_ip[m.group("ip")].append(m.group("user"))
                continue
            m = ACCEPTED_RE.search(line)
            if m:
                accepted.append((m.group("ip"), m.group("user")))

    print(f"Analyzed: {path}\n")
    print("=== Failed login attempts by source IP ===")
    for ip, users in sorted(failures_by_ip.items(), key=lambda kv: -len(kv[1])):
        flag = " <-- possible brute force" if len(users) >= threshold else ""
        print(f"{ip}: {len(users)} attempts, usernames tried: {sorted(set(users))}{flag}")

    print("\n=== Successful logins ===")
    for ip, user in accepted:
        print(f"{ip}: {user}")

    suspects = [ip for ip, users in failures_by_ip.items() if len(users) >= threshold]
    if suspects:
        print(f"\n[!] {len(suspects)} IP(s) exceeded threshold ({threshold} failures): {suspects}")
        return 1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile", help="path to auth.log-style file")
    parser.add_argument("--threshold", type=int, default=5, help="failed attempts to flag as brute force (default: 5)")
    args = parser.parse_args()
    sys.exit(analyze(args.logfile, args.threshold))
