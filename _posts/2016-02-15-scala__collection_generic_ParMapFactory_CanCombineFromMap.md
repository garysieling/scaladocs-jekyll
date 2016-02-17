
#           scala.collection.generic.ParMapFactory#CanCombineFromMap           #

```scala
class CanCombineFromMap[K, V] extends CanCombineFrom[CC[_, _], (K, V), CC[K, V]]
```

* Source
  * [ParMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParMapFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.ParMapFactory.CanCombineFromMap
--------------------------------------------------------------------------------


### `new CanCombineFromMap()`                                                ###

(defined at scala.collection.generic.ParMapFactory.CanCombineFromMap)


--------------------------------------------------------------------------------
  Value Members From scala.collection.generic.ParMapFactory.CanCombineFromMap
--------------------------------------------------------------------------------


### `def apply(): Combiner[(K, V), CC[K, V]]`                                ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * CanCombineFromMap → CanCombineFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.ParMapFactory.CanCombineFromMap)


### `def apply(from: MapColl): Combiner[(K, V), CC[K, V]]`                   ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * CanCombineFromMap → CanCombineFrom → CanBuildFrom

(defined at scala.collection.generic.ParMapFactory.CanCombineFromMap)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CanCombineFromMap [K, V]
    to CollectionsHaveToParArray [CanCombineFromMap [K, V], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    CanCombineFromMap [K, V]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
