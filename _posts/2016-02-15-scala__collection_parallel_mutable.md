
#                      scala.collection.parallel.mutable                      #

```scala
package mutable
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait LazyCombiner[Elem, +To, Buff <: Growable[Elem] with Sizing] extends Combiner[Elem, To]` ###

Implements combining contents of two combiners by postponing the operation until
 `result` method is called. It chains the leaf results together instead of
evaluating the actual collection.

* Elem
  * the type of the elements in the combiner
* To
  * the type of the collection the combiner produces
* Buff
  * the type of the buffers that contain leaf results and this combiner chains
    together

* Source
  * [LazyCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/LazyCombiner.scala#L1)


### `class ParArray[T] extends ParSeq[T] with GenericParTemplate[T, ParArray] with ParSeqLike[T, ParArray[T], ArraySeq[T]] with Serializable` ###

Parallel sequence holding elements in a linear array.

 `ParArray` is a parallel sequence with a predefined size. The size of the array
cannot be changed after it's been created.

 `ParArray` internally keeps an array containing the elements. This means that
bulk operations based on traversal ensure fast access to elements. `ParArray`
uses lazy builders that create the internal data array only after the size of
the array is known. In the meantime, they keep the result set fragmented. The
fragments are copied into the resulting data array in parallel using fast array
copy operations once all the combiners are populated in parallel.

* T
  * type of the elements in the array

* Self Type
  * ParArray [T]
* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParArray.scala#L1)
* Since
  * 2.9
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_array)
    section on `ParArray` for more information.


### `type ParArrayCombiner[T] = ResizableParArrayCombiner[T]`                ###


### `trait ParFlatHashTable[T] extends FlatHashTable[T]`                     ###

Parallel flat hash table.

* T
  * type of the elements in the table.

* Source
  * [ParFlatHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParFlatHashTable.scala#L1)


### `class ParHashMap[K, V] extends ParMap[K, V] with GenericParMapTemplate[K, V, ParHashMap] with ParMapLike[K, V, ParHashMap[K, V], HashMap[K, V]] with ParHashTable[K, DefaultEntry[K, V]] with Serializable` ###

A parallel hash map.

 `ParHashMap` is a parallel map which internally keeps elements within a hash
table. It uses chaining to resolve collisions.

* K
  * type of the keys in the parallel hash map
* V
  * type of the values in the parallel hash map

* Self Type
  * ParHashMap [K, V]
* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashMap.scala#L1)


### `class ParHashSet[T] extends ParSet[T] with GenericParTemplate[T, ParHashSet] with ParSetLike[T, ParHashSet[T], HashSet[T]] with ParFlatHashTable[T] with Serializable` ###

A parallel hash set.

 `ParHashSet` is a parallel set which internally keeps elements within a hash
table. It uses linear probing to resolve collisions.

* T
  * type of the elements in the parallel hash set.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashSet.scala#L1)


### `trait ParHashTable[K, Entry >: Null <: HashEntry[K, Entry]] extends HashTable[K, Entry]` ###

Provides functionality for hash tables with linked list buckets, enriching the
data structure by fulfilling certain requirements for their parallel
construction and iteration.

* Source
  * [ParHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashTable.scala#L1)


### `trait ParIterable[T] extends GenIterable[T] with parallel.ParIterable[T] with GenericParTemplate[T, ParIterable] with ParIterableLike[T, ParIterable[T], Iterable[T]] with Mutable` ###

A template trait for mutable parallel iterable collections.

This is a base trait for Scala parallel collections. It defines behaviour common
to all parallel collections. Concrete parallel collections should inherit this
trait and `ParIterable` if they want to define specific combiner factories.

Parallel operations are implemented with divide and conquer style algorithms
that parallelize well. The basic idea is to split the collection into smaller
parts until they are small enough to be operated on sequentially.

All of the parallel operations are implemented as tasks within this trait. Tasks
rely on the concept of splitters, which extend iterators. Every parallel
collection defines:

```scala
def splitter: IterableSplitter[T]
```

which returns an instance of `IterableSplitter[T]` , which is a subtype of
 `Splitter[T]` . Splitters have a method `remaining` to check the remaining
number of elements, and method `split` which is defined by splitters. Method
 `split` divides the splitters iterate over into disjunct subsets:

```scala
def split: Seq[Splitter]
```

which splits the splitter into a sequence of disjunct subsplitters. This is
typically a very fast operation which simply creates wrappers around the
receiver collection. This can be repeated recursively.

Tasks are scheduled for execution through a
scala.collection.parallel.TaskSupport object, which can be changed through the
 `tasksupport` setter of the collection.

Method `newCombiner` produces a new combiner. Combiners are an extension of
builders. They provide a method `combine` which combines two combiners and
returns a combiner containing elements of both combiners. This method can be
implemented by aggressively copying all the elements into the new combiner or by
lazily binding their results. It is recommended to avoid copying all of the
elements for performance reasons, although that cost might be negligible
depending on the use case. Standard parallel collection combiners avoid copying
when merging results, relying either on a two-step lazy construction or specific
data-structure properties.

Methods:

```scala
def seq: Sequential
def par: Repr
```

produce the sequential or parallel implementation of the collection,
respectively. Method `par` just returns a reference to this parallel collection.
Method `seq` is efficient - it will not copy the elements. Instead, it will
create a sequential version of the collection using the same underlying data
structure. Note that this is not the case for sequential collections in general
- they may copy the elements and produce a different underlying data structure.

The combination of methods `toMap` , `toSeq` or `toSet` along with `par` and
 `seq` is a flexible way to change between different collection types.

Since this trait extends the `GenIterable` trait, methods like `size` must also
be implemented in concrete collections, while `iterator` forwards to `splitter`
by default.

Each parallel collection is bound to a specific fork/join pool, on which dormant
worker threads are kept. The fork/join pool contains other information such as
the parallelism level, that is, the number of processors used. When a collection
is created, it is assigned the default fork/join pool found in the
 `scala.parallel` package object.

Parallel collections are not necessarily ordered in terms of the `foreach`
operation (see `Traversable` ). Parallel sequences have a well defined order for
iterators - creating an iterator and traversing the elements linearly will
always yield the same order. However, bulk operations such as `foreach` , `map`
or `filter` always occur in undefined orders for all parallel collections.

Existing parallel collection implementations provide strict parallel iterators.
Strict parallel iterators are aware of the number of elements they have yet to
traverse. It's also possible to provide non-strict parallel iterators, which do
not know the number of elements remaining. To do this, the new collection
implementation must override `isStrictSplitterCollection` to `false` . This will
make some operations unavailable.

To create a new parallel collection, extend the `ParIterable` trait, and
implement `size` , `splitter` , `newCombiner` and `seq` . Having an implicit
combiner factory requires extending this trait in addition, as well as providing
a companion object, as with regular collections.

Method `size` is implemented as a constant time operation for parallel
collections, and parallel collection operations rely on this assumption.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* T
  * the element type of the collection

* Source
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParIterable.scala#L1)
* Since
  * 2.9


### `trait ParMap[K, V] extends GenMap[K, V] with parallel.ParMap[K, V] with ParIterable[(K, V)] with GenericParMapTemplate[K, V, ParMap] with ParMapLike[K, V, ParMap[K, V], mutable.Map[K, V]]` ###

A template trait for mutable parallel maps.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* K
  * the key type of the map
* V
  * the value type of the map

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParMap.scala#L1)
* Since
  * 2.9


### `trait ParMapLike[K, V, +Repr <: ParMapLike[K, V, Repr, Sequential] with ParMap[K, V], +Sequential <: mutable.Map[K, V] with mutable.MapLike[K, V, Sequential]] extends GenMapLike[K, V, Repr] with parallel.ParMapLike[K, V, Repr, Sequential] with Growable[(K, V)] with Shrinkable[K] with mutable.Cloneable[Repr]` ###

A template trait for mutable parallel maps. This trait is to be mixed in with
concrete parallel maps to override the representation type.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* K
  * the key type of the map
* V
  * the value type of the map

* Source
  * [ParMapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParMapLike.scala#L1)


### `trait ParSeq[T] extends GenSeq[T] with ParIterable[T] with parallel.ParSeq[T] with GenericParTemplate[T, ParSeq] with ParSeqLike[T, ParSeq[T], mutable.Seq[T]]` ###

A mutable variant of `ParSeq` .

* Self Type
  * ParSeq [T]
* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParSeq.scala#L1)


### `trait ParSet[T] extends GenSet[T] with ParIterable[T] with parallel.ParSet[T] with GenericParTemplate[T, ParSet] with ParSetLike[T, ParSet[T], mutable.Set[T]]` ###

A mutable variant of `ParSet` .

* Self Type
  * ParSet [T]
* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParSet.scala#L1)


### `trait ParSetLike[T, +Repr <: ParSetLike[T, Repr, Sequential] with ParSet[T], +Sequential <: mutable.Set[T] with mutable.SetLike[T, Sequential]] extends GenSetLike[T, Repr] with ParIterableLike[T, Repr, Sequential] with parallel.ParSetLike[T, Repr, Sequential] with Growable[T] with Shrinkable[T] with mutable.Cloneable[Repr]` ###

A template trait for mutable parallel sets. This trait is mixed in with concrete
parallel sets to override the representation type.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* T
  * the element type of the set

* Self Type
  * ParSetLike [T, Repr, Sequential]
* Source
  * [ParSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParSetLike.scala#L1)


### `final class ParTrieMap[K, V] extends ParMap[K, V] with GenericParMapTemplate[K, V, ParTrieMap] with ParMapLike[K, V, ParTrieMap[K, V], TrieMap[K, V]] with ParTrieMapCombiner[K, V] with Serializable` ###

Parallel TrieMap collection.

It has its bulk operations parallelized, but uses the snapshot operation to
create the splitter. This means that parallel bulk operations can be called
concurrently with the modifications.

* Source
  * [ParTrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParTrieMap.scala#L1)
* Since
  * 2.10
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_concurrent_tries)
    section on `ParTrieMap` for more information.


### `trait ResizableParArrayCombiner[T] extends LazyCombiner[T, ParArray[T], ExposedArrayBuffer[T]]` ###

An array combiner that uses a chain of arraybuffers to store elements.

* Source
  * [ResizableParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ResizableParArrayCombiner.scala#L1)


### `trait UnrolledParArrayCombiner[T] extends Combiner[T, ParArray[T]]`     ###

An array combiner that uses doubling unrolled buffers to store elements.

* Source
  * [UnrolledParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/UnrolledParArrayCombiner.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object ParArray extends ParFactory[ParArray] with Serializable`         ###

This object provides a set of operations to create `mutable.ParArray` values.

* Source
  * [ParArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParArray.scala#L1)


### `object ParHashMap extends ParMapFactory[ParHashMap] with Serializable`  ###

This object provides a set of operations needed to create `mutable.ParHashMap`
values.

* Source
  * [ParHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashMap.scala#L1)


### `object ParHashSet extends ParSetFactory[ParHashSet] with Serializable`  ###

This object provides a set of operations needed to create `mutable.ParHashSet`
values.

* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashSet.scala#L1)


### `object ParIterable extends ParFactory[ParIterable]`                     ###

This object provides a set of operations to create `ParIterable` values.

* Source
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParIterable.scala#L1)


### `object ParMap extends ParMapFactory[ParMap]`                            ###

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParMap.scala#L1)


### `object ParSeq extends ParFactory[ParSeq]`                               ###

This object provides a set of operations to create `mutable.ParSeq` values.

* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParSeq.scala#L1)


### `object ParSet extends ParSetFactory[ParSet]`                            ###

This object provides a set of operations needed to create `mutable.ParSet`
values.

* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParSet.scala#L1)


### `object ParTrieMap extends ParMapFactory[ParTrieMap] with Serializable`  ###

* Source
  * [ParTrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParTrieMap.scala#L1)


### `object ResizableParArrayCombiner`                                       ###

* Source
  * [ResizableParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ResizableParArrayCombiner.scala#L1)


### `object UnrolledParArrayCombiner`                                        ###

* Source
  * [UnrolledParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/UnrolledParArrayCombiner.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.parallel.mutable
--------------------------------------------------------------------------------


### `val ParArrayCombiner: ResizableParArrayCombiner.type`                   ###
(defined at scala.collection.parallel.mutable)
