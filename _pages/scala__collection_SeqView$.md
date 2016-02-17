
#                           scala.collection.SeqView                           #

```scala
object SeqView
```

An object containing the necessary implicit definitions to make `SeqView` s
work. Its definitions are generally not accessed directly by clients.

* Source
  * [SeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqView.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TraversableView[_, _ <: Traversable[_]]`                    ###


--------------------------------------------------------------------------------
                  Value Members From scala.collection.SeqView
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, SeqView[A, Seq[_]]]` ###
(defined at scala.collection.SeqView)
