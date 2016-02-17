
#                       scala.util.matching.Regex.Groups                       #

```scala
object Groups
```

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


--------------------------------------------------------------------------------
              Value Members From scala.util.matching.Regex.Groups
--------------------------------------------------------------------------------


### `def unapplySeq(m: Match): Option[Seq[String]]`                          ###
(defined at scala.util.matching.Regex.Groups)
