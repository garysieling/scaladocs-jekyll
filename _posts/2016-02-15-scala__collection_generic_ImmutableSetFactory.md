
#                 scala.collection.generic.ImmutableSetFactory                 #

```scala
abstract class ImmutableSetFactory[CC[X] <: immutable.Set[X] with SetLike[X, CC[X]]] extends SetFactory[CC]
```

* Source
  * [ImmutableSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSetFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[CC[_], A, CC[A]]`                  ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): CC[A]`                                         ###

Creates a collection with the specified elements.

* A
  * the type of the collection's elements
* elems
  * the elements of the created collection
* returns
  * a new collection with elements `elems`

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.generic.ImmutableSetFactory
--------------------------------------------------------------------------------


### `new ImmutableSetFactory()`                                              ###

(defined at scala.collection.generic.ImmutableSetFactory)


--------------------------------------------------------------------------------
        Value Members From scala.collection.generic.ImmutableSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A]: Builder[A, CC[A]]`                                   ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ImmutableSetFactory [CC]
    to CollectionsHaveToParArray [ImmutableSetFactory [CC], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    ImmutableSetFactory [CC]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
