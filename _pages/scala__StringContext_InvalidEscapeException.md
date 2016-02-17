
#                  scala.StringContext.InvalidEscapeException                  #

```scala
class InvalidEscapeException extends IllegalArgumentException
```

An exception that is thrown if a string contains a backslash ( `\` ) character
that does not start a valid escape sequence.

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)


--------------------------------------------------------------------------------
                     Value Members From java.lang.Throwable
--------------------------------------------------------------------------------


### `final def addSuppressed(arg0: java.lang.Throwable): Unit`               ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def fillInStackTrace(): java.lang.Throwable`                            ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def getCause(): java.lang.Throwable`                                    ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `final def getSuppressed(): Array[java.lang.Throwable]`                  ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def initCause(arg0: java.lang.Throwable): java.lang.Throwable`          ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def printStackTrace(arg0: PrintStream): Unit`                           ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def printStackTrace(arg0: PrintWriter): Unit`                           ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


### `def setStackTrace(arg0: Array[StackTraceElement]): Unit`                ###

* Definition Classes
  * Throwable

(defined at java.lang.Throwable)


--------------------------------------------------------------------------------
     Instance Constructors From scala.StringContext.InvalidEscapeException
--------------------------------------------------------------------------------


### `new InvalidEscapeException(str: String, index: Int)`                    ###

* str
  * The offending string
* index
  * The index of the offending backslash character in `str` .
(defined at scala.StringContext.InvalidEscapeException)
