
#       scala.collection.parallel.AdaptiveWorkStealingTasks#WrappedTask       #

```scala
trait WrappedTask[R, Tp] extends AdaptiveWorkStealingTasks.WrappedTask[R, Tp]
```

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask
--------------------------------------------------------------------------------


### `abstract def split: scala.Seq[WrappedTask[R, Tp]]`                      ###

* Definition Classes
  * WrappedTask → WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask
--------------------------------------------------------------------------------


### `var next: WrappedTask[R, Tp]`                                           ###

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


### `def spawnSubtasks(): WrappedTask[R, Tp]`                                ###

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.parallel.Tasks.WrappedTask
--------------------------------------------------------------------------------


### `abstract val body: Task[R, Tp]`                                         ###

the body of this task - what it executes, how it gets split and how results are
merged.

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.Tasks.WrappedTask)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.parallel.Tasks.WrappedTask
--------------------------------------------------------------------------------


### `abstract def start(): Unit`                                             ###

Start task.

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.Tasks.WrappedTask)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedTask [R, Tp] to
    CollectionsHaveToParArray [WrappedTask [R, Tp], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (WrappedTask [R, Tp]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
