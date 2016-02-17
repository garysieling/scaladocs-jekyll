
#                         scala.collection.mutable.Map                         #

```scala
object Map extends MutableMapFactory[Map]
```

This object provides a set of operations needed to create `mutable.Map` values.
The current default implementation of a `mutable.Map` is a `HashMap` .

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Map.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Map[_, _]`                                                  ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `class WithDefault[A, B] extends Map.WithDefault[A, B] with Map[A, B]`   ###

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Map.scala#L1)


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


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.MutableMapFactory
--------------------------------------------------------------------------------


### `def newBuilder[A, B]: Builder[(A, B), Map[A, B]]`                       ###

The default builder for Map objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * MutableMapFactory → GenMapFactory

(defined at scala.collection.generic.MutableMapFactory)


--------------------------------------------------------------------------------
                Value Members From scala.collection.mutable.Map
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), Map[A, B]]` ###

The standard `CanBuildFrom` instance for `mutable.Map` objects.

(defined at scala.collection.mutable.Map)


### `def empty[A, B]: Map[A, B]`                                             ###

An empty `mutable.Map`

* Definition Classes
  * Map → MapFactory → GenMapFactory
(defined at scala.collection.mutable.Map)
