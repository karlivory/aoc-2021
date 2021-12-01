#!/usr/bin/env python3

import sys

def solve_part1(m):
    res = 0
    for i in range(1, len(m)):
        if(m[i] > m[i - 1]):
            res += 1
    return res

def solve_part2(m):
    res = 0
    last_sliding_scale = m[0] + m[1] + m[2]
    for i in range(1, len(m) - 2):
        sl = m[i] + m[i + 1] + m[i + 2]

        if(sl > last_sliding_scale):
            res += 1

        last_sliding_scale = sl
    return res

def solve_file(file_path):
    print("Input file: %s" % file_path)
    with open(file_path, 'r') as file:
        lines = map(
            lambda x: x.strip(),
            [line for line in file.readlines()])
        measurements = list(map(int, lines))
        answer1 = solve_part1(measurements)
        answer2 = solve_part2(measurements)
        print("Part 1: %d" % answer1)
        print("Part 2: %d" % answer2)

if __name__ == "__main__":
    for file_path in sys.argv[1:]:
        solve_file(file_path)
