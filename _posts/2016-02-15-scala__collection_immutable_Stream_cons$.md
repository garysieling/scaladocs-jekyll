
#                    scala.collection.immutable.Stream.cons                    #

```scala
object cons
```

An alternative way of building and matching Streams using Stream.cons(hd, tl).

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.immutable.Stream.cons
--------------------------------------------------------------------------------


### `def apply[A](hd: A, tl: ⇒ Stream[A]): Cons[A]`                          ###

A stream consisting of a given first element and remaining elements

* hd
  * The first element of the result stream
* tl
  * The remaining elements of the result stream

(defined at scala.collection.immutable.Stream.cons)


### `def unapply[A](xs: Stream[A]): Option[(A, Stream[A])]`                  ###

Maps a stream to its head and tail
(defined at scala.collection.immutable.Stream.cons)
