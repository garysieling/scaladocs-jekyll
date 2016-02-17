
#                      scala.concurrent.duration.Deadline                      #

```scala
object Deadline extends Serializable
```

* Source
  * [Deadline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Deadline.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `implicit object DeadlineIsOrdered extends Ordering[Deadline]`           ###

The natural ordering for deadline is determined by the natural order of the
underlying (finite) duration.

* Source
  * [Deadline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Deadline.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.concurrent.duration.Deadline
--------------------------------------------------------------------------------


### `def now: Deadline`                                                      ###

Construct a deadline due exactly at the point where this method is called.
Useful for then advancing it to obtain a future deadline, or for sampling the
current time exactly once and then comparing it to multiple deadlines (using
subtraction).
(defined at scala.concurrent.duration.Deadline)
