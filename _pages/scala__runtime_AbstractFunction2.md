
#                       scala.runtime.AbstractFunction2                       #

```scala
abstract class AbstractFunction2[-T1, -T2, +R] extends (T1, T2) ⇒ R
```

* Source
  * [AbstractFunction2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction2.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function2
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2): R`                                  ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

* Definition Classes
  * Function2

(defined at scala.Function2)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function2
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ R`                                           ###

Creates a curried version of this function.

* returns
  * a function `f` such that `f(x1)(x2) == apply(x1, x2)`

* Definition Classes
  * Function2
* Annotations
  * @ unspecialized ()

(defined at scala.Function2)


### `def tupled: ((T1, T2)) ⇒ R`                                             ###

Creates a tupled version of this function: instead of 2 arguments, it accepts a
single scala.Tuple2 argument.

* returns
  * a function `f` such that
     `f((x1, x2)) == f(Tuple2(x1, x2)) == apply(x1, x2)`

* Definition Classes
  * Function2
* Annotations
  * @ unspecialized ()

(defined at scala.Function2)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction2
--------------------------------------------------------------------------------


### `new AbstractFunction2()`                                                ###
(defined at scala.runtime.AbstractFunction2)
