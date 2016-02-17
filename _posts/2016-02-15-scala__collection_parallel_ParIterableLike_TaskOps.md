
#              scala.collection.parallel.ParIterableLike#TaskOps              #

```scala
trait TaskOps[R, Tp] extends AnyRef
```

* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.parallel.ParIterableLike.TaskOps
--------------------------------------------------------------------------------


### `abstract def compose[R3, R2, Tp2](t2: SSCTask[R2, Tp2])(resCombiner: (R, R2) ⇒ R3): SeqComposite[R, R2, R3, SSCTask[R, Tp], SSCTask[R2, Tp2]]` ###

(defined at scala.collection.parallel.ParIterableLike.TaskOps)


### `abstract def mapResult[R1](mapping: (R) ⇒ R1): ResultMapping[R, Tp, R1]` ###

(defined at scala.collection.parallel.ParIterableLike.TaskOps)


### `abstract def parallel[R3, R2, Tp2](t2: SSCTask[R2, Tp2])(resCombiner: (R, R2) ⇒ R3): ParComposite[R, R2, R3, SSCTask[R, Tp], SSCTask[R2, Tp2]]` ###

(defined at scala.collection.parallel.ParIterableLike.TaskOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from TaskOps [R, Tp] to
    CollectionsHaveToParArray [TaskOps [R, Tp], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (TaskOps [R, Tp]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
