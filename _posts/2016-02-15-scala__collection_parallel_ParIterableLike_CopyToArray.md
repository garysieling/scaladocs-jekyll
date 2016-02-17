
#            scala.collection.parallel.ParIterableLike#CopyToArray            #

```scala
class CopyToArray[U >: T, This >: Repr] extends Accessor[Unit, CopyToArray[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Unit`                                                     ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.CopyToArray
--------------------------------------------------------------------------------


### `new CopyToArray(from: Int, len: Int, array: Array[U], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.CopyToArray)


--------------------------------------------------------------------------------
    Value Members From scala.collection.parallel.ParIterableLike.CopyToArray
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Unit]): Unit`                                     ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * CopyToArray → Task

(defined at scala.collection.parallel.ParIterableLike.CopyToArray)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * CopyToArray → Accessor

(defined at scala.collection.parallel.ParIterableLike.CopyToArray)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * CopyToArray → Accessor

(defined at scala.collection.parallel.ParIterableLike.CopyToArray)


### `def split: scala.Seq[Task[Unit, CopyToArray[U, This]]]`                 ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * CopyToArray → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.CopyToArray)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: CopyToArray[U, This]`                                         ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CopyToArray [U, This] to
    CollectionsHaveToParArray [CopyToArray [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (CopyToArray [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
