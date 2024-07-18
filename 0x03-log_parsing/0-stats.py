#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import signal
import sys
import re
import asyncio
try:
    pattern = '\d*\.\d*\.\d*\.\d* - \[\d*-\d*-\d* \d*:\d*:\d*\.\d*\] "GET \/projects\/260 HTTP\/1.1" \d* \d*'
    count = 0
    file_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    code_print = lambda : print(f"{k}: {v}")
    for line in sys.stdin:
        if re.match(pattern,
            line):
            size = re.search('..\d$', line)
            status_code = re.search(' \d* ', line)
            status_code = int(status_code.group(0))
            codes[status_code] += 1
            file_size += int(size.group(0))
            if count == 9 or count == 0:
                count = 0
                print(f"File size: {file_size}")
                for k, v in codes.items():
                    print(f"{k}: {v}")
        count += 1
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in codes.items():
        print(f"{k}: {v}")
