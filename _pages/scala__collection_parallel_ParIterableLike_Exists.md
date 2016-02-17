
#               scala.collection.parallel.ParIterableLike#Exists               #

```scala
class Exists extends Accessor[Boolean, Exists]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Boolean`                                                  ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Boolean, Exists]]`                            ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Exists
--------------------------------------------------------------------------------


### `new Exists(pred: (T) ⇒ Boolean, pit: IterableSplitter[T])`              ###

(defined at scala.collection.parallel.ParIterableLike.Exists)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Exists
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Boolean]): Unit`                                  ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Exists → Task

(defined at scala.collection.parallel.ParIterableLike.Exists)


### `def merge(that: Exists): Unit`                                          ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Exists → Task

(defined at scala.collection.parallel.ParIterableLike.Exists)


### `def newSubtask(p: IterableSplitter[T]): Exists`                         ###

* Attributes
  * protected[this]
* Definition Classes
  * Exists → Accessor

(defined at scala.collection.parallel.ParIterableLike.Exists)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Exists → Accessor

(defined at scala.collection.parallel.ParIterableLike.Exists)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Exists`                                                       ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Exists to
    CollectionsHaveToParArray [Exists, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Exists) ⇒ GenTraversableOnce [
    T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
