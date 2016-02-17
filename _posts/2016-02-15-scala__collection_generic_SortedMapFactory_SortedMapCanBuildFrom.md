
#       scala.collection.generic.SortedMapFactory#SortedMapCanBuildFrom       #

```scala
class SortedMapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]
```

* Source
  * [SortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedMapFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.SortedMapFactory.SortedMapCanBuildFrom
--------------------------------------------------------------------------------


### `new SortedMapCanBuildFrom()(implicit ord: Ordering[A])`                 ###

(defined at scala.collection.generic.SortedMapFactory.SortedMapCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From scala.collection.generic.SortedMapFactory.SortedMapCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[(A, B), CC[A, B]]`                                 ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * SortedMapCanBuildFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.SortedMapFactory.SortedMapCanBuildFrom)


### `def apply(from: Coll): Builder[(A, B), CC[A, B]]`                       ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * SortedMapCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.SortedMapFactory.SortedMapCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SortedMapCanBuildFrom [A,
    B] to CollectionsHaveToParArray [SortedMapCanBuildFrom [A, B], T] performed
    by method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    SortedMapCanBuildFrom [A, B]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
