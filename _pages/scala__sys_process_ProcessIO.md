
#                         scala.sys.process.ProcessIO                         #

```scala
final class ProcessIO extends AnyRef
```

This class is used to control the I/O of every scala.sys.process.Process. The
functions used to create it will be called with the process streams once it has
been started. It might not be necessary to use `ProcessIO` directly --
scala.sys.process.ProcessBuilder can return the process output to the caller, or
use a scala.sys.process.ProcessLogger which avoids direct interaction with a
stream. One can even use the factories at `BasicIO` to create a `ProcessIO` , or
use its helper methods when creating one's own `ProcessIO` .

When creating a `ProcessIO` , it is important to _close all streams_ when
finished, since the JVM might use system resources to capture the process input
and output, and will not release them unless the streams are explicitly closed.

 `ProcessBuilder` will call `writeInput` , `processOutput` and `processError` in
separate threads, and if daemonizeThreads is true, they will all be marked as
daemon threads.

* Source
  * [ProcessIO.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessIO.scala#L1)
* Note
  * Failure to close the passed streams may result in resource leakage.


--------------------------------------------------------------------------------
             Instance Constructors From scala.sys.process.ProcessIO
--------------------------------------------------------------------------------


### `new ProcessIO(in: (OutputStream) ⇒ Unit, out: (InputStream) ⇒ Unit, err: (InputStream) ⇒ Unit)` ###

(defined at scala.sys.process.ProcessIO)


--------------------------------------------------------------------------------
                 Value Members From scala.sys.process.ProcessIO
--------------------------------------------------------------------------------


### `def daemonized(): ProcessIO`                                            ###

Creates a new `ProcessIO` , with `daemonizeThreads` true.

(defined at scala.sys.process.ProcessIO)


### `val processError: (InputStream) ⇒ Unit`                                 ###

Function that will be called with the `InputStream` from which all error output
of the process must be read from. This will be called in a newly spawned thread.

(defined at scala.sys.process.ProcessIO)


### `val processOutput: (InputStream) ⇒ Unit`                                ###

Function that will be called with the `InputStream` from which all normal output
of the process must be read from. This will be called in a newly spawned thread.

(defined at scala.sys.process.ProcessIO)


### `def withError(process: (InputStream) ⇒ Unit): ProcessIO`                ###

Creates a new `ProcessIO` with a different handler for the error output.

(defined at scala.sys.process.ProcessIO)


### `def withInput(write: (OutputStream) ⇒ Unit): ProcessIO`                 ###

Creates a new `ProcessIO` with a different handler for the process input.

(defined at scala.sys.process.ProcessIO)


### `def withOutput(process: (InputStream) ⇒ Unit): ProcessIO`               ###

Creates a new `ProcessIO` with a different handler for the normal output.

(defined at scala.sys.process.ProcessIO)


### `val writeInput: (OutputStream) ⇒ Unit`                                  ###

Function that will be called with the `OutputStream` to which all input to the
process must be written. This will be called in a newly spawned thread.
(defined at scala.sys.process.ProcessIO)
