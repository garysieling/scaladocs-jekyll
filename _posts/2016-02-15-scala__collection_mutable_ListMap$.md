
#                       scala.collection.mutable.ListMap                       #

```scala
object ListMap extends MutableMapFactory[ListMap] with Serializable
```

This object provides a set of operations needed to create `mutable.ListMap`
values.

* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ListMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = ListMap[_, _]`                                              ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): ListMap[A, B]`                         ###

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


### `def newBuilder[A, B]: Builder[(A, B), ListMap[A, B]]`                   ###

The default builder for Map objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * MutableMapFactory → GenMapFactory

(defined at scala.collection.generic.MutableMapFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.ListMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), ListMap[A, B]]` ###

(defined at scala.collection.mutable.ListMap)


### `def empty[A, B]: ListMap[A, B]`                                         ###

An empty `mutable.ListMap`

* Definition Classes
  * ListMap → MapFactory → GenMapFactory
(defined at scala.collection.mutable.ListMap)
