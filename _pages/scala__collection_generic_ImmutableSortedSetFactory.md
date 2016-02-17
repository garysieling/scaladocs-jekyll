
#              scala.collection.generic.ImmutableSortedSetFactory              #

```scala
abstract class ImmutableSortedSetFactory[CC[A] <: immutable.SortedSet[A] with SortedSetLike[A, CC[A]]] extends SortedSetFactory[CC]
```

A template for companion objects of `SortedSet` and subclasses thereof.

* Source
  * [ImmutableSortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSortedSetFactory.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

* Definition Classes
  * SortedSetFactory


### `class SortedSetCanBuildFrom[A] extends CanBuildFrom[Coll, A, CC[A]]`    ###

* Definition Classes
  * SortedSetFactory


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.generic.ImmutableSortedSetFactory
--------------------------------------------------------------------------------


### `new ImmutableSortedSetFactory()`                                        ###

(defined at scala.collection.generic.ImmutableSortedSetFactory)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `abstract def empty[A](implicit ord: Ordering[A]): CC[A]`                ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): CC[A]`              ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, CC[A]]`        ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, CC[A]]` ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    ImmutableSortedSetFactory [CC] to CollectionsHaveToParArray [
    ImmutableSortedSetFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ImmutableSortedSetFactory [CC])
    ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
