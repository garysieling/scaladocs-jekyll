
#                                  scala.sys                                  #

```scala
package sys
```

The package object `scala.sys` contains methods for reading and altering core
aspects of the virtual machine as well as the world outside of it.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/package.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait BooleanProp extends Prop[Boolean]`                                ###

A few additional conveniences for Boolean properties.

* Source
  * [BooleanProp.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/BooleanProp.scala#L1)


### `trait Prop[+T] extends AnyRef`                                          ###

A lightweight interface wrapping a property contained in some unspecified map.
Generally it'll be the system properties but this is not a requirement.

See `scala.sys.SystemProperties` for an example usage.

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


### `class ShutdownHookThread extends Thread`                                ###

A minimal Thread wrapper to enhance shutdown hooks. It knows how to unregister
itself.

* Source
  * [ShutdownHookThread.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/ShutdownHookThread.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


### `class SystemProperties extends AbstractMap[String, String] with Map[String, String]` ###

A bidirectional map wrapping the java System properties. Changes to System
properties will be immediately visible in the map, and modifications made to the
map will be immediately applied to the System properties. If a security manager
is in place which prevents the properties from being read or written, the
AccessControlException will be caught and discarded.

* Source
  * [SystemProperties.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/SystemProperties.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object BooleanProp`                                                     ###

* Source
  * [BooleanProp.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/BooleanProp.scala#L1)


### `object Prop`                                                            ###

* Source
  * [Prop.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/Prop.scala#L1)


### `object ShutdownHookThread`                                              ###

* Source
  * [ShutdownHookThread.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/ShutdownHookThread.scala#L1)


### `object SystemProperties`                                                ###

The values in SystemProperties can be used to access and manipulate designated
system properties. See `scala.sys.Prop` for particulars.

* Source
  * [SystemProperties.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/SystemProperties.scala#L1)

Example:

```scala
if (!headless.isSet) headless.enable()
```


### `package process`                                                        ###

This package handles the execution of external processes. The contents of this
package can be divided in three groups, according to their responsibilities:

* Indicating what to run and how to run it.
* Handling a process input and output.
* Running the process.

For simple uses, the only group that matters is the first one. Running an
external command can be as simple as `"ls".!` , or as complex as building a
pipeline of commands such as this:

```scala
import scala.sys.process._
"ls" #| "grep .scala" #&& Seq("sh", "-c", "scalac *.scala") #|| "echo nothing found" lines
```

We describe below the general concepts and architecture of the package, and then
take a closer look at each of the categories mentioned above.

### Concepts and Architecture

The underlying basis for the whole package is Java's `Process` and
 `ProcessBuilder` classes. While there's no need to use these Java classes, they
impose boundaries on what is possible. One cannot, for instance, retrieve a _
process id_ for whatever is executing.

When executing an external process, one can provide a command's name, arguments
to it, the directory in which it will be executed and what environment variables
will be set. For each executing process, one can feed its standard input through
a `java.io.OutputStream` , and read from its standard output and standard error
through a pair of `java.io.InputStream` . One can wait until a process finishes
execution and then retrieve its return value, or one can kill an executing
process. Everything else must be built on those features.

This package provides a DSL for running and chaining such processes, mimicking
Unix shells ability to pipe output from one process to the input of another, or
control the execution of further processes based on the return status of the
previous one.

In addition to this DSL, this package also provides a few ways of controlling
input and output of these processes, going from simple and easy to use to
complex and flexible.

When processes are composed, a new `ProcessBuilder` is created which, when run,
will execute the `ProcessBuilder` instances it is composed of according to the
manner of the composition. If piping one process to another, they'll be executed
simultaneously, and each will be passed a `ProcessIO` that will copy the output
of one to the input of the other.

### What to Run and How

The central component of the process execution DSL is the
scala.sys.process.ProcessBuilder trait. It is `ProcessBuilder` that implements
the process execution DSL, that creates the scala.sys.process.Process that will
handle the execution, and return the results of such execution to the caller. We
can see that DSL in the introductory example: `#|` , `#&&` and `#!!` are methods
on `ProcessBuilder` used to create a new `ProcessBuilder` through composition.

One creates a `ProcessBuilder` either through factories on the
scala.sys.process.Process 's companion object, or through implicit conversions
available in this package object itself. Implicitly, each process is created
either out of a `String` , with arguments separated by spaces -- no escaping of
spaces is possible -- or out of a scala.collection.Seq, where the first element
represents the command name, and the remaining elements are arguments to it. In
this latter case, arguments may contain spaces.

To further control what how the process will be run, such as specifying the
directory in which it will be run, see the factories on
scala.sys.process.Process 's object companion.

Once the desired `ProcessBuilder` is available, it can be executed in different
ways, depending on how one desires to control its I/O, and what kind of result
one wishes for:

* Return status of the process ( `!` methods)
* Output of the process as a `String` ( `!!` methods)
* Continuous output of the process as a `Stream[String]` ( `lines` methods)
* The `Process` representing it ( `run` methods)

Some simple examples of these methods:

```scala
import scala.sys.process._

// This uses ! to get the exit code
def fileExists(name: String) = Seq("test", "-f", name).! == 0

// This uses !! to get the whole result as a string
val dirContents = "ls".!!

// This "fire-and-forgets" the method, which can be lazily read through
// a Stream[String]
def sourceFilesAt(baseDir: String): Stream[String] = {
  val cmd = Seq("find", baseDir, "-name", "*.scala", "-type", "f")
  cmd.lines
}
```

We'll see more details about controlling I/O of the process in the next section.

### Handling Input and Output

In the underlying Java model, once a `Process` has been started, one can get
 `java.io.InputStream` and `java.io.OutputStream` representing its output and
input respectively. That is, what one writes to an `OutputStream` is turned into
input to the process, and the output of a process can be read from an
 `InputStream` -- of which there are two, one representing normal output, and
the other representing error output.

This model creates a difficulty, which is that the code responsible for actually
running the external processes is the one that has to take decisions about how
to handle its I/O.

This package presents an alternative model: the I/O of a running process is
controlled by a scala.sys.process.ProcessIO object, which can be passed _to_ the
code that runs the external process. A `ProcessIO` will have direct access to
the java streams associated with the process I/O. It must, however, close these
streams afterwards.

Simpler abstractions are available, however. The components of this package that
handle I/O are:

* scala.sys.process.ProcessIO : provides the low level abstraction.
* scala.sys.process.ProcessLogger : provides a higher level abstraction for
   output, and can be created through its object companion
* scala.sys.process.BasicIO : a library of helper methods for the creation of
    `ProcessIO` .
* This package object itself, with a few implicit conversions.

Some examples of I/O handling:

```scala
import scala.sys.process._

// An overly complex way of computing size of a compressed file
def gzFileSize(name: String) = {
  val cat = Seq("zcat", name)
  var count = 0
  def byteCounter(input: java.io.InputStream) = {
    while(input.read() != -1) count += 1
    input.close()
  }
  val p = cat run new ProcessIO(_.close(), byteCounter, _.close())
  p.exitValue()
  count
}

// This "fire-and-forgets" the method, which can be lazily read through
// a Stream[String], and accumulates all errors on a StringBuffer
def sourceFilesAt(baseDir: String): (Stream[String], StringBuffer) = {
  val buffer = new StringBuffer()
  val cmd = Seq("find", baseDir, "-name", "*.scala", "-type", "f")
  val lines = cmd lines_! ProcessLogger(buffer append _)
  (lines, buffer)
}
```

Instances of the java classes `java.io.File` and `java.net.URL` can both be used
directly as input to other processes, and `java.io.File` can be used as output
as well. One can even pipe one to the other directly without any intervening
process, though that's not a design goal or recommended usage. For example, the
following code will copy a web page to a file:

```scala
import java.io.File
import java.net.URL
import scala.sys.process._
new URL("http://www.scala-lang.org/") #> new File("scala-lang.html") !
```

More information about the other ways of controlling I/O can be looked at in the
scaladoc for the associated objects, traits and classes.

### Running the Process

Paradoxically, this is the simplest component of all, and the one least likely
to be interacted with. It consists solely of scala.sys.process.Process, and it
provides only two methods:

*  `exitValue()` : blocks until the process exit, and then returns the exit
   value. This is what happens when one uses the `!` method of `ProcessBuilder` .
*  `destroy()` : this will kill the external process and close the streams
   associated with it.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/package.scala#L1)


--------------------------------------------------------------------------------
                          Value Members From scala.sys
--------------------------------------------------------------------------------


### `def allThreads(): IndexedSeq[Thread]`                                   ###

Returns all active thread in the current thread's thread group and subgroups.

* returns
  * an IndexedSeq containing the threads.

(defined at scala.sys)


### `def addShutdownHook(body: ⇒ Unit): ShutdownHookThread`                  ###

Register a shutdown hook to be run when the VM exits. The hook is automatically
registered: the returned value can be ignored, but is available in case the
Thread requires further modification. It can also be unregistered by calling
ShutdownHookThread#remove().

Note that shutdown hooks are NOT guaranteed to be run.

* body
  * the body of code to run at shutdown
* returns
  * the Thread which will run the shutdown hook.

* See also
  * scala.sys.ShutdownHookThread

(defined at scala.sys)


### `def env: Map[String, String]`                                           ###

An immutable Map representing the current system environment.

* returns
  * a Map containing the system environment variables.

(defined at scala.sys)


### `def error(message: String): Nothing`                                    ###

Throw a new RuntimeException with the supplied message.

* returns
  * Nothing.

(defined at scala.sys)


### `def exit(status: Int): Nothing`                                         ###

Exit the JVM with the given status code.

* returns
  * Nothing.

(defined at scala.sys)


### `def props: SystemProperties`                                            ###

A bidirectional, mutable Map representing the current system Properties.

* returns
  * a SystemProperties.

* See also
  * scala.sys.SystemProperties
(defined at scala.sys)
