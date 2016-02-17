
#                          scala.util.control.Breaks                          #

```scala
class Breaks extends AnyRef
```

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


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `sealed trait TryBlock[T] extends AnyRef`                                ###

* Source
  * [Breaks.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/Breaks.scala#L1)


--------------------------------------------------------------------------------
              Instance Constructors From scala.util.control.Breaks
--------------------------------------------------------------------------------


### `new Breaks()`                                                           ###

(defined at scala.util.control.Breaks)


--------------------------------------------------------------------------------
                  Value Members From scala.util.control.Breaks
--------------------------------------------------------------------------------


### `def breakable(op: ⇒ Unit): Unit`                                        ###

A block from which one can exit with a `break` . The `break` may be executed
further down in the call stack provided that it is called on the exact same
instance of `Breaks` .

(defined at scala.util.control.Breaks)


### `def tryBreakable[T](op: ⇒ T): TryBlock[T]`                              ###

This variant enables the execution of a code block in case of a `break()` :

```scala
tryBreakable {
  for (...) {
    if (...) break()
  }
} catchBreak {
  doCleanup()
}
```
(defined at scala.util.control.Breaks)
