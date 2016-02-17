
#             scala.collection.parallel.AdaptiveWorkStealingTasks             #

```scala
trait AdaptiveWorkStealingTasks extends Tasks
```

This trait implements scheduling by employing an adaptive work stealing
technique.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, Tp] extends AdaptiveWorkStealingTasks.WrappedTask[R, Tp]` ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.AdaptiveWorkStealingTasks
--------------------------------------------------------------------------------


### `abstract def newWrappedTask[R, Tp](b: Task[R, Tp]): WrappedTask[R, Tp]` ###

* Attributes
  * protected

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks)


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
  * This member is added by an implicit conversion from
    AdaptiveWorkStealingTasks to CollectionsHaveToParArray [
    AdaptiveWorkStealingTasks, T] performed by method CollectionsHaveToParArray
    in scala.collection.parallel. This conversion will take place only if an
    implicit value of type (AdaptiveWorkStealingTasks) ⇒ GenTraversableOnce [T]
    is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
