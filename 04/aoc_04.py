import sys
import os
from collections import Counter
from collections import deque
from collections import defaultdict
from itertools import permutations
import re
import numpy as np

def window(seq, n=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

def diagonal_elem(ll, a, b):
    try:
        if a < 0 or b < 0:
            raise IndexError
        return ll[a, b]
    except IndexError:
        return None

def count_words(matrix, wordlist):
    # range of direction for x and y shifts
    dirs = (-1, 0, 1)

    coords = list(matrix.keys())
    word_found = []
    for x,y in coords:
        #check for each coord in all direction (left, right, upwards, diagonals if XMAS can be found
        for x_d in dirs:
            for y_d in dirs:
                for word in wordlist:
                    cur_word = [matrix[(x+x_d*n,y+y_d*n)] for n in range(len(word))]
                    word_found.append(cur_word == list(word))
                        #== list(word)])

    return sum(word_found)

def count_xs(matrix):
    wordlist = list("MAS"),list("SAM")
    coords = list(matrix.keys())
    dirs = (-1, 0, 1)
    xmas = []
    for x,y in coords:
        cur_words_up = [matrix[x+d,y+d] for d in dirs]
        cur_words_down = [matrix[x+d, y-d] for d in dirs] 
        xmas.append(cur_words_up in wordlist and cur_words_down in wordlist)

    return sum(xmas)

if __name__ == "__main__":
    print("aoc 4")
    filename = sys.argv[1]
    nr_part1 = 0
    nr_part2 = 0
    
    # let's use a default dict for the storage/matrix so I don't have to check for out-of-bound reads later -> will just return an empty string, so I can use string comparison
    matrix = defaultdict(str)
    with open(filename,"r") as inputfile:
        matrix = matrix | {(x,y): char for x,row in enumerate(inputfile) for y, char in enumerate(row)}

    wordlist = ["XMAS"]
    nr_part1 = count_words(matrix, wordlist)

    print(f"Part 1: {nr_part1}")

    nr_part2 = count_xs(matrix)
    print(f"Part 2: {nr_part2}")
