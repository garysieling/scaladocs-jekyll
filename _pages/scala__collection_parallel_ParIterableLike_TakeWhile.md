
#             scala.collection.parallel.ParIterableLike#TakeWhile             #

```scala
class TakeWhile[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Boolean), TakeWhile[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = (Combiner[U, This], Boolean)`                             ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.TakeWhile
--------------------------------------------------------------------------------


### `new TakeWhile(pos: Int, pred: (T) ⇒ Boolean, cbf: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.TakeWhile
--------------------------------------------------------------------------------


### `def leaf(prev: Option[(Combiner[U, This], Boolean)]): Unit`             ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * TakeWhile → Task

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


### `def merge(that: TakeWhile[U, This]): Unit`                              ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * TakeWhile → Task

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * TakeWhile → Accessor

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * TakeWhile → Accessor

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


### `var result: (Combiner[U, This], Boolean)`                               ###

A result that can be accessed once the task is completed.

* Definition Classes
  * TakeWhile → Task

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


### `def split: scala.Seq[Task[(Combiner[U, This], Boolean), TakeWhile[U, This]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * TakeWhile → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.TakeWhile)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: TakeWhile[U, This]`                                           ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from TakeWhile [U, This] to
    CollectionsHaveToParArray [TakeWhile [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (TakeWhile [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
