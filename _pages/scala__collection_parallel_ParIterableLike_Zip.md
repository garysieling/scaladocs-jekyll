
#                scala.collection.parallel.ParIterableLike#Zip                #

```scala
class Zip[U >: T, S, That] extends Transformer[Combiner[(U, S), That], Zip[U, S, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[(U, S), That]`                                   ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.ParIterableLike.Zip
--------------------------------------------------------------------------------


### `new Zip(pbf: CombinerFactory[(U, S), That], pit: IterableSplitter[T], othpit: SeqSplitter[S])` ###

(defined at scala.collection.parallel.ParIterableLike.Zip)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.ParIterableLike.Zip
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Result]): Unit`                                   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `def merge(that: Zip[U, S, That]): Unit`                                 ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Zip → Accessor

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `val othpit: SeqSplitter[S]`                                             ###

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Zip → Accessor

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `var result: Result`                                                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParIterableLike.Zip)


### `def split: scala.Seq[Task[Combiner[(U, S), That], Zip[U, S, That]]]`    ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Zip → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Zip)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Zip[U, S, That]`                                              ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Zip [U, S, That] to
    CollectionsHaveToParArray [Zip [U, S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Zip [U, S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
