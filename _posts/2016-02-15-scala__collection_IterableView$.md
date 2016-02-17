
#                        scala.collection.IterableView                        #

```scala
object IterableView
```

An object containing the necessary implicit definitions to make `IterableView` s
work. Its definitions are generally not accessed directly by clients.

* Source
  * [IterableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableView.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TraversableView[_, _ <: Traversable[_]]`                    ###


--------------------------------------------------------------------------------
                Value Members From scala.collection.IterableView
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, IterableView[A, Iterable[_]]]` ###
(defined at scala.collection.IterableView)
