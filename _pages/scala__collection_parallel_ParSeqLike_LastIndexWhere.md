
#             scala.collection.parallel.ParSeqLike#LastIndexWhere             #

```scala
class LastIndexWhere extends Accessor[Int, LastIndexWhere]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Int`                                                      ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParSeqLike.LastIndexWhere
--------------------------------------------------------------------------------


### `new LastIndexWhere(pred: (T) ⇒ Boolean, pos: Int, pit: SeqSplitter[T])` ###

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParSeqLike.LastIndexWhere
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Int]): Unit`                                      ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * LastIndexWhere → Task

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


### `def merge(that: LastIndexWhere): Unit`                                  ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * LastIndexWhere → Task

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * LastIndexWhere → Accessor

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * LastIndexWhere → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


### `def split: scala.Seq[Task[Int, LastIndexWhere]]`                        ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * LastIndexWhere → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.LastIndexWhere)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: LastIndexWhere`                                               ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from LastIndexWhere to
    CollectionsHaveToParArray [LastIndexWhere, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (LastIndexWhere) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
