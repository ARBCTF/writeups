#!/usr/bin/env python3
# 3-solver.py - Automated solver for ISOLVE server.
#
# Use this script to use the solutions provided in the solutions.json file to
# the ISOLVE server. Note that this script requires the pexpect module.
#
# Once complete, the flag should be given in the last lines from the server.
# You can also check the pexpect.log file to see all input/output.

import json
import logging
import pexpect
import sys


solutions = json.load(open('solutions.json', 'r'))

logging.basicConfig(level=logging.INFO)

child = pexpect.spawn("nc hack.bckdr.in 7070")
fout = open("pexpect.log", 'wb')
child.logfile = fout
while True:
    logging.info("Waiting for regex...")
    index = child.expect([
        pexpect.EOF,
        "Your regex:\r\n([^\r\n]+)\r\n"])
    if index == 0:
        logging.info("Server has closed connection. Exiting loop.")
        break

    if child.match is None:
        logging.error("Did not receive regex")
        sys.exit(1)

    regex = child.match.group(1).decode('utf-8')
    logging.info("Got regex %s", regex)

    if solutions.get(regex, None) is None:
        logging.error("No solution found for regex %s", regex)
        sys.exit(1)

    logging.info("Sending solution %s", solutions[regex])
    child.sendline(solutions[regex])

    logging.info("Awaiting confirmation...")
    index = child.expect([
        "Failed regex",
        "Passed regex! Way to go.\r\n"])
    if index == 0:
        logging.error("Solution did not match regex.")
    else:
        logging.info("Confirmation received.")

logging.info("Last lines from server:")
logging.info(child.before)
