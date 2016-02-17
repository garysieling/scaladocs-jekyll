
#                     scala.collection.mutable.Subscriber                     #

```scala
trait Subscriber[-Evt, -Pub] extends AnyRef
```

 `Subscriber[A, B]` objects may subscribe to events of type `A` published by an
object of type `B` . `B` is typically a subtype of
scala.collection.mutable.Publisher.

* Source
  * [Subscriber.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Subscriber.scala#L1)
* Version
  * 2.8
* Since
  * 1


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.mutable.Subscriber
--------------------------------------------------------------------------------


### `abstract def notify(pub: Pub, event: Evt): Unit`                        ###
(defined at scala.collection.mutable.Subscriber)
