
#                          scala.util.matching.Regex                          #

```scala
object Regex extends Serializable
```

This object defines inner classes that describe regex matches and helper
objects.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Match extends MatchData`                                          ###

Provides information about a successful match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


### `trait MatchData extends AnyRef`                                         ###

This class provides methods to access the details of a match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


### `class MatchIterator extends AbstractIterator[String] with Iterator[String] with MatchData` ###

A class to step through a sequence of regex matches.

All methods inherited from scala.util.matching.Regex.MatchData will throw a
java.lang.IllegalStateException until the matcher is initialized. The matcher
can be initialized by calling `hasNext` or `next()` or causing these methods to
be called, such as by invoking `toString` or iterating through the iterator's
elements.

* Self Type
  * MatchIterator
* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)
* See also
  * java.util.regex.Matcher


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Groups`                                                          ###

An extractor object that yields the groups in the match. Using this extractor
rather than the original `Regex` ensures that the match is not recomputed.

```scala
import scala.util.matching.Regex.Groups

val date = """(\d\d\d\d)-(\d\d)-(\d\d)""".r
val text = "The doc spree happened on 2011-07-15."
val day = date replaceAllIn(text, _ match { case Groups(_, month, day) => s"$month/$day" })
```

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


### `object Match`                                                           ###

An extractor object for Matches, yielding the matched string.

This can be used to help writing replacer functions when you are not interested
in match data. For example:

```scala
import scala.util.matching.Regex.Match
"""\w+""".r replaceAllIn ("A simple example.", _ match { case Match(s) => s.toUpperCase })
```

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.util.matching.Regex
--------------------------------------------------------------------------------


### `def quote(text: String): String`                                        ###

Quotes strings to be used literally in regex patterns.

All regex metacharacters in the input match themselves literally in the output.

Example:

```scala
List("US$", "CAN$").map(Regex.quote).mkString("|").r
```

(defined at scala.util.matching.Regex)


### `def quoteReplacement(text: String): String`                             ###

Quotes replacement strings to be used in replacement methods.

Replacement methods give special meaning to backslashes ( `\` ) and dollar signs
( `$` ) in replacement strings, so they are not treated as literals. This method
escapes these characters so the resulting string can be used as a literal
replacement representing the input string.

* text
  * The string one wishes to use as literal replacement.
* returns
  * A string that can be used to replace matches with `text` .

Example:

```scala
"CURRENCY".r.replaceAllIn(input, Regex quoteReplacement "US$")
```
(defined at scala.util.matching.Regex)
