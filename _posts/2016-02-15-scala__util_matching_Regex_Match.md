
#                       scala.util.matching.Regex.Match                       #

```scala
class Match extends MatchData
```

Provides information about a successful match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


--------------------------------------------------------------------------------
           Instance Constructors From scala.util.matching.Regex.Match
--------------------------------------------------------------------------------


### `new Match(source: CharSequence, matcher: Matcher, groupNames: Seq[String])` ###

(defined at scala.util.matching.Regex.Match)


--------------------------------------------------------------------------------
               Value Members From scala.util.matching.Regex.Match
--------------------------------------------------------------------------------


### `def end(i: Int): Int`                                                   ###

The index following the last matched character in group `i` .

* Definition Classes
  * Match → MatchData

(defined at scala.util.matching.Regex.Match)


### `def start(i: Int): Int`                                                 ###

The index of the first matched character in group `i` .

* Definition Classes
  * Match → MatchData

(defined at scala.util.matching.Regex.Match)


--------------------------------------------------------------------------------
             Value Members From scala.util.matching.Regex.MatchData
--------------------------------------------------------------------------------


### `def after(i: Int): CharSequence`                                        ###

The char sequence after last character of match in group `i` , or `null` if
nothing was matched for that group.

* Definition Classes
  * MatchData

(defined at scala.util.matching.Regex.MatchData)


### `def before(i: Int): CharSequence`                                       ###

The char sequence before first character of match in group `i` , or `null` if
nothing was matched for that group.

* Definition Classes
  * MatchData

(defined at scala.util.matching.Regex.MatchData)


### `def group(i: Int): String`                                              ###

The matched string in group `i` , or `null` if nothing was matched.

* Definition Classes
  * MatchData

(defined at scala.util.matching.Regex.MatchData)


### `def group(id: String): String`                                          ###

Returns the group with given name.

* id
  * The group name
* returns
  * The requested group

* Definition Classes
  * MatchData
* Exceptions thrown
  * NoSuchElementException if the requested group name is not defined
(defined at scala.util.matching.Regex.MatchData)
