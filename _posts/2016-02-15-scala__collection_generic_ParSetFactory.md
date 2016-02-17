
#                    scala.collection.generic.ParSetFactory                    #

```scala
abstract class ParSetFactory[CC[X] <: ParSet[X] with ParSetLike[X, CC[X], _] with GenericParTemplate[X, CC]] extends GenSetFactory[CC] with GenericParCompanion[CC]
```

* Source
  * [ParSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParSetFactory.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class GenericCanCombineFrom[A] extends CanCombineFrom[CC[_], A, CC[A]]` ###

* Source
  * [ParSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParSetFactory.scala#L1)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[CC[_], A, CC[A]]`                  ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

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
       Abstract Value Members From scala.collection.generic.ParSetFactory
--------------------------------------------------------------------------------


### `abstract def newCombiner[A]: Combiner[A, CC[A]]`                        ###

The parallel builder for `ParIterable` objects.

* Definition Classes
  * ParSetFactory → GenericParCompanion

(defined at scala.collection.generic.ParSetFactory)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.ParSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A]: Combiner[A, CC[A]]`                                  ###

The default builder for `ParIterable` objects.

* Definition Classes
  * ParSetFactory → GenericParCompanion → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.ParSetFactory)


--------------------------------------------------------------------------------
       Instance Constructors From scala.collection.generic.ParSetFactory
--------------------------------------------------------------------------------


### `new ParSetFactory()`                                                    ###

(defined at scala.collection.generic.ParSetFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParSetFactory [CC] to
    CollectionsHaveToParArray [ParSetFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParSetFactory [CC]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
