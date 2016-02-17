
#                          scala.collection.parallel                          #

```scala
package parallel
```

Package object for parallel collections.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object ThreadPoolTasks`                                                 ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ForkJoinTasks` instead.
* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait AdaptiveWorkStealingForkJoinTasks extends ForkJoinTasks with AdaptiveWorkStealingTasks` ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait AdaptiveWorkStealingTasks extends Tasks`                          ###

This trait implements scheduling by employing an adaptive work stealing
technique.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait AdaptiveWorkStealingThreadPoolTasks extends ThreadPoolTasks with AdaptiveWorkStealingTasks` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `AdaptiveWorkStealingForkJoinTasks` instead.
* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `implicit class CollectionsHaveToParArray[C, T] extends AnyRef`          ###

Adds toParArray method to collection classes.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `trait Combiner[-Elem, +To] extends Builder[Elem, To] with Sizing with Parallel` ###

The base trait for all combiners. A combiner incremental collection construction
just like a regular builder, but also implements an efficient merge operation of
two builders via `combine` method. Once the collection is constructed, it may be
obtained by invoking the `result` method.

The complexity of the `combine` method should be less than linear for best
performance. The `result` method doesn't have to be a constant time operation,
but may be performed in parallel.

* Elem
  * the type of the elements added to the builder
* To
  * the type of the collection the builder produces

* Source
  * [Combiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Combiner.scala#L1)
* Since
  * 2.9


### `trait CombinerFactory[U, Repr] extends AnyRef`                          ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `final case class CompositeThrowable(throwables: Set[Throwable]) extends Exception with Product with Serializable` ###

Composite throwable - thrown when multiple exceptions are thrown at the same
time.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed.
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `class ExecutionContextTaskSupport extends TaskSupport with ExecutionContextTasks` ###

A task support that uses an execution context to schedule tasks.

It can be used with the default execution context implementation in the
 `scala.concurrent` package. It internally forwards the call to either a
forkjoin based task support or a thread pool executor one, depending on what the
execution context uses.

By default, parallel collections are parametrized with this task support object,
so parallel collections share the same execution context backend as the rest of
the `scala.concurrent` package.

* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * scala.collection.parallel.TaskSupport for more information.


### `trait ExecutionContextTasks extends Tasks`                              ###

This tasks implementation uses execution contexts to spawn a parallel
computation.

As an optimization, it internally checks whether the execution context is the
standard implementation based on fork/join pools, and if it is, creates a
 `ForkJoinTaskSupport` that shares the same pool to forward its request to it.

Otherwise, it uses an execution context exclusive `Tasks` implementation to
divide the tasks into smaller chunks and execute operations on it.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait FactoryOps[From, Elem, To] extends AnyRef`                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `class ForkJoinTaskSupport extends TaskSupport with AdaptiveWorkStealingForkJoinTasks` ###

A task support that uses a fork join pool to schedule tasks.

* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * scala.collection.parallel.TaskSupport for more information.


### `trait ForkJoinTasks extends Tasks with HavingForkJoinPool`              ###

An implementation trait for parallel tasks based on the fork/join framework.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait HavingForkJoinPool extends AnyRef`                                ###

A trait describing objects that provide a fork/join pool.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait IterableSplitter[+T] extends AugmentedIterableIterator[T] with Splitter[T] with Signalling with DelegatedSignalling` ###

Parallel iterators allow splitting and provide a `remaining` method to obtain
the number of elements remaining in the iterator.

* T
  * type of the elements iterated.

* Self Type
  * IterableSplitter [T]
* Source
  * [RemainsIterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/RemainsIterator.scala#L1)


### `trait ParIterable[+T] extends GenIterable[T] with GenericParTemplate[T, ParIterable] with ParIterableLike[T, ParIterable[T], scala.Iterable[T]]` ###

A template trait for parallel iterable collections.

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
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterable.scala#L1)
* Since
  * 2.9


### `trait ParIterableLike[+T, +Repr <: ParIterable[T], +Sequential <: scala.Iterable[T] with IterableLike[T, Sequential]] extends GenIterableLike[T, Repr] with CustomParallelizable[T, Repr] with Parallel with HasNewCombiner[T, Repr]` ###

A template trait for parallel collections of type `ParIterable[T]` .

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
* Repr
  * the type of the actual collection containing the elements

* Self Type
  * ParIterableLike [T, Repr, Sequential]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


### `trait ParMap[K, +V] extends GenMap[K, V] with GenericParMapTemplate[K, V, ParMap] with ParIterable[(K, V)] with ParMapLike[K, V, ParMap[K, V], Map[K, V]]` ###

A template trait for parallel maps.

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
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParMap.scala#L1)
* Since
  * 2.9


### `trait ParMapLike[K, +V, +Repr <: ParMapLike[K, V, Repr, Sequential] with ParMap[K, V], +Sequential <: Map[K, V] with MapLike[K, V, Sequential]] extends GenMapLike[K, V, Repr] with ParIterableLike[(K, V), Repr, Sequential]` ###

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

* Self Type
  * ParMapLike [K, V, Repr, Sequential]
* Source
  * [ParMapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParMapLike.scala#L1)


### `trait ParSeq[+T] extends GenSeq[T] with ParIterable[T] with GenericParTemplate[T, ParSeq] with ParSeqLike[T, ParSeq[T], scala.Seq[T]]` ###

A template trait for parallel sequences.

Parallel sequences inherit the `Seq` trait. Their indexing and length
computations are defined to be efficient. Like their sequential counterparts
they always have a defined order of elements. This means they will produce
resulting parallel sequences in the same way sequential sequences do. However,
the order in which they perform bulk operations on elements to produce results
is not defined and is generally nondeterministic. If the higher-order functions
given to them produce no sideeffects, then this won't be noticeable.

This trait defines a new, more general `split` operation and reimplements the
 `split` operation of `ParallelIterable` trait using the new `split` operation.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* T
  * the type of the elements in this parallel sequence

* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeq.scala#L1)


### `trait ParSeqLike[+T, +Repr <: ParSeq[T], +Sequential <: scala.Seq[T] with SeqLike[T, Sequential]] extends GenSeqLike[T, Repr] with ParIterableLike[T, Repr, Sequential]` ###

A template trait for sequences of type `ParSeq[T]` , representing parallel
sequences with element type `T` .

Parallel sequences inherit the `Seq` trait. Their indexing and length
computations are defined to be efficient. Like their sequential counterparts
they always have a defined order of elements. This means they will produce
resulting parallel sequences in the same way sequential sequences do. However,
the order in which they perform bulk operations on elements to produce results
is not defined and is generally nondeterministic. If the higher-order functions
given to them produce no sideeffects, then this won't be noticeable.

This trait defines a new, more general `split` operation and reimplements the
 `split` operation of `ParallelIterable` trait using the new `split` operation.

* T
  * the type of the elements contained in this collection
* Repr
  * the type of the actual collection containing the elements
* Sequential
  * the type of the sequential version of this parallel collection

* Self Type
  * ParSeqLike [T, Repr, Sequential]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


### `trait ParSet[T] extends GenSet[T] with GenericParTemplate[T, ParSet] with ParIterable[T] with ParSetLike[T, ParSet[T], Set[T]]` ###

A template trait for parallel sets.

The higher-order functions passed to certain operations may contain
side-effects. Since implementations of bulk operations may not be sequential,
this means that side-effects may not be predictable and may produce data-races,
deadlocks or invalidation of state if care is not taken. It is up to the
programmer to either avoid using side-effects or to use some form of
synchronization when accessing mutable data.

* T
  * the element type of the set

* Self Type
  * ParSet [T]
* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSet.scala#L1)
* Since
  * 2.9


### `trait ParSetLike[T, +Repr <: ParSetLike[T, Repr, Sequential] with ParSet[T], +Sequential <: Set[T] with SetLike[T, Sequential]] extends GenSetLike[T, Repr] with ParIterableLike[T, Repr, Sequential]` ###

A template trait for parallel sets. This trait is mixed in with concrete
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
  * [ParSetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSetLike.scala#L1)


### `trait PreciseSplitter[+T] extends Splitter[T]`                          ###

A precise splitter (or a precise split iterator) can be split into arbitrary
number of splitters that traverse disjoint subsets of arbitrary sizes.

Implementors might want to override the parameterless `split` method for
efficiency.

* T
  * type of the elements this splitter traverses

* Source
  * [PreciseSplitter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/PreciseSplitter.scala#L1)
* Since
  * 2.9


### `trait SeqSplitter[+T] extends IterableSplitter[T] with AugmentedSeqIterator[T] with PreciseSplitter[T]` ###

Parallel sequence iterators allow splitting into arbitrary subsets.

* T
  * type of the elements iterated.

* Self Type
  * SeqSplitter [T]
* Source
  * [RemainsIterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/RemainsIterator.scala#L1)


### `trait Splitter[+T] extends Iterator[T]`                                 ###

A splitter (or a split iterator) can be split into more splitters that traverse
over disjoint subsets of elements.

* T
  * type of the elements this splitter traverses

* Source
  * [Splitter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Splitter.scala#L1)
* Since
  * 2.9


### `trait Task[R, +Tp] extends AnyRef`                                      ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait TaskSupport extends Tasks`                                        ###

A trait implementing the scheduling of a parallel collection operation.

Parallel collections are modular in the way operations are scheduled. Each
parallel collection is parametrized with a task support object which is
responsible for scheduling and load-balancing tasks to processors.

A task support object can be changed in a parallel collection after it has been
created, but only during a quiescent period, i.e. while there are no concurrent
invocations to parallel collection methods.

There are currently a few task support implementations available for parallel
collections. The scala.collection.parallel.ForkJoinTaskSupport uses a fork-join
pool internally.

The scala.collection.parallel.ExecutionContextTaskSupport uses the default
execution context implementation found in scala.concurrent, and it reuses the
thread pool used in scala.concurrent.

The execution context task support is set to each parallel collection by
default, so parallel collections reuse the same fork-join pool as the future
API.

Here is a way to change the task support of a parallel collection:

```scala
import scala.collection.parallel._
val pc = mutable.ParArray(1, 2, 3)
pc.tasksupport = new ForkJoinTaskSupport(
  new java.util.concurrent.ForkJoinPool(2))
```

* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * [Configuring Parallel Collections](http://docs.scala-lang.org/overviews/parallel-collections/configuration.html)
    section on the parallel collection's guide for more information.


### `trait Tasks extends AnyRef`                                             ###

A trait that declares task execution capabilities used by parallel collections.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `class ThreadPoolTaskSupport extends TaskSupport with AdaptiveWorkStealingThreadPoolTasks` ###

A task support that uses a thread pool executor to schedule tasks.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ForkJoinTaskSupport` instead.
* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * scala.collection.parallel.TaskSupport for more information.


### `trait ThreadPoolTasks extends Tasks`                                    ###

An implementation of tasks objects based on the Java thread pooling API.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ForkJoinTasks` instead.
* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `trait ThrowableOps extends AnyRef`                                      ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This trait will be removed.
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


### `trait TraversableOps[T] extends AnyRef`                                 ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object ForkJoinTasks`                                                   ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `object FutureThreadPoolTasks`                                           ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


### `object ParIterable extends ParFactory[ParIterable]`                     ###

This object provides a set of operations to create `ParIterable` values.

* Source
  * [ParIterable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterable.scala#L1)


### `object ParMap extends ParMapFactory[ParMap]`                            ###

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParMap.scala#L1)


### `object ParSeq extends ParFactory[ParSeq]`                               ###

* Source
  * [ParSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeq.scala#L1)


### `object ParSet extends ParSetFactory[ParSet]`                            ###

* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSet.scala#L1)


### `object Splitter`                                                        ###

* Source
  * [Splitter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Splitter.scala#L1)


### `package immutable`                                                      ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/package.scala#L1)


### `package mutable`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/package.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.collection.parallel
--------------------------------------------------------------------------------


### `val CHECK_RATE: Int`                                                    ###

(defined at scala.collection.parallel)


### `val defaultTaskSupport: TaskSupport`                                    ###

(defined at scala.collection.parallel)


### `def setTaskSupport[Coll](c: Coll, t: TaskSupport): Coll`                ###

(defined at scala.collection.parallel)


### `def thresholdFromSize(sz: Int, parallelismLevel: Int): Int`             ###

Computes threshold from the size of the collection and the parallelism level.
(defined at scala.collection.parallel)
