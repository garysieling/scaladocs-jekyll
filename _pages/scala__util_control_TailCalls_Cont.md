
#                      scala.util.control.TailCalls.Cont                      #

```scala
case class Cont[A, B](a: TailRec[A], f: (A) ⇒ TailRec[B]) extends TailRec[B] with Product with Serializable
```

Internal class representing a continuation with function A => TailRec[B]. It is
needed for the flatMap to be implemented.

* Attributes
  * protected
* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


--------------------------------------------------------------------------------
          Instance Constructors From scala.util.control.TailCalls.Cont
--------------------------------------------------------------------------------


### `new Cont(a: TailRec[A], f: (A) ⇒ TailRec[B])`                           ###

(defined at scala.util.control.TailCalls.Cont)


--------------------------------------------------------------------------------
              Value Members From scala.util.control.TailCalls.Cont
--------------------------------------------------------------------------------


### `val a: TailRec[A]`                                                      ###

(defined at scala.util.control.TailCalls.Cont)


### `val f: (A) ⇒ TailRec[B]`                                                ###

(defined at scala.util.control.TailCalls.Cont)


--------------------------------------------------------------------------------
            Value Members From scala.util.control.TailCalls.TailRec
--------------------------------------------------------------------------------


### `final def flatMap[B](f: (B) ⇒ TailRec[B]): TailRec[B]`                  ###

Continue the computation with `f` and merge the trampolining of this computation
with that of `f` .

* Definition Classes
  * TailRec

(defined at scala.util.control.TailCalls.TailRec)


### `final def map[B](f: (B) ⇒ B): TailRec[B]`                               ###

Continue the computation with `f` .

* Definition Classes
  * TailRec

(defined at scala.util.control.TailCalls.TailRec)


### `final def result: B`                                                    ###

Returns the result of the tailcalling computation.

* Definition Classes
  * TailRec
* Annotations
  * @ tailrec ()

(defined at scala.util.control.TailCalls.TailRec)


### `final def resume: scala.Either[() ⇒ TailRec[B], B]`                     ###

Returns either the next step of the tailcalling computation, or the result if
there are no more steps.

* Definition Classes
  * TailRec
* Annotations
  * @ tailrec ()
(defined at scala.util.control.TailCalls.TailRec)
