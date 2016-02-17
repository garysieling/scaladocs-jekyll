
#               scala.collection.parallel.ParIterableLike#Filter               #

```scala
class Filter[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Filter[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[U, This]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[U, This], Filter[U, This]]]`         ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Filter
--------------------------------------------------------------------------------


### `new Filter(pred: (T) ⇒ Boolean, cbf: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Filter)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Filter
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, This]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Filter → Task

(defined at scala.collection.parallel.ParIterableLike.Filter)


### `def merge(that: Filter[U, This]): Unit`                                 ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Filter → Task

(defined at scala.collection.parallel.ParIterableLike.Filter)


### `def newSubtask(p: IterableSplitter[T]): Filter[U, This]`                ###

* Attributes
  * protected[this]
* Definition Classes
  * Filter → Accessor

(defined at scala.collection.parallel.ParIterableLike.Filter)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Filter → Accessor

(defined at scala.collection.parallel.ParIterableLike.Filter)


### `var result: Combiner[U, This]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Filter → Task

(defined at scala.collection.parallel.ParIterableLike.Filter)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Filter[U, This]`                                              ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Filter [U, This] to
    CollectionsHaveToParArray [Filter [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Filter [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
