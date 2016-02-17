
#                               scala.Responder                               #

```scala
object Responder extends Serializable
```

This object contains utility methods to build responders.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This object will be removed
* Source
  * [Responder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Responder.scala#L1)
* Version
  * 1.0
* Since
  * 2.1
* See also
  * class Responder


--------------------------------------------------------------------------------
                       Value Members From scala.Responder
--------------------------------------------------------------------------------


### `def constant[A](x: A): Responder[A]`                                    ###

Creates a responder that answer continuations with the constant `a` .

(defined at scala.Responder)


### `def exec[A](x: ⇒ Unit): Boolean`                                        ###

Executes `x` and returns `true` , useful as syntactic convenience in for
comprehensions.

(defined at scala.Responder)


### `def loopWhile[A](cond: ⇒ Boolean)(r: Responder[Unit]): Responder[Unit]` ###

(defined at scala.Responder)


### `def loop[A](r: Responder[Unit]): Responder[Nothing]`                    ###

(defined at scala.Responder)


### `def run[A](r: Responder[A]): Option[A]`                                 ###

Runs a responder, returning an optional result.
(defined at scala.Responder)
