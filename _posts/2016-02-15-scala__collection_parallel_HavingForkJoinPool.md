
#                 scala.collection.parallel.HavingForkJoinPool                 #

```scala
trait HavingForkJoinPool extends AnyRef
```

A trait describing objects that provide a fork/join pool.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.parallel.HavingForkJoinPool
--------------------------------------------------------------------------------


### `abstract def forkJoinPool: ForkJoinPool`                                ###

(defined at scala.collection.parallel.HavingForkJoinPool)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from HavingForkJoinPool to
    CollectionsHaveToParArray [HavingForkJoinPool, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (HavingForkJoinPool) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
