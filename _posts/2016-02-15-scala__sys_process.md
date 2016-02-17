
#                              scala.sys.process                              #

```scala
package process
```

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
                                  Type Members
--------------------------------------------------------------------------------


### `class FileProcessLogger extends ProcessLogger with Closeable with Flushable` ###

A scala.sys.process.ProcessLogger that writes output to a file.

* Source
  * [ProcessLogger.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessLogger.scala#L1)


### `trait Process extends AnyRef`                                           ###

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


### `trait ProcessBuilder extends Source with Sink`                          ###

Represents a sequence of one or more external processes that can be executed. A
 `ProcessBuilder` can be a single external process, or a combination of other
 `ProcessBuilder` . One can control where a the output of an external process
will go to, and where its input will come from, or leave that decision to
whoever starts it.

One creates a `ProcessBuilder` through factories provided in
scala.sys.process.Process 's companion object, or implicit conversions based on
these factories made available in the package object scala.sys.process. Here are
some examples:

```scala
import scala.sys.process._

// Executes "ls" and sends output to stdout
"ls".!

// Execute "ls" and assign a `Stream[String]` of its output to "contents".
val contents = Process("ls").lineStream

// Here we use a `Seq` to make the parameter whitespace-safe
def contentsOf(dir: String): String = Seq("ls", dir).!!
```

The methods of `ProcessBuilder` are divided in three categories: the ones that
combine two `ProcessBuilder` to create a third, the ones that redirect input or
output of a `ProcessBuilder` , and the ones that execute the external processes
associated with it.

### Combining `ProcessBuilder`

Two existing `ProcessBuilder` can be combined in the following ways:

* They can be executed in parallel, with the output of the first being fed as
   input to the second, like Unix pipes. This is achieved with the `#|` method.
* They can be executed in sequence, with the second starting as soon as the
   first ends. This is done by the `###` method.
* The execution of the second one can be conditioned by the return code (exit
   status) of the first, either only when it's zero, or only when it's not zero.
   The methods `#&&` and `#||` accomplish these tasks.

### Redirecting Input/Output

Though control of input and output can be done when executing the process,
there's a few methods that create a new `ProcessBuilder` with a pre-configured
input or output. They are `#<` , `#>` and `#>>` , and may take as input either
another `ProcessBuilder` (like the pipe described above), or something else such
as a `java.io.File` or a `java.io.InputStream` . For example:

```scala
new URL("http://databinder.net/dispatch/About") #> "grep JSON" #>> new File("About_JSON") !
```

### Starting Processes

To execute all external commands associated with a `ProcessBuilder` , one may
use one of four groups of methods. Each of these methods have various overloads
and variations to enable further control over the I/O. These methods are:

*  `run` : the most general method, it returns a scala.sys.process.Process
   immediately, and the external command executes concurrently.
*  `!` : blocks until all external commands exit, and returns the exit code of
   the last one in the chain of execution.
*  `!!` : blocks until all external commands exit, and returns a `String` with
   the output generated.
*  `lineStream` : returns immediately like `run` , and the output being
   generated is provided through a `Stream[String]` . Getting the next element
   of that `Stream` may block until it becomes available. This method will throw
   an exception if the return code is different than zero -- if this is not
   desired, use the `lineStream_!` method.

### Handling Input and Output

If not specified, the input of the external commands executed with `run` or `!`
will not be tied to anything, and the output will be redirected to the stdout
and stderr of the Scala process. For the methods `!!` and `lines` , no input
will be provided, and the output will be directed according to the semantics of
these methods.

Some methods will cause stdin to be used as input. Output can be controlled with
a scala.sys.process.ProcessLogger -- `!!` and `lines` will only redirect error
output when passed a `ProcessLogger` . If one desires full control over input
and output, then a scala.sys.process.ProcessIO can be used with `run` .

For example, we could silence the error output from `lines_!` like this:

```scala
val etcFiles = "find /etc" lines_! ProcessLogger(line => ())
```

### Extended Example

Let's examine in detail one example of usage:

```scala
import scala.sys.process._
"find src -name *.scala -exec grep null {} ;"  #|  "xargs test -z"  #&&  "echo null-free"  #||  "echo null detected"  !
```

Note that every `String` is implicitly converted into a `ProcessBuilder` through
the implicits imported from scala.sys.process. These `ProcessBuilder` are then
combined in three different ways.

1.  `#|` pipes the output of the first command into the input of the second
   command. It mirrors a shell pipe ( `|` ).
2.  `#&&` conditionally executes the second command if the previous one finished
   with exit value 0. It mirrors shell's `&&` .
3.  `#||` conditionally executes the third command if the exit value of the
   previous command is different than zero. It mirrors shell's `||` .

Finally, `!` at the end executes the commands, and returns the exit value.
Whatever is printed will be sent to the Scala process standard output. If we
wanted to capture it, we could run that with `!!` instead.

Note: though it is not shown above, the equivalent of a shell's `;` would be
 `###` . The reason for this name is that `;` is a reserved token in Scala.

Note: the `lines` method, though deprecated, may conflict with the `StringLike`
method of the same name. To avoid this, one may wish to call the builders in
 `Process` instead of importing `scala.sys.process._` . The example above would
be

```scala
import scala.sys.process.Process
Process("find src -name *.scala -exec grep null {} ;") #| Process("xargs test -z") #&& Process("echo null-free") #|| Process("echo null detected") !
```

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


### `trait ProcessCreation extends AnyRef`                                   ###

Factories for creating scala.sys.process.ProcessBuilder. They can be found on
and used through scala.sys.process.Process 's companion object.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)


### `final class ProcessIO extends AnyRef`                                   ###

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


### `trait ProcessImplicits extends AnyRef`                                  ###

Provide implicit conversions for the factories offered by
scala.sys.process.Process 's companion object. These implicits can then be used
to decrease the noise in a pipeline of commands, making it look more shell-like.
They are available through the package object scala.sys.process.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)


### `trait ProcessLogger extends AnyRef`                                     ###

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
                                 Value Members
--------------------------------------------------------------------------------


### `object BasicIO`                                                         ###

This object contains factories for scala.sys.process.ProcessIO, which can be
used to control the I/O of a scala.sys.process.Process when a
scala.sys.process.ProcessBuilder is started with the `run` command.

It also contains some helper methods that can be used to in the creation of
 `ProcessIO` .

It is used by other classes in the package in the implementation of various
features, but can also be used by client code.

* Source
  * [BasicIO.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/BasicIO.scala#L1)


### `object Process extends ProcessImpl with ProcessCreation`                ###

Methods for constructing simple commands that can then be combined.

* Source
  * [Process.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/Process.scala#L1)


### `object ProcessBuilder extends ProcessBuilderImpl`                       ###

This object contains traits used to describe input and output sources.

* Source
  * [ProcessBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessBuilder.scala#L1)


### `object ProcessLogger`                                                   ###

Provides factories to create scala.sys.process.ProcessLogger, which are used to
capture output of scala.sys.process.ProcessBuilder commands when run.

* Source
  * [ProcessLogger.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/process/ProcessLogger.scala#L1)


--------------------------------------------------------------------------------
                      Value Members From scala.sys.process
--------------------------------------------------------------------------------


### `def javaVmArguments: List[String]`                                      ###

The arguments passed to `java` when creating this process

(defined at scala.sys.process)


### `def stderr: PrintStream`                                                ###

The error stream of this process

(defined at scala.sys.process)


### `def stdin: InputStream`                                                 ###

The input stream of this process

(defined at scala.sys.process)


### `def stdout: PrintStream`                                                ###

The output stream of this process

(defined at scala.sys.process)


--------------------------------------------------------------------------------
             Value Members From scala.sys.process.ProcessImplicits
--------------------------------------------------------------------------------


### `implicit def builderToProcess(builder: JProcessBuilder): ProcessBuilder` ###

Implicitly convert a `java.lang.ProcessBuilder` into a Scala one.

* Definition Classes
  * ProcessImplicits

(defined at scala.sys.process.ProcessImplicits)


### `implicit def buildersToProcess[T](builders: Seq[T])(implicit convert: (T) ⇒ Source): Seq[Source]` ###

Return a sequence of scala.sys.process.ProcessBuilder.Source from a sequence of
values for which an implicit conversion to `Source` is available.

* Definition Classes
  * ProcessImplicits

(defined at scala.sys.process.ProcessImplicits)


### `implicit def fileToProcess(file: File): FileBuilder`                    ###

Implicitly convert a `java.io.File` into a
scala.sys.process.ProcessBuilder.FileBuilder, which can be used as either input
or output of a process. For example:

```scala
import scala.sys.process._
"ls" #> new java.io.File("dirContents.txt") !
```

* Definition Classes
  * ProcessImplicits

(defined at scala.sys.process.ProcessImplicits)


### `implicit def stringSeqToProcess(command: Seq[String]): ProcessBuilder`  ###

Implicitly convert a sequence of `String` into a
scala.sys.process.ProcessBuilder. The first argument will be taken to be the
command to be executed, and the remaining will be its arguments. When using
this, arguments may contain spaces.

* Definition Classes
  * ProcessImplicits

(defined at scala.sys.process.ProcessImplicits)


### `implicit def stringToProcess(command: String): ProcessBuilder`          ###

Implicitly convert a `String` into a scala.sys.process.ProcessBuilder.

* Definition Classes
  * ProcessImplicits

(defined at scala.sys.process.ProcessImplicits)


### `implicit def urlToProcess(url: URL): URLBuilder`                        ###

Implicitly convert a `java.net.URL` into a
scala.sys.process.ProcessBuilder.URLBuilder, which can be used as input to a
process. For example:

```scala
import scala.sys.process._
Seq("xmllint", "--html", "-") #< new java.net.URL("http://www.scala-lang.org") #> new java.io.File("fixed.html") !
```

* Definition Classes
  * ProcessImplicits
(defined at scala.sys.process.ProcessImplicits)
