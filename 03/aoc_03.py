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
    all_part1 = 0
    all_part2 = 0
    with open(filename,"r") as inputfile:
        # status of do/don't is across lines! initially accept mul instructions
        cur = ""
        for line in inputfile:
            #pattern = r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)"
            pattern = r"(?P<ins>mul\((?P<x>[0-9]{1,3}),(?P<y>[0-9]{1,3})\)|do\(\)|don\'t\(\))"
            matches = re.findall(pattern,line.strip())
            #check if there is a don't and remove all muls until first do
            new_matches = []
            for match in matches:
                if cur == "don't" and match[0][:4] == "do()":
                    cur = ""
                    continue
                elif cur == "" and match[0][:5] == "don't":
                    cur = "don't"
                    continue
                
                if cur == "":
                    new_matches.append(match)
                
            # check if it's a mul instruction, then multiply x*y
            multiply = lambda x: int(x[1])*int(x[2]) if x[0][:3] == "mul" else 0
            res_part1 = sum(map(multiply, matches))
            res_part2 = sum(map(multiply, new_matches))
            all_part1 += res_part1
            all_part2 += res_part2
    


    print(f"Part 1: {all_part1}")
    print(f"Part 2: {all_part2}")
