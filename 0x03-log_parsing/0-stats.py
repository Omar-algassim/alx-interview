#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import re

# Improved pattern to match the log line
pattern = r'\d+\.\d+\.\d+\.\d+ - \[\d+-\d+-\d+ \d+:\d+:\d+\.\d+\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'

count = 0
file_size = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_metrics():
    """Prints the computed metrics"""
    print(f"File size: {file_size}")
    for k in sorted(codes.keys()):
        if codes[k] > 0:
            print(f"{k}: {codes[k]}")

try:
    for line in sys.stdin:
        match = re.search(pattern, line)
        if match:
            status_code = int(match.group(1))
            size = int(match.group(2))
            if status_code in codes:
                codes[status_code] += 1
            file_size += size
            count += 1
            
            if count == 10:
                print_metrics()
                count = 0
except KeyboardInterrupt:
    pass
finally:
    print_metrics()
