
#                        scala.concurrent.Future.never                        #

```scala
object never extends Future[Nothing]
```

A Future which is never completed.

* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From scala.concurrent.Future
--------------------------------------------------------------------------------


### `final def withFilter(p: (Nothing) ⇒ Boolean)(implicit executor: ExecutionContext): Future[Nothing]` ###

Used by for-comprehensions.

* Definition Classes
  * Future

(defined at scala.concurrent.Future)


--------------------------------------------------------------------------------
                Value Members From scala.concurrent.Future.never
--------------------------------------------------------------------------------


### `def andThen[U](pf: PartialFunction[Try[Nothing], U])(implicit executor: ExecutionContext): Future[Nothing]` ###

Applies the side-effecting function to the result of this future, and returns a
new future with the result of this future.

This method allows one to enforce that the callbacks are executed in a specified
order.

Note that if one of the chained `andThen` callbacks throws an exception, that
exception is not propagated to the subsequent `andThen` callbacks. Instead, the
subsequent `andThen` callbacks are given the original value of this future.

The following example prints out `5` :

```scala
val f = Future { 5 }
f andThen {
  case r => sys.error("runtime exception")
} andThen {
  case Failure(t) => println(t)
  case Success(v) => println(v)
}
```

* U
  * only used to accept any return type of the given `PartialFunction`
* pf
  * a `PartialFunction` which will be conditionally applied to the outcome of
    this `Future`
* returns
  * a `Future` which will be completed with the exact same outcome as this
     `Future` but after the `PartialFunction` has been executed.

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def collect[S](pf: PartialFunction[Nothing, S])(implicit executor: ExecutionContext): Future[S]` ###

Creates a new future by mapping the value of the current future, if the given
partial function is defined at that value.

If the current future contains a value for which the partial function is
defined, the new future will also hold that value. Otherwise, the resulting
future will fail with a `NoSuchElementException` .

If the current future fails, then the resulting future also fails.

Example:

```scala
val f = Future { -5 }
val g = f collect {
  case x if x < 0 => -x
}
val h = f collect {
  case x if x > 0 => x * 2
}
g foreach println // Eventually prints 5
Await.result(h, Duration.Zero) // throw a NoSuchElementException
```

* S
  * the type of the returned `Future` @param pf the `PartialFunction` to apply
    to the successful result of this `Future`
* returns
  * a `Future` holding the result of application of the `PartialFunction` or a
     `NoSuchElementException`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def failed: Future[Throwable]`                                          ###

The returned `Future` will be successfully completed with the `Throwable` of the
original `Future` if the original `Future` fails.

If the original `Future` is successful, the returned `Future` is failed with a
 `NoSuchElementException` .

* returns
  * a failed projection of this `Future` .

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def fallbackTo[U](that: Future[U]): Future[U]`                          ###

Creates a new future which holds the result of this future if it was completed
successfully, or, if not, the result of the `that` future if `that` is completed
successfully. If both futures are failed, the resulting future holds the
throwable object of the first future.

Using this method will not cause concurrent programs to become nondeterministic.

Example:

```scala
val f = Future { sys.error("failed") }
val g = Future { 5 }
val h = f fallbackTo g
h foreach println // Eventually prints 5
```

* U
  * the type of the other `Future` and the resulting `Future`
* that
  * the `Future` whose result we want to use if this `Future` fails.
* returns
  * a `Future` with the successful result of this or that `Future` or the
    failure of this `Future` if both fail

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def filter(p: (Nothing) ⇒ Boolean)(implicit executor: ExecutionContext): Future[Nothing]` ###

Creates a new future by filtering the value of the current future with a
predicate.

If the current future contains a value which satisfies the predicate, the new
future will also hold that value. Otherwise, the resulting future will fail with
a `NoSuchElementException` .

If the current future fails, then the resulting future also fails.

Example:

```scala
val f = Future { 5 }
val g = f filter { _ % 2 == 1 }
val h = f filter { _ % 2 == 0 }
g foreach println // Eventually prints 5
Await.result(h, Duration.Zero) // throw a NoSuchElementException
```

* p
  * the predicate to apply to the successful result of this `Future`
* returns
  * a `Future` which will hold the successful result of this `Future` if it
    matches the predicate or a `NoSuchElementException`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def flatMap[S](f: (Nothing) ⇒ Future[S])(implicit executor: ExecutionContext): Future[S]` ###

Creates a new future by applying a function to the successful result of this
future, and returns the result of the function as the new future. If this future
is completed with an exception then the new future will also contain this
exception.

Example:

```scala
val f = Future { 5 }
val g = Future { 3 }
val h = for {
  x: Int <- f // returns Future(5)
  y: Int <- g // returns Future(3)
} yield x + y
```

is translated to:

```scala
f flatMap { (x: Int) => g map { (y: Int) => x + y } }
```

* S
  * the type of the returned `Future`
* f
  * the function which will be applied to the successful result of this
     `Future`
* returns
  * a `Future` which will be completed with the result of the application of the
    function

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def flatten[S](implicit ev: <:<[Nothing, Future[S]]): Future[S]`        ###

Creates a new future with one level of nesting flattened, this method is
equivalent to `flatMap(identity)` .

* S
  * the type of the returned `Future`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def foreach[U](f: (Nothing) ⇒ U)(implicit executor: ExecutionContext): Unit` ###

Asynchronously processes the value in the future once the value becomes
available.

WARNING: Will not be called if this future is never completed or if it is
completed with a failure.

Since this method executes asynchronously and does not produce a return value,
any non-fatal exceptions thrown will be reported to the `ExecutionContext` .

* U
  * only used to accept any return type of the given callback function
* f
  * the function which will be executed if this `Future` completes with a
    result, the return value of `f` will be discarded.

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def mapTo[S](implicit tag: ClassTag[S]): Future[S]`                     ###

Creates a new `Future[S]` which is completed with this `Future` 's result if
that conforms to `S` 's erased type or a `ClassCastException` otherwise.

* S
  * the type of the returned `Future`
* tag
  * the `ClassTag` which will be used to cast the result of this `Future`
* returns
  * a `Future` holding the casted result of this `Future` or a
     `ClassCastException` otherwise

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def map[S](f: (Nothing) ⇒ S)(implicit executor: ExecutionContext): Future[S]` ###

Creates a new future by applying a function to the successful result of this
future. If this future is completed with an exception then the new future will
also contain this exception.

Example:

```scala
val f = Future { 5 }
val g = Future { 3 }
val h = for {
  x: Int <- f // returns Future(5)
  y: Int <- g // returns Future(3)
} yield x + y
```

is translated to:

```scala
f flatMap { (x: Int) => g map { (y: Int) => x + y } }
```

* S
  * the type of the returned `Future`
* f
  * the function which will be applied to the successful result of this
     `Future`
* returns
  * a `Future` which will be completed with the result of the application of the
    function

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def onComplete[U](f: (Try[Nothing]) ⇒ U)(implicit executor: ExecutionContext): Unit` ###

When this future is completed, either through an exception, or a value, apply
the provided function.

If the future has already been completed, this will either be applied
immediately or be scheduled asynchronously.

Since this method executes asynchronously and does not produce a return value,
any non-fatal exceptions thrown will be reported to the `ExecutionContext` .

Multiple callbacks may be registered; there is no guarantee that they will be
executed in a particular order.

The provided callback always runs in the provided implicit `ExecutionContext` ,
though there is no guarantee that the `execute()` method on the
 `ExecutionContext` will be called once per callback or that `execute()` will be
called in the current thread. That is, the implementation may run multiple
callbacks in a batch within a single `execute()` and it may run `execute()`
either immediately or asynchronously.

* U
  * only used to accept any return type of the given callback function
* f
  * the function to be executed when this `Future` completes

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def onFailure[U](pf: PartialFunction[Throwable, U])(implicit executor: ExecutionContext): Unit` ###

When this future is completed with a failure (i.e., with a throwable), apply the
provided callback to the throwable.

The future may contain a throwable object and this means that the future failed.
Futures obtained through combinators have the same exception as the future they
were obtained from. The following throwable objects are not contained in the
future:

*  `Error` - errors are not contained within futures
*  `InterruptedException` - not contained within futures
* all `scala.util.control.ControlThrowable` except `NonLocalReturnControl` - not
   contained within futures

Instead, the future is completed with a ExecutionException with one of the
exceptions above as the cause. If a future is failed with a
 `scala.runtime.NonLocalReturnControl` , it is completed with a value from that
throwable instead.

If the future has already been completed with a failure, this will either be
applied immediately or be scheduled asynchronously.

Will not be called in case that the future is completed with a value.

Since this method executes asynchronously and does not produce a return value,
any non-fatal exceptions thrown will be reported to the `ExecutionContext` .

Multiple callbacks may be registered; there is no guarantee that they will be
executed in a particular order.

The provided callback always runs in the provided implicit `ExecutionContext` ,
though there is no guarantee that the `execute()` method on the
 `ExecutionContext` will be called once per callback or that `execute()` will be
called in the current thread. That is, the implementation may run multiple
callbacks in a batch within a single `execute()` and it may run `execute()`
either immediately or asynchronously.

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def onSuccess[U](pf: PartialFunction[Nothing, U])(implicit executor: ExecutionContext): Unit` ###

When this future is completed successfully (i.e., with a value), apply the
provided partial function to the value if the partial function is defined at
that value.

If the future has already been completed with a value, this will either be
applied immediately or be scheduled asynchronously.

Since this method executes asynchronously and does not produce a return value,
any non-fatal exceptions thrown will be reported to the `ExecutionContext` .

Multiple callbacks may be registered; there is no guarantee that they will be
executed in a particular order.

The provided callback always runs in the provided implicit `ExecutionContext` ,
though there is no guarantee that the `execute()` method on the
 `ExecutionContext` will be called once per callback or that `execute()` will be
called in the current thread. That is, the implementation may run multiple
callbacks in a batch within a single `execute()` and it may run `execute()`
either immediately or asynchronously.

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def ready(atMost: Duration)(implicit permit: CanAwait): never.this.type` ###

Await the "completed" state of this `Awaitable` .

 * _This method should not be called directly; use Await.ready instead._*

* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * this `Awaitable`

* Definition Classes
  * never → Awaitable
* Annotations
  * @ throws (clazz = classOf[TimeoutException]) @ throws (clazz =
    classOf[InterruptedException])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time this `Awaitable` is
    still not ready

(defined at scala.concurrent.Future.never)


### `def recoverWith[U](pf: PartialFunction[Throwable, Future[U]])(implicit executor: ExecutionContext): Future[U]` ###

Creates a new future that will handle any matching throwable that this future
might contain by assigning it a value of another future.

If there is no match, or if this future contains a valid result then the new
future will contain the same result.

Example:

```scala
val f = Future { Int.MaxValue }
Future (6 / 0) recoverWith { case e: ArithmeticException => f } // result: Int.MaxValue
```

* U
  * the type of the returned `Future`
* pf
  * the `PartialFunction` to apply if this `Future` fails
* returns
  * a `Future` with the successful value of this `Future` or the outcome of the
     `Future` returned by the `PartialFunction`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def recover[U](pf: PartialFunction[Throwable, U])(implicit executor: ExecutionContext): Future[U]` ###

Creates a new future that will handle any matching throwable that this future
might contain. If there is no match, or if this future contains a valid result
then the new future will contain the same.

Example:

```scala
Future (6 / 0) recover { case e: ArithmeticException => 0 } // result: 0
Future (6 / 0) recover { case e: NotFoundException   => 0 } // result: exception
Future (6 / 2) recover { case e: ArithmeticException => 0 } // result: 3
```

* U
  * the type of the returned `Future`
* pf
  * the `PartialFunction` to apply if this `Future` fails
* returns
  * a `Future` with the successful value of this `Future` or the result of the
     `PartialFunction`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def result(atMost: Duration)(implicit permit: CanAwait): Nothing`       ###

Await and return the result (of type `T` ) of this `Awaitable` .

 * _This method should not be called directly; use Await.result instead._*

* atMost
  * maximum wait time, which may be negative (no waiting is done), Duration.Inf
    for unbounded waiting, or a finite positive duration
* returns
  * the result value if the `Awaitable` is completed within the specific maximum
    wait time

* Definition Classes
  * never → Awaitable
* Annotations
  * @ throws (clazz = classOf[Exception])
* Exceptions thrown
  * IllegalArgumentException if `atMost` is Duration.Undefined
    InterruptedException if the current thread is interrupted while waiting
    TimeoutException if after waiting for the specified time this `Awaitable` is
    still not ready

(defined at scala.concurrent.Future.never)


### `def transformWith[S](f: (Try[Nothing]) ⇒ Future[S])(implicit executor: ExecutionContext): Future[S]` ###

Creates a new Future by applying the specified function, which produces a
Future, to the result of this Future. If there is any non-fatal exception thrown
when 'f' is applied then that exception will be propagated to the resulting
future.

* S
  * the type of the returned `Future`
* f
  * function that transforms the result of this future
* returns
  * a `Future` that will be completed with the transformed value

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def transform[S](s: (Nothing) ⇒ S, f: (Throwable) ⇒ Throwable)(implicit executor: ExecutionContext): Future[S]` ###

Creates a new future by applying the 's' function to the successful result of
this future, or the 'f' function to the failed result. If there is any non-fatal
exception thrown when 's' or 'f' is applied, that exception will be propagated
to the resulting future.

* S
  * the type of the returned `Future`
* s
  * function that transforms a successful result of the receiver into a
    successful result of the returned future
* f
  * function that transforms a failure of the receiver into a failure of the
    returned future
* returns
  * a `Future` that will be completed with the transformed value

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def transform[S](f: (Try[Nothing]) ⇒ Try[S])(implicit executor: ExecutionContext): Future[S]` ###

Creates a new Future by applying the specified function to the result of this
Future. If there is any non-fatal exception thrown when 'f' is applied then that
exception will be propagated to the resulting future.

* S
  * the type of the returned `Future`
* f
  * function that transforms the result of this future
* returns
  * a `Future` that will be completed with the transformed value

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def value: Option[Try[Nothing]]`                                        ###

The current value of this `Future` .

Note: using this method yields nondeterministic dataflow programs.

If the future is not completed the returned value will be `None` . If the future
is completed the value will be `Some(Success(t))` if it contains a valid result,
or `Some(Failure(error))` if it contains an exception.

* returns
  * `None` if the `Future` wasn't completed, `Some` if it was.

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def zipWith[U, R](that: Future[U])(f: (Nothing, U) ⇒ R)(implicit executor: ExecutionContext): Future[R]` ###

Zips the values of `this` and `that` future using a function `f` , and creates a
new future holding the result.

If `this` future fails, the resulting future is failed with the throwable stored
in `this` . Otherwise, if `that` future fails, the resulting future is failed
with the throwable stored in `that` . If the application of `f` throws a
throwable, the resulting future is failed with that throwable if it is
non-fatal.

* U
  * the type of the other `Future`
* R
  * the type of the resulting `Future`
* that
  * the other `Future`
* f
  * the function to apply to the results of `this` and `that`
* returns
  * a `Future` with the result of the application of `f` to the results of
     `this` and `that`

* Definition Classes
  * never → Future

(defined at scala.concurrent.Future.never)


### `def zip[U](that: Future[U]): Future[(Nothing, U)]`                      ###

Zips the values of `this` and `that` future, and creates a new future holding
the tuple of their results.

If `this` future fails, the resulting future is failed with the throwable stored
in `this` . Otherwise, if `that` future fails, the resulting future is failed
with the throwable stored in `that` .

* U
  * the type of the other `Future`
* that
  * the other `Future`
* returns
  * a `Future` with the results of both futures or the failure of the first of
    them that failed

* Definition Classes
  * never → Future
(defined at scala.concurrent.Future.never)
