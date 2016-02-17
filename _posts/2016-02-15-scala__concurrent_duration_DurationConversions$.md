
#                scala.concurrent.duration.DurationConversions                #

```scala
object DurationConversions
```

This object just holds some cogs which make the DSL machine work, not for direct
consumption.

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Classifier[C] extends AnyRef`                                     ###

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `implicit object fromNowConvert extends Classifier[fromNow.type]`        ###

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)


### `implicit object spanConvert extends Classifier[span.type]`              ###

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)

