
#                  scala.collection.TraversableOnce.MonadOps                  #

```scala
implicit class MonadOps[+A] extends AnyRef
```

* Source
  * [TraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableOnce.scala#L1)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.TraversableOnce.MonadOps
--------------------------------------------------------------------------------


### `new MonadOps(trav: TraversableOnce[A])`                                 ###

(defined at scala.collection.TraversableOnce.MonadOps)


--------------------------------------------------------------------------------
          Value Members From scala.collection.TraversableOnce.MonadOps
--------------------------------------------------------------------------------


### `def filter(p: (A) ⇒ Boolean): TraversableOnce[A]`                       ###

(defined at scala.collection.TraversableOnce.MonadOps)


### `def flatMap[B](f: (A) ⇒ GenTraversableOnce[B]): TraversableOnce[B]`     ###

(defined at scala.collection.TraversableOnce.MonadOps)


### `def map[B](f: (A) ⇒ B): TraversableOnce[B]`                             ###

(defined at scala.collection.TraversableOnce.MonadOps)


### `def withFilter(p: (A) ⇒ Boolean): Iterator[A]`                          ###
(defined at scala.collection.TraversableOnce.MonadOps)
