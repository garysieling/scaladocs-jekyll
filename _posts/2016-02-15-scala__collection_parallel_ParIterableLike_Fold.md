
#                scala.collection.parallel.ParIterableLike#Fold                #

```scala
class Fold[U >: T] extends Accessor[U, Fold[U]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = U`                                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[U, Fold[U]]]`                                 ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.ParIterableLike.Fold
--------------------------------------------------------------------------------


### `new Fold(z: U, op: (U, U) ⇒ U, pit: IterableSplitter[T])`               ###

(defined at scala.collection.parallel.ParIterableLike.Fold)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Fold
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[U]): Unit`                                       ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Fold → Task

(defined at scala.collection.parallel.ParIterableLike.Fold)


### `def merge(that: Fold[U]): Unit`                                         ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Fold → Task

(defined at scala.collection.parallel.ParIterableLike.Fold)


### `def newSubtask(p: IterableSplitter[T]): Fold[U]`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Fold → Accessor

(defined at scala.collection.parallel.ParIterableLike.Fold)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Fold → Accessor

(defined at scala.collection.parallel.ParIterableLike.Fold)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Fold[U]`                                                      ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Fold [U] to
    CollectionsHaveToParArray [Fold [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Fold [U]) ⇒ GenTraversableOnce
    [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
