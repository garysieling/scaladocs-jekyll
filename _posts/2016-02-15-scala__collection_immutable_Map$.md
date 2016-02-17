
#                        scala.collection.immutable.Map                        #

```scala
object Map extends ImmutableMapFactory[Map]
```

This object provides a set of operations needed to create `immutable.Map`
values.

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Map[_, _]`                                                  ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class Map1[A, +B] extends AbstractMap[A, B] with Map[A, B] with Serializable` ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `class Map2[A, +B] extends AbstractMap[A, B] with Map[A, B] with Serializable` ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `class Map3[A, +B] extends AbstractMap[A, B] with Map[A, B] with Serializable` ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `class Map4[A, +B] extends AbstractMap[A, B] with Map[A, B] with Serializable` ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `class WithDefault[A, +B] extends Map.WithDefault[A, B] with Map[A, B]`  ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Map.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): Map[A, B]`                             ###

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


### `def newBuilder[A, B]: Builder[(A, B), Map[A, B]]`                       ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
               Value Members From scala.collection.immutable.Map
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), Map[A, B]]` ###

The standard `CanBuildFrom` instance for `immutable.Map` objects. The created
value is an instance of class `MapCanBuildFrom` .

(defined at scala.collection.immutable.Map)


### `def empty[A, B]: Map[A, B]`                                             ###

An empty `immutable.Map`

* Definition Classes
  * Map → MapFactory → GenMapFactory
(defined at scala.collection.immutable.Map)
