
#                       scala.runtime.AbstractFunction18                       #

```scala
abstract class AbstractFunction18[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, +R] extends (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18) ⇒ R
```

* Source
  * [AbstractFunction18.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction18.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function18
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7, v8: T8, v9: T9, v10: T10, v11: T11, v12: T12, v13: T13, v14: T14, v15: T15, v16: T16, v17: T17, v18: T18): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function18

(defined at scala.Function18)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function18
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ (T8) ⇒ (T9) ⇒ (T10) ⇒ (T11) ⇒ (T12) ⇒ (T13) ⇒ (T14) ⇒ (T15) ⇒ (T16) ⇒ (T17) ⇒ (T18) ⇒ R` ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8)(x9)(x10)(x11)(x12)(x13)(x14)(x15)(x16)(x17)(x18) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18)`

* Definition Classes
  * Function18
* Annotations
  * @ unspecialized ()

(defined at scala.Function18)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18)) ⇒ R` ###

Creates a tupled version of this function: instead of 18 arguments, it accepts a
single scala.Tuple18 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18)) == f(Tuple18(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18)) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18)`

* Definition Classes
  * Function18
* Annotations
  * @ unspecialized ()

(defined at scala.Function18)


--------------------------------------------------------------------------------
          Instance Constructors From scala.runtime.AbstractFunction18
--------------------------------------------------------------------------------


### `new AbstractFunction18()`                                               ###
(defined at scala.runtime.AbstractFunction18)
