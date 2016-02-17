
#                      scala.collection.immutable.IntMap                      #

```scala
object IntMap
```

A companion object for integer maps.

* Source
  * [IntMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/IntMap.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.immutable.IntMap
--------------------------------------------------------------------------------


### `def apply[T](elems: (IntMapUtils.Int, T)*): IntMap[T]`                  ###

(defined at scala.collection.immutable.IntMap)


### `implicit def canBuildFrom[A, B]: CanBuildFrom[IntMap[A], (IntMapUtils.Int, B), IntMap[B]]` ###

The standard `CanBuildFrom` instance for `IntMap` objects. The created value is
an instance of class `MapCanBuildFrom` .

(defined at scala.collection.immutable.IntMap)


### `def empty[T]: IntMap[T]`                                                ###

(defined at scala.collection.immutable.IntMap)


### `def singleton[T](key: IntMapUtils.Int, value: T): IntMap[T]`            ###
(defined at scala.collection.immutable.IntMap)
