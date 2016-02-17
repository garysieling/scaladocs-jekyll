
#                       scala.sys.process.ProcessLogger                       #

```scala
trait ProcessLogger extends AnyRef
```

Encapsulates the output and error streams of a running process. This is used by
scala.sys.process.ProcessBuilder when starting a process, as an alternative to
scala.sys.process.ProcessIO, which can be more difficult to use. Note that a
 `ProcessLogger` will be used to create a `ProcessIO` anyway. The object
 `BasicIO` has some functions to do that.

Here is an example that counts the number of lines in the normal and error
output of a process:

```scala
import scala.sys.process._

var normalLines = 0
var errorLines = 0
val countLogger = ProcessLogger(line => normalLines += 1,
                                line => errorLines += 1)
"find /etc" ! countLogger
```

* Source
  * [ProcessLogger.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessLogger.scala#L1)
* See also
  * scala.sys.process.ProcessBuilder


--------------------------------------------------------------------------------
          Abstract Value Members From scala.sys.process.ProcessLogger
--------------------------------------------------------------------------------


### `abstract def buffer[T](f: ⇒ T): T`                                      ###

If a process is begun with one of these `ProcessBuilder` methods:

```scala
def !(log: ProcessLogger): Int
def !<(log: ProcessLogger): Int
```

The run will be wrapped in a call to buffer. This gives the logger an
opportunity to set up and tear down buffering. At present the library
implementations of `ProcessLogger` simply execute the body unbuffered.

(defined at scala.sys.process.ProcessLogger)


### `abstract def err(s: ⇒ String): Unit`                                    ###

Will be called with each line read from the process error stream.

(defined at scala.sys.process.ProcessLogger)


### `abstract def out(s: ⇒ String): Unit`                                    ###

Will be called with each line read from the process output stream.
(defined at scala.sys.process.ProcessLogger)
