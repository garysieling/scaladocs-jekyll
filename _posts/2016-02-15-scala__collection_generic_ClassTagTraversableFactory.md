
#             scala.collection.generic.ClassTagTraversableFactory             #

```scala
abstract class ClassTagTraversableFactory[CC[X] <: Traversable[X] with GenericClassTagTraversableTemplate[X, CC]] extends GenericClassTagCompanion[CC]
```

A template for companion objects of `ClassTagTraversable` and subclasses
thereof.

* Source
  * [ClassTagTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ClassTagTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericClassTagCompanion


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

* Source
  * [ClassTagTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ClassTagTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.generic.ClassTagTraversableFactory
--------------------------------------------------------------------------------


### `new ClassTagTraversableFactory()`                                       ###

(defined at scala.collection.generic.ClassTagTraversableFactory)


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A](implicit ord: ClassTag[A]): Builder[A, CC[A]]` ###

* Definition Classes
  * GenericClassTagCompanion

(defined at scala.collection.generic.GenericClassTagCompanion)


--------------------------------------------------------------------------------
 Concrete Value Members From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: ClassTag[A]): CC[A]`              ###

* Definition Classes
  * GenericClassTagCompanion

(defined at scala.collection.generic.GenericClassTagCompanion)


### `def empty[A](implicit arg0: ClassTag[A]): CC[A]`                        ###

* Definition Classes
  * GenericClassTagCompanion

(defined at scala.collection.generic.GenericClassTagCompanion)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    ClassTagTraversableFactory [CC] to CollectionsHaveToParArray [
    ClassTagTraversableFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ClassTagTraversableFactory [CC])
    ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
