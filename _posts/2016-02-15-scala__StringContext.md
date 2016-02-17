
#                             scala.StringContext                             #

```scala
case class StringContext(parts: String*) extends Product with Serializable
```

This class provides the basic mechanism to do String Interpolation. String
Interpolation allows users to embed variable references directly in *processed*
string literals. Here's an example:

```scala
val name = "James"
println(s"Hello, $name")  // Hello, James
```

Any processed string literal is rewritten as an instantiation and method call
against this class. For example:

```scala
s"Hello, $name"
```

is rewritten to be:

```scala
StringContext("Hello, ", "").s(name)
```

By default, this class provides the `raw` , `s` and `f` methods as available
interpolators.

To provide your own string interpolator, create an implicit class which adds a
method to `StringContext` . Here's an example:

```scala
implicit class JsonHelper(private val sc: StringContext) extends AnyVal {
  def json(args: Any*): JSONObject = ...
}
val x: JSONObject = json"{ a: $a }"
```

Here the `JsonHelper` extension class implicitly adds the `json` method to
 `StringContext` which can be used for `json` string literals.

* parts
  * The parts that make up the interpolated string, without the expressions that
    get inserted by interpolation.

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)
* Since
  * 2.10.0


--------------------------------------------------------------------------------
                 Instance Constructors From scala.StringContext
--------------------------------------------------------------------------------


### `new StringContext(parts: String*)`                                      ###

* parts
  * The parts that make up the interpolated string, without the expressions that
    get inserted by interpolation.

(defined at scala.StringContext)


--------------------------------------------------------------------------------
                     Value Members From scala.StringContext
--------------------------------------------------------------------------------


### `def checkLengths(args: Seq[Any]): Unit`                                 ###

Checks that the length of the given argument `args` is one less than the number
of `parts` supplied to the enclosing `StringContext` .

* Exceptions thrown
  * IllegalArgumentException if this is not the case.

(defined at scala.StringContext)


### `macro def f[A >: Any](args: A*): String`                                ###

The formatted string interpolator.

It inserts its arguments between corresponding parts of the string context. It
also treats standard escape sequences as defined in the Scala specification.
Finally, if an interpolated expression is followed by a `parts` string that
starts with a formatting specifier, the expression is formatted according to
that specifier. All specifiers allowed in Java format strings are handled, and
in the same way they are treated in Java.

For example:

```scala
val height = 1.9d
val name = "James"
println(f"$name%s is $height%2.2f meters tall")  // James is 1.90 meters tall
```

* Exceptions thrown
  * IllegalArgumentException if the number of `parts` in the enclosing
     `StringContext` does not exceed the number of arguments `arg` by exactly 1.
    if a `parts` string contains a backslash ( `\` ) character that does not
    start a valid escape sequence. Note: The `f` method works by assembling a
    format string from all the `parts` strings and using
     `java.lang.String.format` to format all arguments with that format string.
    The format string is obtained by concatenating all `parts` strings, and
    performing two transformations:

    1. Let a _formatting position_ be a start of any `parts` string except the
       first one. If a formatting position does not refer to a `%` character
       (which is assumed to start a format specifier), then the string format
       specifier `%s` is inserted. 2. Any `%` characters not in formatting
       positions must begin one of the conversions `%%` (the literal percent) or
        `%n` (the platform-specific line separator).


(defined at scala.StringContext)


### `def raw(args: Any*): String`                                            ###

The raw string interpolator.

It inserts its arguments between corresponding parts of the string context. As
opposed to the simple string interpolator `s` , this one does not treat standard
escape sequences as defined in the Scala specification.

For example, the raw processed string `raw"a\nb"` is equal to the scala string
 `"a\\nb"` .

 _Note:_ Even when using the raw interpolator, Scala will preprocess unicode
escapes. For example:

```scala
scala> raw"\u0023"
res0: String = #
```

* Exceptions thrown
  * IllegalArgumentException if the number of `parts` in the enclosing
     `StringContext` does not exceed the number of arguments `arg` by exactly 1.

(defined at scala.StringContext)


### `def s(args: Any*): String`                                              ###

The simple string interpolator.

It inserts its arguments between corresponding parts of the string context. It
also treats standard escape sequences as defined in the Scala specification.
Here's an example of usage:

```scala
val name = "James"
println(s"Hello, $name")  // Hello, James
```

In this example, the expression $name is replaced with the `toString` of the
variable `name` . The `s` interpolator can take the `toString` of any arbitrary
expression within a `${}` block, for example:

```scala
println(s"1 + 1 = ${1 + 1}")
```

will print the string `1 + 1 = 2` .

* Exceptions thrown
  * IllegalArgumentException if the number of `parts` in the enclosing
     `StringContext` does not exceed the number of arguments `arg` by exactly 1.
    StringContext.InvalidEscapeException if a `parts` string contains a
    backslash ( `\` ) character that does not start a valid escape sequence.

(defined at scala.StringContext)


### `def standardInterpolator(process: (String) ⇒ String, args: Seq[Any]): String` ###
(defined at scala.StringContext)
