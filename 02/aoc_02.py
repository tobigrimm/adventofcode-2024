import sys
import os
from collections import Counter
from collections import deque
from itertools import permutations

def window(seq, n=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

monoton_inc = lambda x: x[0] < x[1]
monoton_dec = lambda x: x[0] > x[1]

safe_steps = lambda x: 1 <= abs(x[0] - x[1]) <= 3

def is_report_unidir(report):
    inc = all(map(monoton_inc, window(report)))
    dec = all(map(monoton_dec, window(report)))

    return inc or dec

def are_diff_tolerable(report):
    return all(map(safe_steps, window(report)))

def is_report_safe(report):
    return is_report_unidir(report) and are_diff_tolerable(report)


def check_reports(reports):
    sum = 0
    for report in reports:
        res = is_report_safe(report)
        if res:
            sum += 1

    return sum


def test_tolerate_reports(reports):
    sum = 0
    # go through all the reports, continue if they are safe, otherwise test permutations of dropping one level
    for report in reports:
        if is_report_safe(report):
            sum += 1
        else:
            for drop_index in range(len(report)):
                drop_report = list(report)
                del drop_report[drop_index]
                res = is_report_safe(drop_report)
                if res:
                    sum += 1
                    break
    return sum


if __name__ == "__main__":
    print("aoc 2")
    filename = sys.argv[1]
    reports = []
    with open(filename,"r") as inputfile:
        for line in inputfile:
            levels = [int(x) for x in line.strip().split(" ")]
            reports.append(levels)

    print(f"Part1: {check_reports(reports)}")
    print(f"Part2: {test_tolerate_reports(reports)}")
