
#           scala.collection.parallel.ParIterableLike#CreateScanTree           #

```scala
class CreateScanTree[U >: T] extends Transformer[ScanTree[U], CreateScanTree[U]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = ScanTree[U]`                                              ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.CreateScanTree
--------------------------------------------------------------------------------


### `new CreateScanTree(from: Int, len: Int, z: U, op: (U, U) ⇒ U, pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


--------------------------------------------------------------------------------
  Value Members From scala.collection.parallel.ParIterableLike.CreateScanTree
--------------------------------------------------------------------------------


### `def leaf(prev: Option[ScanTree[U]]): Unit`                              ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * CreateScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


### `def merge(that: CreateScanTree[U]): Unit`                               ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * CreateScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


### `def newSubtask(pit: IterableSplitter[T]): Nothing`                      ###

* Attributes
  * protected[this]
* Definition Classes
  * CreateScanTree → Accessor

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * CreateScanTree → Accessor

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


### `var result: ScanTree[U]`                                                ###

A result that can be accessed once the task is completed.

* Definition Classes
  * CreateScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


### `def split: scala.Seq[Task[ScanTree[U], CreateScanTree[U]]]`             ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * CreateScanTree → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.CreateScanTree)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: CreateScanTree[U]`                                            ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CreateScanTree [U] to
    CollectionsHaveToParArray [CreateScanTree [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (CreateScanTree [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
