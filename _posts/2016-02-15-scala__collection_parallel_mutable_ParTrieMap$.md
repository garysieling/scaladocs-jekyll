
#                 scala.collection.parallel.mutable.ParTrieMap                 #

```scala
object ParTrieMap extends ParMapFactory[ParTrieMap] with Serializable
```

* Source
  * [ParTrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParTrieMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class CanCombineFromMap[K, V] extends CanCombineFrom[CC[_, _], (K, V), CC[K, V]]` ###

* Definition Classes
  * ParMapFactory


### `type Coll = ParTrieMap[_, _]`                                           ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `type MapColl = ParTrieMap[_, _]`                                        ###

* Definition Classes
  * ParMapFactory


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): ParTrieMap[A, B]`                      ###

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


### `def newBuilder[K, V]: Builder[(K, V), ParTrieMap[K, V]]`                ###

The default builder for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMapFactory → GenMapFactory

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParTrieMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[K, V]: CanCombineFrom[Coll, (K, V), ParTrieMap[K, V]]` ###

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def empty[K, V]: ParTrieMap[K, V]`                                      ###

An empty `ParMap`

* Definition Classes
  * ParTrieMap → GenMapFactory

(defined at scala.collection.parallel.mutable.ParTrieMap)


### `def newCombiner[K, V]: Combiner[(K, V), ParTrieMap[K, V]]`              ###

The default combiner for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParTrieMap → ParMapFactory → GenericParMapCompanion
(defined at scala.collection.parallel.mutable.ParTrieMap)
