
#                  scala.collection.generic.GenericCompanion                  #

```scala
abstract class GenericCompanion[+CC[X] <: GenTraversable[X]] extends AnyRef
```

A template class for companion objects of "regular" collection classes represent
an unconstrained higher-kinded type. Typically such classes inherit from trait
 `GenericTraversableTemplate` .

* CC
  * The type constructor representing the collection class.

* Source
  * [GenericCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericCompanion.scala#L1)
* Since
  * 2.8
* See also
  * scala.collection.generic.GenericTraversableTemplate


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A]: Builder[A, CC[A]]`                          ###

The default builder for `CC` objects.

* A
  * the type of the collection's elements

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

(defined at scala.collection.generic.GenericCompanion)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `new GenericCompanion()`                                                 ###
(defined at scala.collection.generic.GenericCompanion)
