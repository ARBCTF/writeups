The hint put me on the lookout for places in the application that deliver files:

```
Analyze and tamper with links in the application that deliver a file directly. Click for more hints.
```

After clicking around in the application for a while I stumbled upon the
"Checkout" functionality. After added items to the checkout basket you can
visit "Your Basket." Once here, clicking on the "Checkout" button takes you
to an invoice page:

```
http://localhost:3000/ftp/order_78263d11ddddd79fd2557de9e9c1d475.pdf
```

Hmm, looks like an FTP server. I wonder what happens if we visit `http://localhost:3000/ftp`...

Visiting this directory yields:

```
acquisitions.md9092017-12-18
coupons_2013.md.bak1312017-12-18
eastere.gg3242017-12-18
incident-support.kdbx32782017-12-18
legal.md30472017-12-18
order_35217501cf4ba4a24260f08bb2feb28d.pdf12202018-1-3
order_78263d11ddddd79fd2557de9e9c1d475.pdf11522018-1-3
order_85d50d46c43c52d8294ec94d0d910597.pdf11532018-1-3
package.json.bak43662017-12-18
suspicious_errors.yml
```

Investigating some of these sensitive markdown files does the trick and
completes the challenge!
