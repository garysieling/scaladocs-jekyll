
#                  scala.collection.parallel.ThreadPoolTasks                  #

```scala
trait ThreadPoolTasks extends Tasks
```

An implementation of tasks objects based on the Java thread pooling API.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ForkJoinTasks` instead.
* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, +Tp] extends Runnable with ThreadPoolTasks.WrappedTask[R, Tp]` ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.parallel.ThreadPoolTasks
--------------------------------------------------------------------------------


### `abstract val environment: ThreadPoolExecutor`                           ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * ThreadPoolTasks → Tasks

(defined at scala.collection.parallel.ThreadPoolTasks)


### `abstract def newWrappedTask[R, Tp](b: Task[R, Tp]): WrappedTask[R, Tp]` ###

* Attributes
  * protected

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

(defined at scala.collection.parallel.ThreadPoolTasks)


### `def queue: LinkedBlockingQueue[Runnable]`                               ###

(defined at scala.collection.parallel.ThreadPoolTasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ThreadPoolTasks to
    CollectionsHaveToParArray [ThreadPoolTasks, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ThreadPoolTasks) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
