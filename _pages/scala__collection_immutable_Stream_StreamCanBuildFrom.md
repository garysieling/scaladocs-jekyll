
#             scala.collection.immutable.Stream.StreamCanBuildFrom             #

```scala
class StreamCanBuildFrom[A] extends GenericCanBuildFrom[A]
```

The factory for streams.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)
* Note
  * Methods such as map/flatMap will not invoke the `Builder` factory, but will
    return a new stream directly, to preserve laziness. The new stream is then
    cast to the factory's result type. This means that every CanBuildFrom that
    takes a Stream as its From type parameter must yield a stream as its result
    parameter. If that assumption is broken, cast errors might result.


--------------------------------------------------------------------------------
Value Members From scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[A, Stream[A]]`                                     ###

Creates a new builder from scratch

* returns
  * the result of invoking the `newBuilder` method of this factory.

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom)


### `def apply(from: Stream.Coll): Builder[A, Stream[A]]`                    ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * the result of invoking the `genericBuilder` method on `from` .

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.immutable.Stream.StreamCanBuildFrom
--------------------------------------------------------------------------------


### `new StreamCanBuildFrom()`                                               ###

(defined at scala.collection.immutable.Stream.StreamCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from StreamCanBuildFrom [A]
    to CollectionsHaveToParArray [StreamCanBuildFrom [A], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (StreamCanBuildFrom [A]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
