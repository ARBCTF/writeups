https://backdoor.sdslabs.co/challenges/LOST

It tells us to visit http://hack.bckdr.in/LOST/

Which then tells us to check out the console. Let's grab the source first:

```
$ curl -X GET http://hack.bckdr.in/LOST
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="http://hack.bckdr.in/LOST/">here</a>.</p>
<hr>
<address>Apache/2.4.7 (Ubuntu) Server at hack.bckdr.in Port 80</address>
</body></html>
```

Bleh, we have to follow the redirect...

```
$ curl -L -X GET http://hack.bckdr.in/LOST
<!DOCTYPE html>
<html>
<head>
	<title>Welcome to Web-50</title>
	<style>
	body {
		width: 100%;
	}
	.welcome-msg, .info {
		text-align:  center;
	}
	</style>
</head>
<body>
<p class="welcome-msg">
Hi! Welcome to Web-50!
</p>
<br/>
<p class="info">
<b>Flag</b> is somewhere around and simple to get, just sneak well in console.
</p>
<br/>
</body>
<script>
if(!window.console) {
	window.alert('You need a console n00b');
} else {
	window.console.log('Welcome n00b to the ctf');
	window.console.log('n00b sometimes you need to POST to flag.php');
}
</script>
</html>
```

And after we follow the instructions:

```
$ curl -X POST hack.bckdr.in/LOST/flag.php
You did well
Here is you flag: <redacted>
```

Ez pz.
