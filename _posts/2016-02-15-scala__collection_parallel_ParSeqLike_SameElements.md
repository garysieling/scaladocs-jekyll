
#              scala.collection.parallel.ParSeqLike#SameElements              #

```scala
class SameElements[U >: T] extends Accessor[Boolean, SameElements[U]]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Boolean`                                                  ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParSeqLike.SameElements
--------------------------------------------------------------------------------


### `new SameElements(pit: SeqSplitter[T], otherpit: SeqSplitter[U])`        ###

(defined at scala.collection.parallel.ParSeqLike.SameElements)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParSeqLike.SameElements
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Boolean]): Unit`                                  ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * SameElements → Task

(defined at scala.collection.parallel.ParSeqLike.SameElements)


### `def merge(that: SameElements[U]): Unit`                                 ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * SameElements → Task

(defined at scala.collection.parallel.ParSeqLike.SameElements)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * SameElements → Accessor

(defined at scala.collection.parallel.ParSeqLike.SameElements)


### `val otherpit: SeqSplitter[U]`                                           ###

(defined at scala.collection.parallel.ParSeqLike.SameElements)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * SameElements → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.SameElements)


### `def split: scala.Seq[Task[Boolean, SameElements[U]]]`                   ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * SameElements → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.SameElements)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: SameElements[U]`                                              ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SameElements [U] to
    CollectionsHaveToParArray [SameElements [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (SameElements [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
