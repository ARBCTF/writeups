# Write-up on Backdoor's JIGSAW Challenge

## URL

https://backdoor.sdslabs.co/challenges/JIGSAW

## Introduction

Jigsaw starts out with a tarball `jigsaw.tar.gz` containing 64 'puzzle pieces' which are 100x100-pixel png files. There is an additional clue in the puzzle description:

> Hint: The pattern on letter seems suspicious


## Assembling the pieces

There was no real 'trick' here; we just worked on assembling the pieces manually through trial-and-error. After some initial effort, a few things became clear:

- The pieces assembled into 2x2 squares to form pictures of letters.
- The background of the pieces was not consistent; that is, the 2x2 squares could consist of both white-on-black pieces and black-on-white pieces (hence the hint).
- Telling whether or not the pieces fit together was tricky; sometimes there was only a few pixels difference in alignment.

Once all of the pieces were assembled, we had pictures of the following 16 letters:

```
B D E E E G I L L N O P U V Z Z
```

(Included in this directory is `assemble.py` which is a python3 script that uses [Pillow](https://python-pillow.org/) to assemble the pieces into 16 pictures. Just place it in the same directory as `jigsaw.tar.gz` and let 'er rip. The new pictures will be placed in an output directory called `tiles`.)


## Decoding the message

The most straightforward thing to try next is rearranging the letters to form a message. For this, I used the [Internet Anagram Server](http://wordsmith.org/anagram/). Unfortunately, with so many letters IAS will generate a lot of results, so I started looking through the results for long words. One that stuck out was `PUZZLE`. I refined the search using the [Advanced Anagramming](http://wordsmith.org/anagram/advanced.html) panel to search for anagrams with the word 'PUZZLE'. I also set the minimum word size to 4 to try and cull the list further.

This gave 30 results, one of which was

> PUZZLE BEING LOVED

This result stuck out to me, because it could be rearranged to form a seemingly-relevant sentence:

> LOVE BEING PUZZLED

Which, as is turns out, is the secret key:

```
SHA256{LOVEBEINGPUZZLED}
```


## Epilogue: Overthinking Things

I admittedly spent way too much time overthinking the solution to this puzzle, mostly due to misreading what the hint meant. It led me to believe that the background pattern on each of the tiles was an attempt to encode a message in binary (black = 0, white = 1, 4 bits per tile). This would mean that the tiles would need to be put in a specific order to decode the message.

If this is the case, however, simply rearranging the letters to spell out a message wasn't enough because some letters (such as 'E') were repeated, and there was no way to determine which 'E' went where.

After an hour or so of struggling with this idea, I noted the point value of the problem and adjusted my expectations accordingly :-P
