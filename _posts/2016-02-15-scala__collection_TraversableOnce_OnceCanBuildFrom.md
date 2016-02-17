
#              scala.collection.TraversableOnce.OnceCanBuildFrom              #

```scala
class OnceCanBuildFrom[A] extends BufferedCanBuildFrom[A, TraversableOnce]
```

With the advent of `TraversableOnce` , it can be useful to have a builder which
operates on `Iterator` s so they can be treated uniformly along with the
collections. See `scala.util.Random.shuffle` or
 `scala.concurrent.Future.sequence` for an example.

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


--------------------------------------------------------------------------------
    Value Members From scala.collection.TraversableOnce.BufferedCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[A, TraversableOnce[A]]`                            ###

Creates a new builder from scratch

* returns
  * the result of invoking the `newBuilder` method of this factory.

* Definition Classes
  * BufferedCanBuildFrom → CanBuildFrom

(defined at scala.collection.TraversableOnce.BufferedCanBuildFrom)


### `def apply(from: TraversableOnce[_]): Builder[A, TraversableOnce[A]]`    ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * the result of invoking the `genericBuilder` method on `from` .

* Definition Classes
  * BufferedCanBuildFrom → CanBuildFrom

(defined at scala.collection.TraversableOnce.BufferedCanBuildFrom)


### `def newIterator: Builder[A, TraversableOnce[A]]`                        ###

* Definition Classes
  * BufferedCanBuildFrom

(defined at scala.collection.TraversableOnce.BufferedCanBuildFrom)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.TraversableOnce.OnceCanBuildFrom
--------------------------------------------------------------------------------


### `new OnceCanBuildFrom()`                                                 ###

(defined at scala.collection.TraversableOnce.OnceCanBuildFrom)


--------------------------------------------------------------------------------
      Value Members From scala.collection.TraversableOnce.OnceCanBuildFrom
--------------------------------------------------------------------------------


### `def bufferToColl[B](buff: ArrayBuffer[B]): Iterator[B]`                 ###

* Definition Classes
  * OnceCanBuildFrom → BufferedCanBuildFrom

(defined at scala.collection.TraversableOnce.OnceCanBuildFrom)


### `def traversableToColl[B](t: GenTraversable[B]): Traversable[B]`         ###

* Definition Classes
  * OnceCanBuildFrom → BufferedCanBuildFrom
(defined at scala.collection.TraversableOnce.OnceCanBuildFrom)
