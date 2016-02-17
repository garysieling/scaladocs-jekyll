
#                                  scala.Any                                  #

```scala
abstract class Any
```

Class `Any` is the root of the Scala class hierarchy. Every class in a Scala
execution environment inherits directly or indirectly from this class.

Starting with Scala 2.10 it is possible to directly extend `Any` using _
universal traits_ . A _universal trait_ is a trait that extends `Any` , only has
 `def` s as members, and does no initialization.

The main use case for universal traits is to allow basic inheritance of methods
for value classes. For example,

```scala
trait Printable extends Any {
  def print(): Unit = println(this)
}
class Wrapper(val underlying: Int) extends AnyVal with Printable

val w = new Wrapper(3)
w.print()
```

See the
[Value Classes and Universal Traits](http://docs.scala-lang.org/overviews/core/value-classes.html)
for more details on the interplay of universal traits and value classes.

