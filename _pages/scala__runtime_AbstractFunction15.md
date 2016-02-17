
#                       scala.runtime.AbstractFunction15                       #

```scala
abstract class AbstractFunction15[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, +R] extends (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15) ⇒ R
```

* Source
  * [AbstractFunction15.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction15.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function15
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7, v8: T8, v9: T9, v10: T10, v11: T11, v12: T12, v13: T13, v14: T14, v15: T15): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function15

(defined at scala.Function15)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function15
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ (T8) ⇒ (T9) ⇒ (T10) ⇒ (T11) ⇒ (T12) ⇒ (T13) ⇒ (T14) ⇒ (T15) ⇒ R` ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8)(x9)(x10)(x11)(x12)(x13)(x14)(x15) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15)`

* Definition Classes
  * Function15
* Annotations
  * @ unspecialized ()

(defined at scala.Function15)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)) ⇒ R` ###

Creates a tupled version of this function: instead of 15 arguments, it accepts a
single scala.Tuple15 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15)) == f(Tuple15(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15)) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15)`

* Definition Classes
  * Function15
* Annotations
  * @ unspecialized ()

(defined at scala.Function15)


--------------------------------------------------------------------------------
          Instance Constructors From scala.runtime.AbstractFunction15
--------------------------------------------------------------------------------


### `new AbstractFunction15()`                                               ###
(defined at scala.runtime.AbstractFunction15)
