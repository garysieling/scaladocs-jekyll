
#                       scala.collection.TraversableOnce                       #

```scala
object TraversableOnce
```

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class FlattenOps[A] extends AnyRef`                                     ###

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


### `class ForceImplicitAmbiguity extends AnyRef`                            ###

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


### `implicit class MonadOps[+A] extends AnyRef`                             ###

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


### `class OnceCanBuildFrom[A] extends BufferedCanBuildFrom[A, TraversableOnce]` ###

With the advent of `TraversableOnce` , it can be useful to have a builder which
operates on `Iterator` s so they can be treated uniformly along with the
collections. See `scala.util.Random.shuffle` or
 `scala.concurrent.Future.sequence` for an example.

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableOnce
--------------------------------------------------------------------------------


### `implicit def OnceCanBuildFrom[A]: OnceCanBuildFrom[A]`                  ###

Evidence for building collections from `TraversableOnce` collections

(defined at scala.collection.TraversableOnce)


### `implicit def alternateImplicit[A](trav: TraversableOnce[A]): ForceImplicitAmbiguity` ###

(defined at scala.collection.TraversableOnce)


### `implicit def flattenTraversableOnce[A, CC[_]](travs: TraversableOnce[CC[A]])(implicit ev: (CC[A]) ⇒ TraversableOnce[A]): FlattenOps[A]` ###
(defined at scala.collection.TraversableOnce)
