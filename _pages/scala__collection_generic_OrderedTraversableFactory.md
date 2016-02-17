
#              scala.collection.generic.OrderedTraversableFactory              #

```scala
abstract class OrderedTraversableFactory[CC[X] <: Traversable[X] with GenericOrderedTraversableTemplate[X, CC]] extends GenericOrderedCompanion[CC]
```

* Source
  * [OrderedTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/OrderedTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###

* Attributes
  * protected[this]
* Definition Classes
  * GenericOrderedCompanion


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

* Source
  * [OrderedTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/OrderedTraversableFactory.scala#L1)


--------------------------------------------------------------------------------
  Abstract Value Members From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A](implicit ord: Ordering[A]): Builder[A, CC[A]]` ###

* Definition Classes
  * GenericOrderedCompanion

(defined at scala.collection.generic.GenericOrderedCompanion)


--------------------------------------------------------------------------------
  Concrete Value Members From scala.collection.generic.GenericOrderedCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): CC[A]`              ###

* Definition Classes
  * GenericOrderedCompanion

(defined at scala.collection.generic.GenericOrderedCompanion)


### `def empty[A](implicit arg0: Ordering[A]): CC[A]`                        ###

* Definition Classes
  * GenericOrderedCompanion

(defined at scala.collection.generic.GenericOrderedCompanion)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.generic.OrderedTraversableFactory
--------------------------------------------------------------------------------


### `new OrderedTraversableFactory()`                                        ###

(defined at scala.collection.generic.OrderedTraversableFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    OrderedTraversableFactory [CC] to CollectionsHaveToParArray [
    OrderedTraversableFactory [CC], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (OrderedTraversableFactory [CC])
    ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
