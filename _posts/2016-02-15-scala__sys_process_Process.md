
#                          scala.sys.process.Process                          #

```scala
trait Process extends AnyRef
```

Represents a process that is running or has finished running. It may be a
compound process with several underlying native processes (such as `a #&& b` ).

This trait is often not used directly, though its companion object contains
factories for scala.sys.process.ProcessBuilder, the main component of this
package.

It is used directly when calling the method `run` on a `ProcessBuilder` , which
makes the process run in the background. The methods provided on `Process` make
it possible for one to block until the process exits and get the exit value, or
destroy the process altogether.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)
* See also
  * scala.sys.process.ProcessBuilder


--------------------------------------------------------------------------------
             Concrete Value Members From scala.sys.process.Process
--------------------------------------------------------------------------------


### `abstract def destroy(): Unit`                                           ###

Destroys this process.
(defined at scala.sys.process.Process)
