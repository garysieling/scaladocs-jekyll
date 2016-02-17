
#            scala.collection.parallel.ParIterableLike#FromScanTree            #

```scala
class FromScanTree[U >: T, That] extends StrictSplitterCheckTask[Combiner[U, That], FromScanTree[U, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[U, That]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.FromScanTree
--------------------------------------------------------------------------------


### `new FromScanTree(tree: ScanTree[U], z: U, op: (U, U) ⇒ U, cbf: CombinerFactory[U, That])` ###

(defined at scala.collection.parallel.ParIterableLike.FromScanTree)


--------------------------------------------------------------------------------
   Value Members From scala.collection.parallel.ParIterableLike.FromScanTree
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * FromScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.FromScanTree)


### `def merge(that: FromScanTree[U, That]): Unit`                           ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * FromScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.FromScanTree)


### `var result: Combiner[U, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * FromScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.FromScanTree)


### `def split: scala.Seq[Task[Combiner[U, That], FromScanTree[U, That]]]`   ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * FromScanTree → Task

(defined at scala.collection.parallel.ParIterableLike.FromScanTree)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: FromScanTree[U, That]`                                        ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from FromScanTree [U, That]
    to CollectionsHaveToParArray [FromScanTree [U, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (FromScanTree [U, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
