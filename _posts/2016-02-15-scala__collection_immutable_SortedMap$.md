
#                     scala.collection.immutable.SortedMap                     #

```scala
object SortedMap extends ImmutableSortedMapFactory[SortedMap]
```

This object provides a set of operations needed to create sorted maps of type
 `immutable.SortedMap` .

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/SortedMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = SortedMap[_, _]`                                            ###

* Definition Classes
  * SortedMapFactory


### `class SortedMapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

* Definition Classes
  * SortedMapFactory


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*)(implicit ord: Ordering[A]): SortedMap[A, B]` ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


### `def newBuilder[A, B](implicit ord: Ordering[A]): Builder[(A, B), SortedMap[A, B]]` ###

* Definition Classes
  * SortedMapFactory

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
            Value Members From scala.collection.immutable.SortedMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B](implicit ord: Ordering[A]): CanBuildFrom[Coll, (A, B), SortedMap[A, B]]` ###

The standard `CanBuildFrom` instance for sorted maps

(defined at scala.collection.immutable.SortedMap)


### `def empty[A, B](implicit ord: Ordering[A]): SortedMap[A, B]`            ###

* Definition Classes
  * SortedMap → SortedMapFactory
(defined at scala.collection.immutable.SortedMap)
