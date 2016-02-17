
#                        scala.collection.immutable.Set                        #

```scala
object Set extends ImmutableSetFactory[Set]
```

This object provides a set of operations needed to create `immutable.Set`
values.

* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Set[_]`                                                     ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class Set1[A] extends AbstractSet[A] with Set[A] with Serializable`     ###

An optimized representation for immutable sets of size 1

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


### `class Set2[A] extends AbstractSet[A] with Set[A] with Serializable`     ###

An optimized representation for immutable sets of size 2

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


### `class Set3[A] extends AbstractSet[A] with Set[A] with Serializable`     ###

An optimized representation for immutable sets of size 3

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


### `class Set4[A] extends AbstractSet[A] with Set[A] with Serializable`     ###

An optimized representation for immutable sets of size 4

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Set.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Set.scala#L1)


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
        Value Members From scala.collection.generic.ImmutableSetFactory
--------------------------------------------------------------------------------


### `def empty[A]: Set[A]`                                                   ###

An empty collection of type `Set[A]`

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


### `def newBuilder[A]: Builder[A, Set[A]]`                                  ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


--------------------------------------------------------------------------------
               Value Members From scala.collection.immutable.Set
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, Set[A]]`            ###

The standard `CanBuildFrom` instance for `immutable.Set` objects.
(defined at scala.collection.immutable.Set)
