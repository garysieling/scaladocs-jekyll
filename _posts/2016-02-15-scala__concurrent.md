
#                               scala.concurrent                               #

```scala
package concurrent
```

This package object contains primitives for concurrent and parallel programming.

### Guide

A more detailed guide to Futures and Promises, including discussion and examples
can be found at
[http://docs.scala-lang.org/overviews/core/futures.html](http://docs.scala-lang.org/overviews/core/futures.html).

### Common Imports

When working with Futures, you will often find that importing the whole
concurrent package is convenient, furthermore you are likely to need an implicit
ExecutionContext in scope for many operations involving Futures and Promises:

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global
```

### Specifying Durations

Operations often require a duration to be specified. A duration DSL is available
to make defining these easier:

```scala
import scala.concurrent.duration._
val d: Duration = 10.seconds
```

### Using Futures For Non-blocking Computation

Basic use of futures is easy with the factory method on Future, which executes a
provided function asynchronously, handing you back a future result of that
function without blocking the current thread. In order to create the Future you
will need either an implicit or explicit ExecutionContext to be provided:

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global  // implicit execution context

val firstZebra: Future[Int] = Future {
  val source = scala.io.Source.fromFile("/etc/dictionaries-common/words")
  source.toSeq.indexOfSlice("zebra")
}
```

### Avoid Blocking

Although blocking is possible in order to await results (with a mandatory
timeout duration):

```scala
import scala.concurrent.duration._
Await.result(firstZebra, 10.seconds)
```

and although this is sometimes necessary to do, in particular for testing
purposes, blocking in general is discouraged when working with Futures and
concurrency in order to avoid potential deadlocks and improve performance.
Instead, use callbacks or combinators to remain in the future domain:

```scala
val animalRange: Future[Int] = for {
  aardvark <- firstAardvark
  zebra <- firstZebra
} yield zebra - aardvark

animalRange.onSuccess {
  case x if x > 500000 => println("It's a long way from Aardvark to Zebra")
}
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Awaitable[+T] extends AnyRef`                                     ###

An object that may eventually be completed with a result value of type `T` which
may be awaited using blocking methods.

The Await object provides methods that allow accessing the result of an
 `Awaitable` by blocking the current thread until the `Awaitable` has been
completed or a timeout has occurred.

* Source
  * [Awaitable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Awaitable.scala#L1)


### `trait BlockContext extends AnyRef`                                      ###

A context to be notified by `scala.concurrent.blocking` when a thread is about
to block. In effect this trait provides the implementation for
 `scala.concurrent.Await` . `scala.concurrent.Await.result()` and
 `scala.concurrent.Await.ready()` locates an instance of `BlockContext` by first
looking for one provided through `BlockContext.withBlockContext()` and failing
that, checking whether `Thread.currentThread` is an instance of `BlockContext` .
So a thread pool can have its `java.lang.Thread` instances implement
 `BlockContext` . There's a default `BlockContext` used if the thread doesn't
implement `BlockContext` .

Typically, you'll want to chain to the previous `BlockContext` , like this:

```scala
val oldContext = BlockContext.current
val myContext = new BlockContext {
  override def blockOn[T](thunk: =>T)(implicit permission: CanAwait): T = {
    // you'd have code here doing whatever you need to do
    // when the thread is about to block.
    // Then you'd chain to the previous context:
    oldContext.blockOn(thunk)
  }
}
BlockContext.withBlockContext(myContext) {
  // then this block runs with myContext as the handler
  // for scala.concurrent.blocking
}
```

* Source
  * [BlockContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/BlockContext.scala#L1)


### `sealed trait CanAwait extends AnyRef`                                   ###

This marker trait is used by Await to ensure that Awaitable.ready and
Awaitable.result are not directly called by user code. An implicit instance of
this trait is only available when user code is currently calling the methods on
Await.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)


### `type CancellationException = java.util.concurrent.CancellationException` ###


### `class Channel[A] extends AnyRef`                                        ###

This class provides a simple FIFO queue of data objects, which are read by one
or more reader threads.

* A
  * type of data exchanged

* Source
  * [Channel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Channel.scala#L1)
* Version
  * 1.0, 10/03/2003


### `class DelayedLazyVal[T] extends AnyRef`                                 ###

A `DelayedLazyVal` is a wrapper for lengthy computations which have a valid
partially computed result.

The first argument is a function for obtaining the result at any given point in
time, and the second is the lengthy computation. Once the computation is
complete, the `apply` method will stop recalculating it and return a fixed value
from that point forward.

* Source
  * [DelayedLazyVal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/DelayedLazyVal.scala#L1)
* Version
  * 2.8


### `trait ExecutionContext extends AnyRef`                                  ###

An `ExecutionContext` can execute program logic asynchronously, typically but
not necessarily on a thread pool.

A general purpose `ExecutionContext` must be asynchronous in executing any
 `Runnable` that is passed into its `execute` -method. A special purpose
 `ExecutionContext` may be synchronous but must only be passed to code that is
explicitly safe to be run using a synchronously executing `ExecutionContext` .

APIs such as `Future.onComplete` require you to provide a callback and an
implicit `ExecutionContext` . The implicit `ExecutionContext` will be used to
execute the callback.

It is possible to simply import
 `scala.concurrent.ExecutionContext.Implicits.global` to obtain an implicit
 `ExecutionContext` . This global context is a reasonable default thread pool.

However, application developers should carefully consider where they want to set
policy; ideally, one place per application (or per logically-related section of
code) will make a decision about which `ExecutionContext` to use. That is, you
might want to avoid hardcoding
 `scala.concurrent.ExecutionContext.Implicits.global` all over the place in your
code. One approach is to add `(implicit ec: ExecutionContext)` to methods which
need an `ExecutionContext` . Then import a specific context in one place for the
entire application or module, passing it implicitly to individual methods.

A custom `ExecutionContext` may be appropriate to execute code which blocks on
IO or performs long-running computations.
 `ExecutionContext.fromExecutorService` and `ExecutionContext.fromExecutor` are
good ways to create a custom `ExecutionContext` .

The intent of `ExecutionContext` is to lexically scope code execution. That is,
each method, class, file, package, or application determines how to run its own
code. This avoids issues such as running application callbacks on a thread pool
belonging to a networking library. The size of a networking library's thread
pool can be safely configured, knowing that only that library's network
operations will be affected. Application callback execution can be configured
separately.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


### `trait ExecutionContextExecutor extends ExecutionContext with Executor`  ###

An ExecutionContext that is also a Java
[Executor](http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html).

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


### `trait ExecutionContextExecutorService extends ExecutionContextExecutor with ExecutorService` ###

An ExecutionContext that is also a Java
[ExecutorService](http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html).

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


### `type ExecutionException = java.util.concurrent.ExecutionException`      ###


### `trait Future[+T] extends Awaitable[T]`                                  ###

The trait that represents futures.

Asynchronous computations that yield futures are created with the
 `Future.apply` call:

```scala
val s = "Hello"
val f: Future[String] = Future {
  s + " future!"
}
f onSuccess {
  case msg => println(msg)
}
```

* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)
* See also
  * [Futures and Promises](http://docs.scala-lang.org/overviews/core/futures.html)


### `class Lock extends AnyRef`                                              ###

This class...

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.2)_ Use java.util.concurrent.locks.Lock
* Source
  * [Lock.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Lock.scala#L1)
* Version
  * 1.0, 10/03/2003


### `trait OnCompleteRunnable extends AnyRef`                                ###

A marker indicating that a `java.lang.Runnable` provided to
 `scala.concurrent.ExecutionContext` wraps a callback provided to
 `Future.onComplete` . All callbacks provided to a `Future` end up going through
 `onComplete` , so this allows an `ExecutionContext` to special-case callbacks
that were executed by `Future` if desired.

* Self Type
  * OnCompleteRunnable with Runnable
* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)


### `trait Promise[T] extends AnyRef`                                        ###

Promise is an object which can be completed with a value or failed with an
exception.

* Source
  * [Promise.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Promise.scala#L1)


### `class SyncChannel[A] extends AnyRef`                                    ###

A `SyncChannel` allows one to exchange data synchronously between a reader and a
writer thread. The writer thread is blocked until the data to be written has
been read by a corresponding reader thread.

* Source
  * [SyncChannel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/SyncChannel.scala#L1)
* Version
  * 2.0, 04/17/2008


### `class SyncVar[A] extends AnyRef`                                        ###

A class to provide safe concurrent access to a mutable cell. All methods are
synchronized.

* A
  * type of the contained value

* Source
  * [SyncVar.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/SyncVar.scala#L1)
* Version
  * 1.0, 10/03/2003


### `type TimeoutException = java.util.concurrent.TimeoutException`          ###


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Await`                                                           ###

 `Await` is what is used to ensure proper handling of blocking for `Awaitable`
instances.

While occasionally useful, e.g. for testing, it is recommended that you avoid
Await when possible in favor of callbacks and combinators like onComplete and
use in for comprehensions. Await will block the thread on which it runs, and
could cause performance and deadlock issues.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)


### `object BlockContext`                                                    ###

* Source
  * [BlockContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/BlockContext.scala#L1)


### `object ExecutionContext`                                                ###

Contains factory methods for creating execution contexts.

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


### `object Future`                                                          ###

Future companion object.

* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)


### `object JavaConversions`                                                 ###

The `JavaConversions` object provides implicit conversions supporting
interoperability between Scala and Java concurrency classes.

* Source
  * [JavaConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/JavaConversions.scala#L1)


### `object Promise`                                                         ###

* Source
  * [Promise.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Promise.scala#L1)


### `package duration`                                                       ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `package forkjoin`                                                       ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/forkjoin/package.scala#L1)


--------------------------------------------------------------------------------
                 Deprecated Value Members From scala.concurrent
--------------------------------------------------------------------------------


### `def future[T](body: ⇒ T)(implicit executor: ExecutionContext): Future[T]` ###

Starts an asynchronous computation and returns a `Future` object with the result
of that computation.

The result becomes available once the asynchronous computation is completed.

* T
  * the type of the result
* body
  * the asynchronous computation
* executor
  * the execution context on which the future is run
* returns
  * the `Future` holding the result of the computation

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `Future { ... }` instead.

(defined at scala.concurrent)


### `def promise[T](): Promise[T]`                                           ###

Creates a promise object which can be completed with a value or an exception.

* T
  * the type of the value in the promise
* returns
  * the newly created `Promise` object

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `Promise[T]()` instead.

(defined at scala.concurrent)


--------------------------------------------------------------------------------
                      Value Members From scala.concurrent
--------------------------------------------------------------------------------


### `def blocking[T](body: ⇒ T): T`                                          ###

Used to designate a piece of code which potentially blocks, allowing the current
BlockContext to adjust the runtime's behavior. Properly marking blocking code
may improve performance or avoid deadlocks.

Blocking on an Awaitable should be done using Await.result instead of
 `blocking` .

* body
  * A piece of code which contains potentially blocking or long running calls.

* Annotations
  * @ throws (clazz = classOf[Exception])
* Exceptions thrown
  * CancellationException if the computation was cancelled InterruptedException
    in the case that a wait within the blocking `body` was interrupted
(defined at scala.concurrent)
