
#                          scala.concurrent.CanAwait                          #

```scala
sealed trait CanAwait extends AnyRef
```

This marker trait is used by Await to ensure that Awaitable.ready and
Awaitable.result are not directly called by user code. An implicit instance of
this trait is only available when user code is currently calling the methods on
Await.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)

