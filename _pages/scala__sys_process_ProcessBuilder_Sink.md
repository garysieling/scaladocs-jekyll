
#                    scala.sys.process.ProcessBuilder.Sink                    #

```scala
trait Sink extends AnyRef
```

Represents everything that can receive an output from a
scala.sys.process.ProcessBuilder.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.sys.process.ProcessBuilder.Sink
--------------------------------------------------------------------------------


### `abstract def toSink: ProcessBuilder`                                    ###

* Attributes
  * protected

(defined at scala.sys.process.ProcessBuilder.Sink)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.sys.process.ProcessBuilder.Sink#
--------------------------------------------------------------------------------


### `def #<(f: File): ProcessBuilder`                                        ###

Reads the given file into the input stream of this process.

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(b: ProcessBuilder): ProcessBuilder`                              ###

Reads the output of a scala.sys.process.ProcessBuilder into the input stream of
this process.

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(f: URL): ProcessBuilder`                                         ###

Reads the given URL into the input stream of this process.

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(in: ⇒ InputStream): ProcessBuilder`                              ###

Reads the given InputStream into the input stream of this process. The argument
is call-by-name, so the stream is recreated, read, and closed each time this
process is executed.
(defined at scala.sys.process.ProcessBuilder.Sink#)
