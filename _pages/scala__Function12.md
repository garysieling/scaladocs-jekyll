
#                               scala.Function12                               #

```scala
trait Function12[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, +R] extends AnyRef
```

A function of 12 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12) ⇒ R
* Source
  * [Function12.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function12.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function12
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7, v8: T8, v9: T9, v10: T10, v11: T11, v12: T12): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

(defined at scala.Function12)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function12
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ (T8) ⇒ (T9) ⇒ (T10) ⇒ (T11) ⇒ (T12) ⇒ R` ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8)(x9)(x10)(x11)(x12) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)`

* Annotations
  * @ unspecialized ()

(defined at scala.Function12)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)) ⇒ R`  ###

Creates a tupled version of this function: instead of 12 arguments, it accepts a
single scala.Tuple12 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)) == f(Tuple12(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)`

* Annotations
  * @ unspecialized ()
(defined at scala.Function12)
