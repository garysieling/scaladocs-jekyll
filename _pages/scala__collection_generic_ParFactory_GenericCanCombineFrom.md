
#          scala.collection.generic.ParFactory#GenericCanCombineFrom          #

```scala
class GenericCanCombineFrom[A] extends GenericCanBuildFrom[A] with CanCombineFrom[CC[_], A, CC[A]]
```

A generic implementation of the `CanCombineFrom` trait, which forwards all calls
to `apply(from)` to the `genericParBuilder` method of the parallel collection
 `from` , and calls to `apply()` to this factory.

* Source
  * [ParFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.ParFactory.GenericCanCombineFrom
--------------------------------------------------------------------------------


### `new GenericCanCombineFrom()`                                            ###

(defined at scala.collection.generic.ParFactory.GenericCanCombineFrom)


--------------------------------------------------------------------------------
  Value Members From scala.collection.generic.ParFactory.GenericCanCombineFrom
--------------------------------------------------------------------------------


### `def apply(): Combiner[A, CC[A]]`                                        ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * GenericCanCombineFrom → CanCombineFrom → GenericCanBuildFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.ParFactory.GenericCanCombineFrom)


### `def apply(from: ParFactory.Coll): Combiner[A, CC[A]]`                   ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * GenericCanCombineFrom → CanCombineFrom → GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.ParFactory.GenericCanCombineFrom)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenericCanCombineFrom [A]
    to CollectionsHaveToParArray [GenericCanCombineFrom [A], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    GenericCanCombineFrom [A]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
