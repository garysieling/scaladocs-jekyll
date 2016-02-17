
#                      scala.collection.mutable.AnyRefMap                      #

```scala
object AnyRefMap extends Serializable
```

* Source
  * [AnyRefMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/AnyRefMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final class AnyRefMapBuilder[K <: AnyRef, V] extends ReusableBuilder[(K, V), AnyRefMap[K, V]]` ###

A builder for instances of `AnyRefMap` .

This builder can be reused to create multiple instances.

* Source
  * [AnyRefMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/AnyRefMap.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.AnyRefMap
--------------------------------------------------------------------------------


### `def apply[K <: AnyRef, V](elems: (K, V)*): AnyRefMap[K, V]`             ###

Creates a new `AnyRefMap` with zero or more key/value pairs.

(defined at scala.collection.mutable.AnyRefMap)


### `implicit def canBuildFrom[K <: AnyRef, V, J <: AnyRef, U]: CanBuildFrom[AnyRefMap[K, V], (J, U), AnyRefMap[J, U]]` ###

(defined at scala.collection.mutable.AnyRefMap)


### `def empty[K <: AnyRef, V]: AnyRefMap[K, V]`                             ###

Creates a new empty `AnyRefMap` .

(defined at scala.collection.mutable.AnyRefMap)


### `def fromZip[K <: AnyRef, V](keys: Array[K], values: Array[V]): AnyRefMap[K, V]` ###

Creates a new `AnyRefMap` from arrays of keys and values. Equivalent to but more
efficient than `AnyRefMap((keys zip values): _*)` .

(defined at scala.collection.mutable.AnyRefMap)


### `def fromZip[K <: AnyRef, V](keys: Iterable[K], values: Iterable[V]): AnyRefMap[K, V]` ###

Creates a new `AnyRefMap` from keys and values. Equivalent to but more efficient
than `AnyRefMap((keys zip values): _*)` .

(defined at scala.collection.mutable.AnyRefMap)


### `def withDefault[K <: AnyRef, V](default: (K) ⇒ V): AnyRefMap[K, V]`     ###

Creates a new empty `AnyRefMap` with the supplied default
(defined at scala.collection.mutable.AnyRefMap)
