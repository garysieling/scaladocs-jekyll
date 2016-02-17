
#                             scala.StringContext                             #

```scala
object StringContext extends Serializable
```

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class InvalidEscapeException extends IllegalArgumentException`          ###

An exception that is thrown if a string contains a backslash ( `\` ) character
that does not start a valid escape sequence.

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)


--------------------------------------------------------------------------------
                     Value Members From scala.StringContext
--------------------------------------------------------------------------------


### `def processEscapes(str: String): String`                                ###

Treats escapes, but disallows octal escape sequences.

(defined at scala.StringContext)


### `def treatEscapes(str: String): String`                                  ###

Expands standard Scala escape sequences in a string. Escape sequences are:
control: `\b` , `\t` , `\n` , `\f` , `\r` escape: `\\` , `\"` , `\'` octal:
 `\d`  `\dd`  `\ddd` where `d` is an octal digit between `0` and `7` .

* str
  * A string that may contain escape sequences
* returns
  * The string with all escape sequences expanded.
(defined at scala.StringContext)
