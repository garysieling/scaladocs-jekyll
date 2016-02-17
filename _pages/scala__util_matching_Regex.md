
#                          scala.util.matching.Regex                          #

```scala
class Regex extends Serializable
```

A regular expression is used to determine whether a string matches a pattern
and, if it does, to extract or transform the parts that match.

This class delegates to the java.util.regex package of the Java Platform. See
the documentation for java.util.regex.Pattern for details about the regular
expression syntax for pattern strings.

An instance of `Regex` represents a compiled regular expression pattern. Since
compilation is expensive, frequently used `Regex` es should be constructed once,
outside of loops and perhaps in a companion object.

The canonical way to create a `Regex` is by using the method `r` , provided
implicitly for strings:

```scala
val date = """(\d\d\d\d)-(\d\d)-(\d\d)""".r
```

Since escapes are not processed in multi-line string literals, using triple
quotes avoids having to escape the backslash character, so that `"\\d"` can be
written `"""\d"""` .

To extract the capturing groups when a `Regex` is matched, use it as an
extractor in a pattern match:

```scala
"2004-01-20" match {
  case date(year, month, day) => s"$year was a good year for PLs."
}
```

To check only whether the `Regex` matches, ignoring any groups, use a sequence
wildcard:

```scala
"2004-01-20" match {
  case date(_*) => "It's a date!"
}
```

That works because a `Regex` extractor produces a sequence of strings.
Extracting only the year from a date could also be expressed with a sequence
wildcard:

```scala
"2004-01-20" match {
  case date(year, _*) => s"$year was a good year for PLs."
}
```

In a pattern match, `Regex` normally matches the entire input. However, an
unanchored `Regex` finds the pattern anywhere in the input.

```scala
val embeddedDate = date.unanchored
"Date: 2004-01-20 17:25:18 GMT (10 years, 28 weeks, 5 days, 17 hours and 51 minutes ago)" match {
  case embeddedDate("2004", "01", "20") => "A Scala is born."
}
```

To find or replace matches of the pattern, use the various find and replace
methods. There is a flavor of each method that produces matched strings and
another that produces `Match` objects.

For example, pattern matching with an unanchored `Regex` , as in the previous
example, is the same as using `findFirstMatchIn` , except that the findFirst
methods return an `Option` , or `None` for no match:

```scala
val dates = "Important dates in history: 2004-01-20, 1958-09-05, 2010-10-06, 2011-07-15"
val firstDate = date findFirstIn dates getOrElse "No date found."
val firstYear = for (m <- date findFirstMatchIn dates) yield m group 1
```

To find all matches:

```scala
val allYears = for (m <- date findAllMatchIn dates) yield m group 1
```

But `findAllIn` returns a special iterator of strings that can be queried for
the `MatchData` of the last match:

```scala
val mi = date findAllIn dates
val oldies = mi filter (_ => (mi group 1).toInt < 1960) map (s => s"$s: An oldie but goodie.")
```

Note that `findAllIn` finds matches that don't overlap. (See findAllIn for more
examples.)

```scala
val num = """(\d+)""".r
val all = (num findAllIn "123").toList  // List("123"), not List("123", "23", "3")
```

Text replacement can be performed unconditionally or as a function of the
current match:

```scala
val redacted    = date replaceAllIn (dates, "XXXX-XX-XX")
val yearsOnly   = date replaceAllIn (dates, m => m group 1)
val months      = (0 to 11) map { i => val c = Calendar.getInstance; c.set(2014, i, 1); f"$c%tb" }
val reformatted = date replaceAllIn (dates, _ match { case date(y,m,d) => f"${months(m.toInt - 1)} $d, $y" })
```

Pattern matching the `Match` against the `Regex` that created it does not
reapply the `Regex` . In the expression for `reformatted` , each `date` match is
computed once. But it is possible to apply a `Regex` to a `Match` resulting from
a different pattern:

```scala
val docSpree = """2011(?:-\d{2}){2}""".r
val docView  = date replaceAllIn (dates, _ match {
  case docSpree() => "Historic doc spree!"
  case _          => "Something else happened"
})
```

* Self Type
  * Regex
* Annotations
  * @ SerialVersionUID ()
* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)
* Version
  * 1.1, 29/01/2008
* See also
  * java.util.regex.Pattern


--------------------------------------------------------------------------------
            Deprecated Value Members From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `def unapplySeq(target: Any): Option[List[String]]`                      ###

Tries to match target.

* target
  * The string to match
* returns
  * The matches

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Extracting a match result from anything but a
    CharSequence or Match is deprecated

(defined at scala.util.matching.Regex)


--------------------------------------------------------------------------------
              Instance Constructors From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `new Regex(regex: String, groupNames: String*)`                          ###

Compile a regular expression, supplied as a string, into a pattern that can be
matched against inputs.

If group names are supplied, they can be used this way:

```scala
val namedDate  = new Regex("""(\d\d\d\d)-(\d\d)-(\d\d)""", "year", "month", "day")
val namedYears = for (m <- namedDate findAllMatchIn dates) yield m group "year"
```

This constructor does not support options as flags, which must be supplied as
inline flags in the pattern string: `(?idmsux-idmsux)` .

* regex
  * The regular expression to compile.
* groupNames
  * Names of capturing groups.

(defined at scala.util.matching.Regex)


--------------------------------------------------------------------------------
                  Value Members From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `def anchored: Regex`                                                    ###

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

Example:

```scala
"""\p{Lower}""".r findPrefixOf "A simple example." // returns None, since the text does not begin with a lowercase letter
```

(defined at scala.util.matching.Regex)


### `val pattern: Pattern`                                                   ###

The compiled pattern

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

(defined at scala.util.matching.Regex)


### `def runMatcher(m: Matcher): Boolean`                                    ###

* Attributes
  * protected

(defined at scala.util.matching.Regex)


### `def split(toSplit: CharSequence): Array[String]`                        ###

Splits the provided character sequence around matches of this regexp.

* toSplit
  * The character sequence to split
* returns
  * The array of strings computed by splitting the input around matches of this
    regexp

(defined at scala.util.matching.Regex)


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

(defined at scala.util.matching.Regex)


### `def unapplySeq(m: Match): Option[List[String]]`                         ###

Tries to match on a scala.util.matching.Regex.Match.

A previously failed match results in None.

If a successful match was made against the current pattern, then that result is
used.

Otherwise, this Regex is applied to the previously matched input, and the result
of that match is used.
(defined at scala.util.matching.Regex)
