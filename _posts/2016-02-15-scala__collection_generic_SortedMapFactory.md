
#                  scala.collection.generic.SortedMapFactory                  #

```scala
abstract class SortedMapFactory[CC[A, B] <: SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends AnyRef
```

A template for companion objects of mutable.Map and subclasses thereof.

* Source
  * [SortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedMapFactory.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = CC[_, _]`                                                   ###


### `class SortedMapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

* Source
  * [SortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedMapFactory.scala#L1)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `abstract def empty[A, B](implicit ord: Ordering[A]): CC[A, B]`          ###

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*)(implicit ord: Ordering[A]): CC[A, B]`   ###

(defined at scala.collection.generic.SortedMapFactory)


### `def newBuilder[A, B](implicit ord: Ordering[A]): Builder[(A, B), CC[A, B]]` ###

(defined at scala.collection.generic.SortedMapFactory)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.generic.SortedMapFactory
--------------------------------------------------------------------------------


### `new SortedMapFactory()`                                                 ###
(defined at scala.collection.generic.SortedMapFactory)
