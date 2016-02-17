
#                  scala.collection.generic.IsTraversableLike                  #

```scala
object IsTraversableLike
```

* Source
  * [IsTraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableLike.scala#L1)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.IsTraversableLike
--------------------------------------------------------------------------------


### `implicit def genTraversableLikeRepr[C[_], A0](implicit conv: (C[A0]) ⇒ GenTraversableLike[A0, C[A0]]): IsTraversableLike[C[A0]] { type A = A0 }` ###

(defined at scala.collection.generic.IsTraversableLike)


### `implicit val stringRepr: IsTraversableLike[String] { type A = Char }`   ###
(defined at scala.collection.generic.IsTraversableLike)
