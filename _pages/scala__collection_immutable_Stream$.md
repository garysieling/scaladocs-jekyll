
#                      scala.collection.immutable.Stream                      #

```scala
object Stream extends SeqFactory[Stream] with Serializable
```

The object `Stream` provides helper functions to manipulate streams.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)
* Version
  * 1.1 08/08/03
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Stream[_]`                                                  ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `final class Cons[+A] extends Stream[A]`                                 ###

A lazy cons cell, from which streams are built.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


### `class ConsWrapper[A] extends AnyRef`                                    ###

A wrapper class that adds `#::` for cons and `#:::` for concat as operations to
streams.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

A generic implementation of the `CanBuildFrom` trait, which forwards all calls
to `apply(from)` to the `genericBuilder` method of collection `from` , and which
forwards all calls of `apply()` to the `newBuilder` method of this factory.

* Definition Classes
  * GenTraversableFactory


### `class StreamBuilder[A] extends LazyBuilder[A, Stream[A]]`               ###

A builder for streams

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)
* Note
  * This builder is lazy only in the sense that it does not go downs the spine
    of traversables that are added as a whole. If more laziness can be achieved,
    this builder should be bypassed.


### `class StreamCanBuildFrom[A] extends GenericCanBuildFrom[A]`             ###

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
                                 Value Members
--------------------------------------------------------------------------------


### `object #::`                                                             ###

An extractor that allows to pattern match streams with `#::` .

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


### `object Empty extends Stream[Nothing]`                                   ###

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


### `object cons`                                                            ###

An alternative way of building and matching Streams using Stream.cons(hd, tl).

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


--------------------------------------------------------------------------------
       Value Members From scala.collection.generic.GenTraversableFactory
--------------------------------------------------------------------------------


### `def ReusableCBF: GenericCanBuildFrom[Nothing]`                          ###

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def concat[A](xss: collection.Traversable[A]*): Stream[A]`              ###

Concatenates all argument collections into a single collection.

* xss
  * the collections that are to be concatenated.
* returns
  * the concatenation of all the collections.

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int)(elem: ⇒ A): Stream[Stream[A]]`            ###

Produces a two-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2` evaluations of `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int)(elem: ⇒ A): Stream[Stream[Stream[A]]]` ###

Produces a three-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3` evaluations of
     `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int, n4: Int)(elem: ⇒ A): Stream[Stream[Stream[Stream[A]]]]` ###

Produces a four-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3 x n4` evaluations of
     `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(elem: ⇒ A): Stream[Stream[Stream[Stream[Stream[A]]]]]` ###

Produces a five-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* n5
  * the number of elements in the 5th dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3 x n4 x n5`
    evaluations of `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def range[T](start: T, end: T)(implicit arg0: Integral[T]): Stream[T]`  ###

Produces a collection containing a sequence of increasing of integers.

* start
  * the first element of the collection
* end
  * the end value of the collection (the first value NOT contained)
* returns
  * a collection with values `start, start + 1, ..., end - 1`

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int)(f: (Int, Int) ⇒ A): Stream[Stream[A]]` ###

Produces a two-dimensional collection containing values of a given function over
ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2)` for `0 <= i1 < n1` and
     `0 <= i2 < n2` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int)(f: (Int, Int, Int) ⇒ A): Stream[Stream[Stream[A]]]` ###

Produces a three-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3)` for `0 <= i1 < n1` ,
     `0 <= i2 < n2` , and `0 <= i3 < n3` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int, n4: Int)(f: (Int, Int, Int, Int) ⇒ A): Stream[Stream[Stream[Stream[A]]]]` ###

Produces a four-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3, i4)` for `0 <= i1 < n1` ,
     `0 <= i2 < n2` , `0 <= i3 < n3` , and `0 <= i4 < n4` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(f: (Int, Int, Int, Int, Int) ⇒ A): Stream[Stream[Stream[Stream[Stream[A]]]]]` ###

Produces a five-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* n5
  * the number of elements in the 5th dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3, i4, i5)` for
     `0 <= i1 < n1` , `0 <= i2 < n2` , `0 <= i3 < n3` , `0 <= i4 < n4` , and
     `0 <= i5 < n5` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.generic.SeqFactory
--------------------------------------------------------------------------------


### `def unapplySeq[A](x: Stream[A]): Some[Stream[A]]`                       ###

This method is called in a pattern match { case Seq(...) => }.

* x
  * the selector value
* returns
  * sequence wrapped in an option, if this is a Seq, otherwise none

* Definition Classes
  * SeqFactory

(defined at scala.collection.generic.SeqFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.immutable.Stream
--------------------------------------------------------------------------------


### `def apply[A](xs: A*): Stream[A]`                                        ###

A stream consisting of given elements

* A
  * the type of the collection's elements
* returns
  * a new collection with elements `elems`

* Definition Classes
  * Stream → GenericCompanion

(defined at scala.collection.immutable.Stream)


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, Stream[A]]`         ###

(defined at scala.collection.immutable.Stream)


### `implicit def consWrapper[A](stream: ⇒ Stream[A]): ConsWrapper[A]`       ###

A wrapper method that adds `#::` for cons and `#:::` for concat as operations to
streams.

(defined at scala.collection.immutable.Stream)


### `def continually[A](elem: ⇒ A): Stream[A]`                               ###

Create an infinite stream containing the given element expression (which is
computed for each occurrence).

* elem
  * the element composing the resulting stream
* returns
  * the stream containing an infinite number of elem

(defined at scala.collection.immutable.Stream)


### `def empty[A]: Stream[A]`                                                ###

The empty stream

* A
  * the type of the collection's elements

* Definition Classes
  * Stream → GenericCompanion

(defined at scala.collection.immutable.Stream)


### `def fill[A](n: Int)(elem: ⇒ A): Stream[A]`                              ###

Produces a collection containing the results of some element computation a
number of times.

* n
  * the number of elements contained in the collection.
* elem
  * the element computation
* returns
  * A collection that contains the results of `n` evaluations of `elem` .

* Definition Classes
  * Stream → GenTraversableFactory

(defined at scala.collection.immutable.Stream)


### `def from(start: Int): Stream[Int]`                                      ###

Create an infinite stream starting at `start` and incrementing by `1` .

* start
  * the start value of the stream
* returns
  * the stream starting at value `start` .

(defined at scala.collection.immutable.Stream)


### `def from(start: Int, step: Int): Stream[Int]`                           ###

Create an infinite stream starting at `start` and incrementing by step `step` .

* start
  * the start value of the stream
* step
  * the increment value of the stream
* returns
  * the stream starting at value `start` .

(defined at scala.collection.immutable.Stream)


### `def iterate[A](start: A)(f: (A) ⇒ A): Stream[A]`                        ###

An infinite stream that repeatedly applies a given function to a start value.

* start
  * the start value of the stream
* f
  * the function that's repeatedly applied
* returns
  * the stream returning the infinite sequence of values
     `start, f(start), f(f(start)), ...`

(defined at scala.collection.immutable.Stream)


### `def iterate[A](start: A, len: Int)(f: (A) ⇒ A): Stream[A]`              ###

Produces a collection containing repeated applications of a function to a start
value.

* start
  * the start value of the collection
* len
  * the number of elements contained inthe collection
* f
  * the function that's repeatedly applied
* returns
  * a collection with `len` values in the sequence
     `start, f(start), f(f(start)), ...`

* Definition Classes
  * Stream → GenTraversableFactory

(defined at scala.collection.immutable.Stream)


### `def newBuilder[A]: Builder[A, Stream[A]]`                               ###

Creates a new builder for a stream

* A
  * the type of the collection's elements

* Definition Classes
  * Stream → GenericCompanion

(defined at scala.collection.immutable.Stream)


### `def range[T](start: T, end: T, step: T)(implicit arg0: Integral[T]): Stream[T]` ###

Produces a collection containing equally spaced values in some integer interval.

* start
  * the start value of the collection
* end
  * the end value of the collection (the first value NOT contained)
* step
  * the difference between successive elements of the collection (must be
    positive or negative)
* returns
  * a collection with values `start, start + step, ...` up to, but excluding
     `end`

* Definition Classes
  * Stream → GenTraversableFactory

(defined at scala.collection.immutable.Stream)


### `def tabulate[A](n: Int)(f: (Int) ⇒ A): Stream[A]`                       ###

Produces a collection containing values of a given function over a range of
integer values starting from 0.

* n
  * The number of elements in the collection
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(0), ..., f(n -1)`

* Definition Classes
  * Stream → GenTraversableFactory
(defined at scala.collection.immutable.Stream)
