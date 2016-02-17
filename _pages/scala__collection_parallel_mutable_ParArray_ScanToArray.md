
#            scala.collection.parallel.mutable.ParArray#ScanToArray            #

```scala
class ScanToArray[U >: T] extends Task[Unit, ScanToArray[U]]
```

* Source
  * [ParArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParArray.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Unit`                                                     ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ScanToArray[U]`                                               ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.mutable.ParArray.ScanToArray
--------------------------------------------------------------------------------


### `new ScanToArray(tree: ParArray.ScanTree[U], z: U, op: (U, U) ⇒ U, targetarr: Array[Any])` ###

(defined at scala.collection.parallel.mutable.ParArray.ScanToArray)


--------------------------------------------------------------------------------
   Value Members From scala.collection.parallel.mutable.ParArray.ScanToArray
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Unit]): Unit`                                     ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ScanToArray → Task

(defined at scala.collection.parallel.mutable.ParArray.ScanToArray)


### `def split: scala.Seq[Task[Unit, ScanToArray[U]]]`                       ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * ScanToArray → Task

(defined at scala.collection.parallel.mutable.ParArray.ScanToArray)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ScanToArray [U] to
    CollectionsHaveToParArray [ScanToArray [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ScanToArray [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
