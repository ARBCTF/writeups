# Write-up on Backdoor's ISOLVE Challenge

## URL

https://backdoor.sdslabs.co/challenges/ISOLVE

## Introduction

The server gives you a regular expression to which you are expected to provide a string that will match it. You have approximately 10 seconds to provide an answer before the server times out and disconnects. Regexes are given in a random order each time, so you won't be able to just replay previous answers.

## Screen-scraping the regexes

The first step was to grab all of the regexes from the server, in the hopes that there were only a finite number of regexes in the server's list. The included python3 script `1-scraper.py` does this by continously connecting to the server, parsing out the regex given, and then disconnecting. We ran the script for a while until the number of unique regexes stopped increasing, at which point we were fairly certain we had all of them. In this case, there were 48 regexes, which you can see in the included `regexes.txt` file.

## Manually solving the regexes

The next step was to find strings which matched the given regexes. As there were only 48 regexes, the fastest method here was to just manually create matching strings. The included python3 script `2-solve_regexes.py` script does this by asking the user for solutions and then checking them using the `re` module.

Note that two of the regexes needed to be altered slightly, specifically `\.?["boys"]{4}\.?` and `[^lol\s=]+["young"]{2}` because python's `re` module doesn't honor double-quoted strings in character sets. To fix this, the script replaces the double-quotes and brackets with parentheses (which should be equivalent) before asking the user for a matching string.

Once matching strings for all the regexes are given, the answers are written to the `solutions.json` file.

## Automatically submitting answers

The final step was to submit the given solutions to the server. The included python3 script `3-solver.py` does this using the [pexpect](https://pexpect.readthedocs.io/en/stable/) module and the `solutions.json` file from the previous step. It scrapes the regex from the server response and submits the appropriate solution from the `solutions.json` file. The flag is returned as part of the 'last lines from the server' log entry.

