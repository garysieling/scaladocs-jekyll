
#               scala.collection.generic.GenericOrderedCompanion               #

```scala
abstract class GenericOrderedCompanion[+CC[X] <: Traversable[X]] extends AnyRef
```

This class represents companions of classes which require the ordered trait for
their element types.

* Source
  * [GenericOrderedCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericOrderedCompanion.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

* Attributes
  * protected[this]


--------------------------------------------------------------------------------
  Abstract Value Members From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A](implicit ord: Ordering[A]): Builder[A, CC[A]]` ###

(defined at scala.collection.generic.GenericOrderedCompanion)


--------------------------------------------------------------------------------
  Concrete Value Members From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): CC[A]`              ###

(defined at scala.collection.generic.GenericOrderedCompanion)


### `def empty[A](implicit arg0: Ordering[A]): CC[A]`                        ###

(defined at scala.collection.generic.GenericOrderedCompanion)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `new GenericOrderedCompanion()`                                          ###
(defined at scala.collection.generic.GenericOrderedCompanion)
