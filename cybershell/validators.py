import ipaddress
import re

def is_valid_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def is_valid_domain(value):
    pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$"
    return re.match(pattern, value) is not None

def is_valid_port(value):
    try:
        port = int(value)
        return 1 <= port <= 65535
    except ValueError:
        return False
