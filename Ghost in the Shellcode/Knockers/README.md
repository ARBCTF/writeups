http://ghostintheshellcode.com/2015-final/

Alright, what do we have here...

```
$ wget -O knockers.dat http://ghostintheshellcode.com/2015-final/knockers-28e0925c5d1a7e50f21a32e5448cf84a4216e46dbedbb2266fd8a6cc6ee889f5
$ file knockers.dat
knockers.dat: XZ compressed data
$ tar xf knockers.dat
$ file knockers.py
knockers.py: Python script, ASCII text executable
```

Now we're getting somewhere.

So let's open it up and see what we've got. Hmm, this looks useful...

```
try:
    from fw import allow
except ImportError:
    def allow(ip,port):
        print 'allowing host ' + ip + ' on port ' + str(port)
```

Ok, so perhaps we're trying to open up some firewall rule? The challenge
said `Dude, here's a knocker token that will let you access my service on port
80. One day I will let you see my cool stuff on port 7175` so that sounds
about right.

```
l = parse_and_verify(g_h, g_key, data)
if l is None:
	print 'bad message'
else:
	for p in l:
		allow(self.client_address[0], p)
```

Searching through the source it looks like here is the only place that the
`allow()` function gets called, so we've got to hit this location in the code.
Looks like we've got to make sure the `l` variable is iterable with data. So
lets check out the `parse_and_verify()` function.

```
ds = h().digest_size
if len(m) < ds:
    return None
mac = m[:ds]
msg = m[ds:]
if h(k+msg).digest() != mac:
    return None
port_list = []
for i in range(0,len(msg),2):
    if i+1 >= len(msg):
        break
    port_list.append(struct.unpack_from('!H', msg, i)[0])
return port_list
```

Ok, so this is where the bulk of our attention will need to be focused. So `m`
is the message and its length can't be `< ds`, which ends up being `64`:

```
In [103]: import hashlib
In [104]: hashlib.sha512().digest_size
Out[104]: 64L
```

...after we notice that `g_h = hashlib.sha512` at the top of the file.
So `m` can't be `< 64`, the first `64` bytes of `m` are the `mac` and the
remainder is the `msg`. If we want to append data to the port list we also
have to pass the message authentication check against the `mac`. So
`h(k+msg).digest()` must `= mac` where `k` is our secret key we've generated
previously. We want to have some longer list of ports that the remote computer
allows than was created when the secret key was initialized. So `msg` needs to
contain some list of integers to be unpacked. But how do we list more ports
than the message authentication code allows? The key line ends up being:

```
if h(k+msg).digest() != mac:
```

Which is a canonical example of a [length extension attack](https://en.wikipedia.org/wiki/Length_extension_attack)
against [Merkle-Damgard](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction) based algorithms.

Googling around for Python based attacks against this weakness leads to plenty
of libraries you can use. I used [this](https://pypi.python.org/pypi/hashpumpy/1.0) one. After getting a single successful
attack off I decided to write a quick attack script. I've included it in the
writeup.as `knock.py`.

And the result...

Client:

```
$ python2.7 knock.py -k 16 -t 'a5b53094ac9ce6b21d3dbe1cd8d5929731fb0bf58a81a8dca0a8338dbdb2b954d006988a850af665be1e7c87f33dceb296020219d0a43c6f830ee8d6e982e8f61f48' -p 7075
```

Server:

```
$ python2.7 knockers.py serve
Client: ::1 len 178
allowing host ::1 on port 8008
allowing host ::1 on port 32768
allowing host ::1 on port 0
allowing host ::1 on port 0
...
allowing host ::1 on port 0
allowing host ::1 on port 0
allowing host ::1 on port 144
allowing host ::1 on port 7075
```

Boom! We've opened up port `8008` and `7075`! You may also be curious why
other ports were opened as well. When performing the length extension attack
the data has to be extended by a full block, so we end up with a full,
additional block of useless data with the useful data at the end (the
additional port we want to open in this case).
