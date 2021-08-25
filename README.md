# Ready-to-Graduate
Honeypot - IT Project II


Created by Ready to Graduate.
UNSW Canberra
This software is designed for educational use only. 

To use async_tcp_scan:

usage: async_tcp_scan.py [-h] -p PORTS [--open] ADDRESSES

Simple asynchronous TCP Connect port scanner

positional arguments:
  ADDRESSES             A comma-separated sequence of IP addresses and/or domain names to scan, e.g., '45.33.32.156,65.61.137.117,testphp.vulnweb.com'.

optional arguments:
  -h, --help            show this help message and exit
  -p PORTS, --ports PORTS
                        A comma-separated sequence of port numbers and/or port ranges to scan on each target specified, e.g., '20-25,53,80,443'.
  --open                Only show open ports in the scan results.

Usage examples:
1. python async_tcp_scan.py google.com -p 80,443
2. python async_tcp_scan.py 45.33.32.156,demo.testfire.net,18.192.172.30 -p 20-25,53,80,111,135,139,443,3306,5900
