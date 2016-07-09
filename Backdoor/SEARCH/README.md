https://backdoor.sdslabs.co/challenges/SEARCH


```
$ wget http://hack.bckdr.in/SEARCH/search.zip
$ file search.zip
search.zip: Zip archive data, at least v2.0 to extract
```

K...

```
$ unzip search.zip
Archive:  search.zip
  inflating: search.txt
$ strings search.txt
JFIF
$3br
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
*huY
okuq
~ |G
y|A.
Z\k7Z^
}F;i
4;{[
iV3\
x~-#
ouuo
x~-#
qkkq
4;{[
]*huX-
>    |h
|Uww
]*huX-
[Awi}
lu]:
iV3\
-tk{
>*xWM
[j7qM
~ |G
nR+I
j7ZT0
Owwc
qkkq
qkkq
TxsM
okuq
Oiic
~4|@
~ |8
u}_\
t]wW
~ _i
l~+|
/<Ay
wZri
*huY
~5|G
TxsR
~4|@
y|A.
wZri
-mn4;]9
okuq
m-<+c
]*huX-
#_`~
>4|m
m-<+c
~0|4
_xWR
~ |8
-mn4;
m-<+c
~0|4
_xWR
~ |8
/<Ay
\x/F
|{wk
>+xs
/<Ay
okuq
quko
]iSC
x~-#
ouuo
okuq
m-<+c
Z\k7Z^
*xWM
~ |G
nR+I
]_`~
k?g_
muXf
x~-#
ouuo
mV{i
uMsY
-mn4;
8?m_
|Uiw
ouuo
}F;i
~4|@
okuq
~+|T
iV3\
~0|K
_xWR
okuq
_iZu
x~-#
ouuo
*huY
~5|G
okuq
mV{i
]*huX-
ouuo
ouuo
+H~@
[Awi}
Ww~*
/-5M
-tk{
*huY
>4|m
u]+N
k?g_
~5|G
>+xs
okuq
x~-#
qkkq
```

Hmm, nada.

```
$ file search.txt
search.txt: JPEG image data, JFIF standard 1.01
```

Tricky, tricky...

```
$ mirage search.txt
# QR code -> https://dhavalkapil.com/assets/files/flag.txt
```
