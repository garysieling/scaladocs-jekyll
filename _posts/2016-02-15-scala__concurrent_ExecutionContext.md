
#                      scala.concurrent.ExecutionContext                      #

```scala
trait ExecutionContext extends AnyRef
```

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


--------------------------------------------------------------------------------
         Abstract Value Members From scala.concurrent.ExecutionContext
--------------------------------------------------------------------------------


### `abstract def execute(runnable: Runnable): Unit`                         ###

Runs a block of code on this execution context.

* runnable
  * the task to execute

(defined at scala.concurrent.ExecutionContext)


### `abstract def reportFailure(cause: Throwable): Unit`                     ###

Reports that an asynchronous computation failed.

* cause
  * the cause of the failure

(defined at scala.concurrent.ExecutionContext)


--------------------------------------------------------------------------------
        Deprecated Value Members From scala.concurrent.ExecutionContext
--------------------------------------------------------------------------------


### `def prepare(): ExecutionContext`                                        ###

Prepares for the execution of a task. Returns the prepared execution context.
The recommended implementation of `prepare` is to return `this` .

This method should no longer be overridden or called. It was originally expected
that `prepare` would be called by all libraries that consume ExecutionContexts,
in order to capture thread local context. However, this usage has proven
difficult to implement in practice and instead it is now better to avoid using
 `prepare` entirely.

Instead, if an `ExecutionContext` needs to capture thread local context, it
should capture that context when it is constructed, so that it doesn't need any
additional preparation later.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12)_ Preparation of ExecutionContexts will be removed.
(defined at scala.concurrent.ExecutionContext)
