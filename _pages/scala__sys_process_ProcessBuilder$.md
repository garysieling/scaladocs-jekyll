
#                       scala.sys.process.ProcessBuilder                       #

```scala
object ProcessBuilder extends ProcessBuilderImpl
```

This object contains traits used to describe input and output sources.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait FileBuilder extends Sink with Source`                             ###

Used when creating scala.sys.process.ProcessBuilder.Source and/or
scala.sys.process.ProcessBuilder.Sink from a file.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


### `trait Sink extends AnyRef`                                              ###

Represents everything that can receive an output from a
scala.sys.process.ProcessBuilder.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


### `trait Source extends AnyRef`                                            ###

Represents everything that can be used as an input to a
scala.sys.process.ProcessBuilder.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


### `trait URLBuilder extends Source`                                        ###

Used when creating scala.sys.process.ProcessBuilder.Source from an URL.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)

