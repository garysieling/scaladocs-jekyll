
#             scala.collection.parallel.ParIterableLike#Partition             #

```scala
class Partition[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Combiner[U, This]), Partition[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = (Combiner[U, This], Combiner[U, This])`                   ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[(Combiner[U, This], Combiner[U, This]), Partition[U, This]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.Partition
--------------------------------------------------------------------------------


### `new Partition(pred: (T) ⇒ Boolean, cbfTrue: CombinerFactory[U, This], cbfFalse: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Partition)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Partition
--------------------------------------------------------------------------------


### `def leaf(prev: Option[(Combiner[U, This], Combiner[U, This])]): Unit`   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Partition → Task

(defined at scala.collection.parallel.ParIterableLike.Partition)


### `def merge(that: Partition[U, This]): Unit`                              ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Partition → Task

(defined at scala.collection.parallel.ParIterableLike.Partition)


### `def newSubtask(p: IterableSplitter[T]): Partition[U, This]`             ###

* Attributes
  * protected[this]
* Definition Classes
  * Partition → Accessor

(defined at scala.collection.parallel.ParIterableLike.Partition)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Partition → Accessor

(defined at scala.collection.parallel.ParIterableLike.Partition)


### `var result: (Combiner[U, This], Combiner[U, This])`                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Partition → Task

(defined at scala.collection.parallel.ParIterableLike.Partition)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Partition[U, This]`                                           ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Partition [U, This] to
    CollectionsHaveToParArray [Partition [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Partition [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
