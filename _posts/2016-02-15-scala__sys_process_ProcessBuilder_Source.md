
#                   scala.sys.process.ProcessBuilder.Source                   #

```scala
trait Source extends AnyRef
```

Represents everything that can be used as an input to a
scala.sys.process.ProcessBuilder.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


--------------------------------------------------------------------------------
      Abstract Value Members From scala.sys.process.ProcessBuilder.Source
--------------------------------------------------------------------------------


### `abstract def toSource: ProcessBuilder`                                  ###

* Attributes
  * protected

(defined at scala.sys.process.ProcessBuilder.Source)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.sys.process.ProcessBuilder.Source
--------------------------------------------------------------------------------


### `def cat: ProcessBuilder`                                                ###

Returnes a scala.sys.process.ProcessBuilder representing this `Source` .

(defined at scala.sys.process.ProcessBuilder.Source)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.sys.process.ProcessBuilder.Source#
--------------------------------------------------------------------------------


### `def #>(f: File): ProcessBuilder`                                        ###

Writes the output stream of this process to the given file.

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>(b: ProcessBuilder): ProcessBuilder`                              ###

Writes the output stream of this process to a scala.sys.process.ProcessBuilder.

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>(out: ⇒ OutputStream): ProcessBuilder`                            ###

Writes the output stream of this process to the given OutputStream. The argument
is call-by-name, so the stream is recreated, written, and closed each time this
process is executed.

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>>(f: File): ProcessBuilder`                                       ###

Appends the output stream of this process to the given file.
(defined at scala.sys.process.ProcessBuilder.Source#)
