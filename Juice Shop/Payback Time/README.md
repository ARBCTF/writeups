> Place an order that makes you rich.

The typical way to do this on sites that allow for payment is to mess with the
payment processing system. E.g. set item's value to $0.00, set negative
quantities of items, etc. Let's start looking there.

After visiting a user's basket we're given a few options. The most obvious
approach is to play with the "Quantity." Clicking on the webpage doesn't allow
us to set a lower value than `1`. Let's crack open the Chrome inspector and
see what API calls are being made.

When clicking the "Quantity" buttons we can see a few requests fly by. The only
one that changes system state is a `PUT` request to the following endpoint:

```
/api/BasketItems/<item-number>
```

We can also see it takes a request payload of:

```
{"quantity": <quantity-value>}
```

Let's "Copy as cURL" and set a negative quantity:

```
$ curl -X PUT ... '{"quantity":-10}'
{"status":"success","data":{"id":9,"quantity":-10,"createdAt":"2018-02-05T19:58:04.663Z","updatedAt":"2018-02-05T20:03:37.738Z","BasketId":2,"ProductId":1}}
```

Success! Now clicking "Checkout" should complete the challenge!
