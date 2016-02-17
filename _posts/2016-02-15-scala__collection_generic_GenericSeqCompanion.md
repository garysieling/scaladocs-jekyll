
#                 scala.collection.generic.GenericSeqCompanion                 #

```scala
trait GenericSeqCompanion[CC[X] <: Traversable[X]] extends GenericCompanion[CC]
```

* Source
  * [GenericSeqCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericSeqCompanion.scala#L1)


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
     Abstract Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A]: Builder[A, CC[A]]`                          ###

The default builder for `CC` objects.

* A
  * the type of the collection's elements

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


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
  * This member is added by an implicit conversion from GenericSeqCompanion [CC]
    to CollectionsHaveToParArray [GenericSeqCompanion [CC], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    GenericSeqCompanion [CC]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
