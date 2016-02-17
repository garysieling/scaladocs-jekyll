
#                    scala.collection.mutable.LinkedHashSet                    #

```scala
object LinkedHashSet extends MutableSetFactory[LinkedHashSet] with Serializable
```

This object provides a set of operations needed to create `LinkedHashSet`
values.

* Source
  * [LinkedHashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LinkedHashSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = LinkedHashSet[_]`                                           ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[LinkedHashSet[_], A, LinkedHashSet[A]]` ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): LinkedHashSet[A]`                              ###

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


### `def newBuilder[A]: Builder[A, LinkedHashSet[A]]`                        ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * MutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.MutableSetFactory)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.LinkedHashSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, LinkedHashSet[A]]`  ###

(defined at scala.collection.mutable.LinkedHashSet)


### `def empty[A]: LinkedHashSet[A]`                                         ###

An empty collection of type `LinkedHashSet[A]`

* A
  * the type of the linked hash set's elements

* Definition Classes
  * LinkedHashSet → GenericCompanion
(defined at scala.collection.mutable.LinkedHashSet)
