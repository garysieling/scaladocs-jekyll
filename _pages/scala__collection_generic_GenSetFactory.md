
#                    scala.collection.generic.GenSetFactory                    #

```scala
abstract class GenSetFactory[CC[X] <: GenSet[X] with GenSetLike[X, CC[X]]] extends GenericCompanion[CC]
```

A template for companion objects of `Set` and subclasses thereof.

* Source
  * [GenSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenSetFactory.scala#L1)


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
       Abstract Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `abstract def newBuilder[A]: Builder[A, CC[A]]`                          ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * GenSetFactory → GenericCompanion

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[CC[_], A, CC[A]]`                  ###

The standard `CanBuildFrom` instance for `Set` objects.

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
       Instance Constructors From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `new GenSetFactory()`                                                    ###

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.generic.GenericCompanion
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
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenSetFactory [CC] to
    CollectionsHaveToParArray [GenSetFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (GenSetFactory [CC]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
