
#  scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks#WrappedTask  #

```scala
class WrappedTask[R, Tp] extends AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp] with AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp]
```

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
Value Members From scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask
--------------------------------------------------------------------------------


### `var next: AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp]`       ###

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


### `def spawnSubtasks(): AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp]` ###

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks.WrappedTask
--------------------------------------------------------------------------------


### `new WrappedTask(body: Task[R, Tp])`                                     ###

(defined at scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks.WrappedTask)


--------------------------------------------------------------------------------
Value Members From scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks.WrappedTask
--------------------------------------------------------------------------------


### `val body: Task[R, Tp]`                                                  ###

the body of this task - what it executes, how it gets split and how results are
merged.

* Definition Classes
  * WrappedTask → WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks.WrappedTask)


### `def split: scala.Seq[AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp]]` ###

* Definition Classes
  * WrappedTask → WrappedTask → WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks.WrappedTask)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
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
