# Packet Capture 101 (Wireshark)

A self-guided exercise for practicing packet analysis fundamentals. Run this on your own machine/lab network only.

## Goal

Capture and identify traffic for a handful of common protocols, then answer what's actually happening in the capture.

## Steps

1. Install [Wireshark](https://www.wireshark.org/).
2. Start a capture on your active interface (Wi-Fi or Ethernet).
3. In a browser, visit a plain HTTP site (not HTTPS) and a DNS lookup will happen automatically. Also run:
   ```
   ping 8.8.8.8
   nslookup example.com
   ```
4. Stop the capture after ~30 seconds.
5. Apply these display filters one at a time and note what you see:
   - `dns` — DNS query/response pairs, question name, resolved IP
   - `icmp` — ping echo request/reply, TTL values
   - `http` — plaintext HTTP request/response (method, host, status code)
   - `tcp.flags.syn==1 && tcp.flags.ack==0` — TCP SYN packets (start of a handshake)

## What to record (fill in after you run it)

| Protocol | Source → Destination | Key fields observed | Notes |
|---|---|---|---|
| DNS | | | |
| ICMP | | | |
| HTTP | | | |
| TCP handshake | | | |

## Stretch goal

Capture traffic while doing an SSH login to a lab VM. Confirm you **cannot** read the password in plaintext (TCP payload is encrypted) — contrast this with the HTTP capture where credentials in a form post *would* be visible. This is a good way to internalize why HTTPS/SSH matter.
