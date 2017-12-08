This one stumped me for a while. I think my final solution may not have been
what they were intending, but, then again, that's security bugs.

For the longest time I was mucking around in the HTML and trying to submit
the form. If we inspect the HTML while clicking the various Rating buttons
we can see that it's changing the `aria-valuenow` value in the form. So I
tried setting this to `0` and submitting by removing `disabled="disabled"`
on the submit button. This didn't work though :(

I never did find out exactly why that didn't work. It seems this form is using
some weird Angular magic to make everything happen, so maybe it's not enough
to simply modify the HTML, it seems like we have to trigger some JS code. I
think the action of clicking one of the ratings has some side-effects that
modifying the HTML manually doesn't.

Anyways, if we look at the rating stars we see that clicking them calls a JS
function: `ng-click="rate($index + 1)"`. This `rate` function must be what's
performing the action behind the scenes. Since my Chrome Inspector skills are
lacking I couldn't find exactly where this `rate` function was defined. Time
to break out the 'ol CLI skills...

There's this cool flag you can pass to `wget` that will pull down all the files
necessary to run a particular web page yourself, including all the JS files for
grepping :)

```
$ wget --mirror http://localhost:3000/#/contact
```

We now have the entire page mirrored in the `localhost:3000` folder. Dope.

We can now search for this `rate` function:

```
$ rg --files-with-matches 'rate\(' localhost\:3000/
localhost:3000/bower_components/angular-bootstrap/ui-bootstrap.min.js
localhost:3000/bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js
```

By the way, `rg` is short for `ripgrep`, an awesome tool that can *almost*
replace `grep`. It's approximately a zillion times faster than `grep`, learn
it, love it.

Anyways... we can now investigate the `ui-bootstrap.min.js` and
`ui-bootstrap-tpls.min.js` files for this `rate` function. Since I don't have
a good CLI de-minify tool I just headed back to the Chrome Inspector and took
a peak at those two files. From here we see they look like:

```
a.rate = function(b) {
	if (!a.readonly && b >= 0 && b <= a.range.length) {
		var c = e.enableReset && d.$viewValue === b ? 0 : b;
		d.$setViewValue(c),
		d.$render()
	}
}
```

Instead of trying to get the correct value passed to this function we can
just place a breakpoint on the `setViewValue` line` and set `c = 0;` ourselves.
Next we click submit, and voila, we've set a 0 star rating!

The Chrome Inspector can be very powerful and a useful tool to have in your
arsenal. Further, you should never rely on Javascript, or anything client-side,
to validate things for you.
