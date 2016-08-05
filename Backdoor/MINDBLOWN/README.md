# Backdoor: MINDBLOWN
====

## URL: https://backdoor.sdslabs.co/challenges/MINDBLOWN

## Description
Figure out the correct login information for Chintu's site utilizing the login
logic provided.

## Resources
The starting page that links to the login page is [here](http://hack.bckdr.in:9003/).

The login logic is as follows:
```
var express = require('express');
var app = express();
var port = process.env.PORT || 9898;
var crypto = require('crypto');
var bodyParser = require('body-parser')
var salt = 'somestring';
var iteration = /// some number here;
var keylength = // some number here;

app.post('/login', function (req, res) {
    var username = req.body.username;
    var password = req.body.password;
    if (username !== 'chintu') {
        res.send('Username is wrong');
        return;
    }
    if (crypto.pbkdf2Sync(password, salt, iteration, keylength).toString() === hashOfPassword) {
        if (password === 'complexPasswordWhichContainsManyCharactersWithRandomSuffixeghjrjg') {
            // some logic here and return something
        } else {
            // return flag here
        }
    } else {
        res.send('Password is wrong');
    }
});
```


## Beginnings/Realizations

After studying the logic for a bit you quickly realize that the login name is
"chintu" and the password has to be "complexPasswordWhichContainsManyCharactersWithRandomSuffixeghjrjg".
However, it then becomes apparent that if the password input is the one given
above, then you will always trigger the first nested if statement, and not the
second one, which is the one we want. Knowing a little bit about hashes and
that it is possible to have two different strings map to the same hash, screams
"HASH COLLISION" for this problem. After doing a quick google search of the
`crypto.pbkdf2Sync collision` we find a site that describes the problemn, and
also a python function to display them.

Here's the python program that can be run to detect collisions:
```
#!/usr/bin/env python
# coding=utf-8

import hashlib
import itertools
import re
import string
import sys

TOTAL_LENGTH = 65
PREFIX = sys.argv[1] if len(sys.argv) > 1 else ''

prefix_length = len(PREFIX)
brute_force_length = TOTAL_LENGTH - prefix_length
passwords = itertools.product(string.ascii_lowercase, repeat=brute_force_length)
regex_printable = re.compile('[\x20-\x7E]+$')
base_hasher = hashlib.sha1()
base_hasher.update(PREFIX)

for item in itertools.imap(''.join, passwords):
    hasher = base_hasher.copy()
    hasher.update(item)
    sha1_hash = hasher.digest()
    if regex_printable.match(sha1_hash):
        print u'%s \U0001F4A5 %s'.encode('utf-8') % (PREFIX + item, sha1_hash)
```

After saving the above code to `collision.py` you can run it as follows:
`python collision.py complexPasswordWhichContainsManyCharactersWithRandomSuffixeghjrjg`
It will output the password whose hash also collides with the above password.
Submitting this output as our password with "chintu" as the user will give us
the flag!

Happy hacking!
