
#                  scala.collection.generic.SortedSetFactory                  #

```scala
abstract class SortedSetFactory[CC[A] <: SortedSet[A] with SortedSetLike[A, CC[A]]] extends AnyRef
```

A template for companion objects of Set and subclasses thereof.

* Source
  * [SortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedSetFactory.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_]`                                                      ###


### `class SortedSetCanBuildFrom[A] extends CanBuildFrom[Coll, A, CC[A]]`    ###

* Source
  * [SortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedSetFactory.scala#L1)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `abstract def empty[A](implicit ord: Ordering[A]): CC[A]`                ###

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `def apply[A](elems: A*)(implicit ord: Ordering[A]): CC[A]`              ###

(defined at scala.collection.generic.SortedSetFactory)


### `def newBuilder[A](implicit ord: Ordering[A]): Builder[A, CC[A]]`        ###

(defined at scala.collection.generic.SortedSetFactory)


### `implicit def newCanBuildFrom[A](implicit ord: Ordering[A]): CanBuildFrom[Coll, A, CC[A]]` ###

(defined at scala.collection.generic.SortedSetFactory)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.generic.SortedSetFactory
--------------------------------------------------------------------------------


### `new SortedSetFactory()`                                                 ###
(defined at scala.collection.generic.SortedSetFactory)
