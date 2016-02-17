
#                             scala.util.matching                             #

```scala
package matching
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Regex extends Serializable`                                       ###

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


### `trait UnanchoredRegex extends Regex`                                    ###

A Regex that finds the first match when used in a pattern match.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)
* See also
  * Regex#unanchored


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Regex extends Serializable`                                      ###

This object defines inner classes that describe regex matches and helper
objects.

* Source
  * [Regex.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/matching/Regex.scala#L1)

