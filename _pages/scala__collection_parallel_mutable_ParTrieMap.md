
#                 scala.collection.parallel.mutable.ParTrieMap                 #

```scala
final class ParTrieMap[K, V] extends ParMap[K, V] with GenericParMapTemplate[K, V, ParTrieMap] with ParMapLike[K, V, ParTrieMap[K, V], TrieMap[K, V]] with ParTrieMapCombiner[K, V] with Serializable
```

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


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Accessor[R, Tp] extends StrictSplitterCheckTask[R, Tp]`           ###

Standard accessor task that iterates over the elements of the collection.

* R
  * type of the result of this method ( `R` for result).
* Tp
  * the representation type of the task at hand.

* Attributes
  * protected
* Definition Classes
  * ParIterableLike


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


### `class DefaultKeySet extends ParSet[K]`                                  ###

* Attributes
  * protected
* Definition Classes
  * ParMapLike


### `class DefaultValuesIterable extends ParIterable[V]`                     ###

* Attributes
  * protected
* Definition Classes
  * ParMapLike


### `class Drop[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Drop[U, This]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


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


### `type SSCTask[R, Tp] = StrictSplitterCheckTask[R, Tp]`                   ###

* Definition Classes
  * ParIterableLike


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


### `abstract class SeqComposite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends Composite[FR, SR, R, First, Second]` ###

Sequentially performs one task after another.

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `trait SignallingOps[PI <: DelegatedSignalling] extends AnyRef`          ###

* Definition Classes
  * ParIterableLike


### `class Size extends Task[Int, Size]`                                     ###

Computes TrieMap size in parallel.

* Source
  * [ParTrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParTrieMap.scala#L1)


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


### `trait Transformer[R, Tp] extends Accessor[R, Tp]`                       ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike


### `class Zip[U >: T, S, That] extends Transformer[Combiner[(U, S), That], Zip[U, S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


### `class ZipAll[U >: T, S, That] extends Transformer[Combiner[(U, S), That], ZipAll[U, S, That]]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike


--------------------------------------------------------------------------------
            Value Members From scala.collection.CustomParallelizable
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[(K, V), ParTrieMap[K, V]]`                    ###

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
                 Value Members From scala.collection.GenMapLike
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

Compares two maps structurally; i.e., checks if all mappings contained in this
map are also contained in the other map, and vice versa.

* that
  * the other map
* returns
  * `true` if both maps contain exactly the same mappings, `false` otherwise.

* Definition Classes
  * GenMapLike → Equals → AnyRef → Any

(defined at scala.collection.GenMapLike)


--------------------------------------------------------------------------------
       Value Members From scala.collection.generic.GenericParMapTemplate
--------------------------------------------------------------------------------


### `def genericMapCombiner[P, Q]: Combiner[(P, Q), ParTrieMap[P, Q]]`       ###

* Definition Classes
  * GenericParMapTemplate

(defined at scala.collection.generic.GenericParMapTemplate)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.GenericParTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Combiner[B, ParIterable[B]]`                     ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def genericCombiner[B]: Combiner[B, ParIterable[B]]`                    ###

* Definition Classes
  * GenericParTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def newBuilder: Builder[(K, V), ParIterable[(K, V)]]`                   ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericParTemplate)


--------------------------------------------------------------------------------
     Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def flatten[B](implicit asTraversable: ((K, V)) ⇒ GenTraversableOnce[B]): ParIterable[B]` ###

[use case]

Converts this parallel map of traversable collections into a parallel map formed
by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of parallel
map. For example:

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
  * a new parallel map resulting from concatenating all element parallel map s.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: ((K, V)) ⇒ GenTraversableOnce[B]): ParIterable[ParIterable[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: ((K, V)) ⇒ (A1, A2, A3)): (ParIterable[A1], ParIterable[A2], ParIterable[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: ((K, V)) ⇒ (A1, A2)): (ParIterable[A1], ParIterable[A2])` ###

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
              Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[(K, V)]): ParTrieMap.this.type`             ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: (K, V), elem2: (K, V), elems: (K, V)*): ParTrieMap.this.type` ###

adds two or more elements to this growable collection.

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * the growable collection itself

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


--------------------------------------------------------------------------------
             Value Members From scala.collection.generic.Shrinkable
--------------------------------------------------------------------------------


### `def --=(xs: TraversableOnce[K]): ParTrieMap.this.type`                  ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: K, elem2: K, elems: K*): ParTrieMap.this.type`            ###

Removes two or more elements from this shrinkable collection.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (ParTrieMap[K, V]) ⇒ NewTo): Builder[(K, V), NewTo]` ###

Creates a new builder by applying a transformation function to the results of
this builder.

* NewTo
  * the type of collection returned by `f` .
* f
  * the transformation function.
* returns
  * a new builder which is the same as the current builder except that a
    transformation function is applied to this builder's result.

* Definition Classes
  * Builder
* Note
  * The original builder should no longer be used after `mapResult` is called.

(defined at scala.collection.mutable.Builder)


### `def sizeHint(size: Int): Unit`                                          ###

Gives a hint how many elements are expected to be added when the next `result`
is called. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _]): Unit`                        ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _], delta: Int): Unit`            ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.
* delta
  * a correction to add to the `coll.size` to produce the size hint.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHintBounded(size: Int, boundingColl: TraversableLike[_, _]): Unit` ###

Gives a hint how many elements are expected to be added when the next `result`
is called, together with an upper bound given by the size of some other
collection. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.
* boundingColl
  * the bounding collection. If it is an IndexedSeqLike, then sizes larger than
    collection's size are reduced.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.Cloneable
--------------------------------------------------------------------------------


### `def clone(): ParTrieMap[K, V]`                                          ###

Create a copy of the receiver object.

The default implementation of the `clone` method is platform dependent.

* returns
  * a copy of the receiver object.

* Definition Classes
  * Cloneable → AnyRef
* Note
  * not specified by SLS as a member of AnyRef

(defined at scala.collection.mutable.Cloneable)


--------------------------------------------------------------------------------
             Value Members From scala.collection.parallel.Combiner
--------------------------------------------------------------------------------


### `var _combinerTaskSupport: TaskSupport`                                  ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport: TaskSupport`                                   ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport_=(cts: TaskSupport): Unit`                      ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def resultWithTaskSupport: ParTrieMap[K, V]`                            ###

Constructs the result and sets the appropriate tasksupport object to the
resulting collection if this is applicable.

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


--------------------------------------------------------------------------------
    Deprecated Value Members From scala.collection.parallel.ParIterableLike
--------------------------------------------------------------------------------


### `def view: IterableView[(K, V), TrieMap[K, V]]`                          ###

* Definition Classes
  * ParIterableLike
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use.seq.view instead

(defined at scala.collection.parallel.ParIterableLike)


--------------------------------------------------------------------------------
          Value Members From scala.collection.parallel.ParIterableLike
--------------------------------------------------------------------------------


### `def ++[U >: (K, V), That](that: GenTraversableOnce[U])(implicit bf: CanBuildFrom[ParTrieMap[K, V], U, That]): That` ###

[use case]

Returns a new parallel map containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
parallel map is the most specific superclass encompassing the element types of
the two operands.

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
  * a new parallel map which contains all elements of this parallel map followed
    by all elements of `that` .

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def /:[S](z: S)(op: (S, (K, V)) ⇒ S): S`                                ###

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


### `def :\[S](z: S)(op: ((K, V), S) ⇒ S): S`                                ###

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


### `def aggregate[S](z: ⇒ S)(seqop: (S, (K, V)) ⇒ S, combop: (S, S) ⇒ S): S` ###

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


### `def bf2seq[S, That](bf: CanBuildFrom[ParTrieMap[K, V], S, That]): CanBuildFrom[TrieMap[K, V], S, That]` ###

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


### `def collect[S, That](pf: PartialFunction[(K, V), S])(implicit bf: CanBuildFrom[ParTrieMap[K, V], S, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
parallel map

on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the parallel map.
* returns
  * a new parallel map resulting from applying the given partial function `pf`
    to each element on which it is defined and collecting the results. The order
    of the elements is preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def combinerFactory: CombinerFactory[(K, V), ParTrieMap[K, V]]`         ###

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


### `def copyToArray[U >: (K, V)](xs: Array[U]): Unit`                       ###

[use case]

Copies the elements of this parallel map to an array. Fills the given array
 `xs` with values of this parallel map. Copying will stop once either the end of
the current parallel map is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: (K, V)](xs: Array[U], start: Int): Unit`           ###

[use case]

Copies the elements of this parallel map to an array. Fills the given array
 `xs` with values of this parallel map, beginning at index `start` . Copying
will stop once either the end of the current parallel map is reached, or the end
of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: (K, V)](xs: Array[U], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this parallel map to an array. Fills the given array
 `xs` with at most `len` elements of this parallel map, starting at position
 `start` . Copying will stop once either the end of the current parallel map is
reached, or the end of the target array is reached, or `len` elements have been
copied.

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


### `def count(p: ((K, V)) ⇒ Boolean): Int`                                  ###

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


### `def drop(n: Int): ParTrieMap[K, V]`                                     ###

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


### `def dropWhile(pred: ((K, V)) ⇒ Boolean): ParTrieMap[K, V]`              ###

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


### `def exists(p: ((K, V)) ⇒ Boolean): Boolean`                             ###

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


### `def filter(pred: ((K, V)) ⇒ Boolean): ParTrieMap[K, V]`                 ###

Selects all elements of this parallel iterable which satisfy a predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new parallel iterable consisting of all elements of this parallel iterable
    that satisfy the given predicate `p` . Their order may not be preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def filterNot(pred: ((K, V)) ⇒ Boolean): ParTrieMap[K, V]`              ###

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


### `def find(p: ((K, V)) ⇒ Boolean): Option[(K, V)]`                        ###

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


### `def flatMap[S, That](f: ((K, V)) ⇒ GenTraversableOnce[S])(implicit bf: CanBuildFrom[ParTrieMap[K, V], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this parallel
map

and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of parallel
map. This might cause unexpected results sometimes. For example:

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
  * a new parallel map resulting from applying the given collection-valued
    function `f` to each element of this parallel map and concatenating the
    results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def foldLeft[S](z: S)(op: (S, (K, V)) ⇒ S): S`                          ###

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


### `def foldRight[S](z: S)(op: ((K, V), S) ⇒ S): S`                         ###

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


### `def fold[U >: (K, V)](z: U)(op: (U, U) ⇒ U): U`                         ###

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


### `def forall(p: ((K, V)) ⇒ Boolean): Boolean`                             ###

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


### `def foreach[U](f: ((K, V)) ⇒ U): Unit`                                  ###

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


### `def groupBy[K](f: ((K, V)) ⇒ K): immutable.ParMap[K, ParTrieMap[K, V]]` ###

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


### `def head: (K, V)`                                                       ###

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


### `def headOption: Option[(K, V)]`                                         ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this parallel iterable if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def init: ParTrieMap[K, V]`                                             ###

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


### `def iterator: Splitter[(K, V)]`                                         ###

Creates a new split iterator used to traverse the elements of this collection.

By default, this method is implemented in terms of the protected `splitter`
method.

* returns
  * a split iterator

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def last: (K, V)`                                                       ###

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


### `def lastOption: Option[(K, V)]`                                         ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this parallel iterable$ if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def map[S, That](f: ((K, V)) ⇒ S)(implicit bf: CanBuildFrom[ParTrieMap[K, V], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this parallel
map.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new parallel map resulting from applying the given function `f` to each
    element of this parallel map and collecting the results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def maxBy[S](f: ((K, V)) ⇒ S)(implicit cmp: Ordering[S]): (K, V)`       ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this parallel map with the largest value measured by
    function f.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def minBy[S](f: ((K, V)) ⇒ S)(implicit cmp: Ordering[S]): (K, V)`       ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this parallel map with the smallest value measured by
    function f.

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


### `def par: ParTrieMap[K, V]`                                              ###

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


### `def partition(pred: ((K, V)) ⇒ Boolean): (ParTrieMap[K, V], ParTrieMap[K, V])` ###

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


### `def reduceLeftOption[U >: (K, V)](op: (U, (K, V)) ⇒ U): Option[U]`      ###

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


### `def reduceLeft[U >: (K, V)](op: (U, (K, V)) ⇒ U): U`                    ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceOption[U >: (K, V)](op: (U, U) ⇒ U): Option[U]`               ###

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


### `def reduceRightOption[U >: (K, V)](op: ((K, V), U) ⇒ U): Option[U]`     ###

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


### `def reduceRight[U >: (K, V)](op: ((K, V), U) ⇒ U): U`                   ###

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


### `def reduce[U >: (K, V)](op: (U, U) ⇒ U): U`                             ###

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


### `def repr: ParTrieMap[K, V]`                                             ###

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


### `def sameElements[U >: (K, V)](that: GenIterable[U]): Boolean`           ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this parallel map.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scan[U >: (K, V), That](z: U)(op: (U, U) ⇒ U)(implicit bf: CanBuildFrom[ParTrieMap[K, V], U, That]): That` ###

[use case]

Computes a prefix scan of the elements of the collection.

Note: The neutral element `z` may be applied more than once.

* z
  * neutral element for the operator `op`
* op
  * the associative operator for the scan
* returns
  * a new parallel map containing the prefix scan of the elements in this
    parallel map

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scanLeft[S, That](z: S)(op: (S, (K, V)) ⇒ S)(implicit bf: CanBuildFrom[ParTrieMap[K, V], S, That]): That` ###

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


### `def scanRight[S, That](z: S)(op: ((K, V), S) ⇒ S)(implicit bf: CanBuildFrom[ParTrieMap[K, V], S, That]): That` ###

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


### `def sequentially[S, That <: Parallel](b: (TrieMap[K, V]) ⇒ Parallelizable[S, That]): ParTrieMap[K, V]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def slice(unc_from: Int, unc_until: Int): ParTrieMap[K, V]`             ###

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


### `def span(pred: ((K, V)) ⇒ Boolean): (ParTrieMap[K, V], ParTrieMap[K, V])` ###

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


### `def splitAt(n: Int): (ParTrieMap[K, V], ParTrieMap[K, V])`              ###

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


### `def tail: ParTrieMap[K, V]`                                             ###

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


### `def take(n: Int): ParTrieMap[K, V]`                                     ###

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


### `def takeWhile(pred: ((K, V)) ⇒ Boolean): ParTrieMap[K, V]`              ###

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


### `def toBuffer[U >: (K, V)]: Buffer[U]`                                   ###

Uses the contents of this parallel iterable to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIndexedSeq: immutable.IndexedSeq[(K, V)]`                         ###

Converts this parallel iterable to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIterator: scala.Iterator[(K, V)]`                                 ###

Returns an Iterator over the elements in this parallel iterable. Will return the
same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toList: List[(K, V)]`                                               ###

Converts this parallel iterable to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toMap[K, V](implicit ev: <:<[(K, V), (K, V)]): immutable.ParMap[K, V]` ###

[use case]

Converts this parallel map to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this parallel map.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toParCollection[U >: (K, V), That](cbf: () ⇒ Combiner[U, That]): That` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toParMap[K, V, That](cbf: () ⇒ Combiner[(K, V), That])(implicit ev: <:<[(K, V), (K, V)]): That` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toSet[U >: (K, V)]: immutable.ParSet[U]`                            ###

Converts this parallel iterable to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toStream: Stream[(K, V)]`                                           ###

Converts this parallel iterable to a stream.

* returns
  * a stream containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toTraversable: GenTraversable[(K, V)]`                              ###

Converts this parallel iterable to an unspecified Traversable. Will return the
same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toVector: Vector[(K, V)]`                                           ###

Converts this parallel iterable to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def withFilter(pred: ((K, V)) ⇒ Boolean): ParTrieMap[K, V]`             ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def wrap[R](body: ⇒ R): NonDivisible[R]`                                ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipAll[S, U >: (K, V), That](that: GenIterable[S], thisElem: U, thatElem: S)(implicit bf: CanBuildFrom[ParTrieMap[K, V], (U, S), That]): That` ###

[use case]

Returns a parallel map formed from this parallel map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is shorter than the other, placeholder elements are used to extend
the shorter collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this parallel map is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    parallel map.
* returns
  * a new parallel map containing pairs consisting of corresponding elements of
    this parallel map and `that` . The length of the returned collection is the
    maximum of the lengths of this parallel map and `that` . If this parallel
    map is shorter than `that` , `thisElem` values are used to pad the result.
    If `that` is shorter than this parallel map, `thatElem` values are used to
    pad the result.

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipWithIndex[U >: (K, V), That](implicit bf: CanBuildFrom[ParTrieMap[K, V], (U, Int), That]): That` ###

[use case]

Zips this parallel map with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new parallel map containing pairs consisting of all elements of this
    parallel map paired with their index. Indices start at `0` .

* Definition Classes
  * ParIterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.parallel.ParIterableLike)


### `def zip[U >: (K, V), S, That](that: GenIterable[S])(implicit bf: CanBuildFrom[ParTrieMap[K, V], (U, S), That]): That` ###

[use case]

Returns a parallel map formed from this parallel map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new parallel map containing pairs consisting of corresponding elements of
    this parallel map and `that` . The length of the returned collection is the
    minimum of the lengths of this parallel map and `that` .

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


--------------------------------------------------------------------------------
            Value Members From scala.collection.parallel.ParMapLike
--------------------------------------------------------------------------------


### `def apply(key: K): V`                                                   ###

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def contains(key: K): Boolean`                                          ###

Tests whether this map contains a binding for a key.

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def default(key: K): V`                                                 ###

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def filterKeys(p: (K) ⇒ Boolean): parallel.ParMap[K, V]`                ###

Filters this map by retaining only keys satisfying a predicate.

* p
  * the predicate used to test keys
* returns
  * an immutable map consisting only of those key value pairs of this map where
    the key satisfies the predicate `p` . The resulting map wraps the original
    map without copying any elements.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def getOrElse[U >: V](key: K, default: ⇒ U): U`                         ###

[use case]

Returns the value associated with a key, or a default value if the key is not
contained in the map.

* key
  * the key.
* default
  * a computation that yields a default value in case no binding for `key` is
    found in the map.
* returns
  * the value associated with `key` if it exists, otherwise the result of the
     `default` computation.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def isDefinedAt(key: K): Boolean`                                       ###

Tests whether this map contains a binding for a key. This method, which
implements an abstract method of trait `PartialFunction` , is equivalent to
 `contains` .

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def keySet: parallel.ParSet[K]`                                         ###

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def keys: parallel.ParIterable[K]`                                      ###

Collects all keys of this map in an iterable collection.

* returns
  * the keys of this map as an iterable.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def keysIterator: IterableSplitter[K]`                                  ###

Creates an iterator for all keys.

* returns
  * an iterator over all keys.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def mapValues[S](f: (V) ⇒ S): parallel.ParMap[K, S]`                    ###

Transforms this map by applying a function to every retrieved value.

* f
  * the function used to transform values of this map.
* returns
  * a map view which maps every key of this map to `f(this(key))` . The
    resulting map wraps the original map without copying any elements.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def values: parallel.ParIterable[V]`                                    ###

Collects all values of this map in an iterable collection.

* returns
  * the values of this map as an iterable.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


### `def valuesIterator: IterableSplitter[V]`                                ###

Creates an iterator for all values in this map.

* returns
  * an iterator over all values that are associated with some key in this map.

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.ParMapLike)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParIterable
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[ParIterable] with GenericParCompanion[ParIterable]` ###

The factory companion object that builds instances of class `ParIterable` . (or
its `Iterable` superclass where class `ParIterable` is not a `Seq` .)

* Definition Classes
  * ParIterable → ParIterable → GenericParTemplate → GenIterable →
    GenTraversable → GenericTraversableTemplate

(defined at scala.collection.parallel.mutable.ParIterable)


### `def toIterable: ParIterable[(K, V)]`                                    ###

Converts this parallel iterable to an iterable collection. Note that the choice
of target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this parallel iterable.

* Definition Classes
  * ParIterable → ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.mutable.ParIterable)


### `def toSeq: ParSeq[(K, V)]`                                              ###

Converts this parallel iterable to a sequence. As with `toIterable` , it's lazy
in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this parallel iterable.

* Definition Classes
  * ParIterable → ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.mutable.ParIterable)


--------------------------------------------------------------------------------
          Value Members From scala.collection.parallel.mutable.ParMap
--------------------------------------------------------------------------------


### `def updated[U >: V](key: K, value: U): ParMap[K, U]`                    ###

* Definition Classes
  * ParMap → ParMap → GenMap

(defined at scala.collection.parallel.mutable.ParMap)


### `def withDefault(d: (K) ⇒ V): ParMap[K, V]`                              ###

The same map with a given default function. Note: `get` , `contains` ,
 `iterator` , `keys` , etc are not affected by `withDefault` .

Invoking transformer methods (e.g. `map` ) will not preserve the default value.

* d
  * the function mapping keys to values, used for non-present keys
* returns
  * a wrapper of the map with a default value

* Definition Classes
  * ParMap

(defined at scala.collection.parallel.mutable.ParMap)


### `def withDefaultValue(d: V): ParMap[K, V]`                               ###

The same map with a given default value.

Invoking transformer methods (e.g. `map` ) will not preserve the default value.

* d
  * default value used for non-present keys
* returns
  * a wrapper of the map with a default value

* Definition Classes
  * ParMap

(defined at scala.collection.parallel.mutable.ParMap)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParMapLike
--------------------------------------------------------------------------------


### `def +[U >: V](kv: (K, U)): ParMap[K, U]`                                ###

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.mutable.ParMapLike)


### `def -(key: K): ParTrieMap[K, V]`                                        ###

* Definition Classes
  * ParMapLike → GenMapLike

(defined at scala.collection.parallel.mutable.ParMapLike)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.mutable.ParTrieMap
--------------------------------------------------------------------------------


### `new ParTrieMap()`                                                       ###

(defined at scala.collection.parallel.mutable.ParTrieMap)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParTrieMap
--------------------------------------------------------------------------------


### `def +=(kv: (K, V)): ParTrieMap.this.type`                               ###

Adds a single element to the builder.

* returns
  * the builder itself.

* Definition Classes
  * ParTrieMap → Builder → ParMapLike → Growable

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def -=(key: K): ParTrieMap.this.type`                                   ###

Removes a single element from this parallel map.

* returns
  * the parallel map itself

* Definition Classes
  * ParTrieMap → ParMapLike → Shrinkable

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def empty: ParTrieMap[K, V]`                                            ###

* Definition Classes
  * ParTrieMap → ParMap → ParMap → ParMapLike

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def get(key: K): Option[V]`                                             ###

* Definition Classes
  * ParTrieMap → GenMapLike

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def mapCompanion: GenericParMapCompanion[ParTrieMap]`                   ###

* Definition Classes
  * ParTrieMap → ParMap → ParMap → GenericParMapTemplate

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def newCombiner: Combiner[(K, V), ParTrieMap[K, V]]`                    ###

* Attributes
  * protected[this]
* Definition Classes
  * ParTrieMap → ParMap → GenericParMapTemplate → GenericParTemplate →
    HasNewCombiner

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def put(key: K, value: V): Option[V]`                                   ###

* Definition Classes
  * ParTrieMap → ParMapLike

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def remove(key: K): Option[V]`                                          ###

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def result(): ParTrieMap[K, V]`                                         ###

Produces a collection from the added elements. This is a terminal operation: the
builder's contents are undefined after this operation, and no further methods
should be called.

* returns
  * a collection containing the elements added to this builder.

* Definition Classes
  * ParTrieMap → Builder

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def seq: TrieMap[K, V]`                                                 ###

* Definition Classes
  * ParTrieMap → ParMap → ParIterable → ParIterableLike → GenMap → GenIterable →
    GenTraversable → GenMapLike → Parallelizable → GenTraversableOnce

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def splitter: ParTrieMapSplitter[K, V]`                                 ###

Creates a new parallel iterator used to traverse the elements of this parallel
collection. This iterator is more specific than the iterator of the returned by
 `iterator` , and augmented with additional accessor and transformer methods.

* returns
  * a parallel iterator

* Definition Classes
  * ParTrieMap → ParIterableLike

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def update(key: K, value: V): Unit`                                     ###

(defined at scala.collection.parallel.mutable.ParTrieMap)


--------------------------------------------------------------------------------
    Value Members From scala.collection.parallel.mutable.ParTrieMapCombiner
--------------------------------------------------------------------------------


### `def combine[N <: (K, V), NewTo >: ParTrieMap[K, V]](other: Combiner[N, NewTo]): Combiner[N, NewTo]` ###

Combines the contents of the receiver builder and the `other` builder, producing
a new builder containing both their elements.

This method may combine the two builders by copying them into a larger
collection, by producing a lazy view that gets evaluated once `result` is
invoked, or use a merge operation specific to the data structure in question.

Note that both the receiver builder and `other` builder become invalidated after
the invocation of this method, and should be cleared (see `clear` ) if they are
to be used again.

Also, combining two combiners `c1` and `c2` for which `c1 eq c2` is `true` ,
that is, they are the same objects in memory:

```scala
c1.combine(c2)
```

always does nothing and returns `c1` .

* N
  * the type of elements contained by the `other` builder
* NewTo
  * the type of collection produced by the `other` builder
* other
  * the other builder
* returns
  * the parallel builder containing both the elements of this and the `other`
    builder

* Definition Classes
  * ParTrieMapCombiner → Combiner

(defined at scala.collection.parallel.mutable.ParTrieMapCombiner)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParTrieMap [K, V] to
    CollectionsHaveToParArray [ParTrieMap [K, V], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParTrieMap [K, V]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
