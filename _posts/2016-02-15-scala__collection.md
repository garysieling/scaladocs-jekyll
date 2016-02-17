
#                               scala.collection                               #

```scala
package collection
```

Contains the base traits and objects needed to use and extend Scala's collection
library.

### Guide

A detailed guide for using the collections library is available at
[http://docs.scala-lang.org/overviews/collections/introduction.html](http://docs.scala-lang.org/overviews/collections/introduction.html).
Developers looking to extend the collections library can find a description of
its architecture at
[http://docs.scala-lang.org/overviews/core/architecture-of-scala-collections.html](http://docs.scala-lang.org/overviews/core/architecture-of-scala-collections.html).

### Using Collections

It is convenient to treat all collections as either a
scala.collection.Traversable or scala.collection.Iterable, as these traits
define the vast majority of operations on a collection.

Collections can, of course, be treated as specifically as needed, and the
library is designed to ensure that the methods that transform collections will
return a collection of the same type:

```scala
scala> val array = Array(1,2,3,4,5,6)
array: Array[Int] = Array(1, 2, 3, 4, 5, 6)

scala> array map { _.toString }
res0: Array[String] = Array(1, 2, 3, 4, 5, 6)

scala> val list = List(1,2,3,4,5,6)
list: List[Int] = List(1, 2, 3, 4, 5, 6)

scala> list map { _.toString }
res1: List[String] = List(1, 2, 3, 4, 5, 6)
```

### Creating Collections

The most common way to create a collection is to use its companion object as a
factory. The three most commonly used collections are scala.collection.Seq,
scala.collection.immutable.Set, and scala.collection.immutable.Map. They can be
used directly as shown below since their companion objects are all available as
type aliases in either the scala package or in `scala.Predef` . New collections
are created like this:

```scala
scala> val seq = Seq(1,2,3,4,1)
seq: Seq[Int] = List(1, 2, 3, 4, 1)

scala> val set = Set(1,2,3,4,1)
set: scala.collection.immutable.Set[Int] = Set(1, 2, 3, 4)

scala> val map = Map(1 -> "one", 2 -> "two", 3 -> "three", 2 -> "too")
map: scala.collection.immutable.Map[Int,String] = Map(1 -> one, 2 -> too, 3 -> three)
```

It is also typical to prefer the scala.collection.immutable collections over
those in scala.collection.mutable; the types aliased in the `scala.Predef`
object are the immutable versions.

Also note that the collections library was carefully designed to include several
implementations of each of the three basic collection types. These
implementations have specific performance characteristics which are described in
[the guide](http://docs.scala-lang.org/overviews/collections/performance-characteristics.html).

The concrete parallel collections also have specific performance characteristics
which are described in
[the parallel collections guide](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#performance-characteristics)

### Converting between Java Collections

The scala.collection.JavaConversions object provides implicit defs that will
allow mostly seamless integration between APIs using Java Collections and the
Scala collections library.

Alternatively the scala.collection.JavaConverters object provides a collection
of decorators that allow converting between Scala and Java collections using
 `asScala` and `asJava` methods.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class AbstractIterable[+A] extends AbstractTraversable[A] with Iterable[A]` ###

Explicit instantiation of the `Iterable` trait to reduce class file size in
subclasses.

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterable.scala#L1)


### `abstract class AbstractIterator[+A] extends Iterator[A]`                ###

Explicit instantiation of the `Iterator` trait to reduce class file size in
subclasses.

* Source
  * [Iterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterator.scala#L1)


### `abstract class AbstractMap[A, +B] extends AbstractIterable[(A, B)] with Map[A, B]` ###

Explicit instantiation of the `Map` trait to reduce class file size in
subclasses.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Map.scala#L1)


### `abstract class AbstractSeq[+A] extends AbstractIterable[A] with Seq[A]` ###

Explicit instantiation of the `Seq` trait to reduce class file size in
subclasses.

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Seq.scala#L1)


### `abstract class AbstractSet[A] extends AbstractIterable[A] with Set[A]`  ###

Explicit instantiation of the `Set` trait to reduce class file size in
subclasses.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Set.scala#L1)


### `abstract class AbstractTraversable[+A] extends Traversable[A]`          ###

Explicit instantiation of the `Traversable` trait to reduce class file size in
subclasses.

* Source
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Traversable.scala#L1)


### `trait BitSet extends SortedSet[Int] with BitSetLike[BitSet]`            ###

A common base class for mutable and immutable bitsets.

Bitsets are sets of non-negative integers which are represented as variable-size
arrays of bits packed into 64-bit words. The memory footprint of a bitset is
determined by the largest number stored in it.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BitSet.scala#L1)


### `trait BitSetLike[+This <: BitSetLike[This] with SortedSet[Int]] extends SortedSetLike[Int, This]` ###

A template trait for bitsets.

Bitsets are sets of non-negative integers which are represented as variable-size
arrays of bits packed into 64-bit words. The memory footprint of a bitset is
determined by the largest number stored in it.

This trait provides most of the operations of a `BitSet` independently of its
representation. It is inherited by all concrete implementations of bitsets.

* This
  * the type of the bitset itself.

* Self Type
  * BitSetLike [This]
* Source
  * [BitSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BitSetLike.scala#L1)


### `trait BufferedIterator[+A] extends Iterator[A]`                         ###

Buffered iterators are iterators which provide a method `head` that inspects the
next element without discarding it.

* Source
  * [BufferedIterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BufferedIterator.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait CustomParallelizable[+A, +ParRepr <: Parallel] extends Parallelizable[A, ParRepr]` ###

* Source
  * [CustomParallelizable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/CustomParallelizable.scala#L1)


### `trait DefaultMap[A, +B] extends Map[A, B]`                              ###

A default map which implements the `+` and `-` methods of maps.

Instances that inherit from `DefaultMap[A, B]` still have to define:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
```

It refers back to the original map.

It might also be advisable to override `foreach` or `size` if efficient
implementations can be found.

* Self Type
  * DefaultMap [A, B]
* Source
  * [DefaultMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/DefaultMap.scala#L1)
* Since
  * 2.8


### `trait GenIterable[+A] extends GenIterableLike[A, GenIterable[A]] with GenTraversable[A] with GenericTraversableTemplate[A, GenIterable]` ###

A trait for all iterable collections which may possibly have their operations
implemented in parallel.

* Source
  * [GenIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenIterable.scala#L1)
* Since
  * 2.9


### `trait GenIterableLike[+A, +Repr] extends GenTraversableLike[A, Repr]`   ###

A template trait for all iterable collections which may possibly have their
operations implemented in parallel.

This trait contains abstract methods and methods that can be implemented
directly in terms of other methods.

* Source
  * [GenIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenIterableLike.scala#L1)


### `trait GenMap[A, +B] extends GenMapLike[A, B, GenMap[A, B]] with GenIterable[(A, B)]` ###

A trait for all traversable collections which may possibly have their operations
implemented in parallel.

* Source
  * [GenMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenMap.scala#L1)
* Since
  * 2.9


### `trait GenMapLike[A, +B, +Repr] extends GenIterableLike[(A, B), Repr] with Equals with Parallelizable[(A, B), ParMap[A, B]]` ###

A trait for all maps upon which operations may be implemented in parallel.

* Source
  * [GenMapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenMapLike.scala#L1)


### `trait GenSeq[+A] extends GenSeqLike[A, GenSeq[A]] with GenIterable[A] with Equals with GenericTraversableTemplate[A, GenSeq]` ###

A trait for all sequences which may possibly have their operations implemented
in parallel.

* Source
  * [GenSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSeq.scala#L1)
* Since
  * 2.9


### `trait GenSeqLike[+A, +Repr] extends GenIterableLike[A, Repr] with Equals with Parallelizable[A, ParSeq[A]]` ###

A template trait for all sequences which may be traversed in parallel.

* Source
  * [GenSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSeqLike.scala#L1)


### `trait GenSet[A] extends GenSetLike[A, GenSet[A]] with GenIterable[A] with GenericSetTemplate[A, GenSet]` ###

A trait for sets which may possibly have their operations implemented in
parallel.

* Source
  * [GenSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSet.scala#L1)
* Since
  * 2.9


### `trait GenSetLike[A, +Repr] extends GenIterableLike[A, Repr] with (A) ⇒ Boolean with Equals with Parallelizable[A, ParSet[A]]` ###

A template trait for sets which may possibly have their operations implemented
in parallel.

* Source
  * [GenSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSetLike.scala#L1)


### `trait GenTraversable[+A] extends GenTraversableLike[A, GenTraversable[A]] with GenTraversableOnce[A] with GenericTraversableTemplate[A, GenTraversable]` ###

A trait for all traversable collections which may possibly have their operations
implemented in parallel.

* Source
  * [GenTraversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenTraversable.scala#L1)
* Since
  * 2.9


### `trait GenTraversableLike[+A, +Repr] extends GenTraversableOnce[A] with Parallelizable[A, ParIterable[A]]` ###

A template trait for all traversable collections upon which operations may be
implemented in parallel.

* Source
  * [GenTraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenTraversableLike.scala#L1)


### `trait GenTraversableOnce[+A] extends Any`                               ###

A template trait for all traversable-once objects which may be traversed in
parallel.

Methods in this trait are either abstract or can be implemented in terms of
other methods.

* Source
  * [GenTraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenTraversableOnce.scala#L1)


### `trait IndexedSeq[+A] extends Seq[A] with GenericTraversableTemplate[A, IndexedSeq] with IndexedSeqLike[A, IndexedSeq[A]]` ###

A base trait for indexed sequences.

Indexed sequences support constant-time or near constant-time element access and
length computation. They are defined in terms of abstract methods `apply` for
indexing and `length` .

Indexed sequences do not add any new methods to `Seq` , but promise efficient
implementations of random access patterns.

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IndexedSeq.scala#L1)


### `trait IndexedSeqLike[+A, +Repr] extends SeqLike[A, Repr]`               ###

A template trait for indexed sequences of type `IndexedSeq[A]` .

Indexed sequences support constant-time or near constant-time element access and
length computation. They are defined in terms of abstract methods `apply` for
indexing and `length` .

Indexed sequences do not add any new methods to `Seq` , but promise efficient
implementations of random access patterns.

This trait just implements `iterator` in terms of `apply` and `length` .
However, see `IndexedSeqOptimized` for an implementation trait that overrides
operations to make them run faster under the assumption of fast random access
with `apply` .

* Self Type
  * IndexedSeqLike [A, Repr]
* Source
  * [IndexedSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IndexedSeqLike.scala#L1)


### `trait IndexedSeqOptimized[+A, +Repr] extends IndexedSeqLike[A, Repr]`   ###

A template trait for indexed sequences of type `IndexedSeq[A]` which optimizes
the implementation of several methods under the assumption of fast random
access.

Indexed sequences support constant-time or near constant-time element access and
length computation. They are defined in terms of abstract methods `apply` for
indexing and `length` .

Indexed sequences do not add any new methods to `Seq` , but promise efficient
implementations of random access patterns.

* Self Type
  * IndexedSeqOptimized [A, Repr]
* Source
  * [IndexedSeqOptimized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IndexedSeqOptimized.scala#L1)


### `trait Iterable[+A] extends Traversable[A] with GenIterable[A] with GenericTraversableTemplate[A, Iterable] with IterableLike[A, Iterable[A]]` ###

A base trait for iterable collections.

This is a base trait for all Scala collections that define an `iterator` method
to step through one-by-one the collection's elements. Implementations of this
trait need to provide a concrete method with signature:

```scala
def iterator: Iterator[A]
```

They also need to provide a method `newBuilder` which creates a builder for
collections of the same kind.

This trait implements `Iterable` 's `foreach` method by stepping through all
elements using `iterator` . Subclasses should re-implement `foreach` with
something more efficient, if possible.

This trait adds methods `iterator` , `sameElements` , `takeRight` , `dropRight`
to the methods inherited from trait `Traversable`.

Note: This trait replaces every method that uses `break` in `TraversableLike` by
an iterator version.

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterable.scala#L1)


### `trait IterableLike[+A, +Repr] extends Equals with TraversableLike[A, Repr] with GenIterableLike[A, Repr]` ###

A template trait for iterable collections of type `Iterable[A]` .

This is a base trait for all Scala collections that define an `iterator` method
to step through one-by-one the collection's elements. Implementations of this
trait need to provide a concrete method with signature:

```scala
def iterator: Iterator[A]
```

They also need to provide a method `newBuilder` which creates a builder for
collections of the same kind.

This trait implements `Iterable` 's `foreach` method by stepping through all
elements using `iterator` . Subclasses should re-implement `foreach` with
something more efficient, if possible.

This trait adds methods `iterator` , `sameElements` , `takeRight` , `dropRight`
to the methods inherited from trait `Traversable`.

Note: This trait replaces every method that uses `break` in `TraversableLike` by
an iterator version.

* Self Type
  * IterableLike [A, Repr]
* Source
  * [IterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableLike.scala#L1)


### `trait IterableProxy[+A] extends Iterable[A] with IterableProxyLike[A, Iterable[A]]` ###

This trait implements a proxy for iterable objects. It forwards all calls to a
different iterable object.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.3)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [IterableProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableProxy.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait IterableProxyLike[+A, +Repr <: IterableLike[A, Repr] with Iterable[A]] extends IterableLike[A, Repr] with TraversableProxyLike[A, Repr]` ###

This trait implements a proxy for Iterable objects. It forwards all calls to a
different Iterable object.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [IterableProxyLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableProxyLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait IterableView[+A, +Coll] extends IterableViewLike[A, Coll, IterableView[A, Coll]]` ###

A base trait for non-strict views of `Iterable` s.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view. All views for iterable collections are defined by
re-interpreting the `iterator` method.

* Source
  * [IterableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableView.scala#L1)


### `trait IterableViewLike[+A, +Coll, +This <: IterableView[A, Coll] with IterableViewLike[A, Coll, This]] extends Iterable[A] with IterableLike[A, This] with TraversableView[A, Coll] with TraversableViewLike[A, Coll, This]` ###

A template trait for non-strict views of iterable collections.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view. All views for iterable collections are defined by
re-interpreting the `iterator` method.

* Self Type
  * IterableViewLike [A, Coll, This]
* Source
  * [IterableViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableViewLike.scala#L1)


### `trait Iterator[+A] extends TraversableOnce[A]`                          ###

Iterators are data structures that allow to iterate over a sequence of elements.
They have a `hasNext` method for checking if there is a next element available,
and a `next` method which returns the next element and discards it from the
iterator.

An iterator is mutable: most operations on it change its state. While it is
often used to iterate through the elements of a collection, it can also be used
without being backed by any collection (see constructors on the companion
object).

It is of particular importance to note that, unless stated otherwise, _one
should never use an iterator after calling a method on it_ . The two most
important exceptions are also the sole abstract methods: `next` and `hasNext` .

Both these methods can be called any number of times without having to discard
the iterator. Note that even `hasNext` may cause mutation -- such as when
iterating from an input stream, where it will block until the stream is closed
or some input becomes available.

Consider this example for safe and unsafe use:

```scala
def f[A](it: Iterator[A]) = {
  if (it.hasNext) {            // Safe to reuse "it" after "hasNext"
    it.next                    // Safe to reuse "it" after "next"
    val remainder = it.drop(2) // it is *not* safe to use "it" again after this line!
    remainder.take(2)          // it is *not* safe to use "remainder" after this line!
  } else it
}
```

* Self Type
  * Iterator [A]
* Source
  * [Iterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterator.scala#L1)
* Version
  * 2.8
* Since
  * 1


### `trait LinearSeq[+A] extends Seq[A] with GenericTraversableTemplate[A, LinearSeq] with LinearSeqLike[A, LinearSeq[A]]` ###

A base trait for linear sequences.

Linear sequences have reasonably efficient `head` , `tail` , and `isEmpty`
methods. If these methods provide the fastest way to traverse the collection, a
collection `Coll` that extends this trait should also extend
 `LinearSeqOptimized[A, Coll[A]]` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/LinearSeq.scala#L1)


### `trait LinearSeqLike[+A, +Repr <: LinearSeqLike[A, Repr]] extends SeqLike[A, Repr]` ###

A template trait for linear sequences of type `LinearSeq[A]` .

This trait just implements `iterator` and `corresponds` in terms of `isEmpty,`
 `head` , and `tail` . However, see `LinearSeqOptimized` for an implementation
trait that overrides many more operations to make them run faster under the
assumption of fast linear access with `head` and `tail` .

Linear sequences do not add any new methods to `Seq` , but promise efficient
implementations of linear access patterns.

* A
  * the element type of the sequence
* Repr
  * the type of the actual sequence containing the elements.

* Self Type
  * Repr
* Source
  * [LinearSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/LinearSeqLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait LinearSeqOptimized[+A, +Repr <: LinearSeqOptimized[A, Repr]] extends LinearSeqLike[A, Repr]` ###

A template trait for linear sequences of type `LinearSeq[A]` which optimizes the
implementation of various methods under the assumption of fast linear access.

Linear-optimized sequences implement most operations in in terms of three
methods, which are assumed to have efficient implementations. These are:

```scala
def isEmpty: Boolean
def head: A
def tail: Repr
```

Here, `A` is the type of the sequence elements and `Repr` is the type of the
sequence itself. Note that default implementations are provided via inheritance,
but these should be overridden for performance.

* Self Type
  * Repr
* Source
  * [LinearSeqOptimized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/LinearSeqOptimized.scala#L1)


### `trait Map[A, +B] extends Iterable[(A, B)] with GenMap[A, B] with MapLike[A, B, Map[A, B]]` ###

A map from keys of type `A` to values of type `B` .

 *Implementation note:* This trait provides most of the operations of a `Map`
independently of its representation. It is typically inherited by concrete
implementations of maps.

To implement a concrete map, you need to provide implementations of the
following methods:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def + [B1 >: B](kv: (A, B1)): This
def -(key: A): This
```

If you wish that methods like `take` , `drop` , `filter` also return the same
kind of map you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

 *Note:* If you do not have specific implementations for `add` and `-` in mind,
you might consider inheriting from `DefaultMap` instead.

 *Note:* If your additions and mutations return the same kind of map as the map
you are defining, you should inherit from `MapLike` as well.

* A
  * the type of the keys in this map.
* B
  * the type of the values associated with keys.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Map.scala#L1)
* Since
  * 1.0


### `trait MapLike[A, +B, +This <: MapLike[A, B, This] with Map[A, B]] extends PartialFunction[A, B] with IterableLike[(A, B), This] with GenMapLike[A, B, This] with Subtractable[A, This] with Parallelizable[(A, B), ParMap[A, B]]` ###

A template trait for maps, which associate keys with values.

 *Implementation note:* This trait provides most of the operations of a `Map`
independently of its representation. It is typically inherited by concrete
implementations of maps.

To implement a concrete map, you need to provide implementations of the
following methods:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def + [B1 >: B](kv: (A, B1)): This
def -(key: A): This
```

If you wish that methods like `take` , `drop` , `filter` also return the same
kind of map you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* Self Type
  * MapLike [A, B, This]
* Source
  * [MapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/MapLike.scala#L1)
* Since
  * 2.8


### `trait MapProxy[A, +B] extends Map[A, B] with MapProxyLike[A, B, Map[A, B]]` ###

This is a simple wrapper class for scala.collection.Map. It is most useful for
assembling customized map abstractions dynamically using object composition and
forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.3)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [MapProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/MapProxy.scala#L1)
* Version
  * 1.0, 21/07/2003
* Since
  * 1


### `trait MapProxyLike[A, +B, +This <: MapLike[A, B, This] with Map[A, B]] extends MapLike[A, B, This] with IterableProxyLike[(A, B), This]` ###

This trait implements a proxy for Map objects. It forwards all calls to a
different Map object.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [MapProxyLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/MapProxyLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait Parallel extends AnyRef`                                          ###

A marker trait for collections which have their operations parallelised.

* Source
  * [Parallel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Parallel.scala#L1)
* Since
  * 2.9


### `trait Parallelizable[+A, +ParRepr <: Parallel] extends Any`             ###

This trait describes collections which can be turned into parallel collections
by invoking the method `par` . Parallelizable collections may be parametrized
with a target type different than their own.

* A
  * the type of the elements in the collection
* ParRepr
  * the actual type of the collection, which has to be parallel

* Source
  * [Parallelizable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Parallelizable.scala#L1)


### `trait Seq[+A] extends PartialFunction[Int, A] with Iterable[A] with GenSeq[A] with GenericTraversableTemplate[A, Seq] with SeqLike[A, Seq[A]]` ###

A base trait for sequences.

Sequences are special cases of iterable collections of class `Iterable` . Unlike
iterables, sequences always have a defined order of elements. Sequences provide
a method `apply` for indexing. Indices range from `0` up to the `length` of a
sequence. Sequences support a number of methods to find occurrences of elements
or subsequences, including `segmentLength` , `prefixLength` , `indexWhere` ,
 `indexOf` , `lastIndexWhere` , `lastIndexOf` , `startsWith` , `endsWith` ,
 `indexOfSlice` .

Another way to see a sequence is as a `PartialFunction` from `Int` values to the
element type of the sequence. The `isDefinedAt` method of a sequence returns
 `true` for the interval from `0` until `length` .

Sequences can be accessed in reverse order of their elements, using methods
 `reverse` and `reverseIterator` .

Sequences have two principal subtraits, `IndexedSeq` and `LinearSeq` , which
give different guarantees for performance. An `IndexedSeq` provides fast
random-access of elements and a fast `length` operation. A `LinearSeq` provides
fast access only to the first element via `head` , but also has a fast `tail`
operation.

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Seq.scala#L1)


### `trait SeqLike[+A, +Repr] extends IterableLike[A, Repr] with GenSeqLike[A, Repr] with Parallelizable[A, ParSeq[A]]` ###

A template trait for sequences of type `Seq[A]`

Sequences are special cases of iterable collections of class `Iterable` . Unlike
iterables, sequences always have a defined order of elements. Sequences provide
a method `apply` for indexing. Indices range from `0` up to the `length` of a
sequence. Sequences support a number of methods to find occurrences of elements
or subsequences, including `segmentLength` , `prefixLength` , `indexWhere` ,
 `indexOf` , `lastIndexWhere` , `lastIndexOf` , `startsWith` , `endsWith` ,
 `indexOfSlice` .

Another way to see a sequence is as a `PartialFunction` from `Int` values to the
element type of the sequence. The `isDefinedAt` method of a sequence returns
 `true` for the interval from `0` until `length` .

Sequences can be accessed in reverse order of their elements, using methods
 `reverse` and `reverseIterator` .

Sequences have two principal subtraits, `IndexedSeq` and `LinearSeq` , which
give different guarantees for performance. An `IndexedSeq` provides fast
random-access of elements and a fast `length` operation. A `LinearSeq` provides
fast access only to the first element via `head` , but also has a fast `tail`
operation.

* Self Type
  * SeqLike [A, Repr]
* Source
  * [SeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqLike.scala#L1)


### `trait SeqProxy[+A] extends Seq[A] with SeqProxyLike[A, Seq[A]]`         ###

This trait implements a proxy for sequence objects. It forwards all calls to a
different sequence object.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SeqProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqProxy.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait SeqProxyLike[+A, +Repr <: SeqLike[A, Repr] with Seq[A]] extends SeqLike[A, Repr] with IterableProxyLike[A, Repr]` ###

This trait implements a proxy for sequences. It forwards all calls to a
different sequence.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SeqProxyLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqProxyLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait SeqView[+A, +Coll] extends SeqViewLike[A, Coll, SeqView[A, Coll]]` ###

A base trait for non-strict views of sequences.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view. All views for sequences are defined by
re-interpreting the `length` and `apply` methods.

* Source
  * [SeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqView.scala#L1)


### `trait SeqViewLike[+A, +Coll, +This <: SeqView[A, Coll] with SeqViewLike[A, Coll, This]] extends Seq[A] with SeqLike[A, This] with IterableView[A, Coll] with IterableViewLike[A, Coll, This]` ###

A template trait for non-strict views of sequences.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view. All views for sequences are defined by
re-interpreting the `length` and `apply` methods.

* Self Type
  * SeqViewLike [A, Coll, This]
* Source
  * [SeqViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqViewLike.scala#L1)


### `trait Set[A] extends (A) ⇒ Boolean with Iterable[A] with GenSet[A] with GenericSetTemplate[A, Set] with SetLike[A, Set[A]]` ###

A base trait for all sets, mutable as well as immutable.

A set is a collection that contains no duplicate elements.

To implement a concrete set, you need to provide implementations of the
following methods:

```scala
def contains(key: A): Boolean
def iterator: Iterator[A]
def +(elem: A): This
def -(elem: A): This
```

If you wish that methods like `take` , `drop` , `filter` return the same kind of
set, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

 *Implementation note:* If your additions and mutations return the same kind of
set as the set you are defining, you should inherit from `SetLike` as well.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Set.scala#L1)
* Since
  * 1.0


### `trait SetLike[A, +This <: SetLike[A, This] with Set[A]] extends IterableLike[A, This] with GenSetLike[A, This] with Subtractable[A, This] with Parallelizable[A, ParSet[A]]` ###

A template trait for sets.

A set is a collection that contains no duplicate elements.

To implement a concrete set, you need to provide implementations of the
following methods:

```scala
def contains(key: A): Boolean
def iterator: Iterator[A]
def +(elem: A): This
def -(elem: A): This
```

If you wish that methods like `take` , `drop` , `filter` return the same kind of
set, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

 *Implementation note:* This trait provides most of the operations of a `Set`
independently of its representation. It is typically inherited by concrete
implementations of sets.

* Self Type
  * SetLike [A, This]
* Source
  * [SetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SetLike.scala#L1)
* Since
  * 2.8


### `trait SetProxy[A] extends Set[A] with SetProxyLike[A, Set[A]]`          ###

This is a simple wrapper class for scala.collection.Set. It is most useful for
assembling customized set abstractions dynamically using object composition and
forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.3)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SetProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SetProxy.scala#L1)
* Version
  * 2.0, 01/01/2007


### `trait SetProxyLike[A, +This <: SetLike[A, This] with Set[A]] extends SetLike[A, This] with IterableProxyLike[A, This]` ###

This trait implements a proxy for sets. It forwards all calls to a different
set.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SetProxyLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SetProxyLike.scala#L1)
* Version
  * 2.8


### `trait SortedMap[A, +B] extends Map[A, B] with SortedMapLike[A, B, SortedMap[A, B]]` ###

A map whose keys are sorted.

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedMap.scala#L1)
* Version
  * 2.8
* Since
  * 2.4


### `trait SortedMapLike[A, +B, +This <: SortedMapLike[A, B, This] with SortedMap[A, B]] extends Sorted[A, This] with MapLike[A, B, This]` ###

A template for maps whose keys are sorted. To create a concrete sorted map, you
need to implement the rangeImpl method, in addition to those of `MapLike` .

* Self Type
  * SortedMapLike [A, B, This]
* Source
  * [SortedMapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedMapLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait SortedSet[A] extends Set[A] with SortedSetLike[A, SortedSet[A]]`  ###

A sorted set.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedSet.scala#L1)
* Version
  * 2.8
* Since
  * 2.4


### `trait SortedSetLike[A, +This <: SortedSet[A] with SortedSetLike[A, This]] extends Sorted[A, This] with SetLike[A, This]` ###

A template for sets which are sorted.

* Self Type
  * SortedSetLike [A, This]
* Source
  * [SortedSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedSetLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait Traversable[+A] extends TraversableLike[A, Traversable[A]] with GenTraversable[A] with TraversableOnce[A] with GenericTraversableTemplate[A, Traversable]` ###

A trait for traversable collections. All operations are guaranteed to be
performed in a single-threaded manner.

This is a base trait of all kinds of Scala collections. It implements the
behavior common to all collections, in terms of a method `foreach` with
signature:

```scala
def foreach[U](f: Elem => U): Unit
```

Collection classes mixing in this trait provide a concrete `foreach` method
which traverses all the elements contained in the collection, applying a given
function to each. They also need to provide a method `newBuilder` which creates
a builder for collections of the same kind.

A traversable class might or might not have two properties: strictness and
orderedness. Neither is represented as a type.

The instances of a strict collection class have all their elements computed
before they can be used as values. By contrast, instances of a non-strict
collection class may defer computation of some of their elements until after the
instance is available as a value. A typical example of a non-strict collection
class is a scala.collection.immutable.Stream. A more general class of examples
are `TraversableViews` .

If a collection is an instance of an ordered collection class, traversing its
elements with `foreach` will always visit elements in the same order, even for
different runs of the program. If the class is not ordered, `foreach` can visit
elements in different orders for different runs (but it will keep the same order
in the same run).'

A typical example of a collection class which is not ordered is a `HashMap` of
objects. The traversal order for hash maps will depend on the hash codes of its
elements, and these hash codes might differ from one run to the next. By
contrast, a `LinkedHashMap` is ordered because its `foreach` method visits
elements in the order they were inserted into the `HashMap` .

* Source
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Traversable.scala#L1)


### `trait TraversableLike[+A, +Repr] extends HasNewBuilder[A, Repr] with FilterMonadic[A, Repr] with TraversableOnce[A] with GenTraversableLike[A, Repr] with Parallelizable[A, ParIterable[A]]` ###

A template trait for traversable collections of type `Traversable[A]` .

This is a base trait of all kinds of Scala collections. It implements the
behavior common to all collections, in terms of a method `foreach` with
signature:

```scala
def foreach[U](f: Elem => U): Unit
```

Collection classes mixing in this trait provide a concrete `foreach` method
which traverses all the elements contained in the collection, applying a given
function to each. They also need to provide a method `newBuilder` which creates
a builder for collections of the same kind.

A traversable class might or might not have two properties: strictness and
orderedness. Neither is represented as a type.

The instances of a strict collection class have all their elements computed
before they can be used as values. By contrast, instances of a non-strict
collection class may defer computation of some of their elements until after the
instance is available as a value. A typical example of a non-strict collection
class is a scala.collection.immutable.Stream. A more general class of examples
are `TraversableViews` .

If a collection is an instance of an ordered collection class, traversing its
elements with `foreach` will always visit elements in the same order, even for
different runs of the program. If the class is not ordered, `foreach` can visit
elements in different orders for different runs (but it will keep the same order
in the same run).'

A typical example of a collection class which is not ordered is a `HashMap` of
objects. The traversal order for hash maps will depend on the hash codes of its
elements, and these hash codes might differ from one run to the next. By
contrast, a `LinkedHashMap` is ordered because its `foreach` method visits
elements in the order they were inserted into the `HashMap` .

* Self Type
  * TraversableLike [A, Repr]
* Source
  * [TraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableLike.scala#L1)


### `trait TraversableOnce[+A] extends GenTraversableOnce[A]`                ###

A template trait for collections which can be traversed either once only or one
or more times.

This trait exists primarily to eliminate code duplication between `Iterator` and
 `Traversable` , and thus implements some of the common methods that can be
implemented solely in terms of foreach without access to a `Builder` . It also
includes a number of abstract methods whose implementations are provided by
 `Iterator` , `Traversable` , etc. It contains implementations common to
 `Iterators` and `Traversables` , such as folds, conversions, and other
operations which traverse some or all of the elements and return a derived
value. Directly subclassing `TraversableOnce` is not recommended - instead,
consider declaring an `Iterator` with a `next` and `hasNext` method, creating an
 `Iterator` with one of the methods on the `Iterator` object, or declaring a
subclass of `Traversable` .

* Self Type
  * TraversableOnce [A]
* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait TraversableProxy[+A] extends Traversable[A] with TraversableProxyLike[A, Traversable[A]]` ###

This trait implements a proxy for traversable objects. It forwards all calls to
a different traversable object

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.3)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [TraversableProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableProxy.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait TraversableProxyLike[+A, +Repr <: TraversableLike[A, Repr] with Traversable[A]] extends TraversableLike[A, Repr] with Proxy` ###

This trait implements a proxy for Traversable objects. It forwards all calls to
a different Traversable object.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [TraversableProxyLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableProxyLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait TraversableView[+A, +Coll] extends TraversableViewLike[A, Coll, TraversableView[A, Coll]]` ###

A base trait for non-strict views of traversable collections.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view.

All views for traversable collections are defined by creating a new `foreach`
method.

* Source
  * [TraversableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableView.scala#L1)


### `trait TraversableViewLike[+A, +Coll, +This <: TraversableView[A, Coll] with TraversableViewLike[A, Coll, This]] extends Traversable[A] with TraversableLike[A, This] with ViewMkString[A]` ###

A template trait for non-strict views of traversable collections.

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view.

All views for traversable collections are defined by creating a new `foreach`
method.

Implementation note: Methods such as `map` or `flatMap` on this view will not
invoke the implicitly passed `Builder` factory, but will return a new view
directly, to preserve by-name behavior. The new view is then cast to the
factory's result type. This means that every `CanBuildFrom` that takes a `View`
as its `From` type parameter must yield the same view (or a generic superclass
of it) as its result parameter. If that assumption is broken, cast errors might
result.

* Self Type
  * TraversableViewLike [A, Coll, This]
* Source
  * [TraversableViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableViewLike.scala#L1)


### `trait ViewMkString[+A] extends AnyRef`                                  ###

* Self Type
  * ViewMkString [A] with Traversable [A]
* Source
  * [TraversableViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableViewLike.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object +:`                                                              ###

An extractor used to head/tail deconstruct sequences.

* Source
  * [SeqExtractors.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqExtractors.scala#L1)


### `object :+`                                                              ###

An extractor used to init/last deconstruct sequences.

* Source
  * [SeqExtractors.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqExtractors.scala#L1)


### `object BitSet extends BitSetFactory[BitSet]`                            ###

This object provides a set of operations to create `BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BitSet.scala#L1)


### `object BitSetLike`                                                      ###

Companion object for BitSets. Contains private data only

* Source
  * [BitSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BitSetLike.scala#L1)


### `object GenIterable extends GenTraversableFactory[GenIterable]`          ###

* Source
  * [GenIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenIterable.scala#L1)


### `object GenMap extends GenMapFactory[GenMap]`                            ###

* Source
  * [GenMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenMap.scala#L1)


### `object GenSeq extends GenTraversableFactory[GenSeq]`                    ###

* Source
  * [GenSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSeq.scala#L1)


### `object GenSet extends GenTraversableFactory[GenSet]`                    ###

* Source
  * [GenSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSet.scala#L1)


### `object GenTraversable extends GenTraversableFactory[GenTraversable]`    ###

* Source
  * [GenTraversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenTraversable.scala#L1)


### `object IndexedSeq extends IndexedSeqFactory[IndexedSeq]`                ###

This object provides a set of operations to create `IndexedSeq` values. The
current default implementation of a `IndexedSeq` is a `Vector` .

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IndexedSeq.scala#L1)


### `object Iterable extends GenTraversableFactory[Iterable] with TraversableFactory[Iterable]` ###

This object provides a set of operations to create `Iterable` values. The
current default implementation of a `Iterable` is a `List` .

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterable.scala#L1)


### `object IterableView`                                                    ###

An object containing the necessary implicit definitions to make `IterableView` s
work. Its definitions are generally not accessed directly by clients.

* Source
  * [IterableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableView.scala#L1)


### `object Iterator`                                                        ###

The `Iterator` object provides various functions for creating specialized
iterators.

* Source
  * [Iterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterator.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `object JavaConversions extends WrapAsScala with WrapAsJava`             ###

A collection of implicit conversions supporting interoperability between Scala
and Java collections.

The following conversions are supported:

```scala
scala.collection.Iterable <=> java.lang.Iterable
scala.collection.Iterable <=> java.util.Collection
scala.collection.Iterator <=> java.util.{ Iterator, Enumeration }
scala.collection.mutable.Buffer <=> java.util.List
scala.collection.mutable.Set <=> java.util.Set
scala.collection.mutable.Map <=> java.util.{ Map, Dictionary }
scala.collection.concurrent.Map <=> java.util.concurrent.ConcurrentMap
```

In all cases, converting from a source type to a target type and back again will
return the original source object, eg.

```scala
import scala.collection.JavaConversions._

val sl = new scala.collection.mutable.ListBuffer[Int]
val jl : java.util.List[Int] = sl
val sl2 : scala.collection.mutable.Buffer[Int] = jl
assert(sl eq sl2)
```

In addition, the following one way conversions are provided:

```scala
scala.collection.Seq         => java.util.List
scala.collection.mutable.Seq => java.util.List
scala.collection.Set         => java.util.Set
scala.collection.Map         => java.util.Map
java.util.Properties         => scala.collection.mutable.Map[String, String]
```

* Source
  * [JavaConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/JavaConversions.scala#L1)
* Since
  * 2.8


### `object JavaConverters extends DecorateAsJava with DecorateAsScala`      ###

A collection of decorators that allow converting between Scala and Java
collections using `asScala` and `asJava` methods.

The following conversions are supported via `asJava` , `asScala`

*  `scala.collection.Iterable` <=> `java.lang.Iterable`
*  `scala.collection.Iterator` <=> `java.util.Iterator`
*  `scala.collection.mutable.Buffer` <=> `java.util.List`
*  `scala.collection.mutable.Set` <=> `java.util.Set`
*  `scala.collection.mutable.Map` <=> `java.util.Map`
*  `scala.collection.mutable.concurrent.Map` <=>
    `java.util.concurrent.ConcurrentMap`

In all cases, converting from a source type to a target type and back again will
return the original source object, e.g.

```scala
import scala.collection.JavaConverters._

val sl = new scala.collection.mutable.ListBuffer[Int]
val jl : java.util.List[Int] = sl.asJava
val sl2 : scala.collection.mutable.Buffer[Int] = jl.asScala
assert(sl eq sl2)
```

The following conversions are also supported, but the direction from Scala to
Java is done by the more specifically named methods: `asJavaCollection` ,
 `asJavaEnumeration` , `asJavaDictionary` .

*  `scala.collection.Iterable` <=> `java.util.Collection`
*  `scala.collection.Iterator` <=> `java.util.Enumeration`
*  `scala.collection.mutable.Map` <=> `java.util.Dictionary`

In addition, the following one way conversions are provided via `asJava` :

*  `scala.collection.Seq` => `java.util.List`
*  `scala.collection.mutable.Seq` => `java.util.List`
*  `scala.collection.Set` => `java.util.Set`
*  `scala.collection.Map` => `java.util.Map`

The following one way conversion is provided via `asScala` :

*  `java.util.Properties` => `scala.collection.mutable.Map`

* Source
  * [JavaConverters.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/JavaConverters.scala#L1)
* Since
  * 2.8.1


### `object LinearSeq extends SeqFactory[LinearSeq]`                         ###

This object provides a set of operations to create `LinearSeq` values. The
current default implementation of a `LinearSeq` is a `List` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/LinearSeq.scala#L1)


### `object Map extends MapFactory[Map]`                                     ###

This object provides a set of operations needed to create `Map` values.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Map.scala#L1)


### `object Searching`                                                       ###

A collection of wrappers that provide sequence classes with search
functionality.

Example usage:

```scala
import scala.collection.Searching._
val l = List(1, 2, 3, 4, 5)
l.search(3)
// == Found(2)
```

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


### `object Seq extends SeqFactory[Seq]`                                     ###

This object provides a set of operations to create `Seq` values. The current
default implementation of a `Seq` is a `List` .

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Seq.scala#L1)


### `object SeqLike`                                                         ###

The companion object for trait `SeqLike` .

* Source
  * [SeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqLike.scala#L1)


### `object SeqView`                                                         ###

An object containing the necessary implicit definitions to make `SeqView` s
work. Its definitions are generally not accessed directly by clients.

* Source
  * [SeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqView.scala#L1)


### `object Set extends SetFactory[Set]`                                     ###

This object provides a set of operations needed to create `Set` values. The
current default implementation of a `Set` is one of `EmptySet` , `Set1` ,
 `Set2` , `Set3` , `Set4` in class `immutable.Set` for sets of sizes up to 4,
and a `immutable.HashSet` for sets of larger sizes.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Set.scala#L1)


### `object SortedMap extends SortedMapFactory[SortedMap]`                   ###

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedMap.scala#L1)
* Since
  * 2.8


### `object SortedSet extends SortedSetFactory[SortedSet]`                   ###

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedSet.scala#L1)
* Since
  * 2.8


### `object Traversable extends GenTraversableFactory[Traversable] with TraversableFactory[Traversable]` ###

This object provides a set of operations to create `Traversable` values. The
current default implementation of a Traversable is a `List` .

* Source
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Traversable.scala#L1)


### `object TraversableOnce`                                                 ###

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


### `object TraversableView`                                                 ###

An object containing the necessary implicit definitions to make
 `TraversableView` s work. Its definitions are generally not accessed directly
by clients.

* Source
  * [TraversableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableView.scala#L1)


### `package concurrent`                                                     ###


### `package convert`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/convert/package.scala#L1)


### `package generic`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/package.scala#L1)


### `package immutable`                                                      ###


### `package mutable`                                                        ###


### `package parallel`                                                       ###

Package object for parallel collections.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `package script`                                                         ###


--------------------------------------------------------------------------------
                      Value Members From scala.collection
--------------------------------------------------------------------------------


### `def breakOut[From, T, To](implicit b: CanBuildFrom[Nothing, T, To]): CanBuildFrom[From, T, To]` ###

Provides a CanBuildFrom instance that builds a specific target collection (
 `To') irrespective of the original collection (` From').
(defined at scala.collection)
