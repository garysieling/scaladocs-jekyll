
#                     scala.sys.process.FileProcessLogger                     #

```scala
class FileProcessLogger extends ProcessLogger with Closeable with Flushable
```

A scala.sys.process.ProcessLogger that writes output to a file.

* Source
  * [ProcessLogger.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessLogger.scala#L1)


--------------------------------------------------------------------------------
         Instance Constructors From scala.sys.process.FileProcessLogger
--------------------------------------------------------------------------------


### `new FileProcessLogger(file: File)`                                      ###

(defined at scala.sys.process.FileProcessLogger)


--------------------------------------------------------------------------------
             Value Members From scala.sys.process.FileProcessLogger
--------------------------------------------------------------------------------


### `def buffer[T](f: ⇒ T): T`                                               ###

If a process is begun with one of these `ProcessBuilder` methods:

```scala
def !(log: ProcessLogger): Int
def !<(log: ProcessLogger): Int
```

The run will be wrapped in a call to buffer. This gives the logger an
opportunity to set up and tear down buffering. At present the library
implementations of `ProcessLogger` simply execute the body unbuffered.

* Definition Classes
  * FileProcessLogger → ProcessLogger

(defined at scala.sys.process.FileProcessLogger)


### `def err(s: ⇒ String): Unit`                                             ###

Will be called with each line read from the process error stream.

* Definition Classes
  * FileProcessLogger → ProcessLogger

(defined at scala.sys.process.FileProcessLogger)


### `def out(s: ⇒ String): Unit`                                             ###

Will be called with each line read from the process output stream.

* Definition Classes
  * FileProcessLogger → ProcessLogger
(defined at scala.sys.process.FileProcessLogger)
