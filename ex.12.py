"""
Exercise 12: Given an IP address, check if the IP address is valid or not.
 Use regular expressions.
 Formats accepted:
 0.0.0.0:80
 0.0.0.0:135
 0.0.0.0:3389
 0.0.0.0:49664
 127.0.0.1:53
 127.0.0.1:6942
 127.0.0.1:27017
 192.168.1.101:139
 192.168.1.101:49601
 [::]:80
 [::]:135
 [::]:7680
 [::]:49664
 [::1]:53
 [::1]:60744
 [2401:4900:32f2:4d55:f8a8:d790:9370:86da]:49772
"""

import re

def is_valid_ip(ip_):

    if not isinstance(ip_, str):
        print("Not a valid ip string!")
        return False

    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:\d{1,5})?$'
    ipv6_pattern = r'^(\[([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\]|\[([0-9a-fA-F]{1,4}:){1,7}:])(\:\d{1,5})?$'
    patterns = [ipv4_pattern, ipv6_pattern]

    for pattern in patterns:
        if re.match(pattern, ip_):
            return True
    return False

test_ips = [None,1,
    "0.0.0.0:80", "0.0.0.0:135", "0.0.0.0:3389", "0.0.0.0:49664", "127.0.0.1:53",
    "127.0.0.1:6942", "127.0.0.1:27017", "192.168.1.101:139", "192.168.1.101:49601",
    "[::]:80", "[::]:135", "[::]:7680", "[::]:49664", "[::1]:53", "[::1]:60744",
    "[2401:4900:32f2:4d55:f8a8:d790:9370:86da]:49772"
]

for ip in test_ips:
    print(f"{ip}: {'Valid' if is_valid_ip(ip) else 'Invalid'}")
