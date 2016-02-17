
#                    scala.collection.mutable.LinkedHashMap                    #

```scala
object LinkedHashMap extends MutableMapFactory[LinkedHashMap] with Serializable
```

This object provides a set of operations needed to create `LinkedHashMap`
values.

* Source
  * [LinkedHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = LinkedHashMap[_, _]`                                        ###

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


### `def apply[A, B](elems: (A, B)*): LinkedHashMap[A, B]`                   ###

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


### `def newBuilder[A, B]: Builder[(A, B), LinkedHashMap[A, B]]`             ###

The default builder for Map objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * MutableMapFactory → GenMapFactory

(defined at scala.collection.generic.MutableMapFactory)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.LinkedHashMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), LinkedHashMap[A, B]]` ###

(defined at scala.collection.mutable.LinkedHashMap)


### `def empty[A, B]: LinkedHashMap[A, B]`                                   ###

An empty `LinkedHashMap`

* Definition Classes
  * LinkedHashMap → MapFactory → GenMapFactory
(defined at scala.collection.mutable.LinkedHashMap)
