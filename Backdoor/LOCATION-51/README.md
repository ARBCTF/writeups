https://backdoor.sdslabs.co/challenges/LOCATION-51

Visiting http://hack.bckdr.in/LOCATION-51/index.html requires a password.
Let's check what the HTML looks like...

```
$ curl http://hack.bckdr.in/LOCATION-51/index.html<!DOCTYPE html>
<html>
<script type="text/javascript">
    window.location.href="trap.html";
</script>
<style type="text/css">
    @import url(http://fonts.googleapis.com/css?family=Open+Sans);
    body {
        font-family: 'Open Sans';
        font-size: 25px;
    }
    #title {
        text-align: center;
        margin-bottom: 100px;
    }
    #body {
    }
    #wrapper {
        padding: 20px 250px 250px 250px;
        margin: 100px 250px;
        border: 2px solid black;
    }
</style>
<head>
    <title>LOCATION 51</title>
</head>
<body>
    <div id="wrapper">

        <div id="title">
            LOCATION 51
        </div>
        <div id="body">
            This is the secret location of all backdoor hackers. Please do not disclose this location to NSA/FBI.
            <br><br>
            Our aim is World Domination.
        </div>

    </div>
<script type="text/javascript">
    a = prompt("Password");
    if(a=="H4CK3D")
    {
        alert("Flag is "+atob("T0hIX1kwVV9DNE5fQkwwQ0tfSkFWQVNDMVBUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA"));
    }
    else
    {
        alert("Wrong Password!");
    }
</script>
</body>
</html>
```

This bit looks interesting:

```
alert("Flag is "+atob("T0hIX1kwVV9DNE5fQkwwQ0tfSkFWQVNDMVBUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA"));
```

Entering `H4CK3D` as the password to the website doesn't give us anything too
useful. Let's see what this `atob` stuff is all about. Running that command in
a Javascript interpreter gives us:

```
-> atob("T0hIX1kwVV9DNE5fQkwwQ0tfSkFWQVNDMVBUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA")
<- "OHH_Y0U_C4N_BL0CK_JAVASC1PT
```

And finally:

```
$ echo -n "OHH_Y0U_C4N_BL0CK_JAVASC1PT" | sha256sum
72ded46b20570bf346b470593f9d7e026a12b5e49f9245dc6bd0f1d610c1aa57
```
