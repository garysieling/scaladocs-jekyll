
#              scala.collection.parallel.mutable.ParTrieMap#Size              #

```scala
class Size extends Task[Int, Size]
```

Computes TrieMap size in parallel.

* Source
  * [ParTrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParTrieMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Int`                                                      ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Size`                                                         ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.mutable.ParTrieMap.Size
--------------------------------------------------------------------------------


### `new Size(offset: Int, howmany: Int, array: Array[BasicNode])`           ###

(defined at scala.collection.parallel.mutable.ParTrieMap.Size)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.mutable.ParTrieMap.Size
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Int]): Unit`                                      ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Size → Task

(defined at scala.collection.parallel.mutable.ParTrieMap.Size)


### `def merge(that: Size): Unit`                                            ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Size → Task

(defined at scala.collection.parallel.mutable.ParTrieMap.Size)


### `def split: Seq[Size]`                                                   ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Size → Task

(defined at scala.collection.parallel.mutable.ParTrieMap.Size)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Size to
    CollectionsHaveToParArray [Size, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Size) ⇒ GenTraversableOnce [T]
    is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
