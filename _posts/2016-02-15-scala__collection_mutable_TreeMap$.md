
#                       scala.collection.mutable.TreeMap                       #

```scala
object TreeMap extends MutableSortedMapFactory[TreeMap] with Serializable
```

This object provides a set of operations needed to create sorted maps of type
 `mutable.TreeMap` .

* Source
  * [TreeMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/TreeMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TreeMap[_, _]`                                              ###

* Definition Classes
  * SortedMapFactory


### `class SortedMapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

* Definition Classes
  * SortedMapFactory


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*)(implicit ord: Ordering[A]): TreeMap[A, B]` ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


### `def newBuilder[A, B](implicit ord: Ordering[A]): Builder[(A, B), TreeMap[A, B]]` ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.TreeMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B](implicit ord: Ordering[A]): CanBuildFrom[Coll, (A, B), TreeMap[A, B]]` ###

The standard `CanBuildFrom` instance for sorted maps

(defined at scala.collection.mutable.TreeMap)


### `def empty[A, B](implicit ord: Ordering[A]): TreeMap[A, B]`              ###

* Definition Classes
  * TreeMap → SortedMapFactory
(defined at scala.collection.mutable.TreeMap)
