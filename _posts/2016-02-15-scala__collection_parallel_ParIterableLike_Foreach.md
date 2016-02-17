
#              scala.collection.parallel.ParIterableLike#Foreach              #

```scala
class Foreach[S] extends Accessor[Unit, Foreach[S]]
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
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Unit, Foreach[S]]]`                           ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Foreach
--------------------------------------------------------------------------------


### `new Foreach(op: (T) ⇒ S, pit: IterableSplitter[T])`                     ###

(defined at scala.collection.parallel.ParIterableLike.Foreach)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Foreach
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[Unit]): Unit`                                    ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Foreach → Task

(defined at scala.collection.parallel.ParIterableLike.Foreach)


### `def newSubtask(p: IterableSplitter[T]): Foreach[S]`                     ###

* Attributes
  * protected[this]
* Definition Classes
  * Foreach → Accessor

(defined at scala.collection.parallel.ParIterableLike.Foreach)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Foreach → Accessor

(defined at scala.collection.parallel.ParIterableLike.Foreach)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Foreach[S]`                                                   ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Foreach [S] to
    CollectionsHaveToParArray [Foreach [S], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Foreach [S]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
