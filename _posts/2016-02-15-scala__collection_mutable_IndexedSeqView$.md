
#                   scala.collection.mutable.IndexedSeqView                   #

```scala
object IndexedSeqView
```

An object containing the necessary implicit definitions to make `SeqView` s
work. Its definitions are generally not accessed directly by clients.

Note that the `canBuildFrom` factories yield `SeqView` s, not `IndexedSeqView`
s. This is intentional, because not all operations yield again a
 `mutable.IndexedSeqView` . For instance, `map` just gives a `SeqView` , which
reflects the fact that `map` cannot do its work and maintain a pointer into the
original indexed sequence.

* Source
  * [IndexedSeqView.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/IndexedSeqView.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TraversableView[_, _ <: Traversable[_]]`                    ###


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.IndexedSeqView
--------------------------------------------------------------------------------


### `implicit def arrCanBuildFrom[A]: CanBuildFrom[TraversableView[_, Array[_]], A, SeqView[A, Array[A]]]` ###

(defined at scala.collection.mutable.IndexedSeqView)


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, SeqView[A, Seq[_]]]` ###
(defined at scala.collection.mutable.IndexedSeqView)
