
#              scala.collection.generic.GenericClassTagCompanion              #

```scala
abstract class GenericClassTagCompanion[+CC[X] <: Traversable[X]] extends AnyRef
```

This class represents companions of classes which require ClassTags for their
element types.

* Source
  * [GenericClassTagCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericClassTagCompanion.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

* Attributes
  * protected[this]


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A](implicit ord: ClassTag[A]): Builder[A, CC[A]]` ###

(defined at scala.collection.generic.GenericClassTagCompanion)


--------------------------------------------------------------------------------
 Concrete Value Members From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: ClassTag[A]): CC[A]`              ###

(defined at scala.collection.generic.GenericClassTagCompanion)


### `def empty[A](implicit arg0: ClassTag[A]): CC[A]`                        ###

(defined at scala.collection.generic.GenericClassTagCompanion)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.generic.GenericClassTagCompanion
--------------------------------------------------------------------------------


### `new GenericClassTagCompanion()`                                         ###
(defined at scala.collection.generic.GenericClassTagCompanion)
