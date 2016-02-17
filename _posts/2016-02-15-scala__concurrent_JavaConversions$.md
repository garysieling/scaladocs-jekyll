
#                       scala.concurrent.JavaConversions                       #

```scala
object JavaConversions
```

The `JavaConversions` object provides implicit conversions supporting
interoperability between Scala and Java concurrency classes.

* Source
  * [JavaConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/JavaConversions.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.concurrent.JavaConversions
--------------------------------------------------------------------------------


### `implicit def asExecutionContext(exec: Executor): ExecutionContextExecutor` ###

Creates a new `ExecutionContext` which uses the provided `Executor` .

(defined at scala.concurrent.JavaConversions)


### `implicit def asExecutionContext(exec: ExecutorService): ExecutionContextExecutorService` ###

Creates a new `ExecutionContext` which uses the provided `ExecutorService` .
(defined at scala.concurrent.JavaConversions)
