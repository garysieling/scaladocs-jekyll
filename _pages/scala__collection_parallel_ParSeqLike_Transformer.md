
#               scala.collection.parallel.ParSeqLike#Transformer               #

```scala
trait Transformer[R, Tp] extends Accessor[R, Tp] with ParSeqLike.Transformer[R, Tp]
```

* Attributes
  * protected
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = R`                                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `abstract def newSubtask(p: IterableSplitter[T]): ParSeqLike.Accessor[R, Tp]` ###

* Attributes
  * protected[this]
* Definition Classes
  * Accessor

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
 Concrete Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[R, Tp]]`                                      ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
   Abstract Value Members From scala.collection.parallel.ParSeqLike.Accessor
--------------------------------------------------------------------------------


### `abstract val pit: SeqSplitter[T]`                                       ###

* Attributes
  * protected[this]
* Definition Classes
  * Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.Accessor)


--------------------------------------------------------------------------------
           Abstract Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `abstract def leaf(result: Option[R]): Unit`                             ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `abstract val result: R`                                                 ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Transformer [R, Tp] to
    CollectionsHaveToParArray [Transformer [R, Tp], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Transformer [R, Tp]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
