
#                     scala.concurrent.OnCompleteRunnable                     #

```scala
trait OnCompleteRunnable extends AnyRef
```

A marker indicating that a `java.lang.Runnable` provided to
 `scala.concurrent.ExecutionContext` wraps a callback provided to
 `Future.onComplete` . All callbacks provided to a `Future` end up going through
 `onComplete` , so this allows an `ExecutionContext` to special-case callbacks
that were executed by `Future` if desired.

* Self Type
  * OnCompleteRunnable with Runnable
* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)

