
#                 scala.concurrent.ExecutionContext.Implicits                 #

```scala
object Implicits
```

* Source
  * [ExecutionContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/ExecutionContext.scala#L1)


--------------------------------------------------------------------------------
         Value Members From scala.concurrent.ExecutionContext.Implicits
--------------------------------------------------------------------------------


### `implicit lazy val global: ExecutionContext`                             ###

The implicit global `ExecutionContext` . Import `global` when you want to
provide the global `ExecutionContext` implicitly.

The default `ExecutionContext` implementation is backed by a work-stealing
thread pool. By default, the thread pool uses a target number of worker threads
equal to the number of
[available processors](https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#availableProcessors--).
(defined at scala.concurrent.ExecutionContext.Implicits)
