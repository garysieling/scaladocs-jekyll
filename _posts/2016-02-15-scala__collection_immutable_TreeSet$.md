
#                      scala.collection.immutable.TreeSet                      #

```scala
object TreeSet extends ImmutableSortedSetFactory[TreeSet] with Serializable
```

This object provides a set of operations needed to create sorted sets of type
 `immutable.TreeSet` .

* Source
  * [TreeSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/TreeSet.scala#L1)


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
             Value Members From scala.collection.immutable.TreeSet
--------------------------------------------------------------------------------


### `def empty[A](implicit ordering: Ordering[A]): TreeSet[A]`               ###

The empty set of this type

* Definition Classes
  * TreeSet → SortedSetFactory

(defined at scala.collection.immutable.TreeSet)


### `implicit def implicitBuilder[A](implicit ordering: Ordering[A]): Builder[A, TreeSet[A]]` ###

(defined at scala.collection.immutable.TreeSet)


### `def newBuilder[A](implicit ordering: Ordering[A]): Builder[A, TreeSet[A]]` ###

* Definition Classes
  * TreeSet → SortedSetFactory
(defined at scala.collection.immutable.TreeSet)
