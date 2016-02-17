
#                         scala.util.control.Exception                         #

```scala
object Exception
```

Classes representing the components of exception handling. Each class is
independently composable. Some example usages:

```scala
import scala.util.control.Exception._
import java.net._

val s = "http://www.scala-lang.org/"
val x1 = catching(classOf[MalformedURLException]) opt new URL(s)
val x2 = catching(classOf[MalformedURLException], classOf[NullPointerException]) either new URL(s)
```

This class differs from `scala.util.Try` in that it focuses on composing
exception handlers rather than composing behavior. All behavior should be
composed first and fed to a `Catch` object using one of the `opt` or `either`
methods.

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class By[T, R] extends AnyRef`                                          ###

Returns a partially constructed `Catch` object, which you must give an exception
handler function as an argument to `by` . Example:

```scala
handling(ex1, ex2) by (_.printStackTrace)
```

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


### `class Catch[+T] extends Described`                                      ###

A container class for catch/finally logic.

Pass a different value for rethrow if you want to probably unwisely allow
catching control exceptions and other throwables which the rest of the world may
expect to get through.

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


### `type Catcher[+T] = PartialFunction[Throwable, T]`                       ###


### `trait Described extends AnyRef`                                         ###

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


### `class Finally extends Described`                                        ###

A container class for finally code.

* Source
  * [Exception.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Exception.scala#L1)


--------------------------------------------------------------------------------
                Value Members From scala.util.control.Exception
--------------------------------------------------------------------------------


### `final def allCatch[T]: Catch[T]`                                        ###

A `Catch` object which catches everything.

(defined at scala.util.control.Exception)


### `final def allCatcher[T]: Catcher[T]`                                    ###

(defined at scala.util.control.Exception)


### `def catchingPromiscuously[T](c: Catcher[T]): Catch[T]`                  ###

(defined at scala.util.control.Exception)


### `def catchingPromiscuously[T](exceptions: Class[_]*): Catch[T]`          ###

Creates a `Catch` object which will catch any of the supplied exceptions. Unlike
"catching" which filters out those in shouldRethrow, this one will catch
whatever you ask of it: `ControlThrowable` , `InterruptedException` ,
 `OutOfMemoryError` , you name it.

(defined at scala.util.control.Exception)


### `def catching[T](c: Catcher[T]): Catch[T]`                               ###

(defined at scala.util.control.Exception)


### `def catching[T](exceptions: Class[_]*): Catch[T]`                       ###

Creates a `Catch` object which will catch any of the supplied exceptions. Since
the returned `Catch` object has no specific logic defined and will simply
rethrow the exceptions it catches, you will typically want to call `opt` or
 `either` on the return value, or assign custom logic by calling "withApply".

Note that `Catch` objects automatically rethrow `ControlExceptions` and others
which should only be caught in exceptional circumstances. If you really want to
catch exactly what you specify, use `catchingPromiscuously` instead.

(defined at scala.util.control.Exception)


### `def failAsValue[T](exceptions: Class[_]*)(value: ⇒ T): Catch[T]`        ###

Creates a `Catch` object which maps all the supplied exceptions to the given
value.

(defined at scala.util.control.Exception)


### `def failing[T](exceptions: Class[_]*): Catch[Option[T]]`                ###

Creates a `Catch` object which maps all the supplied exceptions to `None` .

(defined at scala.util.control.Exception)


### `def handling[T](exceptions: Class[_]*): By[(Throwable) ⇒ T, Catch[T]]`  ###

(defined at scala.util.control.Exception)


### `def ignoring(exceptions: Class[_]*): Catch[Unit]`                       ###

Creates a `Catch` object which catches and ignores any of the supplied
exceptions.

(defined at scala.util.control.Exception)


### `def mkCatcher[Ex <: Throwable, T](isDef: (Ex) ⇒ Boolean, f: (Ex) ⇒ T)(implicit arg0: ClassTag[Ex]): Catcher[T]` ###

(defined at scala.util.control.Exception)


### `def mkThrowableCatcher[T](isDef: (Throwable) ⇒ Boolean, f: (Throwable) ⇒ T): Catcher[T]` ###

(defined at scala.util.control.Exception)


### `final val noCatch: Catch[Nothing]`                                      ###

The empty `Catch` object.

(defined at scala.util.control.Exception)


### `final def nonFatalCatch[T]: Catch[T]`                                   ###

A `Catch` object which catches non-fatal exceptions.

(defined at scala.util.control.Exception)


### `final def nonFatalCatcher[T]: Catcher[T]`                               ###

(defined at scala.util.control.Exception)


### `final val nothingCatcher: Catcher[Nothing]`                             ###

(defined at scala.util.control.Exception)


### `def shouldRethrow(x: Throwable): Boolean`                               ###

!!! Not at all sure of every factor which goes into this, and/or whether we need
multiple standard variations.

(defined at scala.util.control.Exception)


### `implicit def throwableSubtypeToCatcher[Ex <: Throwable, T](pf: PartialFunction[Ex, T])(implicit arg0: ClassTag[Ex]): Catcher[T]` ###

(defined at scala.util.control.Exception)


### `def ultimately[T](body: ⇒ Unit): Catch[T]`                              ###

Returns a `Catch` object with no catch logic and the argument as `Finally` .

(defined at scala.util.control.Exception)


### `def unwrapping[T](exceptions: Class[_]*): Catch[T]`                     ###

Creates a `Catch` object which unwraps any of the supplied exceptions.
(defined at scala.util.control.Exception)
