
#                         scala.concurrent.SyncChannel                         #

```scala
class SyncChannel[A] extends AnyRef
```

A `SyncChannel` allows one to exchange data synchronously between a reader and a
writer thread. The writer thread is blocked until the data to be written has
been read by a corresponding reader thread.

* Source
  * [SyncChannel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/SyncChannel.scala#L1)
* Version
  * 2.0, 04/17/2008


--------------------------------------------------------------------------------
            Instance Constructors From scala.concurrent.SyncChannel
--------------------------------------------------------------------------------


### `new SyncChannel()`                                                      ###

(defined at scala.concurrent.SyncChannel)


--------------------------------------------------------------------------------
                Value Members From scala.concurrent.SyncChannel
--------------------------------------------------------------------------------


### `def write(data: A): Unit`                                               ###
(defined at scala.concurrent.SyncChannel)
