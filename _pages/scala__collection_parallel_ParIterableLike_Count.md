
#               scala.collection.parallel.ParIterableLike#Count               #

```scala
class Count extends Accessor[Int, Count]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Int`                                                      ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Int, Count]]`                                 ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.ParIterableLike.Count
--------------------------------------------------------------------------------


### `new Count(pred: (T) ⇒ Boolean, pit: IterableSplitter[T])`               ###

(defined at scala.collection.parallel.ParIterableLike.Count)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Count
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[Int]): Unit`                                     ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Count → Task

(defined at scala.collection.parallel.ParIterableLike.Count)


### `def merge(that: Count): Unit`                                           ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Count → Task

(defined at scala.collection.parallel.ParIterableLike.Count)


### `def newSubtask(p: IterableSplitter[T]): Count`                          ###

* Attributes
  * protected[this]
* Definition Classes
  * Count → Accessor

(defined at scala.collection.parallel.ParIterableLike.Count)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Count → Accessor

(defined at scala.collection.parallel.ParIterableLike.Count)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Count`                                                        ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Count to
    CollectionsHaveToParArray [Count, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Count) ⇒ GenTraversableOnce [T]
    is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
