# Backdoor: DTUNE

## URL
https://backdoor.sdslabs.co/challenges/DTUNE
Audio sample: http://hack.bckdr.in/DTUNE/Dtune.wav

## Description
Vector recorded this audio when Gill Bates was opening his/her vault and Gru
stole this recording from him (stealing from a thief ain't a crime, right?).
Help Gru decode this message so that he can ... (Use your imagination)

## Beginning
Immediately upon playing the audio clip, it becomes clear there is some decoding
with regards to the pitches and number of beeps that are played. However, there
are a few limitation. First off, the beeps play too fast for a human to be able
to decode it on the fly. Second of all, it's not immediately clear what type of
decoding needs to be done because it sounds like there is more than two pitches
- making binary not an option.

## Realizations
In the description, it states this is taken from a vault, leading us to think
the beeps come from some type of keypad. After listening to the recording
again, it sounds as though the beeps are reminiscent of an older phone pad.
Trying to think how beeps on a keypad could go to some sort of other
information lead us to think of the T9 keyboard, and the struggles of texting
on one of those.

Popping open https://www.sainsmograf.com/t9-emulator/ it is feasible that
each tone corresponds to a key. Now to figure out how to map each tone to a key.

Doing a Google search of 'keypad dial tones' gives the first result of 'DTMF
Dial Tones'. Clicking on the [link](http://onlinetonegenerator.com/dtmf.html)
and messing around with the buttons definitely solidifies the connection
between the DTMF tones and the recording. After all, the problem is titled
'DTUNE'.

This result doesn't really help us because it is still too difficult to map a
key to a tone in an efficient manner. Yes, at this time many people have
probably thrown the clip into an audio program to slow it down and to be able
to better analyze the tones. This is fine, although still difficult to match a
tone with a button. Lucky for us, there is an online decoder of DTMF tones.
This [site](http://dialabc.com/sound/detect/) allows us to upload the audio
clip and then get a list of the keys output.

After uploading the clip and getting the numbers that correspond to each tone,
we can go back to our T9 emulator and punch in a few. The list of numbers output
from the audio upload site is:
[8, 4, 3, 0, 3, 5, 2, 4, 0, 4, 7, 7, 0, 7, 4, 4, 2, 2, 5, 6, 0, 6, 3, 0, 3, 7,
 2, 3, 4, 9, 4, 6, 2, 2, 7, 9]
Typing the '843' into the emulator yeilds 'the'. Awesome! This seems like a
winner! After a little monkeying around, it can be deduced that the '0' is a
space. Therefore the first bit of numbers turns into 'the flag grr phi2256'.
Woah, that doesn't seem right...

Well, the DTMF decoder isn't 100% accurate, apparently the output and exact
number of tones in the audio isn't perfect. What the decoder did give us is the
mapping of each pitch to each number, just not the correct repetition of that
number. If the audio has been slowed down at this point, it might be worthwhile
to slowly go through it and get the exact number of repetitions associated with
each tone.

After rectifying that mismatch, it might come out to be 'the flag is phi2256'
when typed into the predictive text keyboard. This still is a bit funky.
However, seeing the 256 at the end of that word and knowing how the flags are
usually hidden on this site helps us recognize that T9 doesn't have 'SHA256'
in it's dictionary. This now becomes 'the flag is sha256'. At this point, it
can be realized that the predictive text from the T9 emulator isn't the most
accurate. Instead, going by the number of beeps and looking at the T9 keypad is
more accurate, especially because the actual string that needs to be 'SHA256'ed
will be a jumble of characters.

## Conclusion
The correct number of key repeats is:
84433 33355524 4447777 7777442256 666333 337222344994462222779 (with 0's
substituded for spaces to ease readability) and the four "2's" in the flag
part of the answer is actually broken up into a 'C' and a 'A'. If you listen
closely (there's a small pause between letters).

In the end the text is "The flag is sha256 of PLZ_GO_DO_IT_YOURSELF"
The trickiest part after getting most of the legwork done, was figuring out
the flag itself needed to be capitalized. This alone took a while to figure out
since it was thought the decoding was incorrect still.

Happy Hunting!
