#!/usr/bin/env python3
# 1-scraper.py - Screen-scraper for ISOLVE server.
#
# Run this script with no arguments: it will connect to the server, grab the
# regex offered, then disconnect. It will repeat this process looking for unique
# regexes until you Ctrl-C the script, at which point it will write the regexes
# seen to regexes.txt.

import subprocess

def scrape_result(result):
    lines = result.stdout.decode('utf-8').split("\n")
    save = False
    for line in lines:
        if save == True:
            return line
        if line == "Your regex:":
            save = True
            continue

regexes = {}
try:
    while True:
        result = subprocess.run(
            "/bin/echo '' | nc hack.bckdr.in 7070",
            stdout=subprocess.PIPE,
            shell=True)
        regexes[scrape_result(result)] = 1
        print("Saw {0} unique regexes".format(len(regexes.keys())))
except KeyboardInterrupt:
    print("\n".join(regexes.keys()))
    f = open("regexes.txt", 'w')
    f.write("\n".join(regexes.keys()))
