
#                     scala.util.control.ControlThrowable                     #

```scala
trait ControlThrowable extends Throwable with NoStackTrace
```

A marker trait indicating that the `Throwable` it is mixed into is intended for
flow control.

Note that `Throwable` subclasses which extend this trait may extend any other
 `Throwable` subclass (eg. `RuntimeException` ) and are not required to extend
 `Throwable` directly.

Instances of `Throwable` subclasses marked in this way should not normally be
caught. Where catch-all behaviour is required `ControlThrowable` should be
propagated, for example:

```scala
import scala.util.control.ControlThrowable

try {
  // Body might throw arbitrarily
} catch {
  case c: ControlThrowable => throw c // propagate
  case t: Exception        => log(t)  // log and suppress
}
```

* Source
  * [ControlThrowable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/ControlThrowable.scala#L1)


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
