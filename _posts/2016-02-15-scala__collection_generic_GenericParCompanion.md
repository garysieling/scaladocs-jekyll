
#                 scala.collection.generic.GenericParCompanion                 #

```scala
trait GenericParCompanion[+CC[X] <: ParIterable[X]] extends AnyRef
```

A template class for companion objects of parallel collection classes. They
should be mixed in together with `GenericCompanion` type.

* Source
  * [GenericParCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParCompanion.scala#L1)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.generic.GenericParCompanion
--------------------------------------------------------------------------------


### `abstract def newBuilder[A]: Combiner[A, CC[A]]`                         ###

The default builder for `ParIterable` objects.

(defined at scala.collection.generic.GenericParCompanion)


### `abstract def newCombiner[A]: Combiner[A, CC[A]]`                        ###

The parallel builder for `ParIterable` objects.
(defined at scala.collection.generic.GenericParCompanion)
