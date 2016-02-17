
#                          scala.annotation.elidable                          #

```scala
final class elidable extends Annotation with StaticAnnotation
```

An annotation for methods whose bodies may be excluded from compiler-generated
bytecode.

Behavior is influenced by passing `-Xelide-below <arg>` to `scalac` . Calls to
methods marked elidable (as well as the method body) will be omitted from
generated code if the priority given the annotation is lower than that given on
the command line.

```scala
@elidable(123)           // annotation priority
scalac -Xelide-below 456 // command line priority
```

The method call will be replaced with an expression which depends on the type of
the elided expression. In decreasing order of precedence:

```scala
Unit            ()
Boolean         false
T <: AnyVal     0
T >: Null       null
T >: Nothing    Predef.???
```

Complete example:

```scala
import scala.annotation._, elidable._
object Test extends App {
  def expensiveComputation(): Int = { Thread.sleep(1000) ; 172 }

  @elidable(WARNING) def warning(msg: String) = println(msg)
  @elidable(FINE) def debug(msg: String)      = println(msg)
  @elidable(FINE) def computedValue           = expensiveComputation()

  warning("Warning! Danger! Warning!")
  debug("Debug! Danger! Debug!")
  println("I computed a value: " + computedValue)
}
% scalac example.scala && scala Test
Warning! Danger! Warning!
Debug! Danger! Debug!
I computed a value: 172

// INFO lies between WARNING and FINE
% scalac -Xelide-below INFO example.scala && scala Test
Warning! Danger! Warning!
I computed a value: 0
```

* Source
  * [elidable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/elidable.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
              Instance Constructors From scala.annotation.elidable
--------------------------------------------------------------------------------


### `new elidable(level: Int)`                                               ###
(defined at scala.annotation.elidable)
