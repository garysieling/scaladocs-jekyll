
#                    scala.concurrent.forkjoin.ForkJoinTask                    #

```scala
object ForkJoinTask extends Serializable
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0)_ Use java.util.concurrent.ForkJoinTask directly,
    instead of this alias.
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/forkjoin/package.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.concurrent.forkjoin.ForkJoinTask
--------------------------------------------------------------------------------


### `def adapt(runnable: Runnable): ForkJoinTask[_]`                         ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def adapt[T](callable: Callable[_ <: T]): ForkJoinTask[T]`              ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def adapt[T](runnable: Runnable, result: T): ForkJoinTask[T]`           ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def getPool(): ForkJoinPool`                                            ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def invokeAll[T <: ForkJoinTask[_]](tasks: Collection[T]): Collection[T]` ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def invokeAll[T](t1: ForkJoinTask[T]): Unit`                            ###

(defined at scala.concurrent.forkjoin.ForkJoinTask)


### `def invokeAll[T](tasks: ForkJoinTask[T]*): Unit`                        ###
(defined at scala.concurrent.forkjoin.ForkJoinTask)
