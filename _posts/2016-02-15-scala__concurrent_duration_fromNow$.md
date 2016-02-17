
#                      scala.concurrent.duration.fromNow                      #

```scala
object fromNow
```

This object can be used as closing token for declaring a deadline at some future
point in time:

```scala
import scala.concurrent.duration._

val deadline = 3 seconds fromNow
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)

