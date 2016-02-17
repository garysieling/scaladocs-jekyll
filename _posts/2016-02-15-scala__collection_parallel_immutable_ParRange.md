
#                 scala.collection.parallel.immutable.ParRange                 #

```scala
class ParRange extends ParSeq[Int] with Serializable
```

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


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Accessor[R, Tp] extends ParSeqLike.Accessor[R, Tp]`               ###

* Attributes
  * protected
* Definition Classes
  * ParSeqLike


### `class Aggregate[S] extends Accessor[S, Aggregate[S]]`                   ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait BuilderOps[Elem, To] extends AnyRef`                              ###

* Definition Classes
  * ParIterableLike


### `class Collect[S, That] extends Transformer[Combiner[S, That], Collect[S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `abstract class Composite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends NonDivisibleTask[R, Composite[FR, SR, R, First, Second]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Copy[U >: T, That] extends Transformer[Combiner[U, That], Copy[U, That]]` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike


### `class CopyToArray[U >: T, This >: Repr] extends Accessor[Unit, CopyToArray[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Corresponds[S] extends Accessor[Boolean, Corresponds[S]]`         ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class Count extends Accessor[Int, Count]`                               ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class CreateScanTree[U >: T] extends Transformer[ScanTree[U], CreateScanTree[U]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Drop[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Drop[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `abstract class Elements extends SeqSplitter[T] with scala.BufferedIterator[T]` ###

Used to iterate elements using indices

* Attributes
  * protected
* Definition Classes
  * ParSeqLike


### `class Exists extends Accessor[Boolean, Exists]`                         ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Filter[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Filter[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class FilterNot[U >: T, This >: Repr] extends Transformer[Combiner[U, This], FilterNot[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Find[U >: T] extends Accessor[Option[U], Find[U]]`                ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class FlatMap[S, That] extends Transformer[Combiner[S, That], FlatMap[S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Fold[U >: T] extends Accessor[U, Fold[U]]`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Forall extends Accessor[Boolean, Forall]`                         ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Foreach[S] extends Accessor[Unit, Foreach[S]]`                    ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class FromScanTree[U >: T, That] extends StrictSplitterCheckTask[Combiner[U, That], FromScanTree[U, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class GroupBy[K, U >: T] extends Transformer[HashMapCombiner[K, U], GroupBy[K, U]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class IndexWhere extends Accessor[Int, IndexWhere]`                     ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class LastIndexWhere extends Accessor[Int, LastIndexWhere]`             ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class Map[S, That] extends Transformer[Combiner[S, That], Map[S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Max[U >: T] extends Accessor[Option[U], Max[U]]`                  ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Min[U >: T] extends Accessor[Option[U], Min[U]]`                  ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait NonDivisible[R] extends NonDivisibleTask[R, NonDivisible[R]]`     ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait NonDivisibleTask[R, Tp] extends StrictSplitterCheckTask[R, Tp]`   ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `abstract class ParComposite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends Composite[FR, SR, R, First, Second]` ###

Performs two tasks in parallel, and waits for both to finish.

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class ParRangeIterator extends SeqSplitter[Int]`                        ###

* Source
  * [ParRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/immutable/ParRange.scala#L1)


### `class Partition[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Combiner[U, This]), Partition[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Product[U >: T] extends Accessor[U, Product[U]]`                  ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Reduce[U >: T] extends Accessor[Option[U], Reduce[U]]`            ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `abstract class ResultMapping[R, Tp, R1] extends NonDivisibleTask[R1, ResultMapping[R, Tp, R1]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Reverse[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Reverse[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class ReverseMap[S, That] extends Transformer[Combiner[S, That], ReverseMap[S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `type SSCTask[R, Tp] = StrictSplitterCheckTask[R, Tp]`                   ###

* Definition Classes
  * ParIterableLike


### `class SameElements[U >: T] extends Accessor[Boolean, SameElements[U]]`  ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `case class ScanLeaf[U >: T](pit: IterableSplitter[U], op: (U, U) ⇒ U, from: Int, len: Int, prev: Option[ScanLeaf[U]], acc: U) extends ScanTree[U] with scala.Product with Serializable` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `case class ScanNode[U >: T](left: ScanTree[U], right: ScanTree[U]) extends ScanTree[U] with scala.Product with Serializable` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait ScanTree[U >: T] extends AnyRef`                                  ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class SegmentLength extends Accessor[(Int, Boolean), SegmentLength]`    ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `abstract class SeqComposite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends Composite[FR, SR, R, First, Second]` ###

Sequentially performs one task after another.

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait SignallingOps[PI <: DelegatedSignalling] extends AnyRef`          ###

* Definition Classes
  * ParIterableLike


### `class Slice[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Slice[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class Span[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Combiner[U, This]), Span[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class SplitAt[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Combiner[U, This]), SplitAt[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait StrictSplitterCheckTask[R, Tp] extends Task[R, Tp]`               ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike


### `class Sum[U >: T] extends Accessor[U, Sum[U]]`                          ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `type SuperParIterator = IterableSplitter[Int]`                          ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class Take[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Take[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class TakeWhile[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Boolean), TakeWhile[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait TaskOps[R, Tp] extends AnyRef`                                    ###

* Definition Classes
  * ParIterableLike


### `class ToParCollection[U >: T, That] extends Transformer[Combiner[U, That], ToParCollection[U, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class ToParMap[K, V, That] extends Transformer[Combiner[(K, V), That], ToParMap[K, V, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait Transformer[R, Tp] extends Accessor[R, Tp] with ParSeqLike.Transformer[R, Tp]` ###

* Attributes
  * protected
* Definition Classes
  * ParSeqLike


### `class Updated[U >: T, That] extends Transformer[Combiner[U, That], Updated[U, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class Zip[U >: T, S, That] extends Transformer[Combiner[(U, S), That], Zip[U, S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike


### `class ZipAll[U >: T, S, That] extends Transformer[Combiner[(U, S), That], ZipAll[U, S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


--------------------------------------------------------------------------------
            Value Members From scala.collection.CustomParallelizable
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[Int, ParSeq[Int]]`                            ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * CustomParallelizable → Parallelizable

(defined at scala.collection.CustomParallelizable)


--------------------------------------------------------------------------------
                 Value Members From scala.collection.GenSeqLike
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

The equals method for arbitrary sequences. Compares this sequence to some other
object.

* that
  * The object to compare the sequence to
* returns
  * `true` if `that` is a sequence that has the same elements as this sequence
    in the same order, `false` otherwise

* Definition Classes
  * GenSeqLike → Equals → Any

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: Int](elem: B): Int`                                    ###

[use case]

Finds index of first occurrence of some value in this immutable parallel range.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this immutable parallel range that is
    equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: Int](elem: B, from: Int): Int`                         ###

[use case]

Finds index of first occurrence of some value in this immutable parallel range
after or at some start index.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this immutable parallel range
    that is equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (Int) ⇒ Boolean): Int`                                ###

Finds index of first element satisfying some predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the first element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def isDefinedAt(idx: Int): Boolean`                                     ###

Tests whether this general sequence contains given index.

The implementations of methods `apply` and `isDefinedAt` turn a `Seq[A]` into a
 `PartialFunction[Int, A]` .

* idx
  * the index to test
* returns
  * `true` if this general sequence contains an element at position `idx` ,
     `false` otherwise.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: Int](elem: B): Int`                                ###

[use case]

Finds index of last occurrence of some value in this immutable parallel range.

Note: will not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this immutable parallel range that is equal
    (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: Int](elem: B, end: Int): Int`                      ###

[use case]

Finds index of last occurrence of some value in this immutable parallel range
before or at a given end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this immutable parallel range that
    is equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (Int) ⇒ Boolean): Int`                            ###

Finds index of last element satisfying some predicate.

Note: will not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the last element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def prefixLength(p: (Int) ⇒ Boolean): Int`                              ###

Returns the length of the longest prefix whose elements all satisfy some
predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the length of the longest prefix of this general sequence such that every
    element of the segment satisfies the predicate `p` .

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def startsWith[B](that: GenSeq[B]): Boolean`                            ###

Tests whether this general sequence starts with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this collection has `that` as a prefix, `false` otherwise.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def union[B >: Int, That](that: GenSeq[B])(implicit bf: CanBuildFrom[ParSeq[Int], B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this immutable parallel
range and also all elements of a given sequence. `xs union ys` is equivalent to
 `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to add.
* returns
  * a new immutable parallel range which contains all elements of this immutable
    parallel range followed by all elements of `that` .

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.GenericParTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Combiner[B, ParSeq[B]]`                          ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def genericCombiner[B]: Combiner[B, ParSeq[B]]`                         ###

* Definition Classes
  * GenericParTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def newBuilder: Builder[Int, ParSeq[Int]]`                              ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericParTemplate)


### `def newCombiner: Combiner[Int, ParSeq[Int]]`                            ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericParTemplate → HasNewCombiner

(defined at scala.collection.generic.GenericParTemplate)


--------------------------------------------------------------------------------
     Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def flatten[B](implicit asTraversable: (Int) ⇒ GenTraversableOnce[B]): ParSeq[B]` ###

[use case]

Converts this immutable parallel range of traversable collections into a
immutable parallel range formed by the elements of these traversable
collections.

The resulting collection's type will be guided by the static type of immutable
parallel range. For example:

```scala
val xs = List(
           Set(1, 2, 3),
           Set(1, 2, 3)
         ).flatten
// xs == List(1, 2, 3, 1, 2, 3)

val ys = Set(
           List(1, 2, 3),
           List(3, 2, 1)
         ).flatten
// ys == Set(1, 2, 3)
```

* B
  * the type of the elements of each traversable collection.
* returns
  * a new immutable parallel range resulting from concatenating all element
    immutable parallel ranges.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (Int) ⇒ GenTraversableOnce[B]): ParSeq[ParSeq[B]]` ###

Transposes this collection of traversable collections into a collection of
collections.

The resulting collection's type will be guided by the static type of collection.
For example:

```scala
val xs = List(
           Set(1, 2, 3),
           Set(4, 5, 6)).transpose
// xs == List(
//         List(1, 4),
//         List(2, 5),
//         List(3, 6))

val ys = Vector(
           List(1, 2, 3),
           List(4, 5, 6)).transpose
// ys == Vector(
//         Vector(1, 4),
//         Vector(2, 5),
//         Vector(3, 6))
```

* B
  * the type of the elements of each traversable collection.
* asTraversable
  * an implicit conversion which asserts that the element type of this
    collection is a `Traversable` .
* returns
  * a two-dimensional collection of collections which has as _n_ th row the _n_
    th column of this collection.

* Definition Classes
  * GenericTraversableTemplate
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_  `transpose` throws an
     `IllegalArgumentException` if collections are not uniformly sized.
* Exceptions thrown
  * IllegalArgumentException if all collections in this collection are not of
    the same size.

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def unzip3[A1, A2, A3](implicit asTriple: (Int) ⇒ (A1, A2, A3)): (ParSeq[A1], ParSeq[A2], ParSeq[A3])` ###

Converts this collection of triples into three collections of the first, second,
and third element of each triple.

```scala
val xs = Traversable(
           (1, "one", '1'),
           (2, "two", '2'),
           (3, "three", '3')).unzip3
// xs == (Traversable(1, 2, 3),
//        Traversable(one, two, three),
//        Traversable(1, 2, 3))
```

* A1
  * the type of the first member of the element triples
* A2
  * the type of the second member of the element triples
* A3
  * the type of the third member of the element triples
* asTriple
  * an implicit conversion which asserts that the element type of this
    collection is a triple.
* returns
  * a triple of collections, containing the first, second, respectively third
    member of each element triple of this collection.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def unzip[A1, A2](implicit asPair: (Int) ⇒ (A1, A2)): (ParSeq[A1], ParSeq[A2])` ###

Converts this collection of pairs into two collections of the first and second
half of each pair.

```scala
val xs = Traversable(
           (1, "one"),
           (2, "two"),
           (3, "three")).unzip
// xs == (Traversable(1, 2, 3),
//        Traversable(one, two, three))
```

* A1
  * the type of the first half of the element pairs
* A2
  * the type of the second half of the element pairs
* asPair
  * an implicit conversion which asserts that the element type of this
    collection is a pair.
* returns
  * a pair of collections, containing the first, respectively second half of
    each element pair of this collection.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


--------------------------------------------------------------------------------
          Value Members From scala.collection.parallel.ParIterableLike
--------------------------------------------------------------------------------


### `def ++[U >: Int, That](that: GenTraversableOnce[U])(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

Returns a new immutable parallel range containing the elements from the left
hand operand followed by the elements from the right hand operand. The element
type of the immutable parallel range is the most specific superclass
encompassing the element types of the two operands.

Example:

```scala
scala> val a = List(1)
a: List[Int] = List(1)

scala> val b = List(2)
b: List[Int] = List(2)

scala> val c = a ++ b
c: List[Int] = List(1, 2)

scala> val d = List('a')
d: List[Char] = List(a)

scala> val e = c ++ d
e: List[AnyVal] = List(1, 2, a)
```

* B
  * the element type of the returned collection.
* that
  * the traversable to append.
* returns
  * a new immutable parallel range which contains all elements of this immutable
    parallel range followed by all elements of `that` .

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def /:[S](z: S)(op: (S, Int) ⇒ S): S`                                   ###

Applies a binary operator to a start value and all elements of this parallel
iterable, going left to right.

Note: `/:` is alternate syntax for `foldLeft` ; `z /: xs` is the same as
 `xs foldLeft z` .

Examples:

Note that the folding function used to compute b is equivalent to that used to
compute c.

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = (5 /: a)(_+_)
b: Int = 15

scala> val c = (5 /: a)((x,y) => x + y)
c: Int = 15
```

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this parallel
    iterable, going left to right with the start value `z` on the left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def :\[S](z: S)(op: (Int, S) ⇒ S): S`                                   ###

Applies a binary operator to all elements of this parallel iterable and a start
value, going right to left.

Note: `:\` is alternate syntax for `foldRight` ; `xs :\ z` is the same as
 `xs foldRight z` .

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

Examples:

Note that the folding function used to compute b is equivalent to that used to
compute c.

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = (a :\ 5)(_+_)
b: Int = 15

scala> val c = (a :\ 5)((x,y) => x + y)
c: Int = 15
```

* z
  * the start value
* op
  * the binary operator
* returns
  * the result of inserting `op` between consecutive elements of this parallel
    iterable, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def aggregate[S](z: ⇒ S)(seqop: (S, Int) ⇒ S, combop: (S, S) ⇒ S): S`   ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It has similar semantics,
but does not require the result to be a supertype of the element type. It
traverses the elements in different partitions sequentially, using `seqop` to
update the result, and then applies `combop` to results from different
partitions. The implementation of this operation may operate on an arbitrary
number of collection partitions, so `combop` may be invoked arbitrary number of
times.

For example, one might want to process some elements and then produce a `Set` .
In this case, `seqop` would process an element and append it to the set, while
 `combop` would concatenate two sets from different partitions together. The
initial value `z` would be an empty set.

```scala
pc.aggregate(Set[Int]())(_ += process(_), _ ++ _)
```

Another example is calculating geometric mean from a collection of doubles (one
would typically require big doubles for this).

* S
  * the type of accumulated results
* z
  * the initial value for the accumulated result of the partition - this will
    typically be the neutral element for the `seqop` operator (e.g. `Nil` for
    list concatenation or `0` for summation) and may be evaluated more than once
* seqop
  * an operator used to accumulate results within a partition
* combop
  * an associative operator used to combine results from different partitions

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def bf2seq[S, That](bf: CanBuildFrom[ParSeq[Int], S, That]): CanBuildFrom[immutable.Seq[Int], S, That]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `implicit def builder2ops[Elem, To](cb: Builder[Elem, To]): BuilderOps[Elem, To]` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def canEqual(other: Any): Boolean`                                      ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def collect[S, That](pf: PartialFunction[Int, S])(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
immutable parallel range on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the immutable parallel range.
* returns
  * a new immutable parallel range resulting from applying the given partial
    function `pf` to each element on which it is defined and collecting the
    results. The order of the elements is preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def combinerFactory: CombinerFactory[Int, ParSeq[Int]]`                 ###

Creates a combiner factory. Each combiner factory instance is used once per
invocation of a parallel transformer method for a single collection.

The default combiner factory creates a new combiner every time it is requested,
unless the combiner is thread-safe as indicated by its `canBeShared` method. In
this case, the method returns a factory which returns the same combiner each
time. This is typically done for concurrent parallel collections, the combiners
of which allow thread safe access.

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def combinerFactory[S, That](cbf: () ⇒ Combiner[S, That]): CombinerFactory[S, That]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: Int](xs: Array[U]): Unit`                          ###

[use case]

Copies the elements of this immutable parallel range to an array. Fills the
given array `xs` with values of this immutable parallel range. Copying will stop
once either the end of the current immutable parallel range is reached, or the
end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: Int](xs: Array[U], start: Int): Unit`              ###

[use case]

Copies the elements of this immutable parallel range to an array. Fills the
given array `xs` with values of this immutable parallel range, beginning at
index `start` . Copying will stop once either the end of the current immutable
parallel range is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: Int](xs: Array[U], start: Int, len: Int): Unit`    ###

[use case]

Copies the elements of this immutable parallel range to an array. Fills the
given array `xs` with at most `len` elements of this immutable parallel range,
starting at position `start` . Copying will stop once either the end of the
current immutable parallel range is reached, or the end of the target array is
reached, or `len` elements have been copied.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def count(p: (Int) ⇒ Boolean): Int`                                     ###

Counts the number of elements in the parallel iterable which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def debugBuffer: ArrayBuffer[String]`                                   ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `implicit def delegatedSignalling2ops[PI <: DelegatedSignalling](it: PI): SignallingOps[PI]` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def drop(n: Int): ParSeq[Int]`                                          ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this parallel iterable.
* returns
  * a parallel iterable consisting of all elements of this parallel iterable
    except the first `n` ones, or else the empty parallel iterable, if this
    parallel iterable has less than `n` elements.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def dropWhile(pred: (Int) ⇒ Boolean): ParSeq[Int]`                      ###

Drops all elements in the longest prefix of elements that satisfy the predicate,
and returns a collection composed of the remaining elements.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state. The index flag is initially
set to maximum integer value.

* pred
  * the predicate used to test the elements
* returns
  * a collection composed of all the elements after the longest prefix of
    elements in this parallel iterable that satisfy the predicate `pred`

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def exists(p: (Int) ⇒ Boolean): Boolean`                                ###

Tests whether a predicate holds for some element of this parallel iterable.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* p
  * a predicate used to test elements
* returns
  * true if `p` holds for some element, false otherwise

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def filter(pred: (Int) ⇒ Boolean): ParSeq[Int]`                         ###

Selects all elements of this parallel iterable which satisfy a predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new parallel iterable consisting of all elements of this parallel iterable
    that satisfy the given predicate `p` . Their order may not be preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def filterNot(pred: (Int) ⇒ Boolean): ParSeq[Int]`                      ###

Selects all elements of this parallel iterable which do not satisfy a predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new parallel iterable consisting of all elements of this parallel iterable
    that do not satisfy the given predicate `p` . Their order may not be
    preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def find(p: (Int) ⇒ Boolean): Option[Int]`                              ###

Finds some element in the collection for which the predicate holds, if such an
element exists. The element may not necessarily be the first such element in the
iteration order.

If there are multiple elements obeying the predicate, the choice is
nondeterministic.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* p
  * predicate used to test the elements
* returns
  * an option value with the element if such an element exists, or `None`
    otherwise

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def flatMap[S, That](f: (Int) ⇒ GenTraversableOnce[S])(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this immutable
parallel range and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of immutable
parallel range. This might cause unexpected results sometimes. For example:

```scala
// lettersOf will return a Seq[Char] of likely repeated letters, instead of a Set
def lettersOf(words: Seq[String]) = words flatMap (word => word.toSet)

// lettersOf will return a Set[Char], not a Seq
def lettersOf(words: Seq[String]) = words.toSet flatMap (word => word.toSeq)

// xs will be an Iterable[Int]
val xs = Map("a" -> List(11,111), "b" -> List(22,222)).flatMap(_._2)

// ys will be a Map[Int, Int]
val ys = Map("a" -> List(1 -> 11,1 -> 111), "b" -> List(2 -> 22,2 -> 222)).flatMap(_._2)
```

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new immutable parallel range resulting from applying the given
    collection-valued function `f` to each element of this immutable parallel
    range and concatenating the results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def foldLeft[S](z: S)(op: (S, Int) ⇒ S): S`                             ###

Applies a binary operator to a start value and all elements of this parallel
iterable, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this parallel
    iterable, going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this parallel iterable. Returns `z`
    if this parallel iterable is empty.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def foldRight[S](z: S)(op: (Int, S) ⇒ S): S`                            ###

Applies a binary operator to all elements of this parallel iterable and a start
value, going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this parallel
    iterable, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this parallel iterable. Returns `z`
    if this parallel iterable is empty.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def fold[U >: Int](z: U)(op: (U, U) ⇒ U): U`                            ###

Folds the elements of this sequence using the specified associative binary
operator. The order in which the elements are reduced is unspecified and may be
nondeterministic.

Note this method has a different signature than the `foldLeft` and `foldRight`
methods of the trait `Traversable` . The result of folding may only be a
supertype of this parallel collection's type parameter `T` .

* U
  * a type parameter for the binary operator, a supertype of `T` .
* z
  * a neutral element for the fold operation, it may be added to the result an
    arbitrary number of times, not changing the result (e.g. `Nil` for list
    concatenation, 0 for addition, or 1 for multiplication)
* op
  * a binary operator that must be associative
* returns
  * the result of applying fold operator `op` between all the elements and `z`

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def forall(p: (Int) ⇒ Boolean): Boolean`                                ###

Tests whether a predicate holds for all elements of this parallel iterable.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* p
  * a predicate used to test elements
* returns
  * true if `p` holds for all elements, false otherwise

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def foreach[U](f: (Int) ⇒ U): Unit`                                     ###

Applies a function `f` to all the elements of parallel iterable in an undefined
order.

* U
  * the result type of the function applied to each element, which is always
    discarded
* f
  * function applied to each element

* Definition Classes
  * ParIterableLike → GenTraversableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def groupBy[K](f: (Int) ⇒ K): ParMap[K, ParSeq[Int]]`                   ###

Partitions this parallel iterable into a map of parallel iterables according to
some discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new parallel iterable.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to parallel iterables such that the following invariant
    holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a parallel iterable of those elements
     `x` for which `f(x)` equals `k` .

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def head: Int`                                                          ###

Selects the first element of this parallel iterable.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def headOption: Option[Int]`                                            ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this parallel iterable if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def init: ParSeq[Int]`                                                  ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a parallel iterable consisting of all elements of this parallel iterable
    except the last one.

* Definition Classes
  * ParIterableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def last: Int`                                                          ###

Selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * The last element of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def lastOption: Option[Int]`                                            ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this parallel iterable$ if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def map[S, That](f: (Int) ⇒ S)(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this immutable
parallel range.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new immutable parallel range resulting from applying the given function
     `f` to each element of this immutable parallel range and collecting the
    results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def maxBy[S](f: (Int) ⇒ S)(implicit cmp: Ordering[S]): Int`             ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this immutable parallel range with the largest value
    measured by function f.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def minBy[S](f: (Int) ⇒ S)(implicit cmp: Ordering[S]): Int`             ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this immutable parallel range with the smallest value
    measured by function f.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this parallel iterable in a string using a separator
string.

* sep
  * the separator string.
* returns
  * a string representation of this parallel iterable. In the resulting string
    the string representations (w.r.t. the method `toString` ) of all elements
    of this parallel iterable are separated by the string `sep` .

* Definition Classes
  * ParIterableLike → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(defined at scala.collection.parallel.ParIterableLike)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this parallel iterable in a string using start, end,
and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this parallel iterable. The resulting string
    begins with the string `start` and ends with the string `end` . Inside, the
    string representations (w.r.t. the method `toString` ) of all elements of
    this parallel iterable are separated by the string `sep` .

* Definition Classes
  * ParIterableLike → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(defined at scala.collection.parallel.ParIterableLike)


### `def par: ParSeq[Int]`                                                   ###

Returns a parallel implementation of this collection.

For most collection types, this method creates a new parallel collection by
copying all the elements. For these collection, `par` takes linear time. Mutable
collections in this category do not produce a mutable parallel collection that
has the same underlying dataset, so changes in one collection will not be
reflected in the other one.

Specific collections (e.g. `ParArray` or `mutable.ParHashMap` ) override this
default behaviour by creating a parallel collection which shares the same
underlying dataset. For these collections, `par` takes constant or sublinear
time.

All parallel collections return a reference to themselves.

* returns
  * a parallel implementation of this collection

* Definition Classes
  * ParIterableLike → CustomParallelizable → Parallelizable

(defined at scala.collection.parallel.ParIterableLike)


### `def partition(pred: (Int) ⇒ Boolean): (ParSeq[Int], ParSeq[Int])`       ###

Partitions this parallel iterable in two parallel iterables according to a
predicate.

* pred
  * the predicate on which to partition.
* returns
  * a pair of parallel iterables: the first parallel iterable consists of all
    elements that satisfy the predicate `p` and the second parallel iterable
    consists of all elements that don't. The relative order of the elements in
    the resulting parallel iterables may not be preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceLeftOption[U >: Int](op: (U, Int) ⇒ U): Option[U]`            ###

Optionally applies a binary operator to all elements of this parallel iterable,
going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this parallel
    iterable is nonempty, `None` otherwise.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceLeft[U >: Int](op: (U, Int) ⇒ U): U`                          ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceOption[U >: Int](op: (U, U) ⇒ U): Option[U]`                  ###

Optionally reduces the elements of this sequence using the specified associative
binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

Note this method has a different signature than the `reduceLeftOption` and
 `reduceRightOption` methods of the trait `Traversable` . The result of reducing
may only be a supertype of this parallel collection's type parameter `T` .

* U
  * A type parameter for the binary operator, a supertype of `T` .
* op
  * A binary operator that must be associative.
* returns
  * An option value containing result of applying reduce operator `op` between
    all the elements if the collection is nonempty, and `None` otherwise.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceRightOption[U >: Int](op: (Int, U) ⇒ U): Option[U]`           ###

Optionally applies a binary operator to all elements of this parallel iterable,
going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this parallel
    iterable is nonempty, `None` otherwise.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceRight[U >: Int](op: (Int, U) ⇒ U): U`                         ###

Applies a binary operator to all elements of this parallel iterable, going right
to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this parallel
    iterable, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def reduce[U >: Int](op: (U, U) ⇒ U): U`                                ###

Reduces the elements of this sequence using the specified associative binary
operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

Note this method has a different signature than the `reduceLeft` and
 `reduceRight` methods of the trait `Traversable` . The result of reducing may
only be a supertype of this parallel collection's type parameter `T` .

* U
  * A type parameter for the binary operator, a supertype of `T` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    collection is nonempty.

* Definition Classes
  * ParIterableLike → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def repr: ParSeq[Int]`                                                  ###

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def reuse[S, That](oldc: Option[Combiner[S, That]], newc: Combiner[S, That]): Combiner[S, That]` ###

Optionally reuses an existing combiner for better performance. By default it
doesn't - subclasses may override this behaviour. The provided combiner `oldc`
that can potentially be reused will be either some combiner from the previous
computational task, or `None` if there was no previous phase (in which case this
method must return `newc` ).

* oldc
  * The combiner that is the result of the previous task, or `None` if there was
    no previous task.
* newc
  * The new, empty combiner that can be used.
* returns
  * Either `newc` or `oldc` .

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scan[U >: Int, That](z: U)(op: (U, U) ⇒ U)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

Computes a prefix scan of the elements of the collection.

Note: The neutral element `z` may be applied more than once.

* z
  * neutral element for the operator `op`
* op
  * the associative operator for the scan
* returns
  * a new immutable parallel range containing the prefix scan of the elements in
    this immutable parallel range

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scanLeft[S, That](z: S)(op: (S, Int) ⇒ S)(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* That
  * the actual type of the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * collection with intermediate results

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scanRight[S, That](z: S)(op: (Int, S) ⇒ S)(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going right to left. The head of the collection is the last cumulative result.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Example:

```scala
List(1, 2, 3, 4).scanRight(0)(_ + _) == List(10, 9, 7, 4, 0)
```

* That
  * the actual type of the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * collection with intermediate results

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def sequentially[S, That <: Parallel](b: (immutable.Seq[Int]) ⇒ Parallelizable[S, That]): ParSeq[Int]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def slice(unc_from: Int, unc_until: Int): ParSeq[Int]`                  ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* unc_from
  * the lowest index to include from this parallel iterable.
* unc_until
  * the lowest index to EXCLUDE from this parallel iterable.
* returns
  * a parallel iterable containing the elements greater than or equal to index
     `from` extending up to (but not including) index `until` of this parallel
    iterable.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def span(pred: (Int) ⇒ Boolean): (ParSeq[Int], ParSeq[Int])`            ###

Splits this parallel iterable into a prefix/suffix pair according to a
predicate.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state. The index flag is initially
set to maximum integer value.

* pred
  * the predicate used to test the elements
* returns
  * a pair consisting of the longest prefix of the collection for which all the
    elements satisfy `pred` , and the rest of the collection

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def splitAt(n: Int): (ParSeq[Int], ParSeq[Int])`                        ###

Splits this parallel iterable into two at a given position. Note: `c splitAt n`
is equivalent to (but possibly more efficient than) `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of parallel iterables consisting of the first `n` elements of this
    parallel iterable, and the other elements.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def tail: ParSeq[Int]`                                                  ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a parallel iterable consisting of all elements of this parallel iterable
    except the first one.

* Definition Classes
  * ParIterableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the parallel iterable is empty.

(defined at scala.collection.parallel.ParIterableLike)


### `def take(n: Int): ParSeq[Int]`                                          ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this parallel iterable.
* returns
  * a parallel iterable consisting only of the first `n` elements of this
    parallel iterable, or else the whole parallel iterable, if it has less than
     `n` elements.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def takeWhile(pred: (Int) ⇒ Boolean): ParSeq[Int]`                      ###

Takes the longest prefix of elements that satisfy the predicate.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state. The index flag is initially
set to maximum integer value.

* pred
  * the predicate used to test the elements
* returns
  * the longest prefix of this parallel iterable of elements that satisfy the
    predicate `pred`

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `implicit def task2ops[R, Tp](tsk: SSCTask[R, Tp]): TaskOps[R, Tp]`      ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def tasksupport: TaskSupport`                                           ###

The task support object which is responsible for scheduling and load-balancing
tasks to processors.

* Definition Classes
  * ParIterableLike
* See also
  * scala.collection.parallel.TaskSupport

(defined at scala.collection.parallel.ParIterableLike)


### `def tasksupport_=(ts: TaskSupport): Unit`                               ###

Changes the task support object which is responsible for scheduling and
load-balancing tasks to processors.

A task support object can be changed in a parallel collection after it has been
created, but only during a quiescent period, i.e. while there are no concurrent
invocations to parallel collection methods.

Here is a way to change the task support of a parallel collection:

```scala
import scala.collection.parallel._
val pc = mutable.ParArray(1, 2, 3)
pc.tasksupport = new ForkJoinTaskSupport(
  new java.util.concurrent.ForkJoinPool(2))
```

* Definition Classes
  * ParIterableLike
* See also
  * scala.collection.parallel.TaskSupport

(defined at scala.collection.parallel.ParIterableLike)


### `def toBuffer[U >: Int]: Buffer[U]`                                      ###

Uses the contents of this parallel iterable to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIndexedSeq: immutable.IndexedSeq[Int]`                            ###

Converts this parallel iterable to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIterator: scala.Iterator[Int]`                                    ###

Returns an Iterator over the elements in this parallel iterable. Will return the
same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toList: List[Int]`                                                  ###

Converts this parallel iterable to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toMap[K, V](implicit ev: <:<[Int, (K, V)]): ParMap[K, V]`           ###

[use case]

Converts this immutable parallel range to a map. This method is unavailable
unless the elements are members of Tuple2, each ((T, U)) becoming a key-value
pair in the map. Duplicate keys will be overwritten by later keys: if this is an
unordered collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this immutable parallel range.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toParCollection[U >: Int, That](cbf: () ⇒ Combiner[U, That]): That` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toParMap[K, V, That](cbf: () ⇒ Combiner[(K, V), That])(implicit ev: <:<[Int, (K, V)]): That` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toSet[U >: Int]: ParSet[U]`                                         ###

Converts this parallel iterable to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toStream: Stream[Int]`                                              ###

Converts this parallel iterable to a stream.

* returns
  * a stream containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toTraversable: GenTraversable[Int]`                                 ###

Converts this parallel iterable to an unspecified Traversable. Will return the
same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toVector: Vector[Int]`                                              ###

Converts this parallel iterable to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def withFilter(pred: (Int) ⇒ Boolean): ParSeq[Int]`                     ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def wrap[R](body: ⇒ R): NonDivisible[R]`                                ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipAll[S, U >: Int, That](that: GenIterable[S], thisElem: U, thatElem: S)(implicit bf: CanBuildFrom[ParSeq[Int], (U, S), That]): That` ###

[use case]

Returns a immutable parallel range formed from this immutable parallel range and
another iterable collection by combining corresponding elements in pairs. If one
of the two collections is shorter than the other, placeholder elements are used
to extend the shorter collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this immutable parallel
    range is shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    immutable parallel range.
* returns
  * a new immutable parallel range containing pairs consisting of corresponding
    elements of this immutable parallel range and `that` . The length of the
    returned collection is the maximum of the lengths of this immutable parallel
    range and `that` . If this immutable parallel range is shorter than `that` ,
     `thisElem` values are used to pad the result. If `that` is shorter than
    this immutable parallel range, `thatElem` values are used to pad the result.

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipWithIndex[U >: Int, That](implicit bf: CanBuildFrom[ParSeq[Int], (U, Int), That]): That` ###

[use case]

Zips this immutable parallel range with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new immutable parallel range containing pairs consisting of all elements
    of this immutable parallel range paired with their index. Indices start at
     `0` .

* Definition Classes
  * ParIterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.parallel.ParIterableLike)


--------------------------------------------------------------------------------
       Deprecated Value Members From scala.collection.parallel.ParSeqLike
--------------------------------------------------------------------------------


### `def view: SeqView[Int, immutable.Seq[Int]]`                             ###

* Definition Classes
  * ParSeqLike → ParIterableLike
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ use.seq.view

(defined at scala.collection.parallel.ParSeqLike)


--------------------------------------------------------------------------------
            Value Members From scala.collection.parallel.ParSeqLike
--------------------------------------------------------------------------------


### `def +:[U >: Int, That](elem: U)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

A copy of the immutable parallel range with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original immutable parallel range is not modified, so you will want to
capture the result.

Example:

```scala
scala> val x = List(1)
x: List[Int] = List(1)

scala> val y = 2 +: x
y: List[Int] = List(2, 1)

scala> println(x)
List(1)
```

* elem
  * the prepended element
* returns
  * a new immutable parallel range consisting of `elem` followed by all elements
    of this immutable parallel range.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def :+[U >: Int, That](elem: U)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

A copy of this immutable parallel range with an element appended.

A mnemonic for `+:` vs. `:+` is: the COLon goes on the COLlection side.

Note: will not terminate for infinite-sized collections.

Example:

```scala
scala> val a = List(1)
a: List[Int] = List(1)

scala> val b = a :+ 2
b: List[Int] = List(1, 2)

scala> println(a)
List(1)
```

* elem
  * the appended element
* returns
  * a new immutable parallel range consisting of all elements of this immutable
    parallel range followed by `elem` .

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def corresponds[S](that: GenSeq[S])(p: (Int, S) ⇒ Boolean): Boolean`    ###

Tests whether every element of this parallel iterable relates to the
corresponding element of another parallel sequence by satisfying a test
predicate.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* S
  * the type of the elements of `that`
* that
  * the other parallel sequence
* p
  * the test predicate, which relates elements from both sequences
* returns
  * `true` if both parallel sequences have the same length and `p(x, y)` is
     `true` for all corresponding elements `x` of this parallel iterable and
     `y` of `that` , otherwise `false`

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def diff[U >: Int](that: GenSeq[U]): ParSeq[Int]`                       ###

[use case]

Computes the multiset difference between this immutable parallel range and
another sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence of elements to remove
* returns
  * a new immutable parallel range which contains all elements of this immutable
    parallel range except some of occurrences of elements that also appear in
     `that` . If an element value `x` appears _n_ times in `that` , then the
    first _n_ occurrences of `x` will not form part of the result, but any
    following occurrences will.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def distinct: ParSeq[Int]`                                              ###

Builds a new parallel iterable from this parallel iterable without any duplicate
elements.

Note: will not terminate for infinite-sized collections.

* returns
  * A new parallel iterable which contains the first occurrence of every element
    of this parallel iterable.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def down(p: IterableSplitter[_]): SeqSplitter[Int]`                     ###

* Attributes
  * protected[this]
* Definition Classes
  * ParSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def endsWith[S](that: GenSeq[S]): Boolean`                              ###

Tests whether this parallel iterable ends with the given parallel sequence.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* S
  * the type of the elements of `that` sequence
* that
  * the sequence to test
* returns
  * `true` if this parallel iterable has `that` as a suffix, `false` otherwise

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def indexWhere(p: (Int) ⇒ Boolean, from: Int): Int`                     ###

Finds the first element satisfying some predicate.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state.

The index flag is initially set to maximum integer value.

* p
  * the predicate used to test the elements
* from
  * the starting offset for the search
* returns
  * the index `>= from` of the first element of this parallel iterable that
    satisfies the predicate `p` , or `-1` , if none exists

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def intersect[U >: Int](that: GenSeq[U]): ParSeq[Int]`                  ###

[use case]

Computes the multiset intersection between this immutable parallel range and
another sequence.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence of elements to intersect with.
* returns
  * a new immutable parallel range which contains all elements of this immutable
    parallel range which also appear in `that` . If an element value `x` appears
     _n_ times in `that` , then the first _n_ occurrences of `x` will be
    retained in the result, but any following occurrences will be omitted.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def iterator: PreciseSplitter[Int]`                                     ###

Creates a new split iterator used to traverse the elements of this collection.

By default, this method is implemented in terms of the protected `splitter`
method.

* returns
  * a split iterator

* Definition Classes
  * ParSeqLike → ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParSeqLike)


### `def lastIndexWhere(p: (Int) ⇒ Boolean, end: Int): Int`                  ###

Finds the last element satisfying some predicate.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state.

The index flag is initially set to minimum integer value.

* p
  * the predicate used to test the elements
* end
  * the maximum offset for the search
* returns
  * the index `<= end` of the first element of this parallel iterable that
    satisfies the predicate `p` , or `-1` , if none exists

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def padTo[U >: Int, That](len: Int, elem: U)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

A copy of this immutable parallel range with an element value appended until a
given target length is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new immutable parallel range consisting of all elements of this immutable
    parallel range followed by the minimal number of occurrences of `elem` so
    that the resulting immutable parallel range has a length of at least `len` .

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def patch[U >: Int, That](from: Int, patch: GenSeq[U], replaced: Int)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

Produces a new immutable parallel range where a slice of elements in this
immutable parallel range is replaced by another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original immutable parallel range
* returns
  * a new immutable parallel range consisting of all elements of this immutable
    parallel range except that `replaced` elements starting from `from` are
    replaced by `patch` .

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def reverse: ParSeq[Int]`                                               ###

Returns new parallel iterable with elements in reversed order.

Note: will not terminate for infinite-sized collections.

* returns
  * A new parallel iterable with all elements of this parallel iterable in
    reversed order.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def reverseMap[S, That](f: (Int) ⇒ S)(implicit bf: CanBuildFrom[ParSeq[Int], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this immutable
parallel range and collecting the results in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new immutable parallel range resulting from applying the given function
     `f` to each element of this immutable parallel range and collecting the
    results in reversed order.

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def sameElements[U >: Int](that: GenIterable[U]): Boolean`              ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this immutable parallel range.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * ParSeqLike → ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParSeqLike)


### `def segmentLength(p: (Int) ⇒ Boolean, from: Int): Int`                  ###

Returns the length of the longest segment of elements starting at a given
position satisfying some predicate.

This method will use `indexFlag` signalling capabilities. This means that
splitters may set and read the `indexFlag` state.

The index flag is initially set to maximum integer value.

* p
  * the predicate used to test the elements
* from
  * the starting offset for the search
* returns
  * the length of the longest segment of elements starting at `from` and
    satisfying the predicate

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def startsWith[S](that: GenSeq[S], offset: Int): Boolean`               ###

Tests whether this parallel iterable contains the given sequence at a given
index.

This method will use `abort` signalling capabilities. This means that splitters
may send and read `abort` signals.

* S
  * the element type of `that` parallel sequence
* that
  * the parallel sequence this sequence is being searched for
* offset
  * the starting offset for the search
* returns
  * `true` if there is a sequence `that` starting at `offset` in this sequence,
     `false` otherwise

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def updated[U >: Int, That](index: Int, elem: U)(implicit bf: CanBuildFrom[ParSeq[Int], U, That]): That` ###

[use case]

A copy of this immutable parallel range with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this immutable parallel range with the element at position
     `index` replaced by `elem` .

* Definition Classes
  * ParSeqLike → GenSeqLike

(defined at scala.collection.parallel.ParSeqLike)


### `def zip[U >: Int, S, That](that: GenIterable[S])(implicit bf: CanBuildFrom[ParSeq[Int], (U, S), That]): That` ###

[use case]

Returns a immutable parallel range formed from this immutable parallel range and
another iterable collection by combining corresponding elements in pairs. If one
of the two collections is longer than the other, its remaining elements are
ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new immutable parallel range containing pairs consisting of corresponding
    elements of this immutable parallel range and `that` . The length of the
    returned collection is the minimum of the lengths of this immutable parallel
    range and `that` .

* Definition Classes
  * ParSeqLike → ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParSeqLike)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.immutable.ParIterable
--------------------------------------------------------------------------------


### `def toIterable: ParIterable[Int]`                                       ###

Converts this parallel iterable to an iterable collection. Note that the choice
of target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this parallel iterable.

* Definition Classes
  * ParIterable → ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.immutable.ParIterable)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.immutable.ParRange
--------------------------------------------------------------------------------


### `new ParRange(range: immutable.Range)`                                   ###

* range
  * the sequential range this parallel range was obtained from

(defined at scala.collection.parallel.immutable.ParRange)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.immutable.ParRange
--------------------------------------------------------------------------------


### `final def apply(idx: Int): Int`                                         ###

Selects an element by its index in the immutable parallel range.

Example:

```scala
scala> val x = List(1, 2, 3, 4, 5)
x: List[Int] = List(1, 2, 3, 4, 5)

scala> x(3)
res1: Int = 4
```

* idx
  * The index to select.
* returns
  * the element of this immutable parallel range at index `idx` , where `0`
    indicates the first element.

* Definition Classes
  * ParRange → ParSeq → GenSeqLike
* Annotations
  * @ inline ()
* Exceptions thrown
  * IndexOutOfBoundsException if `idx` does not satisfy `0 <= idx < length` .

(defined at scala.collection.parallel.immutable.ParRange)


### `val range: immutable.Range`                                             ###

the sequential range this parallel range was obtained from

(defined at scala.collection.parallel.immutable.ParRange)


### `def seq: immutable.Range`                                               ###

* Definition Classes
  * ParRange → ParIterableLike → GenSeq → GenIterable → GenTraversable →
    GenSeqLike → Parallelizable → GenTraversableOnce

(defined at scala.collection.parallel.immutable.ParRange)


### `def splitter: ParRangeIterator`                                         ###

A more refined version of the iterator found in the `ParallelIterable` trait,
this iterator can be split into arbitrary subsets of iterators.

* returns
  * an iterator that can be split into subsets of precise size

* Definition Classes
  * ParRange → ParSeqLike → ParIterableLike

(defined at scala.collection.parallel.immutable.ParRange)


--------------------------------------------------------------------------------
         Value Members From scala.collection.parallel.immutable.ParSeq
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[ParSeq] with GenericParCompanion[ParSeq]` ###

The factory companion object that builds instances of class `mutable.ParSeq` .
(or its `Iterable` superclass where class `mutable.ParSeq` is not a `Seq` .)

* Definition Classes
  * ParSeq → ParIterable → ParSeq → ParIterable → GenericParTemplate → GenSeq →
    GenIterable → GenTraversable → GenericTraversableTemplate

(defined at scala.collection.parallel.immutable.ParSeq)


### `def toSeq: ParSeq[Int]`                                                 ###

Converts this mutable parallel sequence to a sequence. As with `toIterable` ,
it's lazy in this default implementation, as this `TraversableOnce` may be lazy
and unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this mutable parallel sequence.

* Definition Classes
  * ParSeq → ParIterable → ParSeqLike → ParIterableLike → GenSeqLike →
    GenTraversableOnce

(defined at scala.collection.parallel.immutable.ParSeq)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParRange to
    CollectionsHaveToParArray [ParRange, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParRange) ⇒ GenTraversableOnce
    [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
