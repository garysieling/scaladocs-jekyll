
#                    scala.collection.parallel.TaskSupport                    #

```scala
trait TaskSupport extends Tasks
```

A trait implementing the scheduling of a parallel collection operation.

Parallel collections are modular in the way operations are scheduled. Each
parallel collection is parametrized with a task support object which is
responsible for scheduling and load-balancing tasks to processors.

A task support object can be changed in a parallel collection after it has been
created, but only during a quiescent period, i.e. while there are no concurrent
invocations to parallel collection methods.

There are currently a few task support implementations available for parallel
collections. The scala.collection.parallel.ForkJoinTaskSupport uses a fork-join
pool internally.

The scala.collection.parallel.ExecutionContextTaskSupport uses the default
execution context implementation found in scala.concurrent, and it reuses the
thread pool used in scala.concurrent.

The execution context task support is set to each parallel collection by
default, so parallel collections reuse the same fork-join pool as the future
API.

Here is a way to change the task support of a parallel collection:

```scala
import scala.collection.parallel._
val pc = mutable.ParArray(1, 2, 3)
pc.tasksupport = new ForkJoinTaskSupport(
  new java.util.concurrent.ForkJoinPool(2))
```

* Source
  * [TaskSupport.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/TaskSupport.scala#L1)
* See also
  * [Configuring Parallel Collections](http://docs.scala-lang.org/overviews/parallel-collections/configuration.html)
    section on the parallel collection's guide for more information.


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, +Tp] extends AnyRef`                               ###

* Definition Classes
  * Tasks


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.parallel.Tasks
--------------------------------------------------------------------------------


### `abstract def executeAndWaitResult[R, Tp](task: Task[R, Tp]): R`         ###

Executes a result task, waits for it to finish, then returns its result.
Forwards an exception if some task threw it.

* Definition Classes
  * Tasks

(defined at scala.collection.parallel.Tasks)


### `abstract def execute[R, Tp](fjtask: Task[R, Tp]): () ⇒ R`               ###

Executes a task and returns a future. Forwards an exception if some task threw
it.

* Definition Classes
  * Tasks

(defined at scala.collection.parallel.Tasks)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.parallel.Tasks
--------------------------------------------------------------------------------


### `abstract val environment: AnyRef`                                       ###

The type of the environment is more specific in the implementations.

* Definition Classes
  * Tasks

(defined at scala.collection.parallel.Tasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from TaskSupport to
    CollectionsHaveToParArray [TaskSupport, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (TaskSupport) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
