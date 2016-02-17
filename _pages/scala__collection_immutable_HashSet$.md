
#                      scala.collection.immutable.HashSet                      #

```scala
object HashSet extends ImmutableSetFactory[HashSet] with Serializable
```

This object provides a set of operations needed to create `immutable.HashSet`
values.

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = HashSet[_]`                                                 ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class HashSet1[A] extends LeafHashSet[A]`                               ###

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashSet.scala#L1)


### `class HashTrieSet[A] extends HashSet[A]`                                ###

A branch node of the HashTrieSet with at least one and up to 32 children.

* A
  * the type of the elements contained in this hash set. How levels work: When
    looking up or adding elements, the part of the hashcode that is used to
    address the children array depends on how deep we are in the tree. This is
    accomplished by having a level parameter in all internal methods that starts
    at 0 and increases by 5 (32 = 2 <sup>5) every time we go deeper into the
    tree. hashcode (binary): 00000000000000000000000000000000 level=0 (depth=0)
    </sup> <sup><sup><sup><sup>level=5 (depth=1)</sup></sup></sup></sup> <sup>
    level=10 (depth=2)</sup> ^^^^... Be careful: a non-toplevel HashTrieSet is
    not a self-contained set, so e.g. calling contains on it will not work! It
    relies on its depth in the Trie for which part of a hash to use to address
    the children, but this information (the level) is not stored due to storage
    efficiency reasons but has to be passed explicitly! How bitmap and elems
    correspond: A naive implementation of a HashTrieSet would always have an
    array of size 32 for children and leave the unused children empty (null).
    But that would be very wasteful regarding memory. Instead, only non-empty
    children are stored in elems, and the bitmap is used to encode which elem
    corresponds to which child bucket. The lowest 1 bit corresponds to the first
    element, the second-lowest to the second, etc. bitmap (binary):
    00010000000000000000100000000000 elems: [a,b] children:
    ---b----------------a-----------

* Source
  * [HashSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashSet.scala#L1)


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
        Value Members From scala.collection.generic.ImmutableSetFactory
--------------------------------------------------------------------------------


### `def empty[A]: HashSet[A]`                                               ###

An empty collection of type `Set[A]`

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


### `def newBuilder[A]: Builder[A, HashSet[A]]`                              ###

The default builder for `Set` objects.

* A
  * the type of the set's elements

* Definition Classes
  * ImmutableSetFactory → GenSetFactory → GenericCompanion

(defined at scala.collection.generic.ImmutableSetFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.HashSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, HashSet[A]]`        ###

The standard `CanBuildFrom` instance for `immutable.HashSet` objects.
(defined at scala.collection.immutable.HashSet)
