
#               scala.collection.parallel.ParIterableLike#ZipAll               #

```scala
class ZipAll[U >: T, S, That] extends Transformer[Combiner[(U, S), That], ZipAll[U, S, That]]
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
  Instance Constructors From scala.collection.parallel.ParIterableLike.ZipAll
--------------------------------------------------------------------------------


### `new ZipAll(len: Int, thiselem: U, thatelem: S, pbf: CombinerFactory[(U, S), That], pit: IterableSplitter[T], othpit: SeqSplitter[S])` ###

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.ZipAll
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Result]): Unit`                                   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ZipAll → Task

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `def merge(that: ZipAll[U, S, That]): Unit`                              ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * ZipAll → Task

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * ZipAll → Accessor

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `val othpit: SeqSplitter[S]`                                             ###

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * ZipAll → Accessor

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `var result: Result`                                                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * ZipAll → Task

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


### `def split: scala.Seq[Task[Combiner[(U, S), That], ZipAll[U, S, That]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * ZipAll → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.ZipAll)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ZipAll[U, S, That]`                                           ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ZipAll [U, S, That] to
    CollectionsHaveToParArray [ZipAll [U, S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ZipAll [U, S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
