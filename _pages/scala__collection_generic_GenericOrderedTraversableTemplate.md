
#          scala.collection.generic.GenericOrderedTraversableTemplate          #

```scala
trait GenericOrderedTraversableTemplate[+A, +CC[X] <: Traversable[X]] extends HasNewBuilder[A, CC[A]]
```

This trait represents collections classes which require ordered element types.

* Source
  * [GenericOrderedTraversableTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericOrderedTraversableTemplate.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.generic.GenericOrderedTraversableTemplate
--------------------------------------------------------------------------------


### `abstract def orderedCompanion: GenericOrderedCompanion[CC]`             ###

(defined at scala.collection.generic.GenericOrderedTraversableTemplate)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericOrderedTraversableTemplate
--------------------------------------------------------------------------------


### `implicit abstract val ord: Ordering[A]`                                 ###

* Attributes
  * protected[this]

(defined at scala.collection.generic.GenericOrderedTraversableTemplate)


### `def genericOrderedBuilder[B](implicit ord: Ordering[B]): Builder[B, CC[B]]` ###

(defined at scala.collection.generic.GenericOrderedTraversableTemplate)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.HasNewBuilder
--------------------------------------------------------------------------------


### `abstract def newBuilder: Builder[A, CC[A] @scala.annotation.unchecked.uncheckedVariance]` ###

The builder that builds instances of Repr

* Attributes
  * protected[this]
* Definition Classes
  * HasNewBuilder

(defined at scala.collection.generic.HasNewBuilder)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    GenericOrderedTraversableTemplate [A, CC] to CollectionsHaveToParArray [
    GenericOrderedTraversableTemplate [A, CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (
    GenericOrderedTraversableTemplate [A, CC]) ⇒ GenTraversableOnce [T] is in
    scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
