
#                        scala.concurrent.BlockContext                        #

```scala
trait BlockContext extends AnyRef
```

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


--------------------------------------------------------------------------------
           Abstract Value Members From scala.concurrent.BlockContext
--------------------------------------------------------------------------------


### `abstract def blockOn[T](thunk: ⇒ T)(implicit permission: CanAwait): T`  ###

Used internally by the framework; Designates (and eventually executes) a thunk
which potentially blocks the calling `java.lang.Thread` .

Clients must use `scala.concurrent.blocking` or `scala.concurrent.Await`
instead.
(defined at scala.concurrent.BlockContext)
