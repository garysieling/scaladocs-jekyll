
#                       scala.runtime.AbstractFunction6                       #

```scala
abstract class AbstractFunction6[-T1, -T2, -T3, -T4, -T5, -T6, +R] extends (T1, T2, T3, T4, T5, T6) ⇒ R
```

* Source
  * [AbstractFunction6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction6.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function6
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5, v6: T6): R`  ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function6

(defined at scala.Function6)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function6
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ (T6) ⇒ R`               ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5)(x6) == apply(x1, x2, x3, x4, x5, x6)`

* Definition Classes
  * Function6
* Annotations
  * @ unspecialized ()

(defined at scala.Function6)


### `def tupled: ((T1, T2, T3, T4, T5, T6)) ⇒ R`                             ###

Creates a tupled version of this function: instead of 6 arguments, it accepts a
single scala.Tuple6 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5, x6)) == f(Tuple6(x1, x2, x3, x4, x5, x6)) == apply(x1, x2, x3, x4, x5, x6)`

* Definition Classes
  * Function6
* Annotations
  * @ unspecialized ()

(defined at scala.Function6)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction6
--------------------------------------------------------------------------------


### `new AbstractFunction6()`                                                ###
(defined at scala.runtime.AbstractFunction6)
