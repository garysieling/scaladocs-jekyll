
#                           scala.collection.mutable                           #

```scala
package mutable
```


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object DoubleLinkedList extends SeqFactory[DoubleLinkedList] with Serializable` ###

This object provides a set of operations to create `DoubleLinkedList` values.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated.
* Source
  * [DoubleLinkedList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DoubleLinkedList.scala#L1)


### `object LinkedList extends SeqFactory[LinkedList] with Serializable`     ###

This object provides a set of operations to create `LinkedList` values.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated.
* Source
  * [LinkedList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedList.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class AbstractBuffer[A] extends AbstractSeq[A] with Buffer[A]` ###

Explicit instantiation of the `Buffer` trait to reduce class file size in
subclasses.

* Source
  * [Buffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Buffer.scala#L1)


### `abstract class AbstractIterable[A] extends collection.AbstractIterable[A] with Iterable[A]` ###

Explicit instantiation of the `Iterable` trait to reduce class file size in
subclasses.

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Iterable.scala#L1)


### `abstract class AbstractMap[A, B] extends collection.AbstractMap[A, B] with Map[A, B]` ###

Explicit instantiation of the `Map` trait to reduce class file size in
subclasses.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Map.scala#L1)


### `abstract class AbstractSeq[A] extends collection.AbstractSeq[A] with Seq[A]` ###

Explicit instantiation of the `Seq` trait to reduce class file size in
subclasses.

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Seq.scala#L1)


### `abstract class AbstractSet[A] extends AbstractIterable[A] with Set[A]`  ###

Explicit instantiation of the `Set` trait to reduce class file size in
subclasses.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Set.scala#L1)


### `abstract class AbstractSortedMap[A, B] extends AbstractMap[A, B] with SortedMap[A, B]` ###

Explicit instantiation of the `SortedMap` trait to reduce class file size in
subclasses.

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedMap.scala#L1)


### `abstract class AbstractSortedSet[A] extends AbstractSet[A] with SortedSet[A]` ###

Explicit instantiation of the `SortedSet` trait to reduce class file size in
subclasses.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedSet.scala#L1)


### `final class AnyRefMap[K <: AnyRef, V] extends AbstractMap[K, V] with Map[K, V] with MapLike[K, V, AnyRefMap[K, V]] with Serializable` ###

This class implements mutable maps with `AnyRef` keys based on a hash table with
open addressing.

Basic map operations on single entries, including `contains` and `get` , are
typically significantly faster with `AnyRefMap` than HashMap. Note that numbers
and characters are not handled specially in AnyRefMap; only plain `equals` and
 `hashCode` are used in comparisons.

Methods that traverse or regenerate the map, including `foreach` and `map` , are
not in general faster than with `HashMap` . The methods `foreachKey` ,
 `foreachValue` , `mapValuesNow` , and `transformValues` are, however, faster
than alternative ways to achieve the same functionality.

Maps with open addressing may become less efficient at lookup after repeated
addition/removal of elements. Although `AnyRefMap` makes a decent attempt to
remain efficient regardless, calling `repack` on a map that will no longer have
elements removed but will be used heavily may save both time and storage space.

This map is not intended to contain more than 2 <sup>29</sup> entries
(approximately 500 million). The maximum capacity is 2 <sup>30</sup>, but
performance will degrade rapidly as 2 <sup>30</sup> is approached.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [AnyRefMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/AnyRefMap.scala#L1)


### `class ArrayBuffer[A] extends AbstractBuffer[A] with Buffer[A] with GenericTraversableTemplate[A, ArrayBuffer] with BufferLike[A, ArrayBuffer[A]] with IndexedSeqOptimized[A, ArrayBuffer[A]] with Builder[A, ArrayBuffer[A]] with ResizableArray[A] with CustomParallelizable[A, ParArray[A]] with Serializable` ###

An implementation of the `Buffer` class using an array to represent the
assembled sequence internally. Append, update and random access take constant
time (amortized time). Prepends and removes are linear in the buffer size.

* A
  * the type of this arraybuffer's elements.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ArrayBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuffer.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#array_buffers)
    section on `Array Buffers` for more information.


### `abstract class ArrayBuilder[T] extends ReusableBuilder[T, Array[T]] with Serializable` ###

A builder class for arrays.

* T
  * the type of the elements for the builder.

* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)
* Since
  * 2.8


### `trait ArrayLike[A, +Repr] extends IndexedSeqOptimized[A, Repr]`         ###

A common supertrait of `ArrayOps` and `WrappedArray` that factors out the
 `deep` method for arrays and wrapped arrays and serves as a marker trait for
array wrappers.

* A
  * type of the elements contained in the array like object.
* Repr
  * the type of the actual collection containing the elements.

* Self Type
  * ArrayLike [A, Repr]
* Source
  * [ArrayLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayLike.scala#L1)


### `trait ArrayOps[T] extends ArrayLike[T, Array[T]] with CustomParallelizable[T, ParArray[T]]` ###

This class serves as a wrapper for `Array` s with all the operations found in
indexed sequences. Where needed, instances of arrays are implicitly converted
into this class.

The difference between this class and `WrappedArray` is that calling transformer
methods such as `filter` and `map` will yield an array, whereas a
 `WrappedArray` will remain a `WrappedArray` .

* T
  * type of the elements contained in this array.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [ArrayOps.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayOps.scala#L1)
* Since
  * 2.8


### `class ArraySeq[A] extends AbstractSeq[A] with IndexedSeq[A] with GenericTraversableTemplate[A, ArraySeq] with IndexedSeqOptimized[A, ArraySeq[A]] with CustomParallelizable[A, ParArray[A]] with Serializable` ###

A class for polymorphic arrays of elements that's represented internally by an
array of objects. This means that elements of primitive types are boxed.

* A
  * type of the elements contained in this array sequence.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ArraySeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArraySeq.scala#L1)
* Version
  * 2.8
* Since
  * 2.8
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#array_sequences)
    section on `Array Sequences` for more information.


### `class ArrayStack[T] extends AbstractSeq[T] with IndexedSeq[T] with IndexedSeqLike[T, ArrayStack[T]] with GenericTraversableTemplate[T, ArrayStack] with IndexedSeqOptimized[T, ArrayStack[T]] with Cloneable[ArrayStack[T]] with Builder[T, ArrayStack[T]] with Serializable` ###

Simple stack class backed by an array. Should be significantly faster than the
standard mutable stack.

* T
  * type of the elements contained in this array stack.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ArrayStack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayStack.scala#L1)
* Since
  * 2.7
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#array_stacks)
    section on `Array Stacks` for more information.


### `class BitSet extends AbstractSet[Int] with SortedSet[Int] with collection.BitSet with BitSetLike[BitSet] with SetLike[Int, BitSet] with Serializable` ###

A class for mutable bitsets.

Bitsets are sets of non-negative integers which are represented as variable-size
arrays of bits packed into 64-bit words. The memory footprint of a bitset is
determined by the largest number stored in it.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/BitSet.scala#L1)
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#mutable_bitsets)
    section on `Mutable Bitsets` for more information.


### `trait Buffer[A] extends Seq[A] with GenericTraversableTemplate[A, Buffer] with BufferLike[A, Buffer[A]] with scala.Cloneable` ###

Buffers are used to create sequences of elements incrementally by appending,
prepending, or inserting new elements. It is also possible to access and modify
elements in a random access fashion via the index of the element in the current
sequence.

* A
  * type of the elements contained in this buffer.

* Source
  * [Buffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Buffer.scala#L1)
* Version
  * 2.8
* Since
  * 1


### `trait BufferLike[A, +This <: BufferLike[A, This] with Buffer[A]] extends Growable[A] with Shrinkable[A] with Scriptable[A] with Subtractable[A, This] with SeqLike[A, This] with scala.Cloneable` ###

A template trait for buffers of type `Buffer[A]` .

Buffers are used to create sequences of elements incrementally by appending,
prepending, or inserting new elements. It is also possible to access and modify
elements in a random access fashion via the index of the element in the current
sequence.

* A
  * the type of the elements of the buffer
* This
  * the type of the buffer itself.

* Self Type
  * This
* Source
  * [BufferLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/BufferLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8
* Note
  * This trait provides most of the operations of a `Buffer` independently of
    its representation. It is typically inherited by concrete implementations of
    buffers. To implement a concrete buffer, you need to provide implementations
    of the following methods:

    ```scala
    def apply(idx: Int): A
    def update(idx: Int, elem: A)
    def length: Int
    def clear()
    def +=(elem: A): this.type
    def +=:(elem: A): this.type
    def insertAll(n: Int, iter: Traversable[A])
    def remove(n: Int): A
    ```


### `trait BufferProxy[A] extends Buffer[A] with Proxy`                      ###

This is a simple proxy class for `scala.collection.mutable.Buffer`. It is most
useful for assembling customized set abstractions dynamically using object
composition and forwarding.

* A
  * type of the elements the buffer proxy contains.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [BufferProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/BufferProxy.scala#L1)
* Version
  * 1.0, 16/04/2004
* Since
  * 1


### `trait Builder[-Elem, +To] extends Growable[Elem]`                       ###

The base trait of all builders. A builder lets one construct a collection
incrementally, by adding elements to the builder with `+=` and then converting
to the required collection type with `result` .

One cannot assume that a single `Builder` can build more than one instance of
the desired collection. Particular subclasses may allow such behavior.
Otherwise, `result` should be treated as a terminal operation: after it is
called, no further methods should be called on the builder. Extend the
collection.mutable.ReusableBuilder trait instead of `Builder` for builders that
may be reused to build multiple instances.

* Elem
  * the type of elements that get added to the builder.
* To
  * the type of collection that it produced.

* Source
  * [Builder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Builder.scala#L1)
* Since
  * 2.8


### `trait Cloneable[+A <: AnyRef] extends scala.Cloneable`                  ###

A trait for cloneable collections.

* A
  * Type of the elements contained in the collection, covariant and with
    reference types as upperbound.

* Source
  * [Cloneable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Cloneable.scala#L1)
* Since
  * 2.8


### `final class DefaultEntry[A, B] extends HashEntry[A, DefaultEntry[A, B]] with Serializable` ###

Class used internally for default map model.

* Source
  * [DefaultEntry.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DefaultEntry.scala#L1)
* Since
  * 2.3


### `trait DefaultMapModel[A, B] extends Map[A, B]`                          ###

This class is used internally. It implements the mutable `Map` class in terms of
three functions: `findEntry` , `addEntry` , and `entries` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This trait will be removed.
* Source
  * [DefaultMapModel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DefaultMapModel.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `class DoubleLinkedList[A] extends AbstractSeq[A] with LinearSeq[A] with GenericTraversableTemplate[A, DoubleLinkedList] with DoubleLinkedListLike[A, DoubleLinkedList[A]] with Serializable` ###

This class implements double linked lists where both the head ( `elem` ), the
tail ( `next` ) and a reference to the previous node ( `prev` ) are mutable.

* A
  * the type of the elements contained in this double linked list.

* Annotations
  * @ deprecated @ SerialVersionUID ()
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated due to
    idiosyncrasies in interface and incomplete features.
* Source
  * [DoubleLinkedList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DoubleLinkedList.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#double_linked_lists)
    section on `Double Linked Lists` for more information.


### `trait DoubleLinkedListLike[A, This <: Seq[A] with DoubleLinkedListLike[A, This]] extends SeqLike[A, This] with LinkedListLike[A, This]` ###

This extensible class may be used as a basis for implementing double linked
lists. Type variable `A` refers to the element type of the list, type variable
 `This` is used to model self types of linked lists.

The invariant of this data structure is that `prev` is always a reference to the
previous node in the list. If `this` is the first node of the list, `prev` will
be `null` . Field `next` is set to `this` iff the list is empty.

Examples (right arrow represents `next` , left arrow represents `prev` , `_`
represents no value):

```scala
Empty:

null <-- [ _ ] --,
         [   ] <-`

Single element:

null <-- [ x ] --> [ _ ] --,
         [   ] <-- [   ] <-`

More elements:

null <-- [ x ] --> [ y ] --> [ z ] --> [ _ ] --,
         [   ] <-- [   ] <-- [   ] <-- [   ] <-`
```

* A
  * type of the elements contained in the double linked list
* This
  * the type of the actual linked list holding the elements

* Self Type
  * DoubleLinkedListLike [A, This]
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated due to
    idiosyncrasies in interface and incomplete features.
* Source
  * [DoubleLinkedListLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/DoubleLinkedListLike.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 2.8


### `trait FlatHashTable[A] extends HashUtils[A]`                            ###

An implementation class backing a `HashSet` .

This trait is used internally. It can be mixed in with various collections
relying on hash table as an implementation.

* Source
  * [FlatHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/FlatHashTable.scala#L1)


### `class GrowingBuilder[Elem, To <: Growable[Elem]] extends Builder[Elem, To]` ###

The canonical builder for collections that are growable, i.e. that support an
efficient `+=` method which adds an element to the collection.

GrowableBuilders can produce only a single instance of the collection they are
growing.

* Source
  * [GrowingBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/GrowingBuilder.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait HashEntry[A, E] extends AnyRef`                                   ###

Class used internally.

* Source
  * [HashEntry.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashEntry.scala#L1)
* Since
  * 2.8


### `class HashMap[A, B] extends AbstractMap[A, B] with Map[A, B] with MapLike[A, B, HashMap[A, B]] with HashTable[A, DefaultEntry[A, B]] with CustomParallelizable[(A, B), ParHashMap[A, B]] with Serializable` ###

This class implements mutable maps using a hashtable.

* A
  * the type of the keys contained in this hash map.
* B
  * the type of the values assigned to keys in this hash map.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashMap.scala#L1)
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#hash_tables)
    section on `Hash Tables` for more information.


### `class HashSet[A] extends AbstractSet[A] with Set[A] with GenericSetTemplate[A, HashSet] with SetLike[A, HashSet[A]] with FlatHashTable[A] with CustomParallelizable[A, ParHashSet[A]] with Serializable` ###

This class implements mutable sets using a hashtable.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashSet.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#hash_tables)
    section on `Hash Tables` for more information.


### `trait HashTable[A, Entry >: Null <: HashEntry[A, Entry]] extends HashUtils[A]` ###

This class can be used to construct data structures that are based on
hashtables. Class `HashTable[A]` implements a hashtable that maps keys of type
 `A` to values of the fully abstract member type `Entry` . Classes that make use
of `HashTable` have to provide an implementation for `Entry` .

There are mainly two parameters that affect the performance of a hashtable: the
 _initial size_ and the _load factor_ . The _size_ refers to the number of _
buckets_ in the hashtable, and the _load factor_ is a measure of how full the
hashtable is allowed to get before its size is automatically doubled. Both
parameters may be changed by overriding the corresponding values in class
 `HashTable` .

* A
  * type of the elements contained in this hash table.

* Source
  * [HashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashTable.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


### `class History[Evt, Pub] extends AbstractIterable[(Pub, Evt)] with Subscriber[Evt, Pub] with Iterable[(Pub, Evt)] with Serializable` ###

 `History[A, B]` objects may subscribe to events of type `A` published by an
object of type `B` . The history subscriber object records all published events
up to maximum number of `maxHistory` events.

* Evt
  * Type of events.
* Pub
  * Type of publishers.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [History.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/History.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `class ImmutableMapAdaptor[A, B] extends AbstractMap[A, B] with Map[A, B] with Serializable` ###

This class can be used as an adaptor to create mutable maps from immutable map
implementations. Only method `empty` has to be redefined if the immutable map on
which this mutable map is originally based is not empty. `empty` is supposed to
return the representation of an empty map.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Adaptors are inherently unreliable and prone to
    performance problems.
* Source
  * [ImmutableMapAdaptor.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ImmutableMapAdaptor.scala#L1)
* Version
  * 2.0, 01/01/2007
* Since
  * 1


### `class ImmutableSetAdaptor[A] extends AbstractSet[A] with Set[A] with Serializable` ###

This class can be used as an adaptor to create mutable sets from immutable set
implementations. Only method `empty` has to be redefined if the immutable set on
which this mutable set is originally based is not empty. `empty` is supposed to
return the representation of an empty set.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Adaptors are inherently unreliable and prone to
    performance problems.
* Source
  * [ImmutableSetAdaptor.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ImmutableSetAdaptor.scala#L1)
* Version
  * 1.0, 21/07/2003
* Since
  * 1


### `trait IndexedSeq[A] extends Seq[A] with collection.IndexedSeq[A] with GenericTraversableTemplate[A, IndexedSeq] with IndexedSeqLike[A, IndexedSeq[A]]` ###

A subtrait of `collection.IndexedSeq` which represents sequences that can be
mutated.

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeq.scala#L1)


### `trait IndexedSeqLike[A, +Repr] extends collection.IndexedSeqLike[A, Repr]` ###

A subtrait of scala.collection.IndexedSeq which represents sequences that can be
mutated.

It declares a method `update` which allows updating an element at a specific
index in the sequence.

This trait just implements `iterator` in terms of `apply` and `length` .
However, see `IndexedSeqOptimized` for an implementation trait that overrides
operations to make them run faster under the assumption of fast random access
with `apply` .

* A
  * the element type of the mutable indexed sequence
* Repr
  * the type of the actual mutable indexed sequence containing the elements.

* Self Type
  * IndexedSeqLike [A, Repr]
* Source
  * [IndexedSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeqLike.scala#L1)


### `trait IndexedSeqOptimized[A, +Repr] extends IndexedSeqLike[A, Repr] with collection.IndexedSeqOptimized[A, Repr]` ###

A subtrait of scala.collection.IndexedSeq which represents sequences that can be
mutated.

* Source
  * [IndexedSeqOptimized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeqOptimized.scala#L1)
* Since
  * 2.8


### `trait IndexedSeqView[A, +Coll] extends IndexedSeq[A] with IndexedSeqOptimized[A, IndexedSeqView[A, Coll]] with SeqView[A, Coll] with SeqViewLike[A, Coll, IndexedSeqView[A, Coll]]` ###

A non-strict view of a mutable `IndexedSeq` .

A view is a lazy version of some collection. Collection transformers such as
 `map` or `filter` or `++` do not traverse any elements when applied on a view.
Instead they create a new view which simply records that fact that the operation
needs to be applied. The collection elements are accessed, and the view
operations are applied, when a non-view result is needed, or when the `force`
method is called on a view. Some of the operations of this class will yield
again a mutable indexed sequence, others will just yield a plain indexed
sequence of type `collection.IndexedSeq` . Because this is a leaf class there is
no associated `Like` class.

* A
  * the element type of the view
* Coll
  * the type of the underlying collection containing the elements.

* Self Type
  * IndexedSeqView [A, Coll]
* Source
  * [IndexedSeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeqView.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait Iterable[A] extends Traversable[A] with collection.Iterable[A] with GenericTraversableTemplate[A, Iterable] with IterableLike[A, Iterable[A]] with Parallelizable[A, ParIterable[A]]` ###

A base trait for iterable collections that can be mutated.

This is a base trait for all mutable Scala collections that define an
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
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Iterable.scala#L1)


### `abstract class LazyBuilder[Elem, +To] extends ReusableBuilder[Elem, To]` ###

A builder that constructs its result lazily. Iterators or iterables to be added
to this builder with `++=` are not evaluated until `result` is called.

This builder can be reused.

* Elem
  * type of the elements for this builder.
* To
  * type of the collection this builder builds.

* Source
  * [LazyBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LazyBuilder.scala#L1)
* Since
  * 2.8


### `trait LinearSeq[A] extends Seq[A] with collection.LinearSeq[A] with GenericTraversableTemplate[A, LinearSeq] with LinearSeqLike[A, LinearSeq[A]]` ###

A subtrait of `collection.LinearSeq` which represents sequences that can be
mutated.

Linear sequences have reasonably efficient `head` , `tail` , and `isEmpty`
methods. If these methods provide the fastest way to traverse the collection, a
collection `Coll` that extends this trait should also extend
 `LinearSeqOptimized[A, Coll[A]]` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinearSeq.scala#L1)


### `final class LinkedEntry[A, B] extends HashEntry[A, LinkedEntry[A, B]] with Serializable` ###

Class for the linked hash map entry, used internally.

* Source
  * [LinkedEntry.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedEntry.scala#L1)
* Since
  * 2.8


### `class LinkedHashMap[A, B] extends AbstractMap[A, B] with Map[A, B] with MapLike[A, B, LinkedHashMap[A, B]] with HashTable[A, LinkedEntry[A, B]] with Serializable` ###

This class implements mutable maps using a hashtable. The iterator and all
traversal methods of this class visit elements in the order they were inserted.

* A
  * the type of the keys contained in this hash map.
* B
  * the type of the values assigned to keys in this hash map.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [LinkedHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashMap.scala#L1)


### `class LinkedHashSet[A] extends AbstractSet[A] with Set[A] with GenericSetTemplate[A, LinkedHashSet] with SetLike[A, LinkedHashSet[A]] with HashTable[A, Entry[A]] with Serializable` ###

This class implements mutable sets using a hashtable. The iterator and all
traversal methods of this class visit elements in the order they were inserted.

* A
  * the type of the elements contained in this set.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [LinkedHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashSet.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


### `class LinkedList[A] extends AbstractSeq[A] with LinearSeq[A] with GenericTraversableTemplate[A, LinkedList] with LinkedListLike[A, LinkedList[A]] with Serializable` ###

A more traditional/primitive style of linked list where the "list" is also the
"head" link. Links can be manually created and manipulated, though the use of
the API, when possible, is recommended.

The danger of directly manipulating next:

```scala
scala> val b = LinkedList(1)
b: scala.collection.mutable.LinkedList[Int] = LinkedList(1)

scala> b.next = null

scala> println(b)
java.lang.NullPointerException
```

If the list is empty `next` must be set to `this` . The last node in every
mutable linked list is empty.

Examples ( `_` represents no value):

```scala
Empty:

[ _ ] --,
[   ] <-`

Single element:

[ x ] --> [ _ ] --,
          [   ] <-`

More elements:

[ x ] --> [ y ] --> [ z ] --> [ _ ] --,
                              [   ] <-`
```

* A
  * the type of the elements contained in this linked list.

* Annotations
  * @ SerialVersionUID () @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated due to
    idiosyncrasies in interface and incomplete features.
* Source
  * [LinkedList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedList.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#linked_lists)
    section on `Linked Lists` for more information.


### `trait LinkedListLike[A, This <: Seq[A] with LinkedListLike[A, This]] extends SeqLike[A, This]` ###

This extensible class may be used as a basis for implementing linked list. Type
variable `A` refers to the element type of the list, type variable `This` is
used to model self types of linked lists.

If the list is empty `next` must be set to `this` . The last node in every
mutable linked list is empty.

Examples ( `_` represents no value):

```scala
Empty:

[ _ ] --,
[   ] <-`

Single element:

[ x ] --> [ _ ] --,
          [   ] <-`

More elements:

[ x ] --> [ y ] --> [ z ] --> [ _ ] --,
                              [   ] <-`
```

* A
  * type of the elements contained in the linked list
* This
  * the type of the actual linked list holding the elements

* Self Type
  * LinkedListLike [A, This]
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Low-level linked lists are deprecated due to
    idiosyncrasies in interface and incomplete features.
* Source
  * [LinkedListLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedListLike.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 2.8


### `final class ListBuffer[A] extends AbstractBuffer[A] with Buffer[A] with GenericTraversableTemplate[A, ListBuffer] with BufferLike[A, ListBuffer[A]] with ReusableBuilder[A, immutable.List[A]] with SeqForwarder[A] with Serializable` ###

A `Buffer` implementation backed by a list. It provides constant time prepend
and append. Most other operations are linear.

* A
  * the type of this list buffer's elements.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ListBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ListBuffer.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#list_buffers)
    section on `List Buffers` for more information.


### `class ListMap[A, B] extends AbstractMap[A, B] with Map[A, B] with MapLike[A, B, ListMap[A, B]] with Serializable` ###

A simple mutable map backed by a list.

* A
  * the type of the keys contained in this list map.
* B
  * the type of the values assigned to keys in this list map.

* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ListMap.scala#L1)


### `final class LongMap[V] extends AbstractMap[Long, V] with Map[Long, V] with MapLike[Long, V, LongMap[V]] with Serializable` ###

This class implements mutable maps with `Long` keys based on a hash table with
open addressing.

Basic map operations on single entries, including `contains` and `get` , are
typically substantially faster with `LongMap` than HashMap. Methods that act on
the whole map, including `foreach` and `map` are not in general expected to be
faster than with a generic map, save for those that take particular advantage of
the internal structure of the map: `foreachKey` , `foreachValue` ,
 `mapValuesNow` , and `transformValues` .

Maps with open addressing may become less efficient at lookup after repeated
addition/removal of elements. Although `LongMap` makes a decent attempt to
remain efficient regardless, calling `repack` on a map that will no longer have
elements removed but will be used heavily may save both time and storage space.

This map is not intended to contain more than 2 <sup>29 entries (approximately
500 million). The maximum capacity is 2</sup> 30, but performance will degrade
rapidly as 2^30 is approached.

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LongMap.scala#L1)


### `trait Map[A, B] extends Iterable[(A, B)] with collection.Map[A, B] with MapLike[A, B, Map[A, B]]` ###

A base trait for maps that can be mutated.

 *Implementation note:* This trait provides most of the operations of a mutable
 `Map` independently of its representation. It is typically inherited by
concrete implementations of maps.

To implement a concrete mutable map, you need to provide implementations of the
following methods:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def += (kv: (A, B)): This
def -= (key: A): This
```

If you wish that methods like `take` , `drop` , `filter` also return the same
kind of map you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Map.scala#L1)
* Since
  * 1.0


### `class MapBuilder[A, B, Coll <: GenMap[A, B] with GenMapLike[A, B, Coll]] extends ReusableBuilder[(A, B), Coll]` ###

The canonical builder for immutable maps, working with the map's `+` method to
add new elements. Collections are built from their `empty` element using this +
method.

* A
  * Type of the keys for the map this builder creates.
* B
  * Type of the values for the map this builder creates.
* Coll
  * The type of the actual collection this builder builds.

* Source
  * [MapBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MapBuilder.scala#L1)
* Since
  * 2.8


### `trait MapLike[A, B, +This <: MapLike[A, B, This] with Map[A, B]] extends collection.MapLike[A, B, This] with Builder[(A, B), This] with Growable[(A, B)] with Shrinkable[A] with Cloneable[This] with Parallelizable[(A, B), ParMap[A, B]]` ###

A template trait for mutable maps.

 *Implementation note:* This trait provides most of the operations of a mutable
 `Map` independently of its representation. It is typically inherited by
concrete implementations of maps.

To implement a concrete mutable map, you need to provide implementations of the
following methods:

```scala
def get(key: A): Option[B]
def iterator: Iterator[(A, B)]
def += (kv: (A, B)): This
def -= (key: A): This
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
  * [MapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MapLike.scala#L1)


### `trait MapProxy[A, B] extends Map[A, B] with MapProxyLike[A, B, Map[A, B]]` ###

This trait implements a proxy for scala.collection.mutable.Map.

It is most useful for assembling customized map abstractions dynamically using
object composition and forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [MapProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MapProxy.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


### `trait MultiMap[A, B] extends Map[A, Set[B]]`                            ###

A trait for mutable maps with multiple values assigned to a key.

This class is typically used as a mixin. It turns maps which map `A` to
 `Set[B]` objects into multimaps that map `A` to `B` objects.

* Source
  * [MultiMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MultiMap.scala#L1)

Example:

```scala
// first import all necessary types from package `collection.mutable`
import collection.mutable.{ HashMap, MultiMap, Set }
// to create a `MultiMap` the easiest way is to mixin it into a normal
// `Map` instance
val mm = new HashMap[Int, Set[String]] with MultiMap[Int, String]
// to add key-value pairs to a multimap it is important to use
// the method `addBinding` because standard methods like `+` will
// overwrite the complete key-value pair instead of adding the
// value to the existing key
mm.addBinding(1, "a")
mm.addBinding(2, "b")
mm.addBinding(1, "c")
// mm now contains `Map(2 -> Set(b), 1 -> Set(c, a))`
// to check if the multimap contains a value there is method
// `entryExists`, which allows to traverse the including set
mm.entryExists(1, _ == "a") == true
mm.entryExists(1, _ == "b") == false
mm.entryExists(2, _ == "b") == true
// to remove a previous added value there is the method `removeBinding`
mm.removeBinding(1, "a")
mm.entryExists(1, _ == "a") == false
```


### `class MutableList[A] extends AbstractSeq[A] with LinearSeq[A] with LinearSeqOptimized[A, MutableList[A]] with GenericTraversableTemplate[A, MutableList] with Builder[A, MutableList[A]] with Serializable` ###

This class is used internally to represent mutable lists. It is the basis for
the implementation of the class `Queue` .

* Annotations
  * @ SerialVersionUID ()
* Source
  * [MutableList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MutableList.scala#L1)
* Version
  * 2.8
* Since
  * 1


### `trait ObservableBuffer[A] extends Buffer[A] with Publisher[Message[A] with Undoable]` ###

This class is typically used as a mixin. It adds a subscription mechanism to the
 `Buffer` class into which this abstract class is mixed in. Class
 `ObservableBuffer` publishes events of the type `Message` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Observables are deprecated because scripting is
    deprecated.
* Source
  * [ObservableBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ObservableBuffer.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `trait ObservableMap[A, B] extends Map[A, B] with Publisher[Message[(A, B)] with Undoable]` ###

This class is typically used as a mixin. It adds a subscription mechanism to the
 `Map` class into which this abstract class is mixed in. Class `ObservableMap`
publishes events of the type `Message` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Observables are deprecated because scripting is
    deprecated.
* Source
  * [ObservableMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ObservableMap.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


### `trait ObservableSet[A] extends Set[A] with Publisher[Message[A] with Undoable]` ###

This class is typically used as a mixin. It adds a subscription mechanism to the
 `Set` class into which this abstract class is mixed in. Class `ObservableSet`
publishes events of the type `Message` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Observables are deprecated because scripting is
    deprecated.
* Source
  * [ObservableSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ObservableSet.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `class OpenHashMap[Key, Value] extends AbstractMap[Key, Value] with Map[Key, Value] with MapLike[Key, Value, OpenHashMap[Key, Value]]` ###

A mutable hash map based on an open hashing scheme. The precise scheme is
undefined, but it should make a reasonable effort to ensure that an insert with
consecutive hash codes is not unnecessarily penalised. In particular, mappings
of consecutive integer keys should work without significant performance loss.

* Key
  * type of the keys in this map.
* Value
  * type of the values in this map.

* Source
  * [OpenHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/OpenHashMap.scala#L1)
* Since
  * 2.7


### `class PriorityQueue[A] extends AbstractIterable[A] with Iterable[A] with GenericOrderedTraversableTemplate[A, PriorityQueue] with IterableLike[A, PriorityQueue[A]] with Growable[A] with Builder[A, PriorityQueue[A]] with Serializable with scala.Cloneable` ###

This class implements priority queues using a heap. To prioritize elements of
type A there must be an implicit Ordering[A] available at creation.

Only the `dequeue` and `dequeueAll` methods will return elements in priority
order (while removing elements from the heap). Standard collection methods
including `drop` , `iterator` , and `toString` will remove or traverse the heap
in whichever order seems most convenient.

Therefore, printing a `PriorityQueue` will not reveal the priority order of the
elements, though the highest-priority element will be printed first. To print
the elements in order, one must duplicate the `PriorityQueue` (by using `clone` ,
for instance) and then dequeue them:

* A
  * type of the elements in this priority queue.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [PriorityQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/PriorityQueue.scala#L1)
* Version
  * 1.0, 03/05/2004
* Since
  * 1

Example:

```scala
val pq = collection.mutable.PriorityQueue(1, 2, 5, 3, 7)
println(pq)                  // elements probably not in order
println(pq.clone.dequeueAll) // prints Vector(7, 5, 3, 2, 1)
```


### `abstract class PriorityQueueProxy[A] extends PriorityQueue[A] with Proxy` ###

This class servers as a proxy for priority queues. The elements of the queue
have to be ordered in terms of the `Ordered[T]` class.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [PriorityQueueProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/PriorityQueueProxy.scala#L1)
* Version
  * 1.0, 03/05/2004
* Since
  * 1


### `trait Publisher[Evt] extends AnyRef`                                    ###

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


### `class Queue[A] extends MutableList[A] with LinearSeqOptimized[A, Queue[A]] with GenericTraversableTemplate[A, Queue] with Cloneable[Queue[A]] with Serializable` ###

 `Queue` objects implement data structures that allow to insert and retrieve
elements in a first-in-first-out (FIFO) manner.

* Source
  * [Queue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Queue.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#queues)
    section on `Queues` for more information.


### `trait QueueProxy[A] extends Queue[A] with Proxy`                        ###

 `Queue` objects implement data structures that allow to insert and retrieve
elements in a first-in-first-out (FIFO) manner.

* A
  * type of the elements in this queue proxy.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [QueueProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/QueueProxy.scala#L1)
* Version
  * 1.1, 03/05/2004
* Since
  * 1


### `trait ResizableArray[A] extends IndexedSeq[A] with GenericTraversableTemplate[A, ResizableArray] with IndexedSeqOptimized[A, ResizableArray[A]]` ###

This class is used internally to implement data structures that are based on
resizable arrays.

* A
  * type of the elements contained in this resizable array.

* Source
  * [ResizableArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ResizableArray.scala#L1)
* Version
  * 2.8
* Since
  * 1


### `trait ReusableBuilder[-Elem, +To] extends Builder[Elem, To]`            ###

 `ReusableBuilder` is a marker trait that indicates that a `Builder` can be
reused to build more than one instance of a collection. In particular, calling
 `result` followed by `clear` will produce a collection and reset the builder to
begin building a new collection of the same type.

It is up to subclasses to implement this behavior, and to document any other
behavior that varies from standard `ReusableBuilder` usage (e.g. operations
being well-defined after a call to `result` , or allowing multiple calls to
result to obtain different snapshots of a collection under construction).

* Elem
  * the type of elements that get added to the builder.
* To
  * the type of collection that it produced.

* Source
  * [ReusableBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ReusableBuilder.scala#L1)
* Since
  * 2.12


### `class RevertibleHistory[Evt <: Undoable, Pub] extends History[Evt, Pub] with Undoable with Serializable` ###

A revertible history is a `History` object which supports an undo operation.
Type variable `Evt` refers to the type of the published events, `Pub` denotes
the publisher type. Type `Pub` is typically a subtype of `Publisher` .

* Evt
  * type of the events
* Pub
  * type of the publisher

* Source
  * [RevertibleHistory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/RevertibleHistory.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 2.8


### `trait Seq[A] extends Iterable[A] with collection.Seq[A] with GenericTraversableTemplate[A, Seq] with SeqLike[A, Seq[A]]` ###

A subtrait of `collection.Seq` which represents sequences that can be mutated.

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

The class adds an `update` method to `collection.Seq` .

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Seq.scala#L1)


### `trait SeqLike[A, +This <: SeqLike[A, This] with Seq[A]] extends collection.SeqLike[A, This] with Cloneable[This] with Parallelizable[A, ParSeq[A]]` ###

A template trait for mutable sequences of type `mutable.Seq[A]` .

* A
  * the type of the elements of the set
* This
  * the type of the set itself.

* Self Type
  * SeqLike [A, This]
* Source
  * [SeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SeqLike.scala#L1)


### `trait Set[A] extends Iterable[A] with collection.Set[A] with GenericSetTemplate[A, Set] with SetLike[A, Set[A]]` ###

A generic trait for mutable sets.

To implement a concrete mutable set, you need to provide implementations of the
following methods:

```scala
def contains(elem: A): Boolean
def iterator: Iterator[A]
def += (elem: A): this.type
def -= (elem: A): this.type
```

If you wish that methods like `take` , `drop` , `filter` return the same kind of
set, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Set.scala#L1)
* Since
  * 1.0


### `class SetBuilder[A, Coll <: collection.Set[A] with collection.SetLike[A, Coll]] extends ReusableBuilder[A, Coll]` ###

The canonical builder for mutable Sets.

* A
  * The type of the elements that will be contained in this set.
* Coll
  * The type of the actual collection this set builds.

* Source
  * [SetBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SetBuilder.scala#L1)
* Since
  * 2.8


### `trait SetLike[A, +This <: SetLike[A, This] with Set[A]] extends collection.SetLike[A, This] with Scriptable[A] with Builder[A, This] with Growable[A] with Shrinkable[A] with Cloneable[Set[A]] with Parallelizable[A, ParSet[A]]` ###

A template trait for mutable sets of type `mutable.Set[A]` .

This trait provides most of the operations of a `mutable.Set` independently of
its representation. It is typically inherited by concrete implementations of
sets.

To implement a concrete mutable set, you need to provide implementations of the
following methods:

```scala
def contains(elem: A): Boolean
def iterator: Iterator[A]
def += (elem: A): this.type
def -= (elem: A): this.type
```

If you wish that methods like `take` , `drop` , `filter` return the same kind of
set, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* A
  * the type of the elements of the set
* This
  * the type of the set itself.

* Self Type
  * SetLike [A, This]
* Source
  * [SetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SetLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait SetProxy[A] extends Set[A] with SetProxyLike[A, Set[A]]`          ###

This is a simple wrapper class for scala.collection.mutable.Set. It is most
useful for assembling customized set abstractions dynamically using object
composition and forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SetProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SetProxy.scala#L1)
* Version
  * 1.1, 09/05/2004
* Since
  * 1


### `trait SortedMap[A, B] extends Map[A, B] with collection.SortedMap[A, B] with MapLike[A, B, SortedMap[A, B]] with SortedMapLike[A, B, SortedMap[A, B]]` ###

A mutable map whose keys are sorted.

* A
  * the type of the keys contained in this sorted map.
* B
  * the type of the values associated with the keys.

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedMap.scala#L1)
* Version
  * 2.12
* Since
  * 2.12


### `trait SortedSet[A] extends collection.SortedSet[A] with SortedSetLike[A, SortedSet[A]] with Set[A] with SetLike[A, SortedSet[A]]` ###

Base trait for mutable sorted set.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedSet.scala#L1)


### `class Stack[A] extends AbstractSeq[A] with Seq[A] with SeqLike[A, Stack[A]] with GenericTraversableTemplate[A, Stack] with Cloneable[Stack[A]] with Serializable` ###

A stack implements a data structure which allows to store and retrieve objects
in a last-in-first-out (LIFO) fashion.

* A
  * type of the elements contained in this stack.

* Source
  * [Stack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Stack.scala#L1)
* Version
  * 2.8
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#stacks)
    section on `Stacks` for more information.


### `trait StackProxy[A] extends Stack[A] with Proxy`                        ###

A stack implements a data structure which allows to store and retrieve objects
in a last-in-first-out (LIFO) fashion.

* A
  * type of the elements in this stack proxy.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [StackProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/StackProxy.scala#L1)
* Version
  * 1.0, 10/05/2004
* Since
  * 1


### `final class StringBuilder extends AbstractSeq[Char] with CharSequence with IndexedSeq[Char] with StringLike[StringBuilder] with ReusableBuilder[Char, String] with Serializable` ###

A builder for mutable sequence of characters. This class provides an API mostly
compatible with `java.lang.StringBuilder` , except where there are conflicts
with the Scala collections API (such as the `reverse` method.)

* Annotations
  * @ SerialVersionUID ()
* Source
  * [StringBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/StringBuilder.scala#L1)
* Version
  * 2.8
* Since
  * 2.7


### `trait Subscriber[-Evt, -Pub] extends AnyRef`                            ###

 `Subscriber[A, B]` objects may subscribe to events of type `A` published by an
object of type `B` . `B` is typically a subtype of
scala.collection.mutable.Publisher.

* Source
  * [Subscriber.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Subscriber.scala#L1)
* Version
  * 2.8
* Since
  * 1


### `trait SynchronizedBuffer[A] extends Buffer[A]`                          ###

This class should be used as a mixin. It synchronizes the `Buffer` methods of
the class into which it is mixed in.

* A
  * type of the elements contained in this buffer.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Synchronization via traits is deprecated as it is
    inherently unreliable. Consider java.util.concurrent.ConcurrentLinkedQueue
    as an alternative.
* Source
  * [SynchronizedBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedBuffer.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `trait SynchronizedMap[A, B] extends Map[A, B]`                          ###

This class should be used as a mixin. It synchronizes the `Map` functions of the
class into which it is mixed in.

* A
  * type of the keys contained in this map.
* B
  * type of the values associated with keys.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Synchronization via traits is deprecated as it is
    inherently unreliable. Consider java.util.concurrent.ConcurrentHashMap as an
    alternative.
* Source
  * [SynchronizedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedMap.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


### `class SynchronizedPriorityQueue[A] extends PriorityQueue[A]`            ###

This class implements synchronized priority queues using a binary heap. The
elements of the queue have to be ordered in terms of the `Ordered[T]` class.

* A
  * type of the elements contained in this synchronized priority queue

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Comprehensive synchronization via selective
    overriding of methods is inherently unreliable. Consider
    java.util.concurrent.ConcurrentSkipListSet as an alternative.
* Source
  * [SynchronizedPriorityQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedPriorityQueue.scala#L1)
* Version
  * 1.0, 03/05/2004
* Since
  * 1


### `class SynchronizedQueue[A] extends Queue[A]`                            ###

This is a synchronized version of the `Queue[T]` class. It implements a data
structure that allows one to insert and retrieve elements in a
first-in-first-out (FIFO) manner.

* A
  * type of elements contained in this synchronized queue.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Synchronization via selective overriding of methods
    is inherently unreliable. Consider
    java.util.concurrent.ConcurrentLinkedQueue as an alternative.
* Source
  * [SynchronizedQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedQueue.scala#L1)
* Version
  * 1.0, 03/05/2004
* Since
  * 1


### `trait SynchronizedSet[A] extends Set[A]`                                ###

This class should be used as a mixin. It synchronizes the `Set` functions of the
class into which it is mixed in.

* A
  * type of the elements contained in this synchronized set.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Synchronization via traits is deprecated as it is
    inherently unreliable. Consider
    java.util.concurrent.ConcurrentHashMap[A,Unit] as an alternative.
* Source
  * [SynchronizedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedSet.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `class SynchronizedStack[A] extends Stack[A]`                            ###

This is a synchronized version of the `Stack[T]` class. It implements a data
structure which allows to store and retrieve objects in a last-in-first-out
(LIFO) fashion.

* A
  * type of the elements contained in this stack.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Synchronization via selective overriding of methods
    is inherently unreliable. Consider
    java.util.concurrent.LinkedBlockingDequeue instead.
* Source
  * [SynchronizedStack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SynchronizedStack.scala#L1)
* Version
  * 1.0, 03/05/2004
* Since
  * 1


### `trait Traversable[A] extends collection.Traversable[A] with GenericTraversableTemplate[A, Traversable] with TraversableLike[A, Traversable[A]] with Mutable` ###

A trait for traversable collections that can be mutated.

This is a base trait of all kinds of mutable Scala collections. It implements
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
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Traversable.scala#L1)


### `sealed class TreeMap[A, B] extends AbstractSortedMap[A, B] with SortedMap[A, B] with MapLike[A, B, TreeMap[A, B]] with SortedMapLike[A, B, TreeMap[A, B]] with Serializable` ###

A mutable sorted map implemented using a mutable red-black tree as underlying
data structure.

* A
  * the type of the keys contained in this tree map.
* B
  * the type of the values associated with the keys.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [TreeMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeMap.scala#L1)
* Version
  * 2.12
* Since
  * 2.12


### `sealed class TreeSet[A] extends AbstractSortedSet[A] with SortedSet[A] with SetLike[A, TreeSet[A]] with SortedSetLike[A, TreeSet[A]] with Serializable` ###

A mutable sorted set implemented using a mutable red-black tree as underlying
data structure.

* A
  * the type of the keys contained in this tree set.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeSet.scala#L1)
* Version
  * 2.12
* Since
  * 2.10


### `trait Undoable extends AnyRef`                                          ###

Classes that mix in the `Undoable` class provide an operation `undo` which can
be used to undo the last operation.

* Source
  * [Undoable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Undoable.scala#L1)
* Version
  * 1.0, 08/07/2003
* Since
  * 1


### `class UnrolledBuffer[T] extends AbstractBuffer[T] with Buffer[T] with BufferLike[T, UnrolledBuffer[T]] with GenericClassTagTraversableTemplate[T, UnrolledBuffer] with Builder[T, UnrolledBuffer[T]] with Serializable` ###

A buffer that stores elements in an unrolled linked list.

Unrolled linked lists store elements in linked fixed size arrays.

Unrolled buffers retain locality and low memory overhead properties of array
buffers, but offer much more efficient element addition, since they never
reallocate and copy the internal array.

However, they provide `O(n/m)` complexity random access, where `n` is the number
of elements, and `m` the size of internal array chunks.

Ideal to use when:

* elements are added to the buffer and then all of the elements are traversed
   sequentially
* two unrolled buffers need to be concatenated (see `concat` )

Better than singly linked lists for random access, but should still be avoided
for such a purpose.

* Annotations
  * @ SerialVersionUID () @ deprecatedInheritance (message =..., since =
    "2.11.0")
* Source
  * [UnrolledBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/UnrolledBuffer.scala#L1)


### `class WeakHashMap[A, B] extends convert.Wrappers.JMapWrapper[A, B] with convert.Wrappers.JMapWrapperLike[A, B, WeakHashMap[A, B]]` ###

A hash map with references to entries which are weakly reachable. Entries are
removed from this map when the key is no longer (strongly) referenced. This
class wraps `java.util.WeakHashMap` .

* A
  * type of keys contained in this map
* B
  * type of values associated with the keys

* Source
  * [WeakHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WeakHashMap.scala#L1)
* Since
  * 2.8
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#weak_hash_maps)
    section on `Weak Hash Maps` for more information.


### `abstract class WrappedArray[T] extends AbstractSeq[T] with IndexedSeq[T] with ArrayLike[T, WrappedArray[T]] with CustomParallelizable[T, ParArray[T]]` ###

A class representing `Array[T]` .

* T
  * type of the elements in this wrapped array.

* Source
  * [WrappedArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WrappedArray.scala#L1)
* Version
  * 1.0
* Since
  * 2.8


### `class WrappedArrayBuilder[A] extends ReusableBuilder[A, WrappedArray[A]]` ###

A builder class for arrays.

This builder can be reused.

* A
  * type of elements that can be added to this builder.

* Source
  * [WrappedArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WrappedArrayBuilder.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object AnyRefMap extends Serializable`                                  ###

* Source
  * [AnyRefMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/AnyRefMap.scala#L1)


### `object ArrayBuffer extends SeqFactory[ArrayBuffer] with Serializable`   ###

Factory object for the `ArrayBuffer` class.

This object provides a set of operations to create `ArrayBuffer` values.

* Source
  * [ArrayBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuffer.scala#L1)


### `object ArrayBuilder extends Serializable`                               ###

A companion object for array builders.

* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)
* Since
  * 2.8


### `object ArrayOps`                                                        ###

A companion object for `ArrayOps` .

* Source
  * [ArrayOps.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayOps.scala#L1)
* Since
  * 2.8


### `object ArraySeq extends SeqFactory[ArraySeq] with Serializable`         ###

This object provides a set of operations to create `ArraySeq` values.

* Source
  * [ArraySeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArraySeq.scala#L1)


### `object ArrayStack extends SeqFactory[ArrayStack] with Serializable`     ###

Factory object for the `ArrayStack` class.

This object provides a set of operations to create `ArrayStack` values.

* Source
  * [ArrayStack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayStack.scala#L1)


### `object BitSet extends BitSetFactory[BitSet] with Serializable`          ###

This object provides a set of operations to create `BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/BitSet.scala#L1)


### `object Buffer extends SeqFactory[Buffer]`                               ###

This object provides a set of operations to create `Buffer` values.

* Source
  * [Buffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Buffer.scala#L1)


### `object HashMap extends MutableMapFactory[HashMap] with Serializable`    ###

This object provides a set of operations needed to create `mutable.HashMap`
values.

* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashMap.scala#L1)


### `object HashSet extends MutableSetFactory[HashSet] with Serializable`    ###

This object provides a set of operations needed to create `mutable.HashSet`
values.

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashSet.scala#L1)


### `object IndexedSeq extends SeqFactory[IndexedSeq]`                       ###

This object provides a set of operations to create `mutable.IndexedSeq` values.
The current default implementation of a `mutable.IndexedSeq` is an
 `ArrayBuffer` .

* Source
  * [IndexedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeq.scala#L1)


### `object IndexedSeqView`                                                  ###

An object containing the necessary implicit definitions to make `SeqView` s
work. Its definitions are generally not accessed directly by clients.

Note that the `canBuildFrom` factories yield `SeqView` s, not `IndexedSeqView`
s. This is intentional, because not all operations yield again a
 `mutable.IndexedSeqView` . For instance, `map` just gives a `SeqView` , which
reflects the fact that `map` cannot do its work and maintain a pointer into the
original indexed sequence.

* Source
  * [IndexedSeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeqView.scala#L1)


### `object Iterable extends GenTraversableFactory[Iterable] with TraversableFactory[Iterable]` ###

This object provides a set of operations to create `mutable.Iterable` values.
The current default implementation of a `mutable.Iterable` is an `ArrayBuffer` .

* Source
  * [Iterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Iterable.scala#L1)


### `object LinearSeq extends SeqFactory[LinearSeq]`                         ###

This object provides a set of operations to create `mutable.LinearSeq` values.
The current default implementation of a `mutable.LinearSeq` is a `MutableList` .

* Source
  * [LinearSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinearSeq.scala#L1)


### `object LinkedHashMap extends MutableMapFactory[LinkedHashMap] with Serializable` ###

This object provides a set of operations needed to create `LinkedHashMap`
values.

* Source
  * [LinkedHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashMap.scala#L1)


### `object LinkedHashSet extends MutableSetFactory[LinkedHashSet] with Serializable` ###

This object provides a set of operations needed to create `LinkedHashSet`
values.

* Source
  * [LinkedHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashSet.scala#L1)


### `object ListBuffer extends SeqFactory[ListBuffer] with Serializable`     ###

This object provides a set of operations to create `ListBuffer` values.

* Source
  * [ListBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ListBuffer.scala#L1)


### `object ListMap extends MutableMapFactory[ListMap] with Serializable`    ###

This object provides a set of operations needed to create `mutable.ListMap`
values.

* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ListMap.scala#L1)


### `object LongMap extends Serializable`                                    ###

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LongMap.scala#L1)


### `object Map extends MutableMapFactory[Map]`                              ###

This object provides a set of operations needed to create `mutable.Map` values.
The current default implementation of a `mutable.Map` is a `HashMap` .

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Map.scala#L1)


### `object MutableList extends SeqFactory[MutableList] with Serializable`   ###

* Source
  * [MutableList.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MutableList.scala#L1)


### `object OpenHashMap`                                                     ###

* Source
  * [OpenHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/OpenHashMap.scala#L1)


### `object PriorityQueue extends OrderedTraversableFactory[PriorityQueue] with Serializable` ###

* Source
  * [PriorityQueue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/PriorityQueue.scala#L1)


### `object Queue extends SeqFactory[Queue] with Serializable`               ###

* Source
  * [Queue.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Queue.scala#L1)


### `object ResizableArray extends SeqFactory[ResizableArray]`               ###

* Source
  * [ResizableArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ResizableArray.scala#L1)


### `object Seq extends SeqFactory[Seq]`                                     ###

This object provides a set of operations to create `mutable.Seq` values. The
current default implementation of a `mutable.Seq` is an `ArrayBuffer` .

* Source
  * [Seq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Seq.scala#L1)


### `object Set extends MutableSetFactory[Set]`                              ###

This object provides a set of operations needed to create `mutable.Set` values.
The current default implementation of a `mutable.Set` is a `HashSet` .

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Set.scala#L1)


### `object SortedMap extends MutableSortedMapFactory[SortedMap]`            ###

This object provides a set of operations needed to create sorted maps of type
 `mutable.SortedMap` .

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedMap.scala#L1)


### `object SortedSet extends MutableSortedSetFactory[SortedSet]`            ###

A template for mutable sorted set companion objects.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedSet.scala#L1)


### `object Stack extends SeqFactory[Stack] with Serializable`               ###

Factory object for the `mutable.Stack` class.

This object provides a set of operations to create `mutable.Stack` values.

* Source
  * [Stack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Stack.scala#L1)


### `object StringBuilder extends Serializable`                              ###

* Source
  * [StringBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/StringBuilder.scala#L1)


### `object Traversable extends GenTraversableFactory[Traversable] with TraversableFactory[Traversable]` ###

This object provides a set of operations to create `mutable.Traversable` values.
The current default implementation of a `mutable.Traversable` is an
 `ArrayBuffer` .

* Source
  * [Traversable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Traversable.scala#L1)


### `object TreeMap extends MutableSortedMapFactory[TreeMap] with Serializable` ###

This object provides a set of operations needed to create sorted maps of type
 `mutable.TreeMap` .

* Source
  * [TreeMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeMap.scala#L1)


### `object TreeSet extends MutableSortedSetFactory[TreeSet] with Serializable` ###

* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeSet.scala#L1)


### `object UnrolledBuffer extends ClassTagTraversableFactory[UnrolledBuffer] with Serializable` ###

* Source
  * [UnrolledBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/UnrolledBuffer.scala#L1)


### `object WeakHashMap extends MutableMapFactory[WeakHashMap] with Serializable` ###

This object provides a set of operations needed to create `WeakHashMap` values.

* Source
  * [WeakHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WeakHashMap.scala#L1)


### `object WrappedArray`                                                    ###

A companion object used to create instances of `WrappedArray` .

* Source
  * [WrappedArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WrappedArray.scala#L1)

