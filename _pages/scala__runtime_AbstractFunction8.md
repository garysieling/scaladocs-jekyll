
#                       scala.runtime.AbstractFunction8                       #

```scala
abstract class AbstractFunction8[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, +R] extends (T1, T2, T3, T4, T5, T6, T7, T8) ⇒ R
```

* Source
  * [AbstractFunction8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction8.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function8
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7, v8: T8): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function8

(defined at scala.Function8)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function8
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ (T8) ⇒ R` ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8) == apply(x1, x2, x3, x4, x5, x6, x7, x8)`

* Definition Classes
  * Function8
* Annotations
  * @ unspecialized ()

(defined at scala.Function8)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7, T8)) ⇒ R`                     ###

Creates a tupled version of this function: instead of 8 arguments, it accepts a
single scala.Tuple8 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7, x8)) == f(Tuple8(x1, x2, x3, x4, x5, x6, x7, x8)) == apply(x1, x2, x3, x4, x5, x6, x7, x8)`

* Definition Classes
  * Function8
* Annotations
  * @ unspecialized ()

(defined at scala.Function8)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction8
--------------------------------------------------------------------------------


### `new AbstractFunction8()`                                                ###
(defined at scala.runtime.AbstractFunction8)
