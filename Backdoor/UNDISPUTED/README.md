https://backdoor.sdslabs.co/challenges/UNDISPUTED

Ok, first let's download the file and see what we've got.

```
$ wget http://hack.bckdr.in/UNDISPUTED/file.ext4
$ file file.ext4
file.ext4: Linux rev 1.0 ext4 filesystem data, UUID=088c23fa-b15c-4439-b709-990571544124 (extents) (huge files)
```

Looks like an [ext4 filesystem](https://en.wikipedia.org/wiki/Ext4). Let's mount it.

```
$ mkdir file && sudo mount file.ext4 file
$ ls file
lost+found  n00b.7z
```

So we have a zipfile, let's check it out.

```
$ 7zr x n00b.7z
7-Zip (A) [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,4 CPUs)
Processing archive: n00b.7z
Extracting  n00b/n00b.txt
Extracting  n00b
Everything is Ok
Folders: 1
Files: 1
Size:       28
Compressed: 194
$ ls n00b
n00b.txt
$ cat n00b/n00b.txt
flag: like_a_walk_in_a_park
$ echo -n like_a_walk_in_a_park | sha256sum
bc2e81c4c8abd0fe06d54bf0768036ecaea12892efdd6cd567235c84a16c8c07
```

Bingo.
