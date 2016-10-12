#!/usr/bin/env python3
# 2-solve_regexes.py - Manual regex solver.
#
# Use this script to manually solve the regexes listed in regexes.txt. This
# script will check the solutions to make sure they match the regex. Once
# solutions for all regexes have been given, they will be written to the
# solutions.json file in JSON format.

import json
import re

regexes = open('regexes.txt','r')

def get_solution(regex):
    solved = False
    while not solved:
        # Hack because python re doesn't honor double quoted strings inside character sets.
        regex = re.sub(r'\["(\w+)"\]', r'(\1)', regex)
        print("Regex: {0}".format(regex))
        solution = input("Solution: ")
        if re.fullmatch(regex, solution) is None:
            print("Invalid solution.")
        else:
            print("Valid solution.")
            solved = True

    return solution

solutions = {}
for regex in regexes:
    regex = regex.rstrip("\n")
    solution = get_solution(regex)
    solutions[regex] = solution

f = open("solutions.json", 'w')
f.write(json.dumps(solutions, indent=4))
