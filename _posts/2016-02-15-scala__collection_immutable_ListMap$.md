
#                      scala.collection.immutable.ListMap                      #

```scala
object ListMap extends ImmutableMapFactory[ListMap] with Serializable
```

This object provides a set of operations needed to create `immutable.ListMap`
values.

* Source
  * [ListMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListMap.scala#L1)
* Since
  * 1
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-immutable-collection-classes.html#list_maps)
    section on `List Maps` for more information.


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


### `def newBuilder[A, B]: Builder[(A, B), ListMap[A, B]]`                   ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.ListMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), ListMap[A, B]]` ###

The standard `CanBuildFrom` instance for `immutable.ListMap` objects. The
created value is an instance of class `MapCanBuildFrom` .

(defined at scala.collection.immutable.ListMap)


### `def empty[A, B]: ListMap[A, B]`                                         ###

An empty immutable.ListMap

* Definition Classes
  * ListMap → MapFactory → GenMapFactory
(defined at scala.collection.immutable.ListMap)
