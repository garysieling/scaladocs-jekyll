
#                      scala.collection.generic.IsSeqLike                      #

```scala
object IsSeqLike
```

* Source
  * [IsSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsSeqLike.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.collection.generic.IsSeqLike
--------------------------------------------------------------------------------


### `implicit def seqLikeRepr[C[_], A0](implicit conv: (C[A0]) ⇒ SeqLike[A0, C[A0]]): IsSeqLike[C[A0]] { type A = A0 }` ###

(defined at scala.collection.generic.IsSeqLike)


### `implicit val stringRepr: IsSeqLike[String] { type A = Char }`           ###
(defined at scala.collection.generic.IsSeqLike)
