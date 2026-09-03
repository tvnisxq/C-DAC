import re


def analyze_server_logs(logs_text):
    # Compile one regular expression with named capture groups
    pattern = re.compile(
        r'(?P<ip>\S+) - - '
        r'\[(?P<time>[^\]]+)\] '
        r'"(?P<method>GET|POST|PUT|DELETE) '
        r'(?P<resource>\S+) '
        r'HTTP/\S+" '
        r'(?P<status>\d+) '
        r'(?P<bytes>\d+)'
    )

    result = []

    # Process the log one line at a time
    for line in logs_text.splitlines():

        # Try to match the complete line
        match = pattern.fullmatch(line)

        # If the line is invalid, print warning and skip it
        if not match:
            print(
                f"Warning: Could not parse line: '{line}'. Skipping."
            )
            continue

        # Extract values using the named groups
        ip = match.group("ip")
        time = match.group("time")
        method = match.group("method")
        resource = match.group("resource")
        status_code = int(match.group("status"))
        bytes_sent = int(match.group("bytes"))

        # Ignore local network requests
        if ip.startswith("192.168.") or ip.startswith("10."):
            continue

        # Add external request to result
        result.append({
            "ip": ip,
            "time": time,
            "method": method,
            "resource": resource,
            "status": status_code,
            "bytes": bytes_sent
        })

    return result

# Testing 

log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

result = analyze_server_logs(log_data)

print(result)