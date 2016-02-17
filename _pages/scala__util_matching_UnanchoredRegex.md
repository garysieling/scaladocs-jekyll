
#                     scala.util.matching.UnanchoredRegex                     #

```scala
trait UnanchoredRegex extends Regex
```

A Regex that finds the first match when used in a pattern match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)
* See also
  * Regex#unanchored


--------------------------------------------------------------------------------
            Deprecated Value Members From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `def unapplySeq(target: Any): Option[List[String]]`                      ###

Tries to match target.

* target
  * The string to match
* returns
  * The matches

* Definition Classes
  * Regex
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Extracting a match result from anything but a
    CharSequence or Match is deprecated

(defined at scala.util.matching.Regex)


--------------------------------------------------------------------------------
                  Value Members From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `def anchored: Regex`                                                    ###

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def findAllIn(source: CharSequence): MatchIterator`                     ###

Return all non-overlapping matches of this `Regex` in the given character
sequence as a scala.util.matching.Regex.MatchIterator, which is a special
scala.collection.Iterator that returns the matched strings but can also be
queried for more data about the last match, such as capturing groups and start
position.

A `MatchIterator` can also be converted into an iterator that returns objects of
type scala.util.matching.Regex.Match, such as is normally returned by
 `findAllMatchIn` .

Where potential matches overlap, the first possible match is returned, followed
by the next match that follows the input consumed by the first match:

```scala
val hat  = "hat[^a]+".r
val hathaway = "hathatthattthatttt"
val hats = (hat findAllIn hathaway).toList                     // List(hath, hattth)
val pos  = (hat findAllMatchIn hathaway map (_.start)).toList  // List(0, 7)
```

To return overlapping matches, it is possible to formulate a regular expression
with lookahead ( `?=` ) that does not consume the overlapping region.

```scala
val madhatter = "(h)(?=(at[^a]+))".r
val madhats   = (madhatter findAllMatchIn hathaway map {
  case madhatter(x,y) => s"$x$y"
}).toList                                       // List(hath, hatth, hattth, hatttt)
```

Attempting to retrieve match information before performing the first match or
after exhausting the iterator results in java.lang.IllegalStateException. See
scala.util.matching.Regex.MatchIterator for details.

* source
  * The text to match against.
* returns
  * A scala.util.matching.Regex.MatchIterator of matched substrings.

* Definition Classes
  * Regex

Example:

```scala
for (words <- """\w+""".r findAllIn "A simple example.") yield words
```

(defined at scala.util.matching.Regex)


### `def findAllMatchIn(source: CharSequence): Iterator[Match]`              ###

Return all non-overlapping matches of this regexp in given character sequence as
a scala.collection.Iterator of scala.util.matching.Regex.Match.

* source
  * The text to match against.
* returns
  * A scala.collection.Iterator of scala.util.matching.Regex.Match for all
    matches.

* Definition Classes
  * Regex

Example:

```scala
for (words <- """\w+""".r findAllMatchIn "A simple example.") yield words.start
```

(defined at scala.util.matching.Regex)


### `def findFirstIn(source: CharSequence): Option[String]`                  ###

Return an optional first matching string of this `Regex` in the given character
sequence, or None if there is no match.

* source
  * The text to match against.
* returns
  * An scala.Option of the first matching string in the text.

* Definition Classes
  * Regex

Example:

```scala
"""\w+""".r findFirstIn "A simple example." foreach println // prints "A"
```

(defined at scala.util.matching.Regex)


### `def findFirstMatchIn(source: CharSequence): Option[Match]`              ###

Return an optional first match of this `Regex` in the given character sequence,
or None if it does not exist.

If the match is successful, the scala.util.matching.Regex.Match can be queried
for more data.

* source
  * The text to match against.
* returns
  * A scala.Option of scala.util.matching.Regex.Match of the first matching
    string in the text.

* Definition Classes
  * Regex

Example:

```scala
("""[a-z]""".r findFirstMatchIn "A simple example.") map (_.start) // returns Some(2), the index of the first match in the text
```

(defined at scala.util.matching.Regex)


### `def findPrefixMatchOf(source: CharSequence): Option[Match]`             ###

Return an optional match of this `Regex` at the beginning of the given character
sequence, or None if it matches no prefix of the character sequence.

Unlike `findFirstMatchIn` , this method will only return a match at the
beginning of the input.

* source
  * The text to match against.
* returns
  * A scala.Option of the scala.util.matching.Regex.Match of the matched string.

* Definition Classes
  * Regex

Example:

```scala
"""\w+""".r findPrefixMatchOf "A simple example." map (_.after) // returns Some(" simple example.")
```

(defined at scala.util.matching.Regex)


### `def findPrefixOf(source: CharSequence): Option[String]`                 ###

Return an optional match of this `Regex` at the beginning of the given character
sequence, or None if it matches no prefix of the character sequence.

Unlike `findFirstIn` , this method will only return a match at the beginning of
the input.

* source
  * The text to match against.
* returns
  * A scala.Option of the matched prefix.

* Definition Classes
  * Regex

Example:

```scala
"""\p{Lower}""".r findPrefixOf "A simple example." // returns None, since the text does not begin with a lowercase letter
```

(defined at scala.util.matching.Regex)


### `val pattern: Pattern`                                                   ###

The compiled pattern

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def replaceAllIn(target: CharSequence, replacer: (Match) ⇒ String): String` ###

Replaces all matches using a replacer function. The replacer function takes a
scala.util.matching.Regex.Match so that extra information can be obtained from
the match. For example:

```scala
import scala.util.matching.Regex
val datePattern = new Regex("""(\d\d\d\d)-(\d\d)-(\d\d)""", "year", "month", "day")
val text = "From 2011-07-15 to 2011-07-17"
val repl = datePattern replaceAllIn (text, m => s"${m group "month"}/${m group "day"}")
```

In the replacement String, a dollar sign ( `$` ) followed by a number will be
interpreted as a reference to a group in the matched pattern, with numbers 1
through 9 corresponding to the first nine groups, and 0 standing for the whole
match. Any other character is an error. The backslash ( `\` ) character will be
interpreted as an escape character and can be used to escape the dollar sign.
Use `Regex.quoteReplacement` to escape these characters.

* target
  * The string to match.
* replacer
  * The function which maps a match to another string.
* returns
  * The target string after replacements.

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def replaceAllIn(target: CharSequence, replacement: String): String`    ###

Replaces all matches by a string.

In the replacement String, a dollar sign ( `$` ) followed by a number will be
interpreted as a reference to a group in the matched pattern, with numbers 1
through 9 corresponding to the first nine groups, and 0 standing for the whole
match. Any other character is an error. The backslash ( `\` ) character will be
interpreted as an escape character and can be used to escape the dollar sign.
Use `Regex.quoteReplacement` to escape these characters.

* target
  * The string to match
* replacement
  * The string that will replace each match
* returns
  * The resulting string

* Definition Classes
  * Regex

Example:

```scala
"""\d+""".r replaceAllIn ("July 15", "") // returns "July "
```

(defined at scala.util.matching.Regex)


### `def replaceFirstIn(target: CharSequence, replacement: String): String`  ###

Replaces the first match by a string.

In the replacement String, a dollar sign ( `$` ) followed by a number will be
interpreted as a reference to a group in the matched pattern, with numbers 1
through 9 corresponding to the first nine groups, and 0 standing for the whole
match. Any other character is an error. The backslash ( `\` ) character will be
interpreted as an escape character and can be used to escape the dollar sign.
Use `Regex.quoteReplacement` to escape these characters.

* target
  * The string to match
* replacement
  * The string that will replace the match
* returns
  * The resulting string

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def replaceSomeIn(target: CharSequence, replacer: (Match) ⇒ Option[String]): String` ###

Replaces some of the matches using a replacer function that returns an
scala.Option. The replacer function takes a scala.util.matching.Regex.Match so
that extra information can be obtained from the match. For example:

```scala
import scala.util.matching.Regex._

val vars = Map("x" -> "a var", "y" -> """some $ and \ signs""")
val text = "A text with variables %x, %y and %z."
val varPattern = """%(\w+)""".r
val mapper = (m: Match) => vars get (m group 1) map (quoteReplacement(_))
val repl = varPattern replaceSomeIn (text, mapper)
```

In the replacement String, a dollar sign ( `$` ) followed by a number will be
interpreted as a reference to a group in the matched pattern, with numbers 1
through 9 corresponding to the first nine groups, and 0 standing for the whole
match. Any other character is an error. The backslash ( `\` ) character will be
interpreted as an escape character and can be used to escape the dollar sign.
Use `Regex.quoteReplacement` to escape these characters.

* target
  * The string to match.
* replacer
  * The function which optionally maps a match to another string.
* returns
  * The target string after replacements.

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def split(toSplit: CharSequence): Array[String]`                        ###

Splits the provided character sequence around matches of this regexp.

* toSplit
  * The character sequence to split
* returns
  * The array of strings computed by splitting the input around matches of this
    regexp

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def unapplySeq(c: Char): Option[List[Char]]`                            ###

Tries to match the String representation of a scala.Char.

If the match succeeds, the result is the first matching group if any groups are
defined, or an empty Sequence otherwise.

For example:

```scala
val cat = "cat"
// the case must consume the group to match
val r = """(\p{Lower})""".r
cat(0) match { case r(x) => true }
cat(0) match { case r(_) => true }
cat(0) match { case r(_*) => true }
cat(0) match { case r() => true }     // no match

// there is no group to extract
val r = """\p{Lower}""".r
cat(0) match { case r(x) => true }    // no match
cat(0) match { case r(_) => true }    // no match
cat(0) match { case r(_*) => true }   // matches
cat(0) match { case r() => true }     // matches

// even if there are multiple groups, only one is returned
val r = """((.))""".r
cat(0) match { case r(_) => true }    // matches
cat(0) match { case r(_,_) => true }  // no match
```

* c
  * The Char to match
* returns
  * The match

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def unapplySeq(s: CharSequence): Option[List[String]]`                  ###

Tries to match a java.lang.CharSequence.

If the match succeeds, the result is a list of the matching groups (or a `null`
element if a group did not match any input). If the pattern specifies no groups,
then the result will be an empty list on a successful match.

This method attempts to match the entire input by default; to find the next
matching subsequence, use an unanchored `Regex` .

For example:

```scala
val p1 = "ab*c".r
val p1Matches = "abbbc" match {
  case p1() => true               // no groups
  case _    => false
}
val p2 = "a(b*)c".r
val p2Matches = "abbbc" match {
  case p2(_*) => true             // any groups
  case _      => false
}
val numberOfB = "abbbc" match {
  case p2(b) => Some(b.length)    // one group
  case _     => None
}
val p3 = "b*".r.unanchored
val p3Matches = "abbbc" match {
  case p3() => true               // find the b's
  case _    => false
}
val p4 = "a(b*)(c+)".r
val p4Matches = "abbbcc" match {
  case p4(_*) => true             // multiple groups
  case _      => false
}
val allGroups = "abbbcc" match {
  case p4(all @ _*) => all mkString "/" // "bbb/cc"
  case _            => ""
}
val cGroup = "abbbcc" match {
  case p4(_, c) => c
  case _        => ""
}
```

* s
  * The string to match
* returns
  * The matches

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


### `def unapplySeq(m: Match): Option[List[String]]`                         ###

Tries to match on a scala.util.matching.Regex.Match.

A previously failed match results in None.

If a successful match was made against the current pattern, then that result is
used.

Otherwise, this Regex is applied to the previously matched input, and the result
of that match is used.

* Definition Classes
  * Regex

(defined at scala.util.matching.Regex)


--------------------------------------------------------------------------------
             Value Members From scala.util.matching.UnanchoredRegex
--------------------------------------------------------------------------------


### `def runMatcher(m: Matcher): Boolean`                                    ###

* Attributes
  * protected
* Definition Classes
  * UnanchoredRegex → Regex

(defined at scala.util.matching.UnanchoredRegex)


### `def unanchored: UnanchoredRegex`                                        ###

Create a new Regex with the same pattern, but no requirement that the entire
String matches in extractor patterns.

Normally, matching on `date` behaves as though the pattern were enclosed in
anchors, `"^pattern$".`

The unanchored `Regex` behaves as though those anchors were removed.

Note that this method does not actually strip any matchers from the pattern.

Calling `anchored` returns the original `Regex` .

```scala
val date = """(\d\d\d\d)-(\d\d)-(\d\d)""".r.unanchored

val date(year, month, day) = "Date 2011-07-15"                       // OK

val copyright: String = "Date of this document: 2011-07-15" match {
  case date(year, month, day) => s"Copyright $year"                  // OK
  case _                      => "No copyright"
}
```

* returns
  * The new unanchored regex

* Definition Classes
  * UnanchoredRegex → Regex
(defined at scala.util.matching.UnanchoredRegex)
