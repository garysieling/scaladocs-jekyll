
#                        scala.UninitializedFieldError                        #

```scala
final case class UninitializedFieldError(msg: String) extends RuntimeException with Product with Serializable
```

This class implements errors which are thrown whenever a field is used before it
has been initialized.

Such runtime checks are not emitted by default. They can be enabled by the
 `-Xcheckinit` compiler option.

* Source
  * [UninitializedFieldError.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/UninitializedFieldError.scala#L1)
* Since
  * 2.7


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
            Instance Constructors From scala.UninitializedFieldError
--------------------------------------------------------------------------------


### `new UninitializedFieldError(obj: Any)`                                  ###
(defined at scala.UninitializedFieldError)
