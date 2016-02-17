
#                scala.collection.parallel.ParIterableLike#Max                #

```scala
class Max[U >: T] extends Accessor[Option[U], Max[U]]
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


### `def split: scala.Seq[Task[Option[U], Max[U]]]`                          ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.parallel.ParIterableLike.Max
--------------------------------------------------------------------------------


### `new Max(ord: Ordering[U], pit: IterableSplitter[T])`                    ###

(defined at scala.collection.parallel.ParIterableLike.Max)


--------------------------------------------------------------------------------
        Value Members From scala.collection.parallel.ParIterableLike.Max
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[Option[U]]): Unit`                               ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Max → Task

(defined at scala.collection.parallel.ParIterableLike.Max)


### `def merge(that: Max[U]): Unit`                                          ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Max → Task

(defined at scala.collection.parallel.ParIterableLike.Max)


### `def newSubtask(p: IterableSplitter[T]): Max[U]`                         ###

* Attributes
  * protected[this]
* Definition Classes
  * Max → Accessor

(defined at scala.collection.parallel.ParIterableLike.Max)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Max → Accessor

(defined at scala.collection.parallel.ParIterableLike.Max)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Max[U]`                                                       ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Max [U] to
    CollectionsHaveToParArray [Max [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Max [U]) ⇒ GenTraversableOnce
    [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
