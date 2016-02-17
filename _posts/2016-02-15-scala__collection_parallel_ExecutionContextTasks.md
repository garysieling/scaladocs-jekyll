
#               scala.collection.parallel.ExecutionContextTasks               #

```scala
trait ExecutionContextTasks extends Tasks
```

This tasks implementation uses execution contexts to spawn a parallel
computation.

As an optimization, it internally checks whether the execution context is the
standard implementation based on fork/join pools, and if it is, creates a
 `ForkJoinTaskSupport` that shares the same pool to forward its request to it.

Otherwise, it uses an execution context exclusive `Tasks` implementation to
divide the tasks into smaller chunks and execute operations on it.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, +Tp] extends AnyRef`                               ###

* Definition Classes
  * Tasks


--------------------------------------------------------------------------------
  Abstract Value Members From scala.collection.parallel.ExecutionContextTasks
--------------------------------------------------------------------------------


### `abstract val environment: ExecutionContext`                             ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * ExecutionContextTasks → Tasks

(defined at scala.collection.parallel.ExecutionContextTasks)


--------------------------------------------------------------------------------
  Concrete Value Members From scala.collection.parallel.ExecutionContextTasks
--------------------------------------------------------------------------------


### `def executeAndWaitResult[R, Tp](task: Task[R, Tp]): R`                  ###

Executes a result task, waits for it to finish, then returns its result.
Forwards an exception if some task threw it.

* Definition Classes
  * ExecutionContextTasks → Tasks

(defined at scala.collection.parallel.ExecutionContextTasks)


### `def execute[R, Tp](task: Task[R, Tp]): () ⇒ R`                          ###

Executes a task and returns a future. Forwards an exception if some task threw
it.

* Definition Classes
  * ExecutionContextTasks → Tasks

(defined at scala.collection.parallel.ExecutionContextTasks)


### `def executionContext: ExecutionContext`                                 ###

(defined at scala.collection.parallel.ExecutionContextTasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ExecutionContextTasks to
    CollectionsHaveToParArray [ExecutionContextTasks, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ExecutionContextTasks) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
