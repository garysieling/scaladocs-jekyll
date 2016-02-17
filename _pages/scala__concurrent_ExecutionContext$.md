
#                      scala.concurrent.ExecutionContext                      #

```scala
object ExecutionContext
```

Contains factory methods for creating execution contexts.

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Implicits`                                                       ###

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.concurrent.ExecutionContext
--------------------------------------------------------------------------------


### `def defaultReporter: (Throwable) ⇒ Unit`                                ###

The default reporter simply prints the stack trace of the `Throwable` to
[System.err](http://docs.oracle.com/javase/8/docs/api/java/lang/System.html#err).

* returns
  * the function for error reporting

(defined at scala.concurrent.ExecutionContext)


### `def fromExecutor(e: Executor): ExecutionContextExecutor`                ###

Creates an `ExecutionContext` from the given `Executor` with the default
reporter.

* e
  * the `Executor` to use. If `null` , a new `Executor` is created with
    [default configuration](http://www.scala-lang.org/api/current/index.html#scala.concurrent.ExecutionContext$@global:scala.concurrent.ExecutionContextExecutor).
* returns
  * the `ExecutionContext` using the given `Executor`

(defined at scala.concurrent.ExecutionContext)


### `def fromExecutor(e: Executor, reporter: (Throwable) ⇒ Unit): ExecutionContextExecutor` ###

Creates an `ExecutionContext` from the given `Executor` .

* e
  * the `Executor` to use. If `null` , a new `Executor` is created with
    [default configuration](http://www.scala-lang.org/api/current/index.html#scala.concurrent.ExecutionContext$@global:scala.concurrent.ExecutionContextExecutor).
* reporter
  * a function for error reporting
* returns
  * the `ExecutionContext` using the given `Executor`

(defined at scala.concurrent.ExecutionContext)


### `def fromExecutorService(e: ExecutorService): ExecutionContextExecutorService` ###

Creates an `ExecutionContext` from the given `ExecutorService` with the default
reporter.

If it is guaranteed that none of the executed tasks are blocking, a
single-threaded `ExecutorService` can be used to create an `ExecutionContext` as
follows:

```scala
import java.util.concurrent.Executors
val ec = ExecutionContext.fromExecutorService(Executors.newSingleThreadExecutor())
```

* e
  * the `ExecutorService` to use. If `null` , a new `ExecutorService` is created
    with
    [default configuration](http://www.scala-lang.org/api/current/index.html#scala.concurrent.ExecutionContext$@global:scala.concurrent.ExecutionContextExecutor).
* returns
  * the `ExecutionContext` using the given `ExecutorService`

(defined at scala.concurrent.ExecutionContext)


### `def fromExecutorService(e: ExecutorService, reporter: (Throwable) ⇒ Unit): ExecutionContextExecutorService` ###

Creates an `ExecutionContext` from the given `ExecutorService` .

* e
  * the `ExecutorService` to use. If `null` , a new `ExecutorService` is created
    with
    [default configuration](http://www.scala-lang.org/api/current/index.html#scala.concurrent.ExecutionContext$@global:scala.concurrent.ExecutionContextExecutor).
* reporter
  * a function for error reporting
* returns
  * the `ExecutionContext` using the given `ExecutorService`

(defined at scala.concurrent.ExecutionContext)


### `def global: ExecutionContextExecutor`                                   ###

The explicit global `ExecutionContext` . Invoke `global` when you want to
provide the global `ExecutionContext` explicitly.

The default `ExecutionContext` implementation is backed by a work-stealing
thread pool. By default, the thread pool uses a target number of worker threads
equal to the number of
[available processors](https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#availableProcessors--).

* returns
  * the global `ExecutionContext`
(defined at scala.concurrent.ExecutionContext)
