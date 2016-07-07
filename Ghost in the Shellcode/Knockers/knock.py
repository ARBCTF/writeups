#!/usr/bin/python

"""
http://en.wikipedia.org/wiki/Length_extension_attack
"""

import hashlib
import socket
import argparse
from binascii import unhexlify

import hashpumpy

p = argparse.ArgumentParser()
p.add_argument('-k', '--key-length', required=True, type=int)
p.add_argument('-t', '--token', required=True)
p.add_argument('-p', '--open-port', required=True, type=int)
p.add_argument('-H', '--host', default="::1")
p.add_argument('-P', '--host-port', type=int, default=8008)
args = p.parse_args()

# 2 hex digits for each byte
ds = hashlib.sha512().digest_size * 2

given_digest = args.token[:ds]
original_data = unhexlify(args.token[ds:])
append_data = unhexlify(hex(args.open_port)[2:])

digest, payload = hashpumpy.hashpump(given_digest,
                                     original_data,
                                     append_data,
                                     args.key_length)

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.connect((args.host, args.host_port))
s.sendall(unhexlify(digest) + payload)
