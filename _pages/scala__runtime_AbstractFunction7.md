
#                       scala.runtime.AbstractFunction7                       #

```scala
abstract class AbstractFunction7[-T1, -T2, -T3, -T4, -T5, -T6, -T7, +R] extends (T1, T2, T3, T4, T5, T6, T7) ⇒ R
```

* Source
  * [AbstractFunction7.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction7.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function7
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6, v7: T7): R` ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function7

(defined at scala.Function7)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function7
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ (T7) ⇒ R`        ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6)(x7) == apply(x1, x2, x3, x4, x5, x6, x7)`

* Definition Classes
  * Function7
* Annotations
  * @ unspecialized ()

(defined at scala.Function7)


### `def tupled: ((T1, T2, T3, T4, T5, T6, T7)) ⇒ R`                         ###

Creates a tupled version of this function: instead of 7 arguments, it accepts a
single scala.Tuple7 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6, x7)) == f(Tuple7(x1, x2, x3, x4, x5, x6, x7)) == apply(x1, x2, x3, x4, x5, x6, x7)`

* Definition Classes
  * Function7
* Annotations
  * @ unspecialized ()

(defined at scala.Function7)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction7
--------------------------------------------------------------------------------


### `new AbstractFunction7()`                                                ###
(defined at scala.runtime.AbstractFunction7)
