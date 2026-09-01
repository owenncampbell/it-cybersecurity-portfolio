# Subnetting Cheat Sheet & Practice

## CIDR quick reference (IPv4)

| CIDR | Subnet Mask | Total Addresses | Usable Hosts |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

**Usable hosts formula:** `2^(32 - CIDR) - 2` (subtract network + broadcast addresses)

## Private address ranges (RFC 1918)

| Range | CIDR | Typical use |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Large enterprise networks |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Medium networks |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | Home/small office |

## Method: subnetting a network

Given `192.168.1.0/24`, split into 4 equal subnets:

1. Need 4 subnets → need 2 extra bits (2^2 = 4) → new mask is `/26`.
2. Block size = 256 - 192 (mask value for /26) = 64.
3. Subnets:
   - `192.168.1.0/26`   (hosts: .1–.62, broadcast .63)
   - `192.168.1.64/26`  (hosts: .65–.126, broadcast .127)
   - `192.168.1.128/26` (hosts: .129–.190, broadcast .191)
   - `192.168.1.192/26` (hosts: .193–.254, broadcast .255)

## Practice problems

Try these, then check answers below.

1. How many usable hosts on a `/28`?
2. Split `10.10.0.0/16` into 8 equal subnets — what's the new CIDR and block size?
3. What is the broadcast address for `172.20.5.0/27`?
4. A device has IP `192.168.10.130/26` — what subnet is it on?

<details>
<summary>Answers</summary>

1. `2^(32-28) - 2 = 14` usable hosts.
2. 8 subnets = 2^3 → borrow 3 bits → `/19`. Block size = 256 - 224 = 32 (in the third octet).
3. `/27` = block size 32 → subnets at .0, .32 → `172.20.5.0/27` covers .0–.31, broadcast = `172.20.5.31`.
4. `/26` block size = 64 → subnets at .0, .64, .128, .192 → `.130` falls in `192.168.10.128/26`.

</details>
