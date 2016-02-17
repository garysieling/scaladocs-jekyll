
#             scala.collection.parallel.ForkJoinTasks#WrappedTask             #

```scala
trait WrappedTask[R, +Tp] extends RecursiveAction with ForkJoinTasks.WrappedTask[R, Tp]
```

* Source
  * [Tasks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Tasks.scala#L1)


--------------------------------------------------------------------------------
         Concrete Value Members From java.util.concurrent.ForkJoinTask
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
        Concrete Value Members From java.util.concurrent.RecursiveAction
--------------------------------------------------------------------------------


### `final def setRawResult(arg0: Void): Unit`                               ###

* Attributes
  * protected[java.util.concurrent]
* Definition Classes
  * RecursiveAction → ForkJoinTask

(defined at java.util.concurrent.RecursiveAction)


--------------------------------------------------------------------------------
    Abstract Value Members From scala.collection.parallel.Tasks.WrappedTask
--------------------------------------------------------------------------------


### `abstract val body: Task[R, Tp]`                                         ###

the body of this task - what it executes, how it gets split and how results are
merged.

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.Tasks.WrappedTask)


### `abstract def split: scala.Seq[ForkJoinTasks.WrappedTask[R, Tp]]`        ###

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.Tasks.WrappedTask)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.parallel.Tasks.WrappedTask
--------------------------------------------------------------------------------


### `abstract def compute(): Unit`                                           ###

Code that gets called after the task gets started - it may spawn other tasks
instead of calling `leaf` .

* Definition Classes
  * WrappedTask

(defined at scala.collection.parallel.Tasks.WrappedTask)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
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
