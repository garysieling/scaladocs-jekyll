
#                           scala.concurrent.Promise                           #

```scala
trait Promise[T] extends AnyRef
```

Promise is an object which can be completed with a value or failed with an
exception.

* Source
  * [Promise.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Promise.scala#L1)


--------------------------------------------------------------------------------
              Abstract Value Members From scala.concurrent.Promise
--------------------------------------------------------------------------------


### `abstract def future: Future[T]`                                         ###

Future containing the value of this promise.

(defined at scala.concurrent.Promise)


### `abstract def tryComplete(result: Try[T]): Boolean`                      ###

Tries to complete the promise with either a value or the exception.

Note: Using this method may result in non-deterministic concurrent programs.

* returns
  * If the promise has already been completed returns `false` , or `true`
    otherwise.

(defined at scala.concurrent.Promise)


--------------------------------------------------------------------------------
              Concrete Value Members From scala.concurrent.Promise
--------------------------------------------------------------------------------


### `abstract def isCompleted: Boolean`                                      ###

Returns whether the promise has already been completed with a value or an
exception.

Note: Using this method may result in non-deterministic concurrent programs.

* returns
  * `true` if the promise is already completed, `false` otherwise

(defined at scala.concurrent.Promise)


### `def complete(result: Try[T]): Promise.this.type`                        ###

Completes the promise with either an exception or a value.

* result
  * Either the value or the exception to complete the promise with. If the
    promise has already been fulfilled, failed or has timed out, calling this
    method will throw an IllegalStateException.

(defined at scala.concurrent.Promise)


### `final def completeWith(other: Future[T]): Promise.this.type`            ###

Completes this promise with the specified future, once that future is completed.

* returns
  * This promise

(defined at scala.concurrent.Promise)


### `def failure(cause: Throwable): Promise.this.type`                       ###

Completes the promise with an exception.

* cause
  * The throwable to complete the promise with. If the throwable used to fail
    this promise is an error, a control exception or an interrupted exception,
    it will be wrapped as a cause within an `ExecutionException` which will fail
    the promise. If the promise has already been fulfilled, failed or has timed
    out, calling this method will throw an IllegalStateException.

(defined at scala.concurrent.Promise)


### `def success(value: T): Promise.this.type`                               ###

Completes the promise with a value.

* value
  * The value to complete the promise with. If the promise has already been
    fulfilled, failed or has timed out, calling this method will throw an
    IllegalStateException.

(defined at scala.concurrent.Promise)


### `final def tryCompleteWith(other: Future[T]): Promise.this.type`         ###

Attempts to complete this promise with the specified future, once that future is
completed.

* returns
  * This promise

(defined at scala.concurrent.Promise)


### `def tryFailure(cause: Throwable): Boolean`                              ###

Tries to complete the promise with an exception.

Note: Using this method may result in non-deterministic concurrent programs.

* returns
  * If the promise has already been completed returns `false` , or `true`
    otherwise.

(defined at scala.concurrent.Promise)


### `def trySuccess(value: T): Boolean`                                      ###

Tries to complete the promise with a value.

Note: Using this method may result in non-deterministic concurrent programs.

* returns
  * If the promise has already been completed returns `false` , or `true`
    otherwise.
(defined at scala.concurrent.Promise)
