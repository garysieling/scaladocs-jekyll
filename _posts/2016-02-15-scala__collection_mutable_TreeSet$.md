
#                       scala.collection.mutable.TreeSet                       #

```scala
object TreeSet extends MutableSortedSetFactory[TreeSet] with Serializable
```

* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TreeSet[_]`                                                 ###

* Definition Classes
  * SortedSetFactory


### `class SortedSetCanBuildFrom[A] extends CanBuildFrom[Coll, A, CC[A]]`    ###

* Definition Classes
  * SortedSetFactory


--------------------------------------------------------------------------------
      Value Members From scala.collection.generic.MutableSortedSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, TreeSet[A]]`   ###

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


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): TreeSet[A]`         ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, TreeSet[A]]` ###

* Definition Classes
  * SortedSetFactory

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.TreeSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, TreeSet[A]]` ###

$sortedMapCanBuildFromInfo

(defined at scala.collection.mutable.TreeSet)


### `def empty[A](implicit ordering: Ordering[A]): TreeSet[A]`               ###

The empty set of this type

* Definition Classes
  * TreeSet → SortedSetFactory
(defined at scala.collection.mutable.TreeSet)
