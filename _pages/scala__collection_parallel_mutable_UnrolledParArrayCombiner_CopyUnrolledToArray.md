
# scala.collection.parallel.mutable.UnrolledParArrayCombiner#CopyUnrolledToArray #

```scala
class CopyUnrolledToArray extends Task[Unit, CopyUnrolledToArray]
```

* Source
  * [UnrolledParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/UnrolledParArrayCombiner.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Unit`                                                     ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: CopyUnrolledToArray`                                          ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.mutable.UnrolledParArrayCombiner.CopyUnrolledToArray
--------------------------------------------------------------------------------


### `new CopyUnrolledToArray(array: Array[Any], offset: Int, howmany: Int)`  ###

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner.CopyUnrolledToArray)


--------------------------------------------------------------------------------
Value Members From scala.collection.parallel.mutable.UnrolledParArrayCombiner.CopyUnrolledToArray
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Unit]): Unit`                                     ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * CopyUnrolledToArray → Task

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner.CopyUnrolledToArray)


### `def split: immutable.List[CopyUnrolledToArray]`                         ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * CopyUnrolledToArray → Task

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner.CopyUnrolledToArray)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CopyUnrolledToArray to
    CollectionsHaveToParArray [CopyUnrolledToArray, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (CopyUnrolledToArray) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
