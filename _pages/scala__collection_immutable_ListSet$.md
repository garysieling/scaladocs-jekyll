
#                      scala.collection.immutable.ListSet                      #

```scala
object ListSet extends ImmutableSetFactory[ListSet] with Serializable
```

This object provides a set of operations needed to create `immutable.ListSet`
values.

* Source
  * [ListSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = ListSet[_]`                                                 ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class ListSetBuilder[Elem] extends ReusableBuilder[Elem, ListSet[Elem]]` ###

A custom builder because forgetfully adding elements one at a time to a list
backed set puts the "squared" in N^2. There is a temporary space cost, but it's
improbable a list backed set could become large enough for this to matter given
its pricy element lookup.

This builder is reusable.

* Source
  * [ListSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/ListSet.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenSetFactory
--------------------------------------------------------------------------------


### `def setCanBuildFrom[A]: CanBuildFrom[ListSet[_], A, ListSet[A]]`        ###

The standard `CanBuildFrom` instance for `Set` objects.

* Definition Classes
  * GenSetFactory

(defined at scala.collection.generic.GenSetFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): ListSet[A]`                                    ###

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


### `def empty[A]: ListSet[A]`                                               ###

An empty collection of type `Set[A]`

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.ListSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, ListSet[A]]`        ###

setCanBuildFromInfo

(defined at scala.collection.immutable.ListSet)


### `def newBuilder[A]: Builder[A, ListSet[A]]`                              ###

The default builder for `immutable.ListSet` objects.

* A
  * the type of the immutable list set's elements

* Definition Classes
  * ListSet → ImmutableSetFactory → GenSetFactory → GenericCompanion
(defined at scala.collection.immutable.ListSet)
