
#                       scala.collection.mutable.LongMap                       #

```scala
object LongMap extends Serializable
```

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LongMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final class LongMapBuilder[V] extends ReusableBuilder[(Long, V), LongMap[V]]` ###

A builder for instances of `LongMap` .

This builder can be reused to create multiple instances.

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/LongMap.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.LongMap
--------------------------------------------------------------------------------


### `def apply[V](elems: (Long, V)*): LongMap[V]`                            ###

Creates a new `LongMap` with zero or more key/value pairs.

(defined at scala.collection.mutable.LongMap)


### `implicit def canBuildFrom[V, U]: CanBuildFrom[LongMap[V], (Long, U), LongMap[U]]` ###

(defined at scala.collection.mutable.LongMap)


### `def empty[V]: LongMap[V]`                                               ###

Creates a new empty `LongMap` .

(defined at scala.collection.mutable.LongMap)


### `def fromZip[V](keys: Array[Long], values: Array[V]): LongMap[V]`        ###

Creates a new `LongMap` from arrays of keys and values. Equivalent to but more
efficient than `LongMap((keys zip values): _*)` .

(defined at scala.collection.mutable.LongMap)


### `def fromZip[V](keys: collection.Iterable[Long], values: collection.Iterable[V]): LongMap[V]` ###

Creates a new `LongMap` from keys and values. Equivalent to but more efficient
than `LongMap((keys zip values): _*)` .

(defined at scala.collection.mutable.LongMap)


### `def withDefault[V](default: (Long) ⇒ V): LongMap[V]`                    ###

Creates a new empty `LongMap` with the supplied default
(defined at scala.collection.mutable.LongMap)
