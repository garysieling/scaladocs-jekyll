
#                     scala.collection.generic.MapFactory                     #

```scala
abstract class MapFactory[CC[A, B] <: Map[A, B] with MapLike[A, B, CC[A, B]]] extends GenMapFactory[CC]
```

A template for companion objects of `Map` and subclasses thereof.

* Source
  * [MapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MapFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_, _]`                                                   ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): CC[A, B]`                              ###

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


### `def newBuilder[A, B]: Builder[(A, B), CC[A, B]]`                        ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.generic.MapFactory
--------------------------------------------------------------------------------


### `abstract def empty[A, B]: CC[A, B]`                                     ###

An empty Map

* Definition Classes
  * MapFactory → GenMapFactory

(defined at scala.collection.generic.MapFactory)


--------------------------------------------------------------------------------
         Instance Constructors From scala.collection.generic.MapFactory
--------------------------------------------------------------------------------


### `new MapFactory()`                                                       ###

(defined at scala.collection.generic.MapFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from MapFactory [CC] to
    CollectionsHaveToParArray [MapFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (MapFactory [CC]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
