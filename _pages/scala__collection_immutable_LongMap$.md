
#                      scala.collection.immutable.LongMap                      #

```scala
object LongMap
```

A companion object for long maps.

* Source
  * [LongMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/LongMap.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.LongMap
--------------------------------------------------------------------------------


### `def apply[T](elems: (LongMapUtils.Long, T)*): LongMap[T]`               ###

(defined at scala.collection.immutable.LongMap)


### `implicit def canBuildFrom[A, B]: CanBuildFrom[LongMap[A], (LongMapUtils.Long, B), LongMap[B]]` ###

The standard `CanBuildFrom` instance for `LongMap` objects. The created value is
an instance of class `MapCanBuildFrom` .

(defined at scala.collection.immutable.LongMap)


### `def empty[T]: LongMap[T]`                                               ###

(defined at scala.collection.immutable.LongMap)


### `def singleton[T](key: LongMapUtils.Long, value: T): LongMap[T]`         ###
(defined at scala.collection.immutable.LongMap)
