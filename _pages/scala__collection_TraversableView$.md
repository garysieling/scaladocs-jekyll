
#                       scala.collection.TraversableView                       #

```scala
object TraversableView
```

An object containing the necessary implicit definitions to make
 `TraversableView` s work. Its definitions are generally not accessed directly
by clients.

* Source
  * [TraversableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableView.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TraversableView[_, _ <: Traversable[_]]`                    ###


### `class NoBuilder[A] extends Builder[A, Nothing]`                         ###

* Source
  * [TraversableView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableView.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableView
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, TraversableView[A, Traversable[_]]]` ###
(defined at scala.collection.TraversableView)
