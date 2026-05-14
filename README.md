# CyberShell EDU

CyberShell EDU is an open-source educational cybersecurity shell written in Python.

The goal of this project is to help students learn authorized network diagnostics in a safe lab environment.

## Features

- ping: test connectivity
- nmap-basic: run a basic Nmap service scan
- whois: get domain or IP information
- dig: perform DNS lookup
- traceroute: show network path
- curl-headers: show HTTP headers
- nc-connect: test TCP connection using Netcat

## Safety Notice

This project is for educational and defensive use only.

Only test systems you own or have explicit permission to test.

## How to Run

Run this command:

python3 -m cybershell.main

## Example Commands

help
ping 127.0.0.1
nmap-basic 127.0.0.1
dig example.com
curl-headers https://example.com
exit

## Required System Tools

On Ubuntu/Debian:

sudo apt install nmap netcat-openbsd whois dnsutils traceroute curl

On Fedora:

sudo dnf install nmap nmap-ncat whois bind-utils traceroute curl

## License

MIT License
