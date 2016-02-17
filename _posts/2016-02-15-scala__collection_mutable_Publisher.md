
#                      scala.collection.mutable.Publisher                      #

```scala
trait Publisher[Evt] extends AnyRef
```

 `Publisher[A,This]` objects publish events of type `A` to all registered
subscribers. When subscribing, a subscriber may specify a filter which can be
used to constrain the number of events sent to the subscriber. Subscribers may
suspend their subscription, or reactivate a suspended subscription. Class
 `Publisher` is typically used as a mixin. The abstract type `Pub` models the
type of the publisher itself.

* Evt
  * type of the published event.

* Source
  * [Publisher.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Publisher.scala#L1)
* Version
  * 2.8
* Since
  * 1


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Filter = (Evt) ⇒ Boolean`                                          ###


### `abstract type Pub <: Publisher[Evt]`                                    ###


### `type Sub = Subscriber[Evt, Pub]`                                        ###


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.Publisher
--------------------------------------------------------------------------------


### `def activateSubscription(sub: Sub): Unit`                               ###

(defined at scala.collection.mutable.Publisher)


### `def equals(obj: Any): Boolean`                                          ###

Checks if two publishers are structurally identical.

* returns
  * true, iff both publishers contain the same sequence of elements.

* Definition Classes
  * Publisher → AnyRef → Any

(defined at scala.collection.mutable.Publisher)


### `def publish(event: Evt): Unit`                                          ###

* Attributes
  * protected

(defined at scala.collection.mutable.Publisher)


### `def removeSubscription(sub: Sub): Unit`                                 ###

(defined at scala.collection.mutable.Publisher)


### `val self: Pub`                                                          ###

The publisher itself of type `Pub` . Implemented by a cast from `this` here.
Needs to be overridden if the actual publisher is different from `this` .

* Attributes
  * protected

(defined at scala.collection.mutable.Publisher)


### `def subscribe(sub: Sub): Unit`                                          ###

(defined at scala.collection.mutable.Publisher)


### `def subscribe(sub: Sub, filter: Filter): Unit`                          ###

(defined at scala.collection.mutable.Publisher)


### `def suspendSubscription(sub: Sub): Unit`                                ###
(defined at scala.collection.mutable.Publisher)
