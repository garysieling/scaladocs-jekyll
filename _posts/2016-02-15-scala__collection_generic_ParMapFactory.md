
#                    scala.collection.generic.ParMapFactory                    #

```scala
abstract class ParMapFactory[CC[X, Y] <: ParMap[X, Y] with ParMapLike[X, Y, CC[X, Y], _]] extends GenMapFactory[CC] with GenericParMapCompanion[CC]
```

A template class for companion objects of `ParMap` and subclasses thereof. This
class extends `TraversableFactory` and provides a set of operations to create
 `ParMap` objects.

* Source
  * [ParMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParMapFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class CanCombineFromMap[K, V] extends CanCombineFrom[CC[_, _], (K, V), CC[K, V]]` ###

* Source
  * [ParMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParMapFactory.scala#L1)


### `type Coll = CC[_, _]`                                                   ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


### `type MapColl = CC[_, _]`                                                ###


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `abstract def empty[A, B]: CC[A, B]`                                     ###

An empty `Map`

* Definition Classes
  * GenMapFactory

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

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.ParMapFactory
--------------------------------------------------------------------------------


### `abstract def newCombiner[K, V]: Combiner[(K, V), CC[K, V]]`             ###

The default combiner for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMapFactory → GenericParMapCompanion

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.ParMapFactory
--------------------------------------------------------------------------------


### `def newBuilder[K, V]: Builder[(K, V), CC[K, V]]`                        ###

The default builder for `ParMap` objects.

* K
  * the type of the keys
* V
  * the type of the associated values

* Definition Classes
  * ParMapFactory → GenMapFactory

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
       Instance Constructors From scala.collection.generic.ParMapFactory
--------------------------------------------------------------------------------


### `new ParMapFactory()`                                                    ###

(defined at scala.collection.generic.ParMapFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParMapFactory [CC] to
    CollectionsHaveToParArray [ParMapFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParMapFactory [CC]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
