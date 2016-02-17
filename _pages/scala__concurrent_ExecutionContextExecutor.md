
#                  scala.concurrent.ExecutionContextExecutor                  #

```scala
trait ExecutionContextExecutor extends ExecutionContext with Executor
```

An ExecutionContext that is also a Java
[Executor](http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html).

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


--------------------------------------------------------------------------------
           Abstract Value Members From java.util.concurrent.Executor
--------------------------------------------------------------------------------


### `abstract def execute(arg0: Runnable): Unit`                             ###

* Definition Classes
  * Executor

(defined at java.util.concurrent.Executor)


--------------------------------------------------------------------------------
         Abstract Value Members From scala.concurrent.ExecutionContext
--------------------------------------------------------------------------------


### `abstract def reportFailure(cause: Throwable): Unit`                     ###

Reports that an asynchronous computation failed.

* cause
  * the cause of the failure

* Definition Classes
  * ExecutionContext

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

* Definition Classes
  * ExecutionContext
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12)_ Preparation of ExecutionContexts will be removed.
(defined at scala.concurrent.ExecutionContext)
