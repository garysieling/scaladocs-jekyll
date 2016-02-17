
#                       scala.runtime.AbstractFunction5                       #

```scala
abstract class AbstractFunction5[-T1, -T2, -T3, -T4, -T5, +R] extends (T1, T2, T3, T4, T5) ⇒ R
```

* Source
  * [AbstractFunction5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction5.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function5
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5): R`          ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function5

(defined at scala.Function5)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function5
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ R`                      ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5) == apply(x1, x2, x3, x4, x5)`

* Definition Classes
  * Function5
* Annotations
  * @ unspecialized ()

(defined at scala.Function5)


### `def tupled: ((T1, T2, T3, T4, T5)) ⇒ R`                                 ###

Creates a tupled version of this function: instead of 5 arguments, it accepts a
single scala.Tuple5 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5)) == f(Tuple5(x1, x2, x3, x4, x5)) == apply(x1, x2, x3, x4, x5)`

* Definition Classes
  * Function5
* Annotations
  * @ unspecialized ()

(defined at scala.Function5)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction5
--------------------------------------------------------------------------------


### `new AbstractFunction5()`                                                ###
(defined at scala.runtime.AbstractFunction5)
