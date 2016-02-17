
#      scala.collection.generic.GenTraversableFactory#GenericCanBuildFrom      #

```scala
class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]
```

A generic implementation of the `CanBuildFrom` trait, which forwards all calls
to `apply(from)` to the `genericBuilder` method of collection `from` , and which
forwards all calls of `apply()` to the `newBuilder` method of this factory.

* Source
  * [GenTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom
--------------------------------------------------------------------------------


### `new GenericCanBuildFrom()`                                              ###

(defined at scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[A, CC[A]]`                                         ###

Creates a new builder from scratch

* returns
  * the result of invoking the `newBuilder` method of this factory.

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom)


### `def apply(from: GenTraversableFactory.Coll): Builder[A, CC[A]]`         ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * the result of invoking the `genericBuilder` method on `from` .

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.GenTraversableFactory.GenericCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenericCanBuildFrom [A]
    to CollectionsHaveToParArray [GenericCanBuildFrom [A], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    GenericCanBuildFrom [A]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
