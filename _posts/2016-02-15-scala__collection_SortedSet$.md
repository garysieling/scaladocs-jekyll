
#                          scala.collection.SortedSet                          #

```scala
object SortedSet extends SortedSetFactory[SortedSet]
```

* Source
  * [SortedSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedSet.scala#L1)
* Since
  * 2.8


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
                 Value Members From scala.collection.SortedSet
--------------------------------------------------------------------------------


### `def canBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

(defined at scala.collection.SortedSet)


### `def empty[A](implicit ord: Ordering[A]): immutable.SortedSet[A]`        ###

* Definition Classes
  * SortedSet → SortedSetFactory

(defined at scala.collection.SortedSet)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, SortedSet[A]]` ###

* Definition Classes
  * SortedSet → SortedSetFactory

(defined at scala.collection.SortedSet)


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
