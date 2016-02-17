
#                     scala.collection.immutable.SortedSet                     #

```scala
object SortedSet extends ImmutableSortedSetFactory[SortedSet]
```

This object provides a set of operations needed to create sorted sets of type
 `immutable.SortedSet` .

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedSet.scala#L1)


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
          Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): SortedSet[A]`       ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, SortedSet[A]]` ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
            Value Members From scala.collection.immutable.SortedSet
--------------------------------------------------------------------------------


### `def canBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

The standard `CanBuildFrom` instance for sorted sets

(defined at scala.collection.immutable.SortedSet)


### `def empty[A](implicit ord: Ordering[A]): SortedSet[A]`                  ###

* Definition Classes
  * SortedSet → SortedSetFactory

(defined at scala.collection.immutable.SortedSet)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

* Definition Classes
  * SortedSet → SortedSetFactory
(defined at scala.collection.immutable.SortedSet)
