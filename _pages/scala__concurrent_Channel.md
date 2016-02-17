
#                           scala.concurrent.Channel                           #

```scala
class Channel[A] extends AnyRef
```

This class provides a simple FIFO queue of data objects, which are read by one
or more reader threads.

* A
  * type of data exchanged

* Source
  * [Channel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Channel.scala#L1)
* Version
  * 1.0, 10/03/2003


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class LinkedList[A] extends AnyRef`                                     ###

* Source
  * [Channel.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Channel.scala#L1)


--------------------------------------------------------------------------------
              Instance Constructors From scala.concurrent.Channel
--------------------------------------------------------------------------------


### `new Channel()`                                                          ###

(defined at scala.concurrent.Channel)


--------------------------------------------------------------------------------
                  Value Members From scala.concurrent.Channel
--------------------------------------------------------------------------------


### `def write(x: A): Unit`                                                  ###

Append a value to the FIFO queue to be read by `read` . This operation is
nonblocking and can be executed by any thread.

* x
  * object to enqueue to this channel
(defined at scala.concurrent.Channel)
