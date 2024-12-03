import sys
import os
from collections import Counter
from collections import deque
from itertools import permutations
import re

def window(seq, n=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win


if __name__ == "__main__":
    print("aoc 3")
    filename = sys.argv[1]
    reports = []
    all = 0
    with open(filename,"r") as inputfile:
        for line in inputfile:
            pattern = r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)"
            matches = re.findall(pattern,line.strip())
            multiply = lambda x: int(x[1])*int(x[2])
            res = map(multiply, matches)
            res = sum(res)
            all += res
    


    print(f"Part 1: {all}")
