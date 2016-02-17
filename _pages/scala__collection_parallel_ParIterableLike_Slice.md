
#               scala.collection.parallel.ParIterableLike#Slice               #

```scala
class Slice[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Slice[U, This]]
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
   Instance Constructors From scala.collection.parallel.ParIterableLike.Slice
--------------------------------------------------------------------------------


### `new Slice(from: Int, until: Int, cbf: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Slice)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Slice
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, This]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Slice → Task

(defined at scala.collection.parallel.ParIterableLike.Slice)


### `def merge(that: Slice[U, This]): Unit`                                  ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Slice → Task

(defined at scala.collection.parallel.ParIterableLike.Slice)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Slice → Accessor

(defined at scala.collection.parallel.ParIterableLike.Slice)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Slice → Accessor

(defined at scala.collection.parallel.ParIterableLike.Slice)


### `var result: Combiner[U, This]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Slice → Task

(defined at scala.collection.parallel.ParIterableLike.Slice)


### `def split: scala.Seq[Task[Combiner[U, This], Slice[U, This]]]`          ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Slice → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Slice)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Slice[U, This]`                                               ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Slice [U, This] to
    CollectionsHaveToParArray [Slice [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Slice [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
