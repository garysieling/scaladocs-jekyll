
#                      scala.util.control.TailCalls.Call                      #

```scala
case class Call[A](rest: () ⇒ TailRec[A]) extends TailRec[A] with Product with Serializable
```

Internal class representing a tailcall

* Attributes
  * protected
* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


--------------------------------------------------------------------------------
          Instance Constructors From scala.util.control.TailCalls.Call
--------------------------------------------------------------------------------


### `new Call(rest: () ⇒ TailRec[A])`                                        ###

(defined at scala.util.control.TailCalls.Call)


--------------------------------------------------------------------------------
              Value Members From scala.util.control.TailCalls.Call
--------------------------------------------------------------------------------


### `val rest: () ⇒ TailRec[A]`                                              ###

(defined at scala.util.control.TailCalls.Call)


--------------------------------------------------------------------------------
            Value Members From scala.util.control.TailCalls.TailRec
--------------------------------------------------------------------------------


### `final def flatMap[B](f: (A) ⇒ TailRec[B]): TailRec[B]`                  ###

Continue the computation with `f` and merge the trampolining of this computation
with that of `f` .

* Definition Classes
  * TailRec

(defined at scala.util.control.TailCalls.TailRec)


### `final def map[B](f: (A) ⇒ B): TailRec[B]`                               ###

Continue the computation with `f` .

* Definition Classes
  * TailRec

(defined at scala.util.control.TailCalls.TailRec)


### `final def resume: scala.Either[() ⇒ TailRec[A], A]`                     ###

Returns either the next step of the tailcalling computation, or the result if
there are no more steps.

* Definition Classes
  * TailRec
* Annotations
  * @ tailrec ()
(defined at scala.util.control.TailCalls.TailRec)
