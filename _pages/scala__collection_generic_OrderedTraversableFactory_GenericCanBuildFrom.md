
#    scala.collection.generic.OrderedTraversableFactory#GenericCanBuildFrom    #

```scala
class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]
```

* Source
  * [OrderedTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/OrderedTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.OrderedTraversableFactory.GenericCanBuildFrom
--------------------------------------------------------------------------------


### `new GenericCanBuildFrom()(implicit ord: Ordering[A])`                   ###

(defined at scala.collection.generic.OrderedTraversableFactory.GenericCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From scala.collection.generic.OrderedTraversableFactory.GenericCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[A, CC[A]]`                                         ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.OrderedTraversableFactory.GenericCanBuildFrom)


### `def apply(from: CC[_]): Builder[A, CC[A]]`                              ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * GenericCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.OrderedTraversableFactory.GenericCanBuildFrom)


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
