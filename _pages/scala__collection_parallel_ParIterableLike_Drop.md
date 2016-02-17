
#                scala.collection.parallel.ParIterableLike#Drop                #

```scala
class Drop[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Drop[U, This]]
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
   Instance Constructors From scala.collection.parallel.ParIterableLike.Drop
--------------------------------------------------------------------------------


### `new Drop(n: Int, cbf: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Drop)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Drop
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, This]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Drop → Task

(defined at scala.collection.parallel.ParIterableLike.Drop)


### `def merge(that: Drop[U, This]): Unit`                                   ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Drop → Task

(defined at scala.collection.parallel.ParIterableLike.Drop)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Drop → Accessor

(defined at scala.collection.parallel.ParIterableLike.Drop)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Drop → Accessor

(defined at scala.collection.parallel.ParIterableLike.Drop)


### `var result: Combiner[U, This]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Drop → Task

(defined at scala.collection.parallel.ParIterableLike.Drop)


### `def split: scala.Seq[Task[Combiner[U, This], Drop[U, This]]]`           ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Drop → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Drop)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Drop[U, This]`                                                ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Drop [U, This] to
    CollectionsHaveToParArray [Drop [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Drop [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
