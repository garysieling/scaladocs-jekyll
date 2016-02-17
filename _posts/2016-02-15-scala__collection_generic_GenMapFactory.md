
#                    scala.collection.generic.GenMapFactory                    #

```scala
abstract class GenMapFactory[CC[A, B] <: GenMap[A, B] with GenMapLike[A, B, CC[A, B]]] extends AnyRef
```

A template for companion objects of `Map` and subclasses thereof.

* Source
  * [GenMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenMapFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_, _]`                                                   ###

The type constructor of the collection that can be built by this factory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Source
  * [GenMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenMapFactory.scala#L1)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `abstract def empty[A, B]: CC[A, B]`                                     ###

An empty `Map`

(defined at scala.collection.generic.GenMapFactory)


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

(defined at scala.collection.generic.GenMapFactory)


### `def newBuilder[A, B]: Builder[(A, B), CC[A, B]]`                        ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
       Instance Constructors From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `new GenMapFactory()`                                                    ###
(defined at scala.collection.generic.GenMapFactory)
