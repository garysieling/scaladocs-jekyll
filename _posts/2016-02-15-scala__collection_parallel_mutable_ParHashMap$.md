
#                 scala.collection.parallel.mutable.ParHashMap                 #

```scala
object ParHashMap extends ParMapFactory[ParHashMap] with Serializable
```

This object provides a set of operations needed to create `mutable.ParHashMap`
values.

* Source
  * [ParHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class CanCombineFromMap[K, V] extends CanCombineFrom[CC[_, _], (K, V), CC[K, V]]` ###

* Definition Classes
  * ParMapFactory


### `type Coll = ParHashMap[_, _]`                                           ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `type MapColl = ParHashMap[_, _]`                                        ###

* Definition Classes
  * ParMapFactory


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): ParHashMap[A, B]`                      ###

A collection of type `Map` that contains given key/value bindings.

* A
  * the type of the keys
* B
  * the type of the associated values
* elems
  * the key/value pairs that make up the map
* returns
  * a new map consisting key/value pairs given by `elems` .

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.ParMapFactory
--------------------------------------------------------------------------------


### `def newBuilder[K, V]: Builder[(K, V), ParHashMap[K, V]]`                ###

The default builder for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMapFactory → GenMapFactory

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParHashMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[K, V]: CanCombineFrom[Coll, (K, V), ParHashMap[K, V]]` ###

(defined at scala.collection.parallel.mutable.ParHashMap)


### `def empty[K, V]: ParHashMap[K, V]`                                      ###

An empty `mutable.ParHashMap`

* Definition Classes
  * ParHashMap → GenMapFactory

(defined at scala.collection.parallel.mutable.ParHashMap)


### `def newCombiner[K, V]: Combiner[(K, V), ParHashMap[K, V]]`              ###

The default combiner for `mutable.ParHashMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParHashMap → ParMapFactory → GenericParMapCompanion
(defined at scala.collection.parallel.mutable.ParHashMap)
