
#                                scala.io.StdIn                                #

```scala
object StdIn extends StdIn
```

* Source
  * [StdIn.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/io/StdIn.scala#L1)


--------------------------------------------------------------------------------
                       Value Members From scala.io.StdIn
--------------------------------------------------------------------------------


### `def readLine(text: String, args: Any*): String`                         ###

Print and flush formatted text to the default output, and read a full line from
the default input. Returns `null` if the end of the input stream has been
reached.

* text
  * the format of the text to print out, as in `printf` .
* args
  * the parameters used to instantiate the format, as in `printf` .
* returns
  * the string read from the default input

* Definition Classes
  * StdIn

(defined at scala.io.StdIn)


### `def readf(format: String): List[Any]`                                   ###

Reads in some structured input (from the default input), specified by a format
specifier. See class `java.text.MessageFormat` for details of the format
specification.

* format
  * the format of the input.
* returns
  * a list of all extracted values.

* Definition Classes
  * StdIn
* Exceptions thrown
  * `java.io.EOFException` if the end of the input stream has been reached.

(defined at scala.io.StdIn)


### `def readf1(format: String): Any`                                        ###

Reads in some structured input (from the default input), specified by a format
specifier, returning only the first value extracted, according to the format
specification.

* format
  * format string, as accepted by `readf` .
* returns
  * The first value that was extracted from the input

* Definition Classes
  * StdIn

(defined at scala.io.StdIn)


### `def readf2(format: String): (Any, Any)`                                 ###

Reads in some structured input (from the default input), specified by a format
specifier, returning only the first two values extracted, according to the
format specification.

* format
  * format string, as accepted by `readf` .
* returns
  * A scala.Tuple2 containing the first two values extracted

* Definition Classes
  * StdIn

(defined at scala.io.StdIn)


### `def readf3(format: String): (Any, Any, Any)`                            ###

Reads in some structured input (from the default input), specified by a format
specifier, returning only the first three values extracted, according to the
format specification.

* format
  * format string, as accepted by `readf` .
* returns
  * A scala.Tuple3 containing the first three values extracted

* Definition Classes
  * StdIn
(defined at scala.io.StdIn)
