
#                     scala.collection.parallel.immutable                     #

```scala
package immutable
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class ParHashMap[K, +V] extends ParMap[K, V] with GenericParMapTemplate[K, V, ParHashMap] with ParMapLike[K, V, ParHashMap[K, V], HashMap[K, V]] with Serializable` ###

Immutable parallel hash map, based on hash tries.

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

* K
  * the key type of the map
* V
  * the value type of the map

* Self Type
  * ParHashMap [K, V]
* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParHashMap.scala#L1)
* Since
  * 2.9
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_hash_tries)
    section on Parallel Hash Tries for more information.


### `class ParHashSet[T] extends ParSet[T] with GenericParTemplate[T, ParHashSet] with ParSetLike[T, ParHashSet[T], HashSet[T]] with Serializable` ###

Immutable parallel hash set, based on hash tries.

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
  * the element type of the set

* Self Type
  * ParHashSet [T]
* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParHashSet.scala#L1)
* Since
  * 2.9
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_hash_tries)
    section on Parallel Hash Tries for more information.


### `trait ParIterable[+T] extends GenIterable[T] with parallel.ParIterable[T] with GenericParTemplate[T, ParIterable] with ParIterableLike[T, ParIterable[T], immutable.Iterable[T]] with Immutable` ###

A template trait for immutable parallel iterable collections.

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
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParIterable.scala#L1)
* Since
  * 2.9


### `trait ParMap[K, +V] extends GenMap[K, V] with GenericParMapTemplate[K, V, ParMap] with parallel.ParMap[K, V] with ParIterable[(K, V)] with ParMapLike[K, V, ParMap[K, V], immutable.Map[K, V]]` ###

A template trait for immutable parallel maps.

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

* Self Type
  * ParMap [K, V]
* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParMap.scala#L1)
* Since
  * 2.9


### `class ParRange extends ParSeq[Int] with Serializable`                   ###

Parallel ranges.

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

* Self Type
  * ParRange
* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParRange.scala#L1)
* Since
  * 2.9
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_range)
    section on `ParRange` for more information.


### `trait ParSeq[+T] extends GenSeq[T] with parallel.ParSeq[T] with ParIterable[T] with GenericParTemplate[T, ParSeq] with ParSeqLike[T, ParSeq[T], immutable.Seq[T]]` ###

An immutable variant of `ParSeq` .

* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParSeq.scala#L1)


### `trait ParSet[T] extends GenSet[T] with GenericParTemplate[T, ParSet] with parallel.ParSet[T] with ParIterable[T] with ParSetLike[T, ParSet[T], immutable.Set[T]]` ###

An immutable variant of `ParSet` .

* Self Type
  * ParSet [T]
* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParSet.scala#L1)


### `class ParVector[+T] extends ParSeq[T] with GenericParTemplate[T, ParVector] with ParSeqLike[T, ParVector[T], immutable.Vector[T]] with Serializable` ###

Immutable parallel vectors, based on vectors.

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
  * the element type of the vector

* Source
  * [ParVector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParVector.scala#L1)
* Since
  * 2.9
* See also
  * [Scala's Parallel Collections Library overview](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#parallel_vector)
    section on `ParVector` for more information.


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object HashSetCombiner`                                                 ###

* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParHashSet.scala#L1)


### `object ParHashMap extends ParMapFactory[ParHashMap] with Serializable`  ###

This object provides a set of operations needed to create
 `immutable.ParHashMap` values.

* Source
  * [ParHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParHashMap.scala#L1)


### `object ParHashSet extends ParSetFactory[ParHashSet] with Serializable`  ###

This object provides a set of operations needed to create
 `immutable.ParHashSet` values.

* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParHashSet.scala#L1)


### `object ParIterable extends ParFactory[ParIterable]`                     ###

This object provides a set of operations to create `ParIterable` values.

* Source
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParIterable.scala#L1)


### `object ParMap extends ParMapFactory[ParMap]`                            ###

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParMap.scala#L1)


### `object ParRange extends Serializable`                                   ###

* Source
  * [ParRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParRange.scala#L1)


### `object ParSeq extends ParFactory[ParSeq]`                               ###

This object provides a set of operations to create `mutable.ParSeq` values.

* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParSeq.scala#L1)


### `object ParSet extends ParSetFactory[ParSet]`                            ###

This object provides a set of operations needed to create `mutable.ParSet`
values.

* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParSet.scala#L1)


### `object ParVector extends ParFactory[ParVector] with Serializable`       ###

This object provides a set of operations to create `immutable.ParVector` values.

* Source
  * [ParVector.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParVector.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.collection.parallel.immutable
--------------------------------------------------------------------------------


### `def repetition[T](elem: T, len: Int): Repetition[T]`                    ###
(defined at scala.collection.parallel.immutable)
