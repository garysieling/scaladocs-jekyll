
#                   scala.collection.parallel.mutable.ParMap                   #

```scala
object ParMap extends ParMapFactory[ParMap]
```

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class CanCombineFromMap[K, V] extends CanCombineFrom[CC[_, _], (K, V), CC[K, V]]` ###

* Definition Classes
  * ParMapFactory


### `type Coll = ParMap[_, _]`                                               ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `type MapColl = ParMap[_, _]`                                            ###

* Definition Classes
  * ParMapFactory


### `class WithDefault[K, V] extends ParMap.WithDefault[K, V] with ParMap[K, V]` ###

* Source
  * [ParMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParMap.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): ParMap[A, B]`                          ###

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


### `def newBuilder[K, V]: Builder[(K, V), ParMap[K, V]]`                    ###

The default builder for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMapFactory → GenMapFactory

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.parallel.mutable.ParMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[K, V]: CanCombineFrom[Coll, (K, V), ParMap[K, V]]` ###

(defined at scala.collection.parallel.mutable.ParMap)


### `def empty[K, V]: ParMap[K, V]`                                          ###

An empty `ParMap`

* Definition Classes
  * ParMap → GenMapFactory

(defined at scala.collection.parallel.mutable.ParMap)


### `def newCombiner[K, V]: Combiner[(K, V), ParMap[K, V]]`                  ###

The default combiner for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMap → ParMapFactory → GenericParMapCompanion
(defined at scala.collection.parallel.mutable.ParMap)
