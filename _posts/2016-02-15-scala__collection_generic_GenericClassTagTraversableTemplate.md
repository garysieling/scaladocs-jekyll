
#         scala.collection.generic.GenericClassTagTraversableTemplate         #

```scala
trait GenericClassTagTraversableTemplate[+A, +CC[X] <: Traversable[X]] extends HasNewBuilder[A, CC[A]]
```

This trait represents collections classes which require class tags for their
element types.

* Source
  * [GenericClassTagTraversableTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericClassTagTraversableTemplate.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.generic.GenericClassTagTraversableTemplate
--------------------------------------------------------------------------------


### `abstract def classTagCompanion: GenericClassTagCompanion[CC]`           ###

(defined at scala.collection.generic.GenericClassTagTraversableTemplate)


### `implicit abstract val tag: ClassTag[A]`                                 ###

* Attributes
  * protected[this]

(defined at scala.collection.generic.GenericClassTagTraversableTemplate)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericClassTagTraversableTemplate
--------------------------------------------------------------------------------


### `def genericClassTagBuilder[B](implicit tag: ClassTag[B]): Builder[B, CC[B]]` ###

(defined at scala.collection.generic.GenericClassTagTraversableTemplate)


--------------------------------------------------------------------------------
Deprecated Value Members From scala.collection.generic.GenericClassTagTraversableTemplate
--------------------------------------------------------------------------------


### `def classManifestCompanion: GenericClassManifestCompanion[CC]`          ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use classTagCompanion instead

(defined at scala.collection.generic.GenericClassTagTraversableTemplate)


### `def genericClassManifestBuilder[B](implicit manifest: ClassManifest[B]): Builder[B, CC[B]]` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use genericClassTagBuilder instead

(defined at scala.collection.generic.GenericClassTagTraversableTemplate)


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
    GenericClassTagTraversableTemplate [A, CC] to CollectionsHaveToParArray [
    GenericClassTagTraversableTemplate [A, CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (
    GenericClassTagTraversableTemplate [A, CC]) ⇒ GenTraversableOnce [T] is in
    scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
