
#       scala.collection.generic.SortedSetFactory#SortedSetCanBuildFrom       #

```scala
class SortedSetCanBuildFrom[A] extends CanBuildFrom[Coll, A, CC[A]]
```

* Source
  * [SortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedSetFactory.scala#L1)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.generic.SortedSetFactory.SortedSetCanBuildFrom
--------------------------------------------------------------------------------


### `new SortedSetCanBuildFrom()(implicit ord: Ordering[A])`                 ###

(defined at scala.collection.generic.SortedSetFactory.SortedSetCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From scala.collection.generic.SortedSetFactory.SortedSetCanBuildFrom
--------------------------------------------------------------------------------


### `def apply(): Builder[A, CC[A]]`                                         ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * SortedSetCanBuildFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.SortedSetFactory.SortedSetCanBuildFrom)


### `def apply(from: Coll): Builder[A, CC[A]]`                               ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * SortedSetCanBuildFrom → CanBuildFrom

(defined at scala.collection.generic.SortedSetFactory.SortedSetCanBuildFrom)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SortedSetCanBuildFrom [A]
    to CollectionsHaveToParArray [SortedSetCanBuildFrom [A], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    SortedSetCanBuildFrom [A]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
