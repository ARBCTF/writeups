This one took me a while. Initially I spent quite a bit of time playing
around with the various APIs and seeing if that lead to anything. It did not.

After reading the hint I decided to take a different approach:

```
It's hard for celebrities to pick a security question from a hard-coded list where the answer is not publicly exposed. Click for more hints.
```

This seems like more of an OSINT type problem, not a technical one. It's time
to do a bit of research on this Jim fella'.

Where can we find more information about Jim in the Juice Shop? After clicking
around a bit and becoming more familiar with the system I noticed Jim left some
reviews of various products.

Let's iterate through the reviews and see if we can dig up anything on Jim:

```
$ for i in $(seq 1 30); do curl -s http://localhost:3000/rest/product/$i/reviews | python -mjson.tool; done
...
{
    "data": [
        {
            "_id": "HCQzF4Lju6N56dfbo",
            "author": "jim@juice-sh.op",
            "message": "Fresh out of a replicator.",
            "product": 17,
            "text": "Fresh out of a replicator."
        }
    ],
    "status": "success"
}
...
{
    "data": [
        {
            "_id": "97MjYDqEp24KvBPHi",
            "author": "jim@juice-sh.op",
            "message": "A vital ingredient for a succesful playthrough.",
            "product": 22,
            "text": "A vital ingredient for a succesful playthrough."
        }
    ],
    "status": "success"
}
...
```

Hmm, "replicator" may be a good term we can search on. Searching Google for
"jim replicator" turns up an esoteric Google Books Result for "The Guest on
the Belovo." After reading through the relevant sections it seems like this is
a dead-end.

If we just search Google for "replicator" the second result is a Star Trek
reference. Interesting. This probably would've immediately stood out to a
"Treky", but that I am not.

From here searching "jim star trek" turns up "James T. Kirk", AHA!
James -> Jim. Clicking the Wikipedia entry gives a list of family members.

If we look at the Security Question, it asks:

```
Your eldest siblings middle name?
```

Wikipedia lists George Samuel Kirk as a sibling. Entering "Samuel" and changing
the password solves the problem!
