
#                         scala.collection.mutable.Set                         #

```scala
object Set extends MutableSetFactory[Set]
```

This object provides a set of operations needed to create `mutable.Set` values.
The current default implementation of a `mutable.Set` is a `HashSet` .

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/Set.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Set[_]`                                                     ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[Set[_], A, Set[A]]`                ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): Set[A]`                                        ###

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


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.MutableSetFactory
--------------------------------------------------------------------------------


### `def newBuilder[A]: Builder[A, Set[A]]`                                  ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * MutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.MutableSetFactory)


--------------------------------------------------------------------------------
                Value Members From scala.collection.mutable.Set
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, Set[A]]`            ###

(defined at scala.collection.mutable.Set)


### `def empty[A]: Set[A]`                                                   ###

An empty collection of type `mutable.Set[A]`

* A
  * the type of the mutable set's elements

* Definition Classes
  * Set → GenericCompanion
(defined at scala.collection.mutable.Set)
