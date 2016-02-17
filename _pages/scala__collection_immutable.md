
#                          scala.collection.immutable                          #

```scala
package immutable
```


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object PagedSeq`                                                        ###

The `PagedSeq` object defines a lazy implementations of a random access
sequence.

Provides utility methods that return instances of `PagedSeq[Char]` .
 `fromIterator` and `fromIterable` provide generalised instances of `PagedSeq`

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.8)_ This object will be moved to the
    scala-parser-combinators module
* Source
  * [PagedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/PagedSeq.scala#L1)
* Since
  * 2.7


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final case class ::[B](head: B, tl: List[B]) extends List[B] with Product with Serializable` ###

A non empty list characterized by a head and a tail.

* B
  * the type of the list elements.
* head
  * the first element of the list
* tl
  * the list containing the remaining elements of this list after the first one.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [List.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/List.scala#L1)
* Version
  * 1.0, 15/07/2003
* Since
  * 2.8


### `abstract class AbstractMap[A, +B] extends collection.AbstractMap[A, B] with Map[A, B]` ###

Explicit instantiation of the `Map` trait to reduce class file size in
subclasses.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `abstract class BitSet extends AbstractSet[Int] with SortedSet[Int] with collection.BitSet with BitSetLike[BitSet] with Serializable` ###

A class for immutable bitsets.

Bitsets are sets of non-negative integers which are represented as variable-size
arrays of bits packed into 64-bit words. The memory footprint of a bitset is
determined by the largest number stored in it.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#immutable_bitsets)
    section on `Immutable BitSets` for more information.


### `trait DefaultMap[A, +B] extends Map[A, B]`                              ###

A default map which implements the `+` and `-` methods of maps. It does so using
the default builder for maps defined in the `Map` object. Instances that inherit
from `DefaultMap[A, B]` still have to define:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
```

It refers back to the original map.

It might also be advisable to override `foreach` or `size` if efficient
implementations can be found.

* A
  * the type of the keys contained in this map.
* B
  * the type of the values associated with the keys.

* Self Type
  * DefaultMap [A, B]
* Source
  * [DefaultMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/DefaultMap.scala#L1)
* Since
  * 2.8


### `class HashMap[A, +B] extends AbstractMap[A, B] with Map[A, B] with MapLike[A, B, HashMap[A, B]] with Serializable with CustomParallelizable[(A, B), ParHashMap[A, B]]` ###

This class implements immutable maps using a hash trie.

 *Note:* The builder of this hash map may return specialized representations for
small maps.

* A
  * the type of the keys contained in this hash map.
* B
  * the type of the values associated with the keys.

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashMap.scala#L1)
* Version
  * 2.8
* Since
  * 2.3
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#hash_tries)
    section on `Hash Tries` for more information.


### `class HashSet[A] extends AbstractSet[A] with Set[A] with GenericSetTemplate[A, HashSet] with SetLike[A, HashSet[A]] with CustomParallelizable[A, ParHashSet[A]] with Serializable` ###

This class implements immutable sets using a hash trie.

 *Note:* The builder of this hash set may return specialized representations for
small sets.

* A
  * the type of the elements contained in this hash set.

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashSet.scala#L1)
* Version
  * 2.8
* Since
  * 2.3


### `trait IndexedSeq[+A] extends Seq[A] with collection.IndexedSeq[A] with GenericTraversableTemplate[A, IndexedSeq] with IndexedSeqLike[A, IndexedSeq[A]]` ###

A subtrait of `collection.IndexedSeq` which represents indexed sequences that
are guaranteed immutable.

Indexed sequences support constant-time or near constant-time element access and
length computation. They are defined in terms of abstract methods `apply` for
indexing and `length` .

Indexed sequences do not add any new methods to `Seq` , but promise efficient
implementations of random access patterns.

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/IndexedSeq.scala#L1)


### `sealed abstract class IntMap[+T] extends AbstractMap[immutable.IntMapUtils.Int, T] with Map[immutable.IntMapUtils.Int, T] with MapLike[immutable.IntMapUtils.Int, T, IntMap[T]]` ###

Specialised immutable map structure for integer keys, based on
[Fast Mergeable Integer Maps](http://ittc.ku.edu/~andygill/papers/IntMap98.pdf)
by Okasaki and Gill. Essentially a trie based on binary digits of the integers.

 *Note:* This class is as of 2.8 largely superseded by HashMap.

* T
  * type of the values associated with integer keys.

* Source
  * [IntMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/IntMap.scala#L1)
* Since
  * 2.7


### `trait Iterable[+A] extends Traversable[A] with collection.Iterable[A] with GenericTraversableTemplate[A, Iterable] with IterableLike[A, Iterable[A]] with Parallelizable[A, ParIterable[A]]` ###

A base trait for iterable collections that are guaranteed immutable.

This is a base trait for all immutable Scala collections that define an
 `iterator` method to step through one-by-one the collection's elements.
Implementations of this trait need to provide a concrete method with signature:

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
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Iterable.scala#L1)


### `trait LinearSeq[+A] extends Seq[A] with collection.LinearSeq[A] with GenericTraversableTemplate[A, LinearSeq] with LinearSeqLike[A, LinearSeq[A]]` ###

A subtrait of `collection.LinearSeq` which represents sequences that are
guaranteed immutable.

Linear sequences have reasonably efficient `head` , `tail` , and `isEmpty`
methods. If these methods provide the fastest way to traverse the collection, a
collection `Coll` that extends this trait should also extend
 `LinearSeqOptimized[A, Coll[A]]` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/LinearSeq.scala#L1)


### `sealed abstract class List[+A] extends AbstractSeq[A] with LinearSeq[A] with Product with GenericTraversableTemplate[A, List] with LinearSeqOptimized[A, List[A]] with Serializable` ###

A class for immutable linked lists representing ordered collections of elements
of type `A` .

This class comes with two implementing case classes `scala.Nil` and `scala.::`
that implement the abstract members `isEmpty` , `head` and `tail` .

This class is optimal for last-in-first-out (LIFO), stack-like access patterns.
If you need another access pattern, for example, random access or FIFO, consider
using a collection more suited to this than `List` .

### Performance

 *Time:*  `List` has `O(1)` prepend and head/tail access. Most other operations
are `O(n)` on the number of elements in the list. This includes the index-based
lookup of elements, `length` , `append` and `reverse` .

 *Space:*  `List` implements *structural sharing* of the tail list. This means
that many operations are either zero- or constant-memory cost.

```scala
val mainList = List(3, 2, 1)
val with4 =    4 :: mainList  // re-uses mainList, costs one :: instance
val with42 =   42 :: mainList // also re-uses mainList, cost one :: instance
val shorter =  mainList.tail  // costs nothing as it uses the same 2::1::Nil instances as mainList
```

* Annotations
  * @ SerialVersionUID ()
* Source
  * [List.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/List.scala#L1)
* Version
  * 2.8
* Since
  * 1.0
* Note
  * The functional list is characterized by persistence and structural sharing,
    thus offering considerable performance and space consumption benefits in
    some scenarios if used correctly. However, note that objects having multiple
    references into the same functional list (that is, objects that rely on
    structural sharing), will be serialized and deserialized with multiple
    lists, one for each reference to it. I.e. structural sharing is lost after
    serialization/deserialization.
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#lists)
    section on `Lists` for more information.

Example:

```scala
// Make a list via the companion object factory
val days = List("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
// Make a list element-by-element
val when = "AM" :: "PM" :: List()
// Pattern match
days match {
  case firstDay :: otherDays =>
    println("The first day of the week is: " + firstDay)
  case List() =>
    println("There don't seem to be any week days.")
}
```


### `class ListMap[A, +B] extends AbstractMap[A, B] with Map[A, B] with MapLike[A, B, ListMap[A, B]] with Serializable` ###

This class implements immutable maps using a list-based data structure, which
preserves insertion order. Instances of `ListMap` represent empty maps; they can
be either created by calling the constructor directly, or by applying the
function `ListMap.empty` .

* A
  * the type of the keys in this list map.
* B
  * the type of the values associated with the keys.

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListMap.scala#L1)
* Version
  * 2.0, 01/01/2007
* Since
  * 1


### `class ListSet[A] extends AbstractSet[A] with Set[A] with GenericSetTemplate[A, ListSet] with SetLike[A, ListSet[A]] with Serializable` ###

This class implements immutable sets using a list-based data structure.
Instances of `ListSet` represent empty sets; they can be either created by
calling the constructor directly, or by applying the function `ListSet.empty` .

* A
  * the type of the elements contained in this list set.

* Self Type
  * ListSet [A]
* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ListSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListSet.scala#L1)
* Version
  * 1.0, 09/07/2003
* Since
  * 1


### `sealed abstract class LongMap[+T] extends AbstractMap[immutable.LongMapUtils.Long, T] with Map[immutable.LongMapUtils.Long, T] with MapLike[immutable.LongMapUtils.Long, T, LongMap[T]]` ###

Specialised immutable map structure for long keys, based on
[Fast Mergeable Long Maps](http://citeseer.ist.psu.edu/okasaki98fast.html) by
Okasaki and Gill. Essentially a trie based on binary digits of the integers.

Note: This class is as of 2.8 largely superseded by HashMap.

* T
  * type of the values associated with the long keys.

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/LongMap.scala#L1)
* Since
  * 2.7


### `trait Map[A, +B] extends Iterable[(A, B)] with collection.Map[A, B] with MapLike[A, B, Map[A, B]]` ###

A generic trait for immutable maps. Concrete classes have to provide
functionality for the abstract methods in `Map` :

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def + [B1 >: B](kv: (A, B1)): Map[A, B1]
def -(key: A): Map[A, B]
```

* Self Type
  * Map [A, B]
* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)
* Since
  * 1


### `trait MapLike[A, +B, +This <: MapLike[A, B, This] with Map[A, B]] extends collection.MapLike[A, B, This] with Parallelizable[(A, B), ParMap[A, B]]` ###

A generic template for immutable maps from keys of type `A` to values of type
 `B` . To implement a concrete map, you need to provide implementations of the
following methods (where `This` is the type of the actual map implementation):

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def + [B1 >: B](kv: (A, B)): Map[A, B1]
def - (key: A): This
```

If you wish that transformer methods like `take` , `drop` , `filter` return the
same kind of map, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* A
  * the type of the keys contained in this collection.
* B
  * the type of the values associated with the keys.
* This
  * The type of the actual map implementation.

* Self Type
  * MapLike [A, B, This]
* Source
  * [MapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/MapLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait MapProxy[A, +B] extends Map[A, B] with MapProxyLike[A, B, Map[A, B]]` ###

This is a simple wrapper class for `scala.collection.immutable.Map`.

It is most useful for assembling customized map abstractions dynamically using
object composition and forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [MapProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/MapProxy.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 2.8


### `abstract class NumericRange[T] extends AbstractSeq[T] with IndexedSeq[T] with Serializable` ###

 `NumericRange` is a more generic version of the `Range` class which works with
arbitrary types. It must be supplied with an `Integral` implementation of the
range type.

Factories for likely types include `Range.BigInt` , `Range.Long` , and
 `Range.BigDecimal` . `Range.Int` exists for completeness, but the `Int` -based
 `scala.Range` should be more performant.

```scala
val r1 = new Range(0, 100, 1)
val veryBig = Int.MaxValue.toLong + 1
val r2 = Range.Long(veryBig, veryBig + 100, 1)
assert(r1 sameElements r2.map(_ - veryBig))
```

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)
* Version
  * 2.8


### `class PagedSeq[T] extends AbstractSeq[T] with collection.IndexedSeq[T]` ###

An implementation of lazily computed sequences, where elements are stored in
"pages", i.e. arrays of fixed size.

A paged sequence is constructed from a function that produces more elements when
asked. The producer function - `more` , is similar to the read method in
java.io.Reader. The `more` function takes three parameters: an array of
elements, a start index, and an end index. It should try to fill the array
between start and end indices (excluding end index). It returns the number of
elements produced, or -1 if end of logical input stream was reached before
reading any element.

* T
  * the type of the elements contained in this paged sequence, with an
     `ClassTag` context bound.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.8)_ This class will be moved to the
    scala-parser-combinators module
* Source
  * [PagedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/PagedSeq.scala#L1)
* Since
  * 2.7


### `class Queue[+A] extends AbstractSeq[A] with LinearSeq[A] with GenericTraversableTemplate[A, Queue] with LinearSeqLike[A, Queue[A]] with Serializable` ###

 `Queue` objects implement data structures that allow to insert and retrieve
elements in a first-in-first-out (FIFO) manner.

 `Queue` is implemented as a pair of `List` s, one containing the _in_ elements
and the other the _out_ elements. Elements are added to the _in_ list and
removed from the _out_ list. When the _out_ list runs dry, the queue is pivoted
by replacing the _out_ list by _in.reverse_ , and _in_ by _Nil_ .

Adding items to the queue always has cost `O(1)` . Removing items has cost
 `O(1)` , except in the case where a pivot is required, in which case, a cost of
 `O(n)` is incurred, where `n` is the number of elements in the queue. When this
happens, `n` remove operations with `O(1)` cost are guaranteed. Removing an item
is on average `O(1)` .

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [Queue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Queue.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#immutable_queues)
    section on `Immutable Queues` for more information.


### `class Range extends AbstractSeq[Int] with IndexedSeq[Int] with CustomParallelizable[Int, ParRange] with Serializable` ###

The `Range` class represents integer values in range _[start;end)_ with non-zero
step value `step` . It's a special case of an indexed sequence. For example:

```scala
val r1 = 0 until 10
val r2 = r1.start until r1.end by r1.step + 1
println(r2.length) // = 5
```

Ranges that contain more than `Int.MaxValue` elements can be created, but these
overfull ranges have only limited capabilities. Any method that could require a
collection of over `Int.MaxValue` length to be created, or could be asked to
index beyond `Int.MaxValue` elements will throw an exception. Overfull ranges
can safely be reduced in size by changing the step size (e.g. `by 3` ) or
taking/dropping elements. `contains` , `equals` , and access to the ends of the
range ( `head` , `last` , `tail` , `init` ) are also permitted on overfull
ranges.

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)
* Version
  * 2.8
* Since
  * 2.5
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#ranges)
    section on `Ranges` for more information.


### `trait Seq[+A] extends Iterable[A] with collection.Seq[A] with GenericTraversableTemplate[A, Seq] with SeqLike[A, Seq[A]] with Parallelizable[A, ParSeq[A]]` ###

A subtrait of `collection.Seq` which represents sequences that are guaranteed
immutable.

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
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Seq.scala#L1)


### `trait Set[A] extends Iterable[A] with collection.Set[A] with GenericSetTemplate[A, Set] with SetLike[A, Set[A]] with Parallelizable[A, ParSet[A]]` ###

A generic trait for immutable sets.

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

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)
* Since
  * 1.0


### `trait SetProxy[A] extends Set[A] with SetProxyLike[A, Set[A]]`          ###

This is a simple wrapper class for `scala.collection.immutable.Set`.

It is most useful for assembling customized set abstractions dynamically using
object composition and forwarding.

* A
  * type of the elements contained in this set proxy.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SetProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SetProxy.scala#L1)
* Since
  * 2.8


### `trait SortedMap[A, +B] extends Map[A, B] with collection.SortedMap[A, B] with MapLike[A, B, SortedMap[A, B]] with SortedMapLike[A, B, SortedMap[A, B]]` ###

A map whose keys are sorted.

* A
  * the type of the keys contained in this sorted map.
* B
  * the type of the values associated with the keys.

* Self Type
  * SortedMap [A, B]
* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedMap.scala#L1)
* Version
  * 2.8
* Since
  * 2.4


### `trait SortedSet[A] extends Set[A] with collection.SortedSet[A] with SortedSetLike[A, SortedSet[A]]` ###

A subtrait of `collection.SortedSet` which represents sorted sets which cannot
be mutated.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedSet.scala#L1)
* Version
  * 2.8
* Since
  * 2.4


### `class Stack[+A] extends AbstractSeq[A] with LinearSeq[A] with GenericTraversableTemplate[A, Stack] with LinearSeqOptimized[A, Stack[A]] with Serializable` ###

This class implements immutable stacks using a list-based data structure.

 *Note:* This class exists only for historical reason and as an analogue of
mutable stacks. Instead of an immutable stack you can just use a list.

* A
  * the type of the elements contained in this stack.

* Annotations
  * @ SerialVersionUID () @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Stack is an inelegant and potentially
    poorly-performing wrapper around List. Use List instead: stack push x
    becomes x :: list; stack.pop is list.tail.
* Source
  * [Stack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stack.scala#L1)
* Version
  * 1.0, 10/07/2003
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#immutable_stacks)
    section on `Immutable stacks` for more information.


### `abstract class Stream[+A] extends AbstractSeq[A] with LinearSeq[A] with GenericTraversableTemplate[A, Stream] with LinearSeqOptimized[A, Stream[A]] with Serializable` ###

The class `Stream` implements lazy lists where elements are only evaluated when
they are needed. Here is an example:

```scala
import scala.math.BigInt
object Main extends App {

  val fibs: Stream[BigInt] = BigInt(0) #:: BigInt(1) #:: fibs.zip(fibs.tail).map { n => n._1 + n._2 }

  fibs take 5 foreach println
}

// prints
//
// 0
// 1
// 1
// 2
// 3
```

The `Stream` class also employs memoization such that previously computed values
are converted from `Stream` elements to concrete values of type `A` . To
illustrate, we will alter body of the `fibs` value above and take some more
values:

```scala
import scala.math.BigInt
object Main extends App {

  val fibs: Stream[BigInt] = BigInt(0) #:: BigInt(1) #:: fibs.zip(
    fibs.tail).map(n => {
      println("Adding %d and %d".format(n._1, n._2))
      n._1 + n._2
    })

  fibs take 5 foreach println
  fibs take 6 foreach println
}

// prints
//
// 0
// 1
// Adding 0 and 1
// 1
// Adding 1 and 1
// 2
// Adding 1 and 2
// 3

// And then prints
//
// 0
// 1
// 1
// 2
// 3
// Adding 2 and 3
// 5
```

There are a number of subtle points to the above example.

* The definition of `fibs` is a `val` not a method. The memoization of the
    `Stream` requires us to have somewhere to store the information and a `val`
   allows us to do that.
* While the `Stream` is actually being modified during access, this does not
   change the notion of its immutability. Once the values are memoized they do
   not change and values that have yet to be memoized still "exist", they simply
   haven't been realized yet.
* One must be cautious of memoization; you can very quickly eat up large amounts
   of memory if you're not careful. The reason for this is that the memoization
   of the `Stream` creates a structure much like scala.collection.immutable.List.
   So long as something is holding on to the head, the head holds on to the
   tail, and so it continues recursively. If, on the other hand, there is
   nothing holding on to the head (e.g. we used `def` to define the `Stream` )
   then once it is no longer being used directly, it disappears.
* Note that some operations, including drop, dropWhile, flatMap or collect may
   process a large number of intermediate elements before returning. These
   necessarily hold onto the head, since they are methods on `Stream` , and a
   stream holds its own head. For computations of this sort where memoization is
   not desired, use `Iterator` when possible.

```scala
// For example, let's build the natural numbers and do some silly iteration
// over them.

// We'll start with a silly iteration
def loop(s: String, i: Int, iter: Iterator[Int]): Unit = {
  // Stop after 200,000
  if (i < 200001) {
    if (i % 50000 == 0) println(s + i)
    loop(s, iter.next, iter)
  }
}

// Our first Stream definition will be a val definition
val stream1: Stream[Int] = {
  def loop(v: Int): Stream[Int] = v #:: loop(v + 1)
  loop(0)
}

// Because stream1 is a val, everything that the iterator produces is held
// by virtue of the fact that the head of the Stream is held in stream1
val it1 = stream1.iterator
loop("Iterator1: ", it1.next, it1)

// We can redefine this Stream such that all we have is the Iterator left
// and allow the Stream to be garbage collected as required.  Using a def
// to provide the Stream ensures that no val is holding onto the head as
// is the case with stream1
def stream2: Stream[Int] = {
  def loop(v: Int): Stream[Int] = v #:: loop(v + 1)
  loop(0)
}
val it2 = stream2.iterator
loop("Iterator2: ", it2.next, it2)

// And, of course, we don't actually need a Stream at all for such a simple
// problem.  There's no reason to use a Stream if you don't actually need
// one.
val it3 = new Iterator[Int] {
  var i = -1
  def hasNext = true
  def next(): Int = { i += 1; i }
}
loop("Iterator3: ", it3.next, it3)
```

* The fact that `tail` works at all is of interest. In the definition of `fibs`
   we have an initial `(0, 1, Stream(...))` so `tail` is deterministic. If we
   defined `fibs` such that only `0` were concretely known then the act of
   determining `tail` would require the evaluation of `tail` which would cause
   an infinite recursion and stack overflow. If we define a definition where the
   tail is not initially computable then we're going to have an infinite
   recursion:

```scala
// The first time we try to access the tail we're going to need more
// information which will require us to recurse, which will require us to
// recurse, which...
val sov: Stream[Vector[Int]] = Vector(0) #:: sov.zip(sov.tail).map { n => n._1 ++ n._2 }
```

The definition of `fibs` above creates a larger number of objects than necessary
depending on how you might want to implement it. The following implementation
provides a more "cost effective" implementation due to the fact that it has a
more direct route to the numbers themselves:

```scala
lazy val fib: Stream[Int] = {
  def loop(h: Int, n: Int): Stream[Int] = h #:: loop(n, h + n)
  loop(1, 1)
}
```

Note that `mkString` forces evaluation of a `Stream` , but `addString` does not.
In both cases, a `Stream` that is or ends in a cycle (e.g.
 `lazy val s: Stream[Int] = 0 #:: s` ) will convert additional trips through the
cycle to `...` . Additionally, `addString` will display an un-memoized tail as
 `?` .

* A
  * the type of the elements contained in this stream.

* Self Type
  * Stream [A]
* Annotations
  * @ deprecatedInheritance (message = "This class will be sealed.", since =
    "2.11.0")
* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)
* Version
  * 1.1 08/08/03
* Since
  * 2.8
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#streams)
    section on `Streams` for more information.


### `final class StreamIterator[+A] extends AbstractIterator[A] with Iterator[A]` ###

A specialized, extra-lazy implementation of a stream iterator, so it can iterate
as lazily as it traverses the tail.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


### `trait StreamView[+A, +Coll] extends StreamViewLike[A, Coll, StreamView[A, Coll]]` ###

* Source
  * [StreamView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/StreamView.scala#L1)


### `trait StreamViewLike[+A, +Coll, +This <: StreamView[A, Coll] with StreamViewLike[A, Coll, This]] extends SeqView[A, Coll] with SeqViewLike[A, Coll, This]` ###

* Self Type
  * StreamViewLike [A, Coll, This]
* Source
  * [StreamViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/StreamViewLike.scala#L1)


### `trait StringLike[+Repr] extends IndexedSeqOptimized[Char, Repr] with Ordered[String]` ###

A trait describing stringlike collections.

* Repr
  * The type of the actual collection inheriting `StringLike` .

* Self Type
  * StringLike [Repr]
* Source
  * [StringLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/StringLike.scala#L1)
* Since
  * 2.8


### `final class StringOps extends AnyVal with StringLike[String]`           ###

This class serves as a wrapper providing scala.Predef.String s with all the
operations found in indexed sequences. Where needed, `String` s are implicitly
converted into instances of this class.

The difference between this class and `WrappedString` is that calling
transformer methods such as `filter` and `map` will yield a `String` object,
whereas a `WrappedString` will remain a `WrappedString` .

* Source
  * [StringOps.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/StringOps.scala#L1)
* Since
  * 2.8


### `trait Traversable[+A] extends collection.Traversable[A] with GenericTraversableTemplate[A, Traversable] with TraversableLike[A, Traversable[A]] with Immutable` ###

A trait for traversable collections that are guaranteed immutable.

This is a base trait of all kinds of immutable Scala collections. It implements
the behavior common to all collections, in terms of a method `foreach` with
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
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Traversable.scala#L1)


### `class TreeMap[A, +B] extends SortedMap[A, B] with SortedMapLike[A, B, TreeMap[A, B]] with MapLike[A, B, TreeMap[A, B]] with Serializable` ###

This class implements immutable maps using a tree.

* A
  * the type of the keys contained in this tree map.
* B
  * the type of the values associated with the keys.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [TreeMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/TreeMap.scala#L1)
* Version
  * 1.1, 03/05/2004
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#redblack_trees)
    section on `Red-Black Trees` for more information.


### `class TreeSet[A] extends SortedSet[A] with SortedSetLike[A, TreeSet[A]] with Serializable` ###

This class implements immutable sets using a tree.

* A
  * the type of the elements contained in this tree set

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/TreeSet.scala#L1)
* Version
  * 2.0, 02/01/2007
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#redblack_trees)
    section on `Red-Black Trees` for more information.


### `final class Vector[+A] extends AbstractSeq[A] with IndexedSeq[A] with GenericTraversableTemplate[A, Vector] with IndexedSeqLike[A, Vector[A]] with VectorPointer[A] with Serializable with CustomParallelizable[A, ParVector[A]]` ###

Vector is a general-purpose, immutable data structure. It provides random access
and updates in effectively constant time, as well as very fast append and
prepend. Because vectors strike a good balance between fast random selections
and fast random functional updates, they are currently the default
implementation of immutable indexed sequences. It is backed by a little endian
bit-mapped vector trie with a branching factor of 32. Locality is very good, but
not contiguous, which is good for very large sequences.

* A
  * the element type

* Self Type
  * Vector [A]
* Source
  * [Vector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Vector.scala#L1)
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#vectors)
    section on `Vectors` for more information.


### `final class VectorBuilder[A] extends ReusableBuilder[A, Vector[A]] with VectorPointer[A]` ###

A class to build instances of `Vector` . This builder is reusable.

* Source
  * [Vector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Vector.scala#L1)


### `class VectorIterator[+A] extends AbstractIterator[A] with Iterator[A] with VectorPointer[A]` ###

* Source
  * [Vector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Vector.scala#L1)


### `class WrappedString extends AbstractSeq[Char] with IndexedSeq[Char] with StringLike[WrappedString]` ###

This class serves as a wrapper augmenting `String` s with all the operations
found in indexed sequences.

The difference between this class and `StringOps` is that calling transformer
methods such as `filter` and `map` will yield an object of type `WrappedString`
rather than a `String` .

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [WrappedString.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/WrappedString.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object BitSet extends BitSetFactory[BitSet] with Serializable`          ###

This object provides a set of operations to create `immutable.BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)


### `object HashMap extends ImmutableMapFactory[HashMap] with generic.BitOperations.Int with Serializable` ###

This object provides a set of operations needed to create `immutable.HashMap`
values.

* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashMap.scala#L1)


### `object HashSet extends ImmutableSetFactory[HashSet] with Serializable`  ###

This object provides a set of operations needed to create `immutable.HashSet`
values.

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashSet.scala#L1)


### `object IndexedSeq extends IndexedSeqFactory[IndexedSeq]`                ###

This object provides a set of operations to create `IndexedSeq` values. The
current default implementation of a `IndexedSeq` is a `Vector` .

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/IndexedSeq.scala#L1)


### `object IntMap`                                                          ###

A companion object for integer maps.

* Source
  * [IntMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/IntMap.scala#L1)


### `object Iterable extends GenTraversableFactory[Iterable] with TraversableFactory[Iterable]` ###

This object provides a set of operations to create `immutable.Iterable` values.
The current default implementation of a `immutable.Iterable` is a `List` .

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Iterable.scala#L1)


### `object LinearSeq extends SeqFactory[LinearSeq]`                         ###

This object provides a set of operations to create `immutable.LinearSeq` values.
The current default implementation of a `immutable.LinearSeq` is a `List` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/LinearSeq.scala#L1)


### `object List extends SeqFactory[List] with Serializable`                 ###

This object provides a set of operations to create `List` values.

* Source
  * [List.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/List.scala#L1)


### `object ListMap extends ImmutableMapFactory[ListMap] with Serializable`  ###

This object provides a set of operations needed to create `immutable.ListMap`
values.

* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListMap.scala#L1)
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#list_maps)
    section on `List Maps` for more information.


### `object ListSet extends ImmutableSetFactory[ListSet] with Serializable`  ###

This object provides a set of operations needed to create `immutable.ListSet`
values.

* Source
  * [ListSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListSet.scala#L1)


### `object LongMap`                                                         ###

A companion object for long maps.

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/LongMap.scala#L1)


### `object Map extends ImmutableMapFactory[Map]`                            ###

This object provides a set of operations needed to create `immutable.Map`
values.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `object Nil extends List[Nothing] with Product with Serializable`        ###

The empty list.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [List.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/List.scala#L1)
* Version
  * 1.0, 15/07/2003
* Since
  * 2.8


### `object NumericRange extends Serializable`                               ###

A companion object for numeric ranges.

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)


### `object Queue extends SeqFactory[Queue] with Serializable`               ###

This object provides a set of operations to create `immutable.Queue` values.

* Source
  * [Queue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Queue.scala#L1)


### `object Range extends Serializable`                                      ###

A companion object for the `Range` class.

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `object Seq extends SeqFactory[Seq]`                                     ###

This object provides a set of operations to create `immutable.Seq` values.

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Seq.scala#L1)


### `object Set extends ImmutableSetFactory[Set]`                            ###

This object provides a set of operations needed to create `immutable.Set`
values.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


### `object SortedMap extends ImmutableSortedMapFactory[SortedMap]`          ###

This object provides a set of operations needed to create sorted maps of type
 `immutable.SortedMap` .

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedMap.scala#L1)


### `object SortedSet extends ImmutableSortedSetFactory[SortedSet]`          ###

This object provides a set of operations needed to create sorted sets of type
 `immutable.SortedSet` .

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedSet.scala#L1)


### `object Stack extends SeqFactory[Stack] with Serializable`               ###

This object provides a set of operations to create `immutable.Stack` values.

* Source
  * [Stack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stack.scala#L1)


### `object Stream extends SeqFactory[Stream] with Serializable`             ###

The object `Stream` provides helper functions to manipulate streams.

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)
* Version
  * 1.1 08/08/03
* Since
  * 2.8


### `object StringLike`                                                      ###

A companion object for the `StringLike` containing some constants.

* Source
  * [StringLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/StringLike.scala#L1)
* Since
  * 2.8


### `object Traversable extends GenTraversableFactory[Traversable] with TraversableFactory[Traversable]` ###

This object provides a set of operations to create `immutable.Traversable`
values. The current default implementation of a `immutable.Traversable` is a
 `List` .

* Source
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Traversable.scala#L1)


### `object TreeMap extends ImmutableSortedMapFactory[TreeMap] with Serializable` ###

This object provides a set of operations needed to create sorted maps of type
 `immutable.TreeMap` .

* Source
  * [TreeMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/TreeMap.scala#L1)


### `object TreeSet extends ImmutableSortedSetFactory[TreeSet] with Serializable` ###

This object provides a set of operations needed to create sorted sets of type
 `immutable.TreeSet` .

* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/TreeSet.scala#L1)


### `object Vector extends IndexedSeqFactory[Vector] with Serializable`      ###

Companion object to the Vector class

* Source
  * [Vector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Vector.scala#L1)


### `object WrappedString`                                                   ###

A companion object for wrapped strings.

* Source
  * [WrappedString.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/WrappedString.scala#L1)
* Since
  * 2.8

