
#                       scala.runtime.AbstractFunction10                       #

```scala
abstract class AbstractFunction10[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, +R] extends (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10) ⇒ R
```

* Source
  * [AbstractFunction10.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction10.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function10
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7, v8: T8, v9: T9, v10: T10): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function10

(defined at scala.Function10)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function10
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ (T8) ⇒ (T9) ⇒ (T10) ⇒ R` ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8)(x9)(x10) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)`

* Definition Classes
  * Function10
* Annotations
  * @ unspecialized ()

(defined at scala.Function10)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)) ⇒ R`            ###

Creates a tupled version of this function: instead of 10 arguments, it accepts a
single scala.Tuple10 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)) == f(Tuple10(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)) == apply(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)`

* Definition Classes
  * Function10
* Annotations
  * @ unspecialized ()

(defined at scala.Function10)


--------------------------------------------------------------------------------
          Instance Constructors From scala.runtime.AbstractFunction10
--------------------------------------------------------------------------------


### `new AbstractFunction10()`                                               ###
(defined at scala.runtime.AbstractFunction10)
