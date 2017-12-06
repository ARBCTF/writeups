I initially looked around the page for a "Scoreboard" button, or some UI
element leading to a score board.

Next I guessed at the URL `/#/scoreboard`, which ended up being close, but
incorrect.

Finally, I figured they would do the classic "first challenge" for a webapp...
commented out HTML. Sure enough, after inspecting the source and searching for
"score" it lead to the following code:

```
<!--
<li class="dropdown">
	<a href="#/score-board">Score Board</a>
</li>
-->
```

And voila! `/#/score-board` did the trick.
