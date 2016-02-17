
#                scala.collection.parallel.ParIterableLike#Map                #

```scala
class Map[S, That] extends Transformer[Combiner[S, That], Map[S, That]]
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


### `def split: scala.Seq[Task[Combiner[S, That], Map[S, That]]]`            ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.ParIterableLike.Map
--------------------------------------------------------------------------------


### `new Map(f: (T) ⇒ S, cbf: CombinerFactory[S, That], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Map)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.ParIterableLike.Map
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[S, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Map → Task

(defined at scala.collection.parallel.ParIterableLike.Map)


### `def merge(that: Map[S, That]): Unit`                                    ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Map → Task

(defined at scala.collection.parallel.ParIterableLike.Map)


### `def newSubtask(p: IterableSplitter[T]): Map[S, That]`                   ###

* Attributes
  * protected[this]
* Definition Classes
  * Map → Accessor

(defined at scala.collection.parallel.ParIterableLike.Map)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Map → Accessor

(defined at scala.collection.parallel.ParIterableLike.Map)


### `var result: Combiner[S, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Map → Task

(defined at scala.collection.parallel.ParIterableLike.Map)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Map[S, That]`                                                 ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Map [S, That] to
    CollectionsHaveToParArray [Map [S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Map [S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
