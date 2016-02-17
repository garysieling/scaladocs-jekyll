
#                       scala.sys.process.ProcessBuilder                       #

```scala
trait ProcessBuilder extends Source with Sink
```

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


--------------------------------------------------------------------------------
          Abstract Value Members From scala.sys.process.ProcessBuilder
--------------------------------------------------------------------------------


### `abstract def !!(log: ProcessLogger): String`                            ###

Starts the process represented by this builder, blocks until it exits, and
returns the output as a String. Standard error is sent to the provided
ProcessLogger. If the exit code is non-zero, an exception is thrown.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def !!<(log: ProcessLogger): String`                           ###

Starts the process represented by this builder, blocks until it exits, and
returns the output as a String. Standard error is sent to the provided
ProcessLogger. If the exit code is non-zero, an exception is thrown. The newly
started process reads from standard input of the current process.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def !(log: ProcessLogger): Int`                                ###

Starts the process represented by this builder, blocks until it exits, and
returns the exit code. Standard output and error are sent to the given
ProcessLogger.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def !<(log: ProcessLogger): Int`                               ###

Starts the process represented by this builder, blocks until it exits, and
returns the exit code. Standard output and error are sent to the given
ProcessLogger. The newly started process reads from standard input of the
current process.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def lineStream(log: ProcessLogger): Stream[String]`            ###

Starts the process represented by this builder. The output is returned as a
Stream that blocks when lines are not available but the process has not
completed. Standard error is sent to the provided ProcessLogger. If the process
exits with a non-zero value, the Stream will provide all lines up to termination
and then throw an exception.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def lineStream_!(log: ProcessLogger): Stream[String]`          ###

Starts the process represented by this builder. The output is returned as a
Stream that blocks when lines are not available but the process has not
completed. Standard error is sent to the provided ProcessLogger. If the process
exits with a non-zero value, the Stream will provide all lines up to termination
but will not throw an exception.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def run(): Process`                                            ###

Starts the process represented by this builder. Standard output and error are
sent to the console.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def run(connectInput: Boolean): Process`                       ###

Starts the process represented by this builder. Standard output and error are
sent to the console. The newly started process reads from standard input of the
current process if `connectInput` is true.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def run(io: ProcessIO): Process`                               ###

Starts the process represented by this builder. I/O is handled by the given
ProcessIO instance.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def run(log: ProcessLogger): Process`                          ###

Starts the process represented by this builder. Standard output and error are
sent to the given ProcessLogger.

(defined at scala.sys.process.ProcessBuilder)


### `abstract def run(log: ProcessLogger, connectInput: Boolean): Process`   ###

Starts the process represented by this builder, blocks until it exits, and
returns the exit code. Standard output and error are sent to the given
ProcessLogger. The newly started process reads from standard input of the
current process if `connectInput` is true.

(defined at scala.sys.process.ProcessBuilder)


--------------------------------------------------------------------------------
         Deprecated Value Members From scala.sys.process.ProcessBuilder
--------------------------------------------------------------------------------


### `abstract def !: Int`                                                    ###

Starts the process represented by this builder, blocks until it exits, and
returns the exit code. Standard output and error are sent to the console.

(defined at scala.sys.process.ProcessBuilder)


### `def lines(log: ProcessLogger): Stream[String]`                          ###

Deprecated (renamed). Use `lineStream(log: ProcessLogger)` instead.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use stream instead.

(defined at scala.sys.process.ProcessBuilder)


### `def lines_!(log: ProcessLogger): Stream[String]`                        ###

Deprecated (renamed). Use `lineStream_!(log: ProcessLogger)` instead.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use stream_! instead.

(defined at scala.sys.process.ProcessBuilder)


--------------------------------------------------------------------------------
         Abstract Value Members From scala.sys.process.ProcessBuilder#
--------------------------------------------------------------------------------


### `abstract def #&&(other: ProcessBuilder): ProcessBuilder`                ###

Constructs a command that runs this command first and then `other` if this
command succeeds.

(defined at scala.sys.process.ProcessBuilder#)


### `abstract def #|(other: ProcessBuilder): ProcessBuilder`                 ###

Constructs a command that will run this command and pipes the output to `other` .
 `other` must be a simple command.

(defined at scala.sys.process.ProcessBuilder#)


### `abstract def #||(other: ProcessBuilder): ProcessBuilder`                ###

Constructs a command that runs this command first and then `other` if this
command does not succeed.

(defined at scala.sys.process.ProcessBuilder#)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.sys.process.ProcessBuilder####
--------------------------------------------------------------------------------


### `abstract def ###(other: ProcessBuilder): ProcessBuilder`                ###

Constructs a command that will run this command and then `other` . The exit code
will be the exit code of `other` .

(defined at scala.sys.process.ProcessBuilder####)


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
