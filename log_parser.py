import re

log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - 👦.?👦 "GET (.?) HTTP/.*" (\d+)')

def parse_log_line(line):
    """Extracts IP, URL, and response code from a log line."""
    match = log_pattern.search(line)
    if match:
        ip, url, status = match.groups()
        return ip, url, status
    return None