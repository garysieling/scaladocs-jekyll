
#                scala.collection.parallel.ParIterableLike#Take                #

```scala
class Take[U >: T, This >: Repr] extends Transformer[Combiner[U, This], Take[U, This]]
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
   Instance Constructors From scala.collection.parallel.ParIterableLike.Take
--------------------------------------------------------------------------------


### `new Take(n: Int, cbf: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Take)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Take
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, This]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Take → Task

(defined at scala.collection.parallel.ParIterableLike.Take)


### `def merge(that: Take[U, This]): Unit`                                   ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Take → Task

(defined at scala.collection.parallel.ParIterableLike.Take)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Take → Accessor

(defined at scala.collection.parallel.ParIterableLike.Take)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Take → Accessor

(defined at scala.collection.parallel.ParIterableLike.Take)


### `var result: Combiner[U, This]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Take → Task

(defined at scala.collection.parallel.ParIterableLike.Take)


### `def split: scala.Seq[Task[Combiner[U, This], Take[U, This]]]`           ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Take → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Take)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Take[U, This]`                                                ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Take [U, This] to
    CollectionsHaveToParArray [Take [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Take [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
