
#                scala.collection.immutable.Stream.ConsWrapper                #

```scala
class ConsWrapper[A] extends AnyRef
```

A wrapper class that adds `#::` for cons and `#:::` for concat as operations to
streams.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.immutable.Stream.ConsWrapper
--------------------------------------------------------------------------------


### `new ConsWrapper(tl: ⇒ Stream[A])`                                       ###

(defined at scala.collection.immutable.Stream.ConsWrapper)


--------------------------------------------------------------------------------
       Value Members From scala.collection.immutable.Stream.ConsWrapper#
--------------------------------------------------------------------------------


### `def #::(hd: A): Stream[A]`                                              ###

Construct a stream consisting of a given first element followed by elements from
a lazily evaluated Stream.

(defined at scala.collection.immutable.Stream.ConsWrapper#)


### `def #:::(prefix: Stream[A]): Stream[A]`                                 ###

Construct a stream consisting of the concatenation of the given stream and a
lazily evaluated Stream.

(defined at scala.collection.immutable.Stream.ConsWrapper#)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ConsWrapper [A] to
    CollectionsHaveToParArray [ConsWrapper [A], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ConsWrapper [A]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
