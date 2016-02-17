
#                 scala.collection.parallel.mutable.ParHashSet                 #

```scala
class ParHashSet[T] extends ParSet[T] with GenericParTemplate[T, ParHashSet] with ParSetLike[T, ParHashSet[T], HashSet[T]] with ParFlatHashTable[T] with Serializable
```

A parallel hash set.

 `ParHashSet` is a parallel set which internally keeps elements within a hash
table. It uses linear probing to resolve collisions.

* T
  * type of the elements in the parallel hash set.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashSet.scala#L1)


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


### `abstract class ParFlatHashTableIterator extends IterableSplitter[T] with SizeMapUtils` ###

* Definition Classes
  * ParFlatHashTable


### `class ParHashSetIterator extends ParFlatHashTableIterator`              ###

* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashSet.scala#L1)


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
                       Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def andThen[A](g: (Boolean) ⇒ A): (T) ⇒ A`                              ###

Composes two instances of Function1 in a new Function1, with this function
applied first.

* A
  * the result type of function `g`
* g
  * a function R => A
* returns
  * a new function `f` such that `f(x) == g(apply(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


### `def compose[A](g: (A) ⇒ T): (A) ⇒ Boolean`                              ###

Composes two instances of Function1 in a new Function1, with this function
applied last.

* A
  * the type to which function `g` can be applied
* g
  * a function A => T1
* returns
  * a new function `f` such that `f(x) == apply(g(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


--------------------------------------------------------------------------------
            Value Members From scala.collection.CustomParallelizable
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[T, ParHashSet[T]]`                            ###

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
                 Value Members From scala.collection.GenSetLike
--------------------------------------------------------------------------------


### `def &(that: GenSet[T]): ParHashSet[T]`                                  ###

Computes the intersection between this set and another set.

 *Note:* Same as `intersect` .

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def &~(that: GenSet[T]): ParHashSet[T]`                                 ###

The difference of this set and another set.

 *Note:* Same as `diff` .

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def apply(elem: T): Boolean`                                            ###

Tests if some element is contained in this set.

This method is equivalent to `contains` . It allows sets to be interpreted as
predicates.

* elem
  * the element to test for membership.
* returns
  * `true` if `elem` is contained in this set, `false` otherwise.

* Definition Classes
  * GenSetLike → Function1

(defined at scala.collection.GenSetLike)


### `def equals(that: Any): Boolean`                                         ###

Compares this set with another object for equality.

 *Note:* This operation contains an unchecked cast: if `that` is a set, it will
assume with an unchecked cast that it has the same element type as this set. Any
subsequent ClassCastException is treated as a `false` result.

* that
  * the other object
* returns
  * `true` if `that` is a set which contains the same elements as this set.

* Definition Classes
  * GenSetLike → Equals → AnyRef → Any

(defined at scala.collection.GenSetLike)


### `def intersect(that: GenSet[T]): ParHashSet[T]`                          ###

Computes the intersection between this set and another set.

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def subsetOf(that: GenSet[T]): Boolean`                                 ###

Tests whether this set is a subset of another set.

* that
  * the set to test.
* returns
  * `true` if this set is a subset of `that` , i.e. if every element of this set
    is also an element of `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def |(that: GenSet[T]): ParHashSet[T]`                                  ###

Computes the union between this set and another set.

 *Note:* Same as `union` .

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.GenericParTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Combiner[B, ParHashSet[B]]`                      ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def genericCombiner[B]: Combiner[B, ParHashSet[B]]`                     ###

* Definition Classes
  * GenericParTemplate

(defined at scala.collection.generic.GenericParTemplate)


### `def newBuilder: Builder[T, ParHashSet[T]]`                              ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericParTemplate)


### `def newCombiner: Combiner[T, ParHashSet[T]]`                            ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericParTemplate → HasNewCombiner

(defined at scala.collection.generic.GenericParTemplate)


--------------------------------------------------------------------------------
     Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def flatten[B](implicit asTraversable: (T) ⇒ GenTraversableOnce[B]): ParHashSet[B]` ###

[use case]

Converts this parallel hash set of traversable collections into a parallel hash
set formed by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of parallel
hash set. For example:

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
  * a new parallel hash set resulting from concatenating all element parallel
    hash set s.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (T) ⇒ GenTraversableOnce[B]): ParHashSet[ParHashSet[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (T) ⇒ (A1, A2, A3)): (ParHashSet[A1], ParHashSet[A2], ParHashSet[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (T) ⇒ (A1, A2)): (ParHashSet[A1], ParHashSet[A2])` ###

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


### `def ++=(xs: TraversableOnce[T]): ParHashSet.this.type`                  ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: T, elem2: T, elems: T*): ParHashSet.this.type`            ###

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


### `def --=(xs: TraversableOnce[T]): ParHashSet.this.type`                  ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: T, elem2: T, elems: T*): ParHashSet.this.type`            ###

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
             Value Members From scala.collection.mutable.Cloneable
--------------------------------------------------------------------------------


### `def clone(): ParHashSet[T]`                                             ###

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
           Value Members From scala.collection.mutable.FlatHashTable
--------------------------------------------------------------------------------


### `def addElem(elem: T): Boolean`                                          ###

Add elem if not yet in table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def addEntry(newEntry: AnyRef): Boolean`                                ###

Add an entry (an elem converted to an entry via elemToEntry) if not yet in
table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def calcSizeMapSize(tableLength: Int): Int`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def capacity(expectedSize: Int): Int`                                   ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def containsElem(elem: T): Boolean`                                     ###

Checks whether an element is contained in the hash table.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def findEntry(elem: T): Option[T]`                                      ###

Finds an entry in the hash table if such an element exists.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `final def index(hcode: Int): Int`                                       ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def initWithContents(c: Contents[T]): Unit`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapAdd(h: Int): Unit`                                         ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapRemove(h: Int): Unit`                                      ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapReset(tableLength: Int): Unit`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def removeElem(elem: T): Boolean`                                       ###

Removes an elem from the hash table returning true if the element was found (and
thus removed) or false if it didn't exist.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def sizeMapInit(tableLength: Int): Unit`                                ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


--------------------------------------------------------------------------------
      Value Members From scala.collection.mutable.FlatHashTable.HashUtils
--------------------------------------------------------------------------------


### `final def elemToEntry(elem: T): AnyRef`                                 ###

Elems have type A, but we store AnyRef in the table. Plus we need to deal with
null elems, which need to be stored as NullSentinel

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


### `final def entryToElem(entry: AnyRef): T`                                ###

Does the inverse translation of elemToEntry

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


### `final def improve(hcode: Int, seed: Int): Int`                          ###

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


--------------------------------------------------------------------------------
    Deprecated Value Members From scala.collection.parallel.ParIterableLike
--------------------------------------------------------------------------------


### `def view: IterableView[T, HashSet[T]]`                                  ###

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


### `def ++[U >: T, That](that: GenTraversableOnce[U])(implicit bf: CanBuildFrom[ParHashSet[T], U, That]): That` ###

[use case]

Returns a new parallel hash set containing the elements from the left hand
operand followed by the elements from the right hand operand. The element type
of the parallel hash set is the most specific superclass encompassing the
element types of the two operands.

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
  * a new parallel hash set which contains all elements of this parallel hash
    set followed by all elements of `that` .

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def /:[S](z: S)(op: (S, T) ⇒ S): S`                                     ###

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


### `def :\[S](z: S)(op: (T, S) ⇒ S): S`                                     ###

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


### `def aggregate[S](z: ⇒ S)(seqop: (S, T) ⇒ S, combop: (S, S) ⇒ S): S`     ###

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


### `def bf2seq[S, That](bf: CanBuildFrom[ParHashSet[T], S, That]): CanBuildFrom[HashSet[T], S, That]` ###

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


### `def collect[S, That](pf: PartialFunction[T, S])(implicit bf: CanBuildFrom[ParHashSet[T], S, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
parallel hash set

on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the parallel hash set.
* returns
  * a new parallel hash set resulting from applying the given partial function
     `pf` to each element on which it is defined and collecting the results. The
    order of the elements is preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def combinerFactory: CombinerFactory[T, ParHashSet[T]]`                 ###

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


### `def copyToArray[U >: T](xs: Array[U]): Unit`                            ###

[use case]

Copies the elements of this parallel hash set to an array. Fills the given array
 `xs` with values of this parallel hash set. Copying will stop once either the
end of the current parallel hash set is reached, or the end of the target array
is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: T](xs: Array[U], start: Int): Unit`                ###

[use case]

Copies the elements of this parallel hash set to an array. Fills the given array
 `xs` with values of this parallel hash set, beginning at index `start` .
Copying will stop once either the end of the current parallel hash set is
reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def copyToArray[U >: T](xs: Array[U], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this parallel hash set to an array. Fills the given array
 `xs` with at most `len` elements of this parallel hash set, starting at
position `start` . Copying will stop once either the end of the current parallel
hash set is reached, or the end of the target array is reached, or `len`
elements have been copied.

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


### `def count(p: (T) ⇒ Boolean): Int`                                       ###

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


### `def drop(n: Int): ParHashSet[T]`                                        ###

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


### `def dropWhile(pred: (T) ⇒ Boolean): ParHashSet[T]`                      ###

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


### `def exists(p: (T) ⇒ Boolean): Boolean`                                  ###

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


### `def filter(pred: (T) ⇒ Boolean): ParHashSet[T]`                         ###

Selects all elements of this parallel iterable which satisfy a predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new parallel iterable consisting of all elements of this parallel iterable
    that satisfy the given predicate `p` . Their order may not be preserved.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def filterNot(pred: (T) ⇒ Boolean): ParHashSet[T]`                      ###

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


### `def find(p: (T) ⇒ Boolean): Option[T]`                                  ###

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


### `def flatMap[S, That](f: (T) ⇒ GenTraversableOnce[S])(implicit bf: CanBuildFrom[ParHashSet[T], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this parallel
hash set

and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of parallel
hash set. This might cause unexpected results sometimes. For example:

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
  * a new parallel hash set resulting from applying the given collection-valued
    function `f` to each element of this parallel hash set and concatenating the
    results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def foldLeft[S](z: S)(op: (S, T) ⇒ S): S`                               ###

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


### `def foldRight[S](z: S)(op: (T, S) ⇒ S): S`                              ###

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


### `def fold[U >: T](z: U)(op: (U, U) ⇒ U): U`                              ###

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


### `def forall(p: (T) ⇒ Boolean): Boolean`                                  ###

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


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

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


### `def groupBy[K](f: (T) ⇒ K): immutable.ParMap[K, ParHashSet[T]]`         ###

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


### `def init: ParHashSet[T]`                                                ###

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


### `def map[S, That](f: (T) ⇒ S)(implicit bf: CanBuildFrom[ParHashSet[T], S, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this parallel
hash set.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new parallel hash set resulting from applying the given function `f` to
    each element of this parallel hash set and collecting the results.

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def maxBy[S](f: (T) ⇒ S)(implicit cmp: Ordering[S]): T`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this parallel hash set with the largest value measured
    by function f.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def minBy[S](f: (T) ⇒ S)(implicit cmp: Ordering[S]): T`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this parallel hash set with the smallest value measured
    by function f.

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


### `def par: ParHashSet[T]`                                                 ###

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


### `def partition(pred: (T) ⇒ Boolean): (ParHashSet[T], ParHashSet[T])`     ###

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


### `def reduceLeftOption[U >: T](op: (U, T) ⇒ U): Option[U]`                ###

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


### `def reduceLeft[U >: T](op: (U, T) ⇒ U): U`                              ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def reduceOption[U >: T](op: (U, U) ⇒ U): Option[U]`                    ###

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


### `def reduceRightOption[U >: T](op: (T, U) ⇒ U): Option[U]`               ###

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


### `def reduceRight[U >: T](op: (T, U) ⇒ U): U`                             ###

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


### `def reduce[U >: T](op: (U, U) ⇒ U): U`                                  ###

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


### `def repr: ParHashSet[T]`                                                ###

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


### `def sameElements[U >: T](that: GenIterable[U]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this parallel hash set.

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


### `def scan[U >: T, That](z: U)(op: (U, U) ⇒ U)(implicit bf: CanBuildFrom[ParHashSet[T], U, That]): That` ###

[use case]

Computes a prefix scan of the elements of the collection.

Note: The neutral element `z` may be applied more than once.

* z
  * neutral element for the operator `op`
* op
  * the associative operator for the scan
* returns
  * a new parallel hash set containing the prefix scan of the elements in this
    parallel hash set

* Definition Classes
  * ParIterableLike → GenTraversableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def scanLeft[S, That](z: S)(op: (S, T) ⇒ S)(implicit bf: CanBuildFrom[ParHashSet[T], S, That]): That` ###

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


### `def scanRight[S, That](z: S)(op: (T, S) ⇒ S)(implicit bf: CanBuildFrom[ParHashSet[T], S, That]): That` ###

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


### `def sequentially[S, That <: Parallel](b: (HashSet[T]) ⇒ Parallelizable[S, That]): ParHashSet[T]` ###

* Attributes
  * protected[this]
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def slice(unc_from: Int, unc_until: Int): ParHashSet[T]`                ###

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


### `def span(pred: (T) ⇒ Boolean): (ParHashSet[T], ParHashSet[T])`          ###

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


### `def splitAt(n: Int): (ParHashSet[T], ParHashSet[T])`                    ###

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


### `def tail: ParHashSet[T]`                                                ###

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


### `def take(n: Int): ParHashSet[T]`                                        ###

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


### `def takeWhile(pred: (T) ⇒ Boolean): ParHashSet[T]`                      ###

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


### `def toBuffer[U >: T]: Buffer[U]`                                        ###

Uses the contents of this parallel iterable to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIndexedSeq: immutable.IndexedSeq[T]`                              ###

Converts this parallel iterable to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toIterator: scala.Iterator[T]`                                      ###

Returns an Iterator over the elements in this parallel iterable. Will return the
same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toMap[K, V](implicit ev: <:<[T, (K, V)]): immutable.ParMap[K, V]`   ###

[use case]

Converts this parallel hash set to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this parallel hash set.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toParCollection[U >: T, That](cbf: () ⇒ Combiner[U, That]): That`   ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toParMap[K, V, That](cbf: () ⇒ Combiner[(K, V), That])(implicit ev: <:<[T, (K, V)]): That` ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def toSet[U >: T]: immutable.ParSet[U]`                                 ###

Converts this parallel iterable to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def toTraversable: GenTraversable[T]`                                   ###

Converts this parallel iterable to an unspecified Traversable. Will return the
same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this parallel iterable.

* Definition Classes
  * ParIterableLike → GenTraversableOnce

(defined at scala.collection.parallel.ParIterableLike)


### `def withFilter(pred: (T) ⇒ Boolean): ParHashSet[T]`                     ###

* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def wrap[R](body: ⇒ R): NonDivisible[R]`                                ###

* Attributes
  * protected
* Definition Classes
  * ParIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipAll[S, U >: T, That](that: GenIterable[S], thisElem: U, thatElem: S)(implicit bf: CanBuildFrom[ParHashSet[T], (U, S), That]): That` ###

[use case]

Returns a parallel hash set formed from this parallel hash set and another
iterable collection by combining corresponding elements in pairs. If one of the
two collections is shorter than the other, placeholder elements are used to
extend the shorter collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this parallel hash set is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    parallel hash set.
* returns
  * a new parallel hash set containing pairs consisting of corresponding
    elements of this parallel hash set and `that` . The length of the returned
    collection is the maximum of the lengths of this parallel hash set and
     `that` . If this parallel hash set is shorter than `that` , `thisElem`
    values are used to pad the result. If `that` is shorter than this parallel
    hash set, `thatElem` values are used to pad the result.

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


### `def zipWithIndex[U >: T, That](implicit bf: CanBuildFrom[ParHashSet[T], (U, Int), That]): That` ###

[use case]

Zips this parallel hash set with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new parallel hash set containing pairs consisting of all elements of this
    parallel hash set paired with their index. Indices start at `0` .

* Definition Classes
  * ParIterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.parallel.ParIterableLike)


### `def zip[U >: T, S, That](that: GenIterable[S])(implicit bf: CanBuildFrom[ParHashSet[T], (U, S), That]): That` ###

[use case]

Returns a parallel hash set formed from this parallel hash set and another
iterable collection by combining corresponding elements in pairs. If one of the
two collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new parallel hash set containing pairs consisting of corresponding
    elements of this parallel hash set and `that` . The length of the returned
    collection is the minimum of the lengths of this parallel hash set and
     `that` .

* Definition Classes
  * ParIterableLike → GenIterableLike

(defined at scala.collection.parallel.ParIterableLike)


--------------------------------------------------------------------------------
            Value Members From scala.collection.parallel.ParSetLike
--------------------------------------------------------------------------------


### `def diff(that: GenSet[T]): ParHashSet[T]`                               ###

Computes the difference of this set and another set.

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * ParSetLike → GenSetLike

(defined at scala.collection.parallel.ParSetLike)


### `def union(that: GenSet[T]): ParHashSet[T]`                              ###

Computes the union between of set and another set.

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * ParSetLike → GenSetLike

(defined at scala.collection.parallel.ParSetLike)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.mutable.ParHashSet
--------------------------------------------------------------------------------


### `new ParHashSet()`                                                       ###

(defined at scala.collection.parallel.mutable.ParHashSet)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParHashSet
--------------------------------------------------------------------------------


### `def +=(elem: T): ParHashSet.this.type`                                  ###

adds a single element to this parallel hash set.

* elem
  * the element to add.
* returns
  * the parallel hash set itself

* Definition Classes
  * ParHashSet → ParSetLike → Growable

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def -=(elem: T): ParHashSet.this.type`                                  ###

Removes a single element from this parallel hash set.

* elem
  * the element to remove.
* returns
  * the parallel hash set itself

* Definition Classes
  * ParHashSet → ParSetLike → Shrinkable

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def companion: ParHashSet.type`                                         ###

The factory companion object that builds instances of class `ParHashSet` . (or
its `Iterable` superclass where class `ParHashSet` is not a `Seq` .)

* Definition Classes
  * ParHashSet → ParSet → ParSet → ParIterable → ParIterable →
    GenericParTemplate → GenSet → GenIterable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def contains(elem: T): Boolean`                                         ###

* Definition Classes
  * ParHashSet → GenSetLike

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def empty: ParHashSet[T]`                                               ###

* Definition Classes
  * ParHashSet → ParSet → ParSetLike → ParSet → ParSetLike → GenericSetTemplate

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def iterator: ParHashSetIterator`                                       ###

Creates a new split iterator used to traverse the elements of this collection.

By default, this method is implemented in terms of the protected `splitter`
method.

* returns
  * a split iterator

* Definition Classes
  * ParHashSet → FlatHashTable → ParIterableLike → GenSetLike → GenIterableLike

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def seq: HashSet[T]`                                                    ###

* Definition Classes
  * ParHashSet → ParSet → ParIterable → ParIterableLike → GenSet → GenIterable →
    GenTraversable → GenSetLike → Parallelizable → GenTraversableOnce

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def splitter: ParHashSetIterator`                                       ###

Creates a new parallel iterator used to traverse the elements of this parallel
collection. This iterator is more specific than the iterator of the returned by
 `iterator` , and augmented with additional accessor and transformer methods.

* returns
  * a parallel iterator

* Definition Classes
  * ParHashSet → ParIterableLike

(defined at scala.collection.parallel.mutable.ParHashSet)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParIterable
--------------------------------------------------------------------------------


### `def toIterable: ParIterable[T]`                                         ###

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


### `def toSeq: ParSeq[T]`                                                   ###

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
        Value Members From scala.collection.parallel.mutable.ParSetLike
--------------------------------------------------------------------------------


### `def +(elem: T): ParHashSet[T]`                                          ###

* Definition Classes
  * ParSetLike → GenSetLike

(defined at scala.collection.parallel.mutable.ParSetLike)


### `def -(elem: T): ParHashSet[T]`                                          ###

* Definition Classes
  * ParSetLike → GenSetLike

(defined at scala.collection.parallel.mutable.ParSetLike)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParHashSet [T] to
    CollectionsHaveToParArray [ParHashSet [T], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParHashSet [T]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
