
#                          scala.concurrent.Awaitable                          #

```scala
trait Awaitable[+T] extends AnyRef
```

An object that may eventually be completed with a result value of type `T` which
may be awaited using blocking methods.

The Await object provides methods that allow accessing the result of an
 `Awaitable` by blocking the current thread until the `Awaitable` has been
completed or a timeout has occurred.

* Source
  * [Awaitable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Awaitable.scala#L1)


--------------------------------------------------------------------------------
             Abstract Value Members From scala.concurrent.Awaitable
--------------------------------------------------------------------------------


### `abstract def ready(atMost: Duration)(implicit permit: CanAwait): Awaitable.this.type` ###

Await the "completed" state of this `Awaitable` .

 * _This method should not be called directly; use Await.ready instead._*

* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * this `Awaitable`

* Annotations
  * @ throws (clazz = classOf[TimeoutException]) @ throws (clazz =
    classOf[InterruptedException])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time this `Awaitable` is
    still not ready

(defined at scala.concurrent.Awaitable)


### `abstract def result(atMost: Duration)(implicit permit: CanAwait): T`    ###

Await and return the result (of type `T` ) of this `Awaitable` .

 * _This method should not be called directly; use Await.result instead._*

* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * the result value if the `Awaitable` is completed within the specific maximum
    wait time

* Annotations
  * @ throws (clazz = classOf[Exception])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time this `Awaitable` is
    still not ready
(defined at scala.concurrent.Awaitable)
