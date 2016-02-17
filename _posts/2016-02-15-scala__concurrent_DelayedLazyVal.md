
#                       scala.concurrent.DelayedLazyVal                       #

```scala
class DelayedLazyVal[T] extends AnyRef
```

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


--------------------------------------------------------------------------------
           Instance Constructors From scala.concurrent.DelayedLazyVal
--------------------------------------------------------------------------------


### `new DelayedLazyVal(f: () ⇒ T, body: ⇒ Unit)(implicit exec: ExecutionContext)` ###

* f
  * the function to obtain the current value at any point in time
* body
  * the computation to run to completion in another thread
(defined at scala.concurrent.DelayedLazyVal)
