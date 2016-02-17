
#                       scala.util.control.NoStackTrace                       #

```scala
trait NoStackTrace extends Throwable
```

A trait for exceptions which, for efficiency reasons, do not fill in the stack
trace. Stack trace suppression can be disabled on a global basis via a system
property wrapper in scala.sys.SystemProperties.

* Source
  * [NoStackTrace.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/NoStackTrace.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                     Value Members From java.lang.Throwable
--------------------------------------------------------------------------------


### `final def addSuppressed(arg0: java.lang.Throwable): Unit`               ###

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
