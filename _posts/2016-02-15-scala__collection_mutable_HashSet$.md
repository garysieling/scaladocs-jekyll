
#                       scala.collection.mutable.HashSet                       #

```scala
object HashSet extends MutableSetFactory[HashSet] with Serializable
```

This object provides a set of operations needed to create `mutable.HashSet`
values.

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = HashSet[_]`                                                 ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[HashSet[_], A, HashSet[A]]`        ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): HashSet[A]`                                    ###

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


### `def newBuilder[A]: Builder[A, HashSet[A]]`                              ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * MutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.MutableSetFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.HashSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, HashSet[A]]`        ###

(defined at scala.collection.mutable.HashSet)


### `def empty[A]: HashSet[A]`                                               ###

An empty collection of type `mutable.HashSet[A]`

* A
  * the type of the mutable hash set's elements

* Definition Classes
  * HashSet → GenericCompanion
(defined at scala.collection.mutable.HashSet)
