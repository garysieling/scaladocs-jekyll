
#               scala.collection.generic.MutableSortedSetFactory               #

```scala
abstract class MutableSortedSetFactory[CC[A] <: mutable.SortedSet[A] with SortedSetLike[A, CC[A]] with mutable.Set[A] with mutable.SetLike[A, CC[A]]] extends SortedSetFactory[CC]
```

* Source
  * [MutableSortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableSortedSetFactory.scala#L1)


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
  Concrete Value Members From scala.collection.generic.MutableSortedSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, CC[A]]`        ###

mutable.SetBuilder uses '+' which is not a primitive for anything extending
mutable.SetLike, this causes serious performance issues since each time 'elems =
elems + x' is evaluated elems is cloned (which is O(n)).

Fortunately GrowingBuilder comes to rescue.

* Definition Classes
  * MutableSortedSetFactory → SortedSetFactory

(defined at scala.collection.generic.MutableSortedSetFactory)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.generic.MutableSortedSetFactory
--------------------------------------------------------------------------------


### `new MutableSortedSetFactory()`                                          ###

(defined at scala.collection.generic.MutableSortedSetFactory)


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


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, CC[A]]` ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from MutableSortedSetFactory
    [CC] to CollectionsHaveToParArray [MutableSortedSetFactory [CC], T]
    performed by method CollectionsHaveToParArray in scala.collection.parallel.
    This conversion will take place only if an implicit value of type (
    MutableSortedSetFactory [CC]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
