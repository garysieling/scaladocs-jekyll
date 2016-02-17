
#                  scala.collection.generic.IsTraversableOnce                  #

```scala
object IsTraversableOnce
```

* Source
  * [IsTraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableOnce.scala#L1)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.IsTraversableOnce
--------------------------------------------------------------------------------


### `implicit def genTraversableLikeRepr[C[_], A0](implicit conv: (C[A0]) ⇒ GenTraversableOnce[A0]): IsTraversableOnce[C[A0]] { type A = A0 }` ###

(defined at scala.collection.generic.IsTraversableOnce)


### `implicit val stringRepr: IsTraversableOnce[String] { type A = Char }`   ###
(defined at scala.collection.generic.IsTraversableOnce)
