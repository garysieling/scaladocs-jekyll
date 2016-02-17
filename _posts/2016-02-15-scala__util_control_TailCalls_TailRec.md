
#                     scala.util.control.TailCalls.TailRec                     #

```scala
abstract class TailRec[+A] extends AnyRef
```

This class represents a tailcalling computation

* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


--------------------------------------------------------------------------------
        Instance Constructors From scala.util.control.TailCalls.TailRec
--------------------------------------------------------------------------------


### `new TailRec()`                                                          ###

(defined at scala.util.control.TailCalls.TailRec)


--------------------------------------------------------------------------------
            Value Members From scala.util.control.TailCalls.TailRec
--------------------------------------------------------------------------------


### `final def flatMap[B](f: (A) ⇒ TailRec[B]): TailRec[B]`                  ###

Continue the computation with `f` and merge the trampolining of this computation
with that of `f` .

(defined at scala.util.control.TailCalls.TailRec)


### `final def map[B](f: (A) ⇒ B): TailRec[B]`                               ###

Continue the computation with `f` .

(defined at scala.util.control.TailCalls.TailRec)


### `final def resume: scala.Either[() ⇒ TailRec[A], A]`                     ###

Returns either the next step of the tailcalling computation, or the result if
there are no more steps.

* Annotations
  * @ tailrec ()
(defined at scala.util.control.TailCalls.TailRec)
