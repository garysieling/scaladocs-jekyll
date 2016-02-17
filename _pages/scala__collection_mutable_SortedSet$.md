
#                      scala.collection.mutable.SortedSet                      #

```scala
object SortedSet extends MutableSortedSetFactory[SortedSet]
```

A template for mutable sorted set companion objects.

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SortedSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = SortedSet[_]`                                               ###

* Definition Classes
  * SortedSetFactory


### `class SortedSetCanBuildFrom[A] extends CanBuildFrom[Coll, A, CC[A]]`    ###

* Definition Classes
  * SortedSetFactory


--------------------------------------------------------------------------------
      Value Members From scala.collection.generic.MutableSortedSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, SortedSet[A]]` ###

mutable.SetBuilder uses '+' which is not a primitive for anything extending
mutable.SetLike, this causes serious performance issues since each time 'elems =
elems + x' is evaluated elems is cloned (which is O(n)).

Fortunately GrowingBuilder comes to rescue.

* Definition Classes
  * MutableSortedSetFactory → SortedSetFactory

(defined at scala.collection.generic.MutableSortedSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): SortedSet[A]`       ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.SortedSet
--------------------------------------------------------------------------------


### `def canBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

(defined at scala.collection.mutable.SortedSet)


### `def empty[A](implicit ord: Ordering[A]): SortedSet[A]`                  ###

* Definition Classes
  * SortedSet → SortedSetFactory

(defined at scala.collection.mutable.SortedSet)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

* Definition Classes
  * SortedSet → SortedSetFactory
(defined at scala.collection.mutable.SortedSet)
