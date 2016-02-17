
#              scala.collection.parallel.ParSeqLike#SegmentLength              #

```scala
class SegmentLength extends Accessor[(Int, Boolean), SegmentLength]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = (Int, Boolean)`                                           ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParSeqLike.SegmentLength
--------------------------------------------------------------------------------


### `new SegmentLength(pred: (T) ⇒ Boolean, from: Int, pit: SeqSplitter[T])` ###

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParSeqLike.SegmentLength
--------------------------------------------------------------------------------


### `def leaf(prev: Option[(Int, Boolean)]): Unit`                           ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * SegmentLength → Task

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


### `def merge(that: SegmentLength): Unit`                                   ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * SegmentLength → Task

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * SegmentLength → Accessor

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * SegmentLength → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


### `def split: scala.Seq[Task[(Int, Boolean), SegmentLength]]`              ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * SegmentLength → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.SegmentLength)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: SegmentLength`                                                ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SegmentLength to
    CollectionsHaveToParArray [SegmentLength, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (SegmentLength) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
