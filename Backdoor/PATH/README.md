https://backdoor.sdslabs.co/challenges/PATH

Hmmm, "The flag is somewhere on the domain flag.bckdr.in"

Hmmm... domain...

```
$ dig ANY flag.bckdr.in
; <<>> DiG 9.9.5-4.3ubuntu0.2-Ubuntu <<>> ANY flag.bckdr.in
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 65328
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 2, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;flag.bckdr.in.         IN  ANY
;; ANSWER SECTION:
flag.bckdr.in.      300 IN  TXT "e4de7470b35f7b3627283a61a808d32b99f91d5a1092a892bdb5bcdb4af3b7ab"
flag.bckdr.in.      300 IN  A   173.194.126.99
;; AUTHORITY SECTION:
bckdr.in.       80869   IN  NS  kip.ns.cloudflare.com.
bckdr.in.       80869   IN  NS  lisa.ns.cloudflare.com.
;; Query time: 15 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Thu Mar 26 19:16:01 EDT 2015
;; MSG SIZE  rcvd: 189
```

```
...
;; ANSWER SECTION:
flag.bckdr.in.      300 IN  TXT "e4de7470b35f7b3627283a61a808d32b99f91d5a1092a892bdb5bcdb4af3b7ab"
...
```

That sure looks like a flag to me.
