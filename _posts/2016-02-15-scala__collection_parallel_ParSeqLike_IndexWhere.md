
#               scala.collection.parallel.ParSeqLike#IndexWhere               #

```scala
class IndexWhere extends Accessor[Int, IndexWhere]
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
   Instance Constructors From scala.collection.parallel.ParSeqLike.IndexWhere
--------------------------------------------------------------------------------


### `new IndexWhere(pred: (T) ⇒ Boolean, from: Int, pit: SeqSplitter[T])`    ###

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParSeqLike.IndexWhere
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Int]): Unit`                                      ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * IndexWhere → Task

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


### `def merge(that: IndexWhere): Unit`                                      ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * IndexWhere → Task

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * IndexWhere → Accessor

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * IndexWhere → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


### `def split: scala.Seq[Task[Int, IndexWhere]]`                            ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * IndexWhere → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.IndexWhere)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: IndexWhere`                                                   ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from IndexWhere to
    CollectionsHaveToParArray [IndexWhere, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (IndexWhere) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
