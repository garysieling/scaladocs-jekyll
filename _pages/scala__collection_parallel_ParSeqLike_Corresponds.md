
#               scala.collection.parallel.ParSeqLike#Corresponds               #

```scala
class Corresponds[S] extends Accessor[Boolean, Corresponds[S]]
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
  Instance Constructors From scala.collection.parallel.ParSeqLike.Corresponds
--------------------------------------------------------------------------------


### `new Corresponds(corr: (T, S) ⇒ Boolean, pit: SeqSplitter[T], otherpit: SeqSplitter[S])` ###

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParSeqLike.Corresponds
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Boolean]): Unit`                                  ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Corresponds → Task

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


### `def merge(that: Corresponds[S]): Unit`                                  ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Corresponds → Task

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Corresponds → Accessor

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


### `val otherpit: SeqSplitter[S]`                                           ###

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * Corresponds → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


### `def split: scala.Seq[Task[Boolean, Corresponds[S]]]`                    ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Corresponds → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.Corresponds)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Corresponds[S]`                                               ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Corresponds [S] to
    CollectionsHaveToParArray [Corresponds [S], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Corresponds [S]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
