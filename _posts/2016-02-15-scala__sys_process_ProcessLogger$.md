
#                       scala.sys.process.ProcessLogger                       #

```scala
object ProcessLogger
```

Provides factories to create scala.sys.process.ProcessLogger, which are used to
capture output of scala.sys.process.ProcessBuilder commands when run.

* Source
  * [ProcessLogger.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessLogger.scala#L1)


--------------------------------------------------------------------------------
               Value Members From scala.sys.process.ProcessLogger
--------------------------------------------------------------------------------


### `def apply(fn: (String) ⇒ Unit): ProcessLogger`                          ###

Creates a scala.sys.process.ProcessLogger that sends all output, standard and
error, to the passed function.

(defined at scala.sys.process.ProcessLogger)


### `def apply(fout: (String) ⇒ Unit, ferr: (String) ⇒ Unit): ProcessLogger` ###

Creates a scala.sys.process.ProcessLogger that sends all output to the
corresponding function.

* fout
  * This function will receive standard output.
* ferr
  * This function will receive standard error.

(defined at scala.sys.process.ProcessLogger)


### `def apply(file: File): FileProcessLogger`                               ###

Creates a scala.sys.process.ProcessLogger that redirects output to a
 `java.io.File` .
(defined at scala.sys.process.ProcessLogger)
