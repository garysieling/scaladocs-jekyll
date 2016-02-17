
#                       scala.util.matching.Regex.Match                       #

```scala
object Match
```

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
               Value Members From scala.util.matching.Regex.Match
--------------------------------------------------------------------------------


### `def unapply(m: Match): Some[String]`                                    ###
(defined at scala.util.matching.Regex.Match)
