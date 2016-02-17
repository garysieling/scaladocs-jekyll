
#                             scala.collection.:+                             #

```scala
object :+
```

An extractor used to init/last deconstruct sequences.

* Source
  * [SeqExtractors.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqExtractors.scala#L1)


--------------------------------------------------------------------------------
                     Value Members From scala.collection.:+
--------------------------------------------------------------------------------


### `def unapply[T, Coll <: SeqLike[T, Coll]](t: Coll with SeqLike[T, Coll]): Option[(Coll, T)]` ###

Splits a sequence into init :+ tail.

* returns
  * Some((init, tail)) if sequence is non-empty. None otherwise.
(defined at scala.collection.:+)
