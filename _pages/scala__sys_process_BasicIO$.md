
#                          scala.sys.process.BasicIO                          #

```scala
object BasicIO
```

This object contains factories for scala.sys.process.ProcessIO, which can be
used to control the I/O of a scala.sys.process.Process when a
scala.sys.process.ProcessBuilder is started with the `run` command.

It also contains some helper methods that can be used to in the creation of
 `ProcessIO` .

It is used by other classes in the package in the implementation of various
features, but can also be used by client code.

* Source
  * [BasicIO.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/BasicIO.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.sys.process.BasicIO
--------------------------------------------------------------------------------


### `def apply(withIn: Boolean, output: (String) ⇒ Unit, log: Option[ProcessLogger]): ProcessIO` ###

Creates a `ProcessIO` from a function `String => Unit` . It can attach the
process input to stdin, and it will either send the error stream to stderr, or
to a `ProcessLogger` .

For example, the `ProcessIO` created below will print all normal output while
ignoring all error output. No input will be provided.

```scala
import scala.sys.process.BasicIO
val errToDevNull = BasicIO(false, println(_), None)
```

* withIn
  * True if the process input should be attached to stdin.
* output
  * A function that will be called with the process output.
* log
  * An optional `ProcessLogger` to which the output should be sent. If `None` ,
    output will be sent to stderr.
* returns
  * A `ProcessIO` with the characteristics above.

(defined at scala.sys.process.BasicIO)


### `def apply(withIn: Boolean, log: ProcessLogger): ProcessIO`              ###

Creates a `ProcessIO` from a `ProcessLogger` . It can attach the process input
to stdin.

* withIn
  * True if the process input should be attached to stdin.
* log
  * A `ProcessLogger` to receive all output, normal and error.
* returns
  * A `ProcessIO` with the characteristics above.

(defined at scala.sys.process.BasicIO)


### `def apply(withIn: Boolean, buffer: StringBuffer, log: Option[ProcessLogger]): ProcessIO` ###

Creates a `ProcessIO` that appends its output to a `StringBuffer` . It can
attach the process input to stdin, and it will either send the error stream to
stderr, or to a `ProcessLogger` .

For example, the `ProcessIO` created by the function below will store the normal
output on the buffer provided, and print all error on stderr. The input will be
read from stdin.

```scala
import scala.sys.process.{BasicIO, ProcessLogger}
val printer = ProcessLogger(println(_))
def appendToBuffer(b: StringBuffer) = BasicIO(true, b, Some(printer))
```

* withIn
  * True if the process input should be attached to stdin.
* buffer
  * A `StringBuffer` which will receive the process normal output.
* log
  * An optional `ProcessLogger` to which the output should be sent. If `None` ,
    output will be sent to stderr.
* returns
  * A `ProcessIO` with the characteristics above.

(defined at scala.sys.process.BasicIO)


### `def close(c: Closeable): Unit`                                          ###

Closes a `Closeable` without throwing an exception

(defined at scala.sys.process.BasicIO)


### `def connectToIn(o: OutputStream): Unit`                                 ###

Copy contents of stdin to the `OutputStream` .

(defined at scala.sys.process.BasicIO)


### `def getErr(log: Option[ProcessLogger]): (InputStream) ⇒ Unit`           ###

Returns a function `InputStream => Unit` given an optional `ProcessLogger` . If
no logger is passed, the function will send the output to stderr. This function
can be used to create a scala.sys.process.ProcessIO.

* log
  * An optional `ProcessLogger` to which the contents of the `InputStream` will
    be sent.
* returns
  * A function `InputStream => Unit` (used by scala.sys.process.ProcessIO) which
    will send the data to either the provided `ProcessLogger` or, if `None` , to
    stderr.

(defined at scala.sys.process.BasicIO)


### `def input(connect: Boolean): (OutputStream) ⇒ Unit`                     ###

Returns a function `OutputStream => Unit` that either reads the content from
stdin or does nothing. This function can be used by scala.sys.process.ProcessIO.

(defined at scala.sys.process.BasicIO)


### `def processFully(processLine: (String) ⇒ Unit): (InputStream) ⇒ Unit`   ###

Returns a function `InputStream => Unit` that will call the passed function with
all data read. This function can be used to create a scala.sys.process.ProcessIO.
The `processLine` function will be called with each line read, and `Newline`
will be appended after each line.

* processLine
  * A function that will be called with all data read from the stream.
* returns
  * A function `InputStream => Unit` (used by scala.sys.process.ProcessIO which
    will call `processLine` with all data read from the stream.

(defined at scala.sys.process.BasicIO)


### `def processFully(buffer: Appendable): (InputStream) ⇒ Unit`             ###

Returns a function `InputStream => Unit` that appends all data read to the
provided `Appendable` . This function can be used to create a
scala.sys.process.ProcessIO. The buffer will be appended line by line.

* buffer
  * An `Appendable` such as `StringBuilder` or `StringBuffer` .
* returns
  * A function `InputStream => Unit` (used by scala.sys.process.ProcessIO which
    will append all data read from the stream to the buffer.

(defined at scala.sys.process.BasicIO)


### `def processLinesFully(processLine: (String) ⇒ Unit)(readLine: () ⇒ String): Unit` ###

Calls `processLine` with the result of `readLine` until the latter returns
 `null` or the current thread is interrupted.

(defined at scala.sys.process.BasicIO)


### `def standard(in: (OutputStream) ⇒ Unit): ProcessIO`                     ###

Returns a `ProcessIO` connected to stdout, stderr and the provided `in`

(defined at scala.sys.process.BasicIO)


### `def standard(connectInput: Boolean): ProcessIO`                         ###

Returns a `ProcessIO` connected to stdout and stderr, and, optionally, stdin.

(defined at scala.sys.process.BasicIO)


### `def toStdErr: (InputStream) ⇒ Unit`                                     ###

Send all the input from the stream to stderr, and closes the input stream
afterwards.

(defined at scala.sys.process.BasicIO)


### `def toStdOut: (InputStream) ⇒ Unit`                                     ###

Send all the input from the stream to stdout, and closes the input stream
afterwards.

(defined at scala.sys.process.BasicIO)


### `def transferFully(in: InputStream, out: OutputStream): Unit`            ###

Copy all input from the input stream to the output stream. Closes the input
stream once it's all read.
(defined at scala.sys.process.BasicIO)
