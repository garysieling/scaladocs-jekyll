
#   scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks#WrappedTask   #

```scala
class WrappedTask[R, Tp] extends RecursiveAction with AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp] with AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp]
```

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
              Value Members From java.util.concurrent.ForkJoinTask
--------------------------------------------------------------------------------


### `def cancel(arg0: Boolean): Boolean`                                     ###

* Definition Classes
  * ForkJoinTask → Future

(defined at java.util.concurrent.ForkJoinTask)


### `final def compareAndSetForkJoinTaskTag(arg0: Short, arg1: Short): Boolean` ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `def complete(arg0: Void): Unit`                                         ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `def completeExceptionally(arg0: java.lang.Throwable): Unit`             ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `final def fork(): ForkJoinTask[Void]`                                   ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `final def get(): Void`                                                  ###

* Definition Classes
  * ForkJoinTask → Future
* Annotations
  * @ throws (...) @ throws (...)

(defined at java.util.concurrent.ForkJoinTask)


### `final def get(arg0: Long, arg1: TimeUnit): Void`                        ###

* Definition Classes
  * ForkJoinTask → Future
* Annotations
  * @ throws (...) @ throws (...) @ throws (...)

(defined at java.util.concurrent.ForkJoinTask)


### `final def getException(): java.lang.Throwable`                          ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `final def invoke(): Void`                                               ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `final def join(): Void`                                                 ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


### `final def setForkJoinTaskTag(arg0: Short): Short`                       ###

* Definition Classes
  * ForkJoinTask

(defined at java.util.concurrent.ForkJoinTask)


--------------------------------------------------------------------------------
            Value Members From java.util.concurrent.RecursiveAction
--------------------------------------------------------------------------------


### `final def setRawResult(arg0: Void): Unit`                               ###

* Attributes
  * protected[java.util.concurrent]
* Definition Classes
  * RecursiveAction → ForkJoinTask

(defined at java.util.concurrent.RecursiveAction)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks.WrappedTask
--------------------------------------------------------------------------------


### `new WrappedTask(body: Task[R, Tp])`                                     ###

(defined at scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks.WrappedTask)


--------------------------------------------------------------------------------
Value Members From scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks.WrappedTask
--------------------------------------------------------------------------------


### `val body: Task[R, Tp]`                                                  ###

the body of this task - what it executes, how it gets split and how results are
merged.

* Definition Classes
  * WrappedTask → WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks.WrappedTask)


### `def split: scala.Seq[AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp]]` ###

* Definition Classes
  * WrappedTask → WrappedTask → WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingForkJoinTasks.WrappedTask)


--------------------------------------------------------------------------------
Value Members From scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask
--------------------------------------------------------------------------------


### `var next: AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp]`         ###

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


### `def spawnSubtasks(): AdaptiveWorkStealingForkJoinTasks.WrappedTask[R, Tp]` ###

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.AdaptiveWorkStealingTasks.WrappedTask)


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
