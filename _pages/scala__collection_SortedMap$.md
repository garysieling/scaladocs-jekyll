
#                          scala.collection.SortedMap                          #

```scala
object SortedMap extends SortedMapFactory[SortedMap]
```

* Source
  * [SortedMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SortedMap.scala#L1)
* Since
  * 2.8


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
                 Value Members From scala.collection.SortedMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B](implicit ord: Ordering[A]): CanBuildFrom[Coll, (A, B), SortedMap[A, B]]` ###

(defined at scala.collection.SortedMap)


### `def empty[A, B](implicit ord: Ordering[A]): SortedMap[A, B]`            ###

* Definition Classes
  * SortedMap → SortedMapFactory

(defined at scala.collection.SortedMap)


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
