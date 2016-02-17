
#                            scala.concurrent.Await                            #

```scala
object Await
```

 `Await` is what is used to ensure proper handling of blocking for `Awaitable`
instances.

While occasionally useful, e.g. for testing, it is recommended that you avoid
Await when possible in favor of callbacks and combinators like onComplete and
use in for comprehensions. Await will block the thread on which it runs, and
could cause performance and deadlock issues.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From scala.concurrent.Await
--------------------------------------------------------------------------------


### `def ready[T](awaitable: Awaitable[T], atMost: Duration): awaitable.type` ###

Await the "completed" state of an `Awaitable` .

Although this method is blocking, the internal use of blocking ensures that the
underlying ExecutionContext is prepared to properly manage the blocking.

* awaitable
  * the `Awaitable` to be awaited
* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * the `awaitable`

* Annotations
  * @ throws (clazz = classOf[TimeoutException]) @ throws (clazz =
    classOf[InterruptedException])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time this `Awaitable` is
    still not ready

(defined at scala.concurrent.Await)


### `def result[T](awaitable: Awaitable[T], atMost: Duration): T`            ###

Await and return the result (of type `T` ) of an `Awaitable` .

Although this method is blocking, the internal use of blocking ensures that the
underlying ExecutionContext to properly detect blocking and ensure that there
are no deadlocks.

* awaitable
  * the `Awaitable` to be awaited
* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * the result value if `awaitable` is completed within the specific maximum
    wait time

* Annotations
  * @ throws (clazz = classOf[Exception])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time `awaitable` is
    still not ready
(defined at scala.concurrent.Await)
