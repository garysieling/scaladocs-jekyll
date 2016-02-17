
#                    scala.collection.generic.BitSetFactory                    #

```scala
trait BitSetFactory[Coll <: BitSet with BitSetLike[Coll]] extends AnyRef
```

* Source
  * [BitSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/BitSetFactory.scala#L1)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.BitSetFactory
--------------------------------------------------------------------------------


### `abstract def newBuilder: Builder[Int, Coll]`                            ###

(defined at scala.collection.generic.BitSetFactory)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.BitSetFactory
--------------------------------------------------------------------------------


### `abstract def empty: Coll`                                               ###

(defined at scala.collection.generic.BitSetFactory)


### `def apply(elems: Int*): Coll`                                           ###

(defined at scala.collection.generic.BitSetFactory)


### `def bitsetCanBuildFrom: CanBuildFrom[Coll, Int, Coll]`                  ###
(defined at scala.collection.generic.BitSetFactory)
