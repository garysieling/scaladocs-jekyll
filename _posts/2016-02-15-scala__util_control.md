
#                              scala.util.control                              #

```scala
package control
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Breaks extends AnyRef`                                            ###

A class that can be instantiated for the break control abstraction. Example
usage:

```scala
val mybreaks = new Breaks
import mybreaks.{break, breakable}

breakable {
  for (...) {
    if (...) break()
  }
}
```

Calls to break from one instantiation of `Breaks` will never target breakable
objects of some other instantiation.

* Source
  * [Breaks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Breaks.scala#L1)


### `trait ControlThrowable extends Throwable with NoStackTrace`             ###

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


### `trait NoStackTrace extends Throwable`                                   ###

A trait for exceptions which, for efficiency reasons, do not fill in the stack
trace. Stack trace suppression can be disabled on a global basis via a system
property wrapper in scala.sys.SystemProperties.

* Source
  * [NoStackTrace.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/NoStackTrace.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Breaks extends Breaks`                                           ###

An object that can be used for the break control abstraction. Example usage:

```scala
import Breaks.{break, breakable}

breakable {
  for (...) {
    if (...) break
  }
}
```

* Source
  * [Breaks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Breaks.scala#L1)


### `object Exception`                                                       ###

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


### `object NoStackTrace extends Serializable`                               ###

* Source
  * [NoStackTrace.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/NoStackTrace.scala#L1)


### `object NonFatal`                                                        ###

Extractor of non-fatal Throwables. Will not match fatal errors like
 `VirtualMachineError` (for example, `OutOfMemoryError` and
 `StackOverflowError` , subclasses of `VirtualMachineError` ), `ThreadDeath` ,
 `LinkageError` , `InterruptedException` , `ControlThrowable` .

Note that scala.util.control.ControlThrowable, an internal Throwable, is not
matched by `NonFatal` (and would therefore be thrown).

For example, all harmless Throwables can be caught by:

```scala
try {
  // dangerous stuff
} catch {
  case NonFatal(e) => log.error(e, "Something not that bad.")
 // or
  case e if NonFatal(e) => log.error(e, "Something not that bad.")
}
```

* Source
  * [NonFatal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/NonFatal.scala#L1)


### `object TailCalls`                                                       ###

Methods exported by this object implement tail calls via trampolining. Tail
calling methods have to return their result using `done` or call the next method
using `tailcall` . Both return a `TailRec` object. The result of evaluating a
tailcalling function can be retrieved from a `Tailrec` value using method
 `result` . Implemented as described in "Stackless Scala with Free Monads"
http://blog.higher-order.com/assets/trampolines.pdf

Here's a usage example:

```scala
import scala.util.control.TailCalls._

def isEven(xs: List[Int]): TailRec[Boolean] =
  if (xs.isEmpty) done(true) else tailcall(isOdd(xs.tail))

def isOdd(xs: List[Int]): TailRec[Boolean] =
 if (xs.isEmpty) done(false) else tailcall(isEven(xs.tail))

isEven((1 to 100000).toList).result

def fib(n: Int): TailRec[Int] =
  if (n < 2) done(n) else for {
    x <- tailcall(fib(n - 1))
    y <- tailcall(fib(n - 2))
  } yield (x + y)

fib(40).result
```

* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)

