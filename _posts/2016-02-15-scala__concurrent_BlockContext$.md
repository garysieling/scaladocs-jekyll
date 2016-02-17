
#                        scala.concurrent.BlockContext                        #

```scala
object BlockContext
```

* Source
  * [BlockContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/BlockContext.scala#L1)


--------------------------------------------------------------------------------
                Value Members From scala.concurrent.BlockContext
--------------------------------------------------------------------------------


### `def current: BlockContext`                                              ###

* returns
  * the `BlockContext` that would be used for the current `java.lang.Thread` at
    this point

(defined at scala.concurrent.BlockContext)


### `def defaultBlockContext: BlockContext`                                  ###

* returns
  * the `BlockContext` that will be used if no other is found.

(defined at scala.concurrent.BlockContext)


### `def withBlockContext[T](blockContext: BlockContext)(body: ⇒ T): T`      ###

Installs a current `BlockContext` around executing `body` .
(defined at scala.concurrent.BlockContext)
