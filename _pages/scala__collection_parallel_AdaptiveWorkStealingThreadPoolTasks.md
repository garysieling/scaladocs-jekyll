
#        scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks        #

```scala
trait AdaptiveWorkStealingThreadPoolTasks extends ThreadPoolTasks with AdaptiveWorkStealingTasks
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `AdaptiveWorkStealingForkJoinTasks` instead.
* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WrappedTask[R, Tp] extends AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp] with AdaptiveWorkStealingThreadPoolTasks.WrappedTask[R, Tp]` ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks
--------------------------------------------------------------------------------


### `def newWrappedTask[R, Tp](b: Task[R, Tp]): WrappedTask[R, Tp]`          ###

* Definition Classes
  * AdaptiveWorkStealingThreadPoolTasks → AdaptiveWorkStealingTasks →
    ThreadPoolTasks

(defined at scala.collection.parallel.AdaptiveWorkStealingThreadPoolTasks)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.parallel.ThreadPoolTasks
--------------------------------------------------------------------------------


### `abstract val environment: ThreadPoolExecutor`                           ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * ThreadPoolTasks → Tasks

(defined at scala.collection.parallel.ThreadPoolTasks)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.parallel.ThreadPoolTasks
--------------------------------------------------------------------------------


### `def executeAndWaitResult[R, Tp](task: Task[R, Tp]): R`                  ###

Executes a result task, waits for it to finish, then returns its result.
Forwards an exception if some task threw it.

* Definition Classes
  * ThreadPoolTasks → Tasks

(defined at scala.collection.parallel.ThreadPoolTasks)


### `def execute[R, Tp](task: Task[R, Tp]): () ⇒ R`                          ###

Executes a task and returns a future. Forwards an exception if some task threw
it.

* Definition Classes
  * ThreadPoolTasks → Tasks

(defined at scala.collection.parallel.ThreadPoolTasks)


### `def executor: ThreadPoolExecutor`                                       ###

* Definition Classes
  * ThreadPoolTasks

(defined at scala.collection.parallel.ThreadPoolTasks)


### `def queue: LinkedBlockingQueue[Runnable]`                               ###

* Definition Classes
  * ThreadPoolTasks

(defined at scala.collection.parallel.ThreadPoolTasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    AdaptiveWorkStealingThreadPoolTasks to CollectionsHaveToParArray [
    AdaptiveWorkStealingThreadPoolTasks, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (
    AdaptiveWorkStealingThreadPoolTasks) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
