
#                       scala.collection.parallel.ParSet                       #

```scala
object ParSet extends ParSetFactory[ParSet]
```

* Source
  * [ParSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = ParSet[_]`                                                  ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class GenericCanCombineFrom[A] extends CanCombineFrom[CC[_], A, CC[A]]` ###

* Definition Classes
  * ParSetFactory


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[ParSet[_], A, ParSet[A]]`          ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): ParSet[A]`                                     ###

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


### `def empty[A]: ParSet[A]`                                                ###

An empty collection of type `CC[A]`

* A
  * the type of the collection's elements

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.ParSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A]: Combiner[A, ParSet[A]]`                              ###

The default builder for `ParIterable` objects.

* Definition Classes
  * ParSetFactory → GenericParCompanion → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.ParSetFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.parallel.ParSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[T]: CanCombineFrom[Coll, T, ParSet[T]]`       ###

(defined at scala.collection.parallel.ParSet)


### `def newCombiner[T]: Combiner[T, ParSet[T]]`                             ###

The parallel builder for `ParIterable` objects.

* Definition Classes
  * ParSet → ParSetFactory → GenericParCompanion
(defined at scala.collection.parallel.ParSet)
