
#                       scala.collection.parallel.Tasks                       #

```scala
trait Tasks extends AnyRef
```

A trait that declares task execution capabilities used by parallel collections.

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait WrappedTask[R, +Tp] extends AnyRef`                               ###

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.parallel.Tasks
--------------------------------------------------------------------------------


### `abstract def executeAndWaitResult[R, Tp](task: Task[R, Tp]): R`         ###

Executes a result task, waits for it to finish, then returns its result.
Forwards an exception if some task threw it.

(defined at scala.collection.parallel.Tasks)


### `abstract def execute[R, Tp](fjtask: Task[R, Tp]): () ⇒ R`               ###

Executes a task and returns a future. Forwards an exception if some task threw
it.

(defined at scala.collection.parallel.Tasks)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.parallel.Tasks
--------------------------------------------------------------------------------


### `abstract val environment: AnyRef`                                       ###

The type of the environment is more specific in the implementations.

(defined at scala.collection.parallel.Tasks)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Tasks to
    CollectionsHaveToParArray [Tasks, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Tasks) ⇒ GenTraversableOnce [T]
    is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
