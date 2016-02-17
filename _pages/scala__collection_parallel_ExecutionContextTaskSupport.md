
#            scala.collection.parallel.ExecutionContextTaskSupport            #

```scala
class ExecutionContextTaskSupport extends TaskSupport with ExecutionContextTasks
```

A task support that uses an execution context to schedule tasks.

It can be used with the default execution context implementation in the
 `scala.concurrent` package. It internally forwards the call to either a
forkjoin based task support or a thread pool executor one, depending on what the
execution context uses.

By default, parallel collections are parametrized with this task support object,
so parallel collections share the same execution context backend as the rest of
the `scala.concurrent` package.

* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * scala.collection.parallel.TaskSupport for more information.


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, +Tp] extends AnyRef`                               ###

* Definition Classes
  * Tasks


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ExecutionContextTaskSupport
--------------------------------------------------------------------------------


### `new ExecutionContextTaskSupport(environment: ExecutionContext = ...)`   ###

(defined at scala.collection.parallel.ExecutionContextTaskSupport)


--------------------------------------------------------------------------------
    Value Members From scala.collection.parallel.ExecutionContextTaskSupport
--------------------------------------------------------------------------------


### `val environment: ExecutionContext`                                      ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * ExecutionContextTaskSupport → ExecutionContextTasks → Tasks

(defined at scala.collection.parallel.ExecutionContextTaskSupport)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ExecutionContextTasks
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

* Definition Classes
  * ExecutionContextTasks

(defined at scala.collection.parallel.ExecutionContextTasks)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from
    ExecutionContextTaskSupport to CollectionsHaveToParArray [
    ExecutionContextTaskSupport, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ExecutionContextTaskSupport) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
