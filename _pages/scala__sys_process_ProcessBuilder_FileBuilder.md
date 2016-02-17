
#                 scala.sys.process.ProcessBuilder.FileBuilder                 #

```scala
trait FileBuilder extends Sink with Source
```

Used when creating scala.sys.process.ProcessBuilder.Source and/or
scala.sys.process.ProcessBuilder.Sink from a file.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


--------------------------------------------------------------------------------
   Abstract Value Members From scala.sys.process.ProcessBuilder.FileBuilder#
--------------------------------------------------------------------------------


### `abstract def #<<(f: File): ProcessBuilder`                              ###

Append the contents of a `java.io.File` to this file

(defined at scala.sys.process.ProcessBuilder.FileBuilder#)


### `abstract def #<<(p: ProcessBuilder): ProcessBuilder`                    ###

Append the contents of a scala.sys.process.ProcessBuilder to this file

(defined at scala.sys.process.ProcessBuilder.FileBuilder#)


### `abstract def #<<(u: URL): ProcessBuilder`                               ###

Append the contents from a `java.net.URL` to this file

(defined at scala.sys.process.ProcessBuilder.FileBuilder#)


### `abstract def #<<(i: ⇒ InputStream): ProcessBuilder`                     ###

Append the contents of a `java.io.InputStream` to this file

(defined at scala.sys.process.ProcessBuilder.FileBuilder#)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.sys.process.ProcessBuilder.Sink
--------------------------------------------------------------------------------


### `abstract def toSink: ProcessBuilder`                                    ###

* Attributes
  * protected
* Definition Classes
  * Sink

(defined at scala.sys.process.ProcessBuilder.Sink)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.sys.process.ProcessBuilder.Sink#
--------------------------------------------------------------------------------


### `def #<(f: File): ProcessBuilder`                                        ###

Reads the given file into the input stream of this process.

* Definition Classes
  * Sink

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(b: ProcessBuilder): ProcessBuilder`                              ###

Reads the output of a scala.sys.process.ProcessBuilder into the input stream of
this process.

* Definition Classes
  * Sink

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(f: URL): ProcessBuilder`                                         ###

Reads the given URL into the input stream of this process.

* Definition Classes
  * Sink

(defined at scala.sys.process.ProcessBuilder.Sink#)


### `def #<(in: ⇒ InputStream): ProcessBuilder`                              ###

Reads the given InputStream into the input stream of this process. The argument
is call-by-name, so the stream is recreated, read, and closed each time this
process is executed.

* Definition Classes
  * Sink

(defined at scala.sys.process.ProcessBuilder.Sink#)


--------------------------------------------------------------------------------
      Abstract Value Members From scala.sys.process.ProcessBuilder.Source
--------------------------------------------------------------------------------


### `abstract def toSource: ProcessBuilder`                                  ###

* Attributes
  * protected
* Definition Classes
  * Source

(defined at scala.sys.process.ProcessBuilder.Source)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.sys.process.ProcessBuilder.Source
--------------------------------------------------------------------------------


### `def cat: ProcessBuilder`                                                ###

Returnes a scala.sys.process.ProcessBuilder representing this `Source` .

* Definition Classes
  * Source

(defined at scala.sys.process.ProcessBuilder.Source)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.sys.process.ProcessBuilder.Source#
--------------------------------------------------------------------------------


### `def #>(f: File): ProcessBuilder`                                        ###

Writes the output stream of this process to the given file.

* Definition Classes
  * Source

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>(b: ProcessBuilder): ProcessBuilder`                              ###

Writes the output stream of this process to a scala.sys.process.ProcessBuilder.

* Definition Classes
  * Source

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>(out: ⇒ OutputStream): ProcessBuilder`                            ###

Writes the output stream of this process to the given OutputStream. The argument
is call-by-name, so the stream is recreated, written, and closed each time this
process is executed.

* Definition Classes
  * Source

(defined at scala.sys.process.ProcessBuilder.Source#)


### `def #>>(f: File): ProcessBuilder`                                       ###

Appends the output stream of this process to the given file.

* Definition Classes
  * Source
(defined at scala.sys.process.ProcessBuilder.Source#)
