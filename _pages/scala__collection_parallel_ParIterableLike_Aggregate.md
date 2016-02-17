
#             scala.collection.parallel.ParIterableLike#Aggregate             #

```scala
class Aggregate[S] extends Accessor[S, Aggregate[S]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = S`                                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[S, Aggregate[S]]]`                            ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.Aggregate
--------------------------------------------------------------------------------


### `new Aggregate(z: () ⇒ S, seqop: (S, T) ⇒ S, combop: (S, S) ⇒ S, pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Aggregate)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Aggregate
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[S]): Unit`                                       ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Aggregate → Task

(defined at scala.collection.parallel.ParIterableLike.Aggregate)


### `def merge(that: Aggregate[S]): Unit`                                    ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Aggregate → Task

(defined at scala.collection.parallel.ParIterableLike.Aggregate)


### `def newSubtask(p: IterableSplitter[T]): Aggregate[S]`                   ###

* Attributes
  * protected[this]
* Definition Classes
  * Aggregate → Accessor

(defined at scala.collection.parallel.ParIterableLike.Aggregate)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Aggregate → Accessor

(defined at scala.collection.parallel.ParIterableLike.Aggregate)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Aggregate[S]`                                                 ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Aggregate [S] to
    CollectionsHaveToParArray [Aggregate [S], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Aggregate [S]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
