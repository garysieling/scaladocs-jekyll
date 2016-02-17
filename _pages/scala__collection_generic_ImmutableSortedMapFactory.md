
#              scala.collection.generic.ImmutableSortedMapFactory              #

```scala
abstract class ImmutableSortedMapFactory[CC[A, B] <: immutable.SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends SortedMapFactory[CC]
```

A template for companion objects of `SortedMap` and subclasses thereof.

* Source
  * [ImmutableSortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSortedMapFactory.scala#L1)
* Since
  * 2.8


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
 Instance Constructors From scala.collection.generic.ImmutableSortedMapFactory
--------------------------------------------------------------------------------


### `new ImmutableSortedMapFactory()`                                        ###

(defined at scala.collection.generic.ImmutableSortedMapFactory)


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
  * This member is added by an implicit conversion from
    ImmutableSortedMapFactory [CC] to CollectionsHaveToParArray [
    ImmutableSortedMapFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ImmutableSortedMapFactory [CC])
    ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
