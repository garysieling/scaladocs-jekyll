
#                 scala.collection.parallel.ParSeqLike#Reverse                 #

```scala
class Reverse[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Reverse[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[U, This]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[U, This], Reverse[U, This]]]`        ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.ParSeqLike.Reverse
--------------------------------------------------------------------------------


### `new Reverse(cbf: () ⇒ Combiner[U, This], pit: SeqSplitter[T])`          ###

(defined at scala.collection.parallel.ParSeqLike.Reverse)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.ParSeqLike.Reverse
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, This]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Reverse → Task

(defined at scala.collection.parallel.ParSeqLike.Reverse)


### `def merge(that: Reverse[U, This]): Unit`                                ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Reverse → Task

(defined at scala.collection.parallel.ParSeqLike.Reverse)


### `def newSubtask(p: SuperParIterator): Reverse[U, This]`                  ###

* Attributes
  * protected[this]
* Definition Classes
  * Reverse → Accessor

(defined at scala.collection.parallel.ParSeqLike.Reverse)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * Reverse → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.Reverse)


### `var result: Combiner[U, This]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Reverse → Task

(defined at scala.collection.parallel.ParSeqLike.Reverse)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Reverse[U, This]`                                             ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Reverse [U, This] to
    CollectionsHaveToParArray [Reverse [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Reverse [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
