
#               scala.collection.parallel.ParIterableLike#Forall               #

```scala
class Forall extends Accessor[Boolean, Forall]
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


### `def split: scala.Seq[Task[Boolean, Forall]]`                            ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Forall
--------------------------------------------------------------------------------


### `new Forall(pred: (T) ⇒ Boolean, pit: IterableSplitter[T])`              ###

(defined at scala.collection.parallel.ParIterableLike.Forall)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Forall
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Boolean]): Unit`                                  ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Forall → Task

(defined at scala.collection.parallel.ParIterableLike.Forall)


### `def merge(that: Forall): Unit`                                          ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Forall → Task

(defined at scala.collection.parallel.ParIterableLike.Forall)


### `def newSubtask(p: IterableSplitter[T]): Forall`                         ###

* Attributes
  * protected[this]
* Definition Classes
  * Forall → Accessor

(defined at scala.collection.parallel.ParIterableLike.Forall)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Forall → Accessor

(defined at scala.collection.parallel.ParIterableLike.Forall)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Forall`                                                       ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Forall to
    CollectionsHaveToParArray [Forall, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Forall) ⇒ GenTraversableOnce [
    T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
