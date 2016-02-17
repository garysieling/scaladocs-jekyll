
#                       scala.runtime.AbstractFunction4                       #

```scala
abstract class AbstractFunction4[-T1, -T2, -T3, -T4, +R] extends (T1, T2, T3, T4) ⇒ R
```

* Source
  * [AbstractFunction4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction4.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function4
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4): R`                  ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function4

(defined at scala.Function4)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function4
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ R`                             ###

Creates a curried version of this function.

* returns
  * a function `f` such that `f(x1)(x2)(x3)(x4) == apply(x1, x2, x3, x4)`

* Definition Classes
  * Function4
* Annotations
  * @ unspecialized ()

(defined at scala.Function4)


### `def tupled: ((T1, T2, T3, T4)) ⇒ R`                                     ###

Creates a tupled version of this function: instead of 4 arguments, it accepts a
single scala.Tuple4 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4)) == f(Tuple4(x1, x2, x3, x4)) == apply(x1, x2, x3, x4)`

* Definition Classes
  * Function4
* Annotations
  * @ unspecialized ()

(defined at scala.Function4)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction4
--------------------------------------------------------------------------------


### `new AbstractFunction4()`                                                ###
(defined at scala.runtime.AbstractFunction4)
