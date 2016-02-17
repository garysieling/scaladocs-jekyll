
#                       scala.collection.mutable.BitSet                       #

```scala
object BitSet extends BitSetFactory[BitSet] with Serializable
```

This object provides a set of operations to create `BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/BitSet.scala#L1)


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
               Value Members From scala.collection.mutable.BitSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom: CanBuildFrom[BitSet, Int, BitSet]`           ###

The standard `CanBuildFrom` instance for bitsets.

(defined at scala.collection.mutable.BitSet)


### `def empty: BitSet`                                                      ###

* Definition Classes
  * BitSet → BitSetFactory

(defined at scala.collection.mutable.BitSet)


### `def fromBitMask(elems: Array[Long]): BitSet`                            ###

A bitset containing all the bits in an array

(defined at scala.collection.mutable.BitSet)


### `def fromBitMaskNoCopy(elems: Array[Long]): BitSet`                      ###

A bitset containing all the bits in an array, wrapping the existing array
without copying.

(defined at scala.collection.mutable.BitSet)


### `def newBuilder: Builder[Int, BitSet]`                                   ###

A growing builder for mutable Sets.

* Definition Classes
  * BitSet → BitSetFactory
(defined at scala.collection.mutable.BitSet)
