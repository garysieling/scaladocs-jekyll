
#               scala.collection.generic.MutableSortedMapFactory               #

```scala
abstract class MutableSortedMapFactory[CC[A, B] <: mutable.SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends SortedMapFactory[CC]
```

A template for companion objects of `SortedMap` and subclasses thereof.

* CC
  * the type of the collection.

* Source
  * [MutableSortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableSortedMapFactory.scala#L1)
* Version
  * 2.12
* Since
  * 2.12


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_, _]`                                                   ###

* Definition Classes
  * SortedMapFactory


### `class SortedMapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

* Definition Classes
  * SortedMapFactory


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.generic.MutableSortedMapFactory
--------------------------------------------------------------------------------


### `new MutableSortedMapFactory()`                                          ###

(defined at scala.collection.generic.MutableSortedMapFactory)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `abstract def empty[A, B](implicit ord: Ordering[A]): CC[A, B]`          ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*)(implicit ord: Ordering[A]): CC[A, B]`   ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


### `def newBuilder[A, B](implicit ord: Ordering[A]): Builder[(A, B), CC[A, B]]` ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from MutableSortedMapFactory
    [CC] to CollectionsHaveToParArray [MutableSortedMapFactory [CC], T]
    performed by method CollectionsHaveToParArray in scala.collection.parallel.
    This conversion will take place only if an implicit value of type (
    MutableSortedMapFactory [CC]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
