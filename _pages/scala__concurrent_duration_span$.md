
#                        scala.concurrent.duration.span                        #

```scala
object span
```

This object can be used as closing token if you prefer dot-less style but do not
want to enable language.postfixOps:

```scala
import scala.concurrent.duration._

val duration = 2 seconds span
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)

