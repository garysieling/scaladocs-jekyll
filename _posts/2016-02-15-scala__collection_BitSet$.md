
#                           scala.collection.BitSet                           #

```scala
object BitSet extends BitSetFactory[BitSet]
```

This object provides a set of operations to create `BitSet` values.

* Source
  * [BitSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/BitSet.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From scala.collection.BitSet
--------------------------------------------------------------------------------


### `implicit def canBuildFrom: CanBuildFrom[BitSet, Int, BitSet]`           ###

The standard `CanBuildFrom` instance for `BitSet` objects.

(defined at scala.collection.BitSet)


### `val empty: BitSet`                                                      ###

* Definition Classes
  * BitSet → BitSetFactory

(defined at scala.collection.BitSet)


### `def newBuilder: Builder[Int, immutable.BitSet]`                         ###

* Definition Classes
  * BitSet → BitSetFactory

(defined at scala.collection.BitSet)


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
