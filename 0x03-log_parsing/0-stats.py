#!/usr/bin/python3
"""
This script parses log files and calculates statistics on the status codes
and file sizes.
"""
import sys
from time import sleep


def print_stats(stats_p: dict, file_size_p: int) -> None:
    """
    Prints the statistics calculated.
    Args:
        stats_p: Dictionary containing status code counts.
        file_size_p: Total file size.
    Returns:
        None
    """
    print(f"File size: {file_size_p}")
    for k, v in sorted(stats_p.items()):
        if v:
            print(f"{k}: {v}")


if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        sleep(1)
        print_stats(stats, filesize)
        raise
