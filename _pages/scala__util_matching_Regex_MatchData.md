
#                     scala.util.matching.Regex.MatchData                     #

```scala
trait MatchData extends AnyRef
```

This class provides methods to access the details of a match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.util.matching.Regex.MatchData
--------------------------------------------------------------------------------


### `abstract def end(i: Int): Int`                                          ###

The index following the last matched character in group `i` , or -1 if nothing
was matched for that group.

(defined at scala.util.matching.Regex.MatchData)


### `abstract def start(i: Int): Int`                                        ###

The index of the first matched character in group `i` , or -1 if nothing was
matched for that group.

(defined at scala.util.matching.Regex.MatchData)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.util.matching.Regex.MatchData
--------------------------------------------------------------------------------


### `abstract def end: Int`                                                  ###

The index following the last matched character, or -1 if nothing was matched.

(defined at scala.util.matching.Regex.MatchData)


### `def after(i: Int): CharSequence`                                        ###

The char sequence after last character of match in group `i` , or `null` if
nothing was matched for that group.

(defined at scala.util.matching.Regex.MatchData)


### `def before(i: Int): CharSequence`                                       ###

The char sequence before first character of match in group `i` , or `null` if
nothing was matched for that group.

(defined at scala.util.matching.Regex.MatchData)


### `def group(i: Int): String`                                              ###

The matched string in group `i` , or `null` if nothing was matched.

(defined at scala.util.matching.Regex.MatchData)


### `def group(id: String): String`                                          ###

Returns the group with given name.

* id
  * The group name
* returns
  * The requested group

* Exceptions thrown
  * NoSuchElementException if the requested group name is not defined
(defined at scala.util.matching.Regex.MatchData)
