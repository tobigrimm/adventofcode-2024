import sys
import os
from collections import Counter


def list_diff(list1, list2):
    sum = 0
    for l1, l2 in zip(list1,list2):
        diff = abs(l1-l2)
        print(diff)
        sum += diff
    return sum

def similarity_score(list1, list2):
    # get the counter for list2:
    c = Counter(list2)
    
    result = 0

    for i in list1:
        result += i*c[i]

    return result
if __name__ == "__main__":
    print("aoc 1")
    filename = sys.argv[1]
    list1 = []
    list2 =  []
    with open(filename,"r") as inputfile:
        for line in inputfile:
            l1 = line.strip().split(" ")
            list1.append(int(l1[0]))
            list2.append(int(l1[-1]))


    print(list_diff(sorted(list1), sorted(list2)))
    print(similarity_score(list1, list2))
