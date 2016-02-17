
#               scala.collection.parallel.ParIterableLike#Reduce               #

```scala
class Reduce[U >: T] extends Accessor[Option[U], Reduce[U]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Option[U]`                                                ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Option[U], Reduce[U]]]`                       ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Reduce
--------------------------------------------------------------------------------


### `new Reduce(op: (U, U) ⇒ U, pit: IterableSplitter[T])`                   ###

(defined at scala.collection.parallel.ParIterableLike.Reduce)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Reduce
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[Option[U]]): Unit`                               ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Reduce → Task

(defined at scala.collection.parallel.ParIterableLike.Reduce)


### `def merge(that: Reduce[U]): Unit`                                       ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Reduce → Task

(defined at scala.collection.parallel.ParIterableLike.Reduce)


### `def newSubtask(p: IterableSplitter[T]): Reduce[U]`                      ###

* Attributes
  * protected[this]
* Definition Classes
  * Reduce → Accessor

(defined at scala.collection.parallel.ParIterableLike.Reduce)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Reduce → Accessor

(defined at scala.collection.parallel.ParIterableLike.Reduce)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Reduce[U]`                                                    ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Reduce [U] to
    CollectionsHaveToParArray [Reduce [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Reduce [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
