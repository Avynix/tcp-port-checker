# TCP Port Checker

A simple Python utility for checking whether a TCP port is accepting connections on a hostname or IP address.

## Features

* Accepts hostnames, IP addresses, and URLs
* Resolves hostnames to IPv4 addresses
* Tests TCP connectivity
* Configurable port input
* 3-second connection timeout
* Distinguishes between:

  * Open ports
  * Connection refused / closed ports
  * Connection timeouts
  * Other connection errors

## Requirements

* Python 3.x
* No external Python packages are required.

## Usage

Run:

```bash
python tcp_checker.py
```

Then enter a hostname, IP address, or URL and a TCP port.

Example:

```text
Enter hostname or URL: example.com
Enter TCP port (1-65535): 443

Hostname: example.com
IPv4 address: [resolved address]
TCP port 443: Open.
```

## Important limitation

A failed TCP connection does **not** prove that the host is offline.

A connection can fail because the port is closed, a firewall filters the connection, the connection times out, the network is unreachable, or another networking error occurs.

## Authorized Use

Use this tool only on systems and networks that you own or have explicit permission to test.

The author is not responsible for unauthorized use of this software.

## Project

This project was created as a Python networking and cybersecurity learning project.

Documentation: README drafted with AI assistance and reviewed/edited by the author.
