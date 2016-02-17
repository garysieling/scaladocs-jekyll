
#                             scala.collection.Set                             #

```scala
object Set extends SetFactory[Set]
```

This object provides a set of operations needed to create `Set` values. The
current default implementation of a `Set` is one of `EmptySet` , `Set1` ,
 `Set2` , `Set3` , `Set4` in class `immutable.Set` for sets of sizes up to 4,
and a `immutable.HashSet` for sets of larger sizes.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Set.scala#L1)


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
                    Value Members From scala.collection.Set
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, Set[A]]`            ###

(defined at scala.collection.Set)


### `def empty[A]: Set[A]`                                                   ###

An empty collection of type `Set[A]`

* A
  * the type of the set's elements

* Definition Classes
  * Set → GenericCompanion

(defined at scala.collection.Set)


### `def newBuilder[A]: Builder[A, immutable.Set[A]]`                        ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * Set → GenSetFactory → GenericCompanion

(defined at scala.collection.Set)


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
