
#                               scala.Function5                               #

```scala
trait Function5[-T1, -T2, -T3, -T4, -T5, +R] extends AnyRef
```

A function of 5 parameters.

* Self Type
  * (T1, T2, T3, T4, T5) ⇒ R
* Source
  * [Function5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function5.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function5
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3, v4: T4, v5: T5): R`          ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

(defined at scala.Function5)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function5
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ (T4) ⇒ (T5) ⇒ R`                      ###

Creates a curried version of this function.

* returns
  * a function `f` such that
     `f(x1)(x2)(x3)(x4)(x5) == apply(x1, x2, x3, x4, x5)`

* Annotations
  * @ unspecialized ()

(defined at scala.Function5)


### `def tupled: ((T1, T2, T3, T4, T5)) ⇒ R`                                 ###

Creates a tupled version of this function: instead of 5 arguments, it accepts a
single scala.Tuple5 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3, x4, x5)) == f(Tuple5(x1, x2, x3, x4, x5)) == apply(x1, x2, x3, x4, x5)`

* Annotations
  * @ unspecialized ()
(defined at scala.Function5)
