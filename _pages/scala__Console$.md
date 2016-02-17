
#                                scala.Console                                #

```scala
object Console extends DeprecatedConsole with AnsiColor
```

Implements functionality for printing Scala values on the terminal as well as
reading specific values. Also defines constants for marking up text on ANSI
terminals.

* Source
  * [Console.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Console.scala#L1)
* Version
  * 1.0, 03/09/2003


--------------------------------------------------------------------------------
                        Value Members From scala.Console
--------------------------------------------------------------------------------


### `def err: PrintStream`                                                   ###

The default error, can be overridden by `setErr`

(defined at scala.Console)


### `def in: BufferedReader`                                                 ###

The default input, can be overridden by `setIn`

(defined at scala.Console)


### `def out: PrintStream`                                                   ###

The default output, can be overridden by `setOut`

(defined at scala.Console)


### `def print(obj: Any): Unit`                                              ###

Prints an object to `out` using its `toString` method.

* obj
  * the object to print; may be null.

(defined at scala.Console)


### `def printf(text: String, args: Any*): Unit`                             ###

Prints its arguments as a formatted string to the default output, based on a
string pattern (in a fashion similar to printf in C).

The interpretation of the formatting patterns is described in
`java.util.Formatter`.

* text
  * the pattern for formatting the arguments.
* args
  * the arguments used to instantiating the pattern.

* Exceptions thrown
  * `java.lang.IllegalArgumentException` if there was a problem with the format
    string or arguments

(defined at scala.Console)


### `def println(x: Any): Unit`                                              ###

Prints out an object to the default output, followed by a newline character.

* x
  * the object to print.

(defined at scala.Console)


### `def setErrDirect(err: PrintStream): Unit`                               ###

* Attributes
  * protected
* Definition Classes
  * Console → DeprecatedConsole

(defined at scala.Console)


### `def setInDirect(in: BufferedReader): Unit`                              ###

* Attributes
  * protected
* Definition Classes
  * Console → DeprecatedConsole

(defined at scala.Console)


### `def setOutDirect(out: PrintStream): Unit`                               ###

Internal usage only.

* Attributes
  * protected
* Definition Classes
  * Console → DeprecatedConsole

(defined at scala.Console)


### `def withErr[T](err: OutputStream)(thunk: ⇒ T): T`                       ###

Sets the default error stream for the duration of execution of one thunk.

* err
  * the new error stream.
* thunk
  * the code to execute with the new error stream active
* returns
  * the results of `thunk`

* See also
  * `withErr[T](err:PrintStream)(thunk: =>T)`

(defined at scala.Console)


### `def withErr[T](err: PrintStream)(thunk: ⇒ T): T`                        ###

Set the default error stream for the duration of execution of one thunk.

* err
  * the new error stream.
* thunk
  * the code to execute with the new error stream active
* returns
  * the results of `thunk`

* See also
  * `withErr[T](err:OutputStream)(thunk: =>T)`

Example:

```scala
withErr(Console.out) { println("This goes to default _out_") }
```

(defined at scala.Console)


### `def withIn[T](in: InputStream)(thunk: ⇒ T): T`                          ###

Sets the default input stream for the duration of execution of one thunk.

* in
  * the new input stream.
* thunk
  * the code to execute with the new input stream active
* returns
  * the results of `thunk`

* See also
  * `withIn[T](reader:Reader)(thunk: =>T)`

(defined at scala.Console)


### `def withIn[T](reader: Reader)(thunk: ⇒ T): T`                           ###

Sets the default input stream for the duration of execution of one thunk.

* thunk
  * the code to execute with the new input stream active
* returns
  * the results of `thunk`

* See also
  * `withIn[T](in:InputStream)(thunk: =>T)`

Example:

```scala
val someFile:Reader = openFile("file.txt")
withIn(someFile) {
  // Reads a line from file.txt instead of default input
  println(readLine)
}
```

(defined at scala.Console)


### `def withOut[T](out: OutputStream)(thunk: ⇒ T): T`                       ###

Sets the default output stream for the duration of execution of one thunk.

* out
  * the new output stream.
* thunk
  * the code to execute with the new output stream active
* returns
  * the results of `thunk`

* See also
  * `withOut[T](out:PrintStream)(thunk: => T)`

(defined at scala.Console)


### `def withOut[T](out: PrintStream)(thunk: ⇒ T): T`                        ###

Sets the default output stream for the duration of execution of one thunk.

* out
  * the new output stream.
* thunk
  * the code to execute with the new output stream active
* returns
  * the results of `thunk`

* See also
  * `withOut[T](out:OutputStream)(thunk: => T)`

Example:

```scala
withOut(Console.err) { println("This goes to default _error_") }
```

(defined at scala.Console)


--------------------------------------------------------------------------------
             Deprecated Value Members From scala.DeprecatedConsole
--------------------------------------------------------------------------------


### `def readLine(text: String, args: Any*): String`                         ###

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in scala.io.StdIn

(defined at scala.DeprecatedConsole)


### `def readf(format: String): List[Any]`                                   ###

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in scala.io.StdIn

(defined at scala.DeprecatedConsole)


### `def readf1(format: String): Any`                                        ###

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in scala.io.StdIn

(defined at scala.DeprecatedConsole)


### `def readf2(format: String): (Any, Any)`                                 ###

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in scala.io.StdIn

(defined at scala.DeprecatedConsole)


### `def readf3(format: String): (Any, Any, Any)`                            ###

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in scala.io.StdIn

(defined at scala.DeprecatedConsole)


### `def setErr(err: OutputStream): Unit`                                    ###

Sets the default error stream.

* err
  * the new error stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withErr

(defined at scala.DeprecatedConsole)


### `def setErr(err: PrintStream): Unit`                                     ###

Sets the default error stream.

* err
  * the new error stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withErr

(defined at scala.DeprecatedConsole)


### `def setIn(in: InputStream): Unit`                                       ###

Sets the default input stream.

* in
  * the new input stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withIn

(defined at scala.DeprecatedConsole)


### `def setIn(reader: Reader): Unit`                                        ###

Sets the default input stream.

* reader
  * specifies the new input stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withIn

(defined at scala.DeprecatedConsole)


### `def setOut(out: OutputStream): Unit`                                    ###

Sets the default output stream.

* out
  * the new output stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withOut

(defined at scala.DeprecatedConsole)


### `def setOut(out: PrintStream): Unit`                                     ###

Sets the default output stream.

* out
  * the new output stream.

* Definition Classes
  * DeprecatedConsole
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use withOut
(defined at scala.DeprecatedConsole)
