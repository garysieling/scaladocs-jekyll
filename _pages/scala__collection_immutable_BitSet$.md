
#                      scala.collection.immutable.BitSet                      #

```scala
object BitSet extends BitSetFactory[BitSet] with Serializable
```

This object provides a set of operations to create `immutable.BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class BitSet1 extends BitSet`                                           ###

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)


### `class BitSet2 extends BitSet`                                           ###

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)


### `class BitSetN extends BitSet`                                           ###

The implementing class for bit sets with elements >= 128 (exceeding the capacity
of two long values). The constructor wraps an existing bit mask without copying,
thus exposing a mutable part of the internal implementation. Care needs to be
taken not to modify the exposed array.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/BitSet.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.BitSetFactory
--------------------------------------------------------------------------------


### `def apply(elems: Int*): BitSet`                                         ###

* Definition Classes
  * BitSetFactory

(defined at scala.collection.generic.BitSetFactory)


### `def bitsetCanBuildFrom: CanBuildFrom[BitSet, Int, BitSet]`              ###

* Definition Classes
  * BitSetFactory

(defined at scala.collection.generic.BitSetFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.immutable.BitSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom: CanBuildFrom[BitSet, Int, BitSet]`           ###

The standard `CanBuildFrom` instance for bitsets.

(defined at scala.collection.immutable.BitSet)


### `val empty: BitSet`                                                      ###

The empty bitset

* Definition Classes
  * BitSet → BitSetFactory

(defined at scala.collection.immutable.BitSet)


### `def fromBitMask(elems: Array[Long]): BitSet`                            ###

A bitset containing all the bits in an array

(defined at scala.collection.immutable.BitSet)


### `def fromBitMaskNoCopy(elems: Array[Long]): BitSet`                      ###

A bitset containing all the bits in an array, wrapping the existing array
without copying.

(defined at scala.collection.immutable.BitSet)


### `def newBuilder: Builder[Int, BitSet]`                                   ###

A builder that takes advantage of mutable BitSets.

* Definition Classes
  * BitSet → BitSetFactory
(defined at scala.collection.immutable.BitSet)
