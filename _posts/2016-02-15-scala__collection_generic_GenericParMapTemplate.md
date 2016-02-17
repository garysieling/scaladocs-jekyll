
#                scala.collection.generic.GenericParMapTemplate                #

```scala
trait GenericParMapTemplate[K, +V, +CC[X, Y] <: ParMap[X, Y]] extends GenericParTemplate[(K, V), ParIterable]
```

* Source
  * [GenericParTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParTemplate.scala#L1)


--------------------------------------------------------------------------------
   Abstract Value Members From scala.collection.generic.GenericParMapTemplate
--------------------------------------------------------------------------------


### `abstract def mapCompanion: GenericParMapCompanion[CC]`                  ###

(defined at scala.collection.generic.GenericParMapTemplate)


--------------------------------------------------------------------------------
   Concrete Value Members From scala.collection.generic.GenericParMapTemplate
--------------------------------------------------------------------------------


### `def genericMapCombiner[P, Q]: Combiner[(P, Q), CC[P, Q]]`               ###

(defined at scala.collection.generic.GenericParMapTemplate)


### `def newCombiner: Combiner[(K, V), CC[K, V]]`                            ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericParMapTemplate → GenericParTemplate → HasNewCombiner

(defined at scala.collection.generic.GenericParMapTemplate)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.generic.GenericParTemplate
--------------------------------------------------------------------------------


### `abstract def companion: GenericCompanion[ParIterable] with GenericParCompanion[ParIterable]` ###

The factory companion object that builds instances of class Traversable. (or its
 `Iterable` superclass where class Traversable is not a `Seq` .)

* Definition Classes
  * GenericParTemplate → GenericTraversableTemplate

(defined at scala.collection.generic.GenericParTemplate)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.generic.GenericParTemplate
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
Abstract Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `abstract def head: (K, V)`                                              ###

Selects the first element of this collection.

* returns
  * the first element of this collection.

* Definition Classes
  * GenericTraversableTemplate
* Exceptions thrown
  * NoSuchElementException if the collection is empty.

(defined at scala.collection.generic.GenericTraversableTemplate)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `abstract def isEmpty: Boolean`                                          ###

Tests whether this collection is empty.

* returns
  * `true` if the collection contain no elements, `false` otherwise.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `abstract def foreach[U](f: ((K, V)) ⇒ U): Unit`                         ###

[use case]

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

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
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenericParMapTemplate [K,
    V, CC] to CollectionsHaveToParArray [GenericParMapTemplate [K, V, CC], T]
    performed by method CollectionsHaveToParArray in scala.collection.parallel.
    This conversion will take place only if an implicit value of type (
    GenericParMapTemplate [K, V, CC]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
