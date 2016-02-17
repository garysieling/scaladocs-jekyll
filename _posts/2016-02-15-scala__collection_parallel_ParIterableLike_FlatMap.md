
#              scala.collection.parallel.ParIterableLike#FlatMap              #

```scala
class FlatMap[S, That] extends Transformer[Combiner[S, That], FlatMap[S, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[S, That]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[S, That], FlatMap[S, That]]]`        ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.FlatMap
--------------------------------------------------------------------------------


### `new FlatMap(f: (T) ⇒ GenTraversableOnce[S], pbf: CombinerFactory[S, That], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.FlatMap
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[S, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * FlatMap → Task

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


### `def merge(that: FlatMap[S, That]): Unit`                                ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * FlatMap → Task

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


### `def newSubtask(p: IterableSplitter[T]): FlatMap[S, That]`               ###

* Attributes
  * protected[this]
* Definition Classes
  * FlatMap → Accessor

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * FlatMap → Accessor

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


### `var result: Combiner[S, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * FlatMap → Task

(defined at scala.collection.parallel.ParIterableLike.FlatMap)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: FlatMap[S, That]`                                             ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from FlatMap [S, That] to
    CollectionsHaveToParArray [FlatMap [S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (FlatMap [S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
