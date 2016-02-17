
#                           scala.collection.GenMap                           #

```scala
object GenMap extends GenMapFactory[GenMap]
```

* Source
  * [GenMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = GenMap[_, _]`                                               ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


--------------------------------------------------------------------------------
                   Value Members From scala.collection.GenMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), GenMap[A, B]]` ###

The standard `CanBuildFrom` instance for `Map` objects. The created value is an
instance of class `MapCanBuildFrom` .

(defined at scala.collection.GenMap)


### `def empty[A, B]: immutable.Map[A, B]`                                   ###

An empty `Map`

* Definition Classes
  * GenMap → GenMapFactory

(defined at scala.collection.GenMap)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): GenMap[A, B]`                          ###

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


### `def newBuilder[A, B]: Builder[(A, B), GenMap[A, B]]`                    ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * GenMapFactory
(defined at scala.collection.generic.GenMapFactory)
