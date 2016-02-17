
#                 scala.collection.parallel.ParSeqLike#Updated                 #

```scala
class Updated[U >: T, That] extends Transformer[Combiner[U, That], Updated[U, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[U, That]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.ParSeqLike.Updated
--------------------------------------------------------------------------------


### `new Updated(pos: Int, elem: U, pbf: CombinerFactory[U, That], pit: SeqSplitter[T])` ###

(defined at scala.collection.parallel.ParSeqLike.Updated)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.ParSeqLike.Updated
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Updated → Task

(defined at scala.collection.parallel.ParSeqLike.Updated)


### `def merge(that: Updated[U, That]): Unit`                                ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Updated → Task

(defined at scala.collection.parallel.ParSeqLike.Updated)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Updated → Accessor

(defined at scala.collection.parallel.ParSeqLike.Updated)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * Updated → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.Updated)


### `var result: Combiner[U, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Updated → Task

(defined at scala.collection.parallel.ParSeqLike.Updated)


### `def split: scala.Seq[Task[Combiner[U, That], Updated[U, That]]]`        ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Updated → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.Updated)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Updated[U, That]`                                             ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Updated [U, That] to
    CollectionsHaveToParArray [Updated [U, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Updated [U, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
