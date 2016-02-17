
#                 scala.collection.parallel.mutable.ParHashSet                 #

```scala
object ParHashSet extends ParSetFactory[ParHashSet] with Serializable
```

This object provides a set of operations needed to create `mutable.ParHashSet`
values.

* Source
  * [ParHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = ParHashSet[_]`                                              ###

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


### `def setCanBuildFrom[A]: CanBuildFrom[ParHashSet[_], A, ParHashSet[A]]`  ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): ParHashSet[A]`                                 ###

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


### `def empty[A]: ParHashSet[A]`                                            ###

An empty collection of type `CC[A]`

* A
  * the type of the collection's elements

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.mutable.ParHashSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[T]: CanCombineFrom[Coll, T, ParHashSet[T]]`   ###

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def newBuilder[T]: Combiner[T, ParHashSet[T]]`                          ###

The default builder for `mutable.ParHashSet` objects.

* Definition Classes
  * ParHashSet → ParSetFactory → GenericParCompanion → GenSetFactory →
    GenericCompanion

(defined at scala.collection.parallel.mutable.ParHashSet)


### `def newCombiner[T]: Combiner[T, ParHashSet[T]]`                         ###

The parallel builder for `mutable.ParHashSet` objects.

* Definition Classes
  * ParHashSet → ParSetFactory → GenericParCompanion
(defined at scala.collection.parallel.mutable.ParHashSet)
