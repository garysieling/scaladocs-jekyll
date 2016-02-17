
#                          scala.util.control.Breaks                          #

```scala
object Breaks extends Breaks
```

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


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `sealed trait TryBlock[T] extends AnyRef`                                ###

* Definition Classes
  * Breaks


--------------------------------------------------------------------------------
                  Value Members From scala.util.control.Breaks
--------------------------------------------------------------------------------


### `def breakable(op: ⇒ Unit): Unit`                                        ###

A block from which one can exit with a `break` . The `break` may be executed
further down in the call stack provided that it is called on the exact same
instance of `Breaks` .

* Definition Classes
  * Breaks

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

* Definition Classes
  * Breaks
(defined at scala.util.control.Breaks)
