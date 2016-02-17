
#         scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks         #

```scala
trait AdaptiveWorkStealingForkJoinTasks extends ForkJoinTasks with AdaptiveWorkStealingTasks
```

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WrappedTask[R, Tp] extends RecursiveAction with AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp] with AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp]` ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks
--------------------------------------------------------------------------------


### `def newWrappedTask[R, Tp](b: Task[R, Tp]): WrappedTask[R, Tp]`          ###

* Definition Classes
  * AdaptiveWorkStealingForkJoinTasks → AdaptiveWorkStealingTasks →
    ForkJoinTasks

(defined at scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks)


--------------------------------------------------------------------------------
      Abstract Value Members From scala.collection.parallel.ForkJoinTasks
--------------------------------------------------------------------------------


### `abstract val environment: ForkJoinPool`                                 ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * ForkJoinTasks → Tasks

(defined at scala.collection.parallel.ForkJoinTasks)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.parallel.ForkJoinTasks
--------------------------------------------------------------------------------


### `def executeAndWaitResult[R, Tp](task: Task[R, Tp]): R`                  ###

Executes a task on a fork/join pool and waits for it to finish. Returns its
result when it does.

If the current thread is a fork/join worker thread, the task's `fork` method
will be invoked. Otherwise, the task will be executed on the fork/join pool.

* returns
  * the result of the task

* Definition Classes
  * ForkJoinTasks → Tasks

(defined at scala.collection.parallel.ForkJoinTasks)


### `def execute[R, Tp](task: Task[R, Tp]): () ⇒ R`                          ###

Executes a task and does not wait for it to finish - instead returns a future.

If the current thread is a fork/join worker thread, the task's `fork` method
will be invoked. Otherwise, the task will be executed on the fork/join pool.

* Definition Classes
  * ForkJoinTasks → Tasks

(defined at scala.collection.parallel.ForkJoinTasks)


### `def forkJoinPool: ForkJoinPool`                                         ###

The fork/join pool of this collection.

* Definition Classes
  * ForkJoinTasks → HavingForkJoinPool

(defined at scala.collection.parallel.ForkJoinTasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    AdaptiveWorkStealingForkJoinTasks to CollectionsHaveToParArray [
    AdaptiveWorkStealingForkJoinTasks, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (
    AdaptiveWorkStealingForkJoinTasks) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
