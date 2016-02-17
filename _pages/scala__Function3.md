
#                               scala.Function3                               #

```scala
trait Function3[-T1, -T2, -T3, +R] extends AnyRef
```

A function of 3 parameters.

* Self Type
  * (T1, T2, T3) ⇒ R
* Source
  * [Function3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function3.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function3
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2, v3: T3): R`                          ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

(defined at scala.Function3)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function3
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ (T3) ⇒ R`                                    ###

Creates a curried version of this function.

* returns
  * a function `f` such that `f(x1)(x2)(x3) == apply(x1, x2, x3)`

* Annotations
  * @ unspecialized ()

(defined at scala.Function3)


### `def tupled: ((T1, T2, T3)) ⇒ R`                                         ###

Creates a tupled version of this function: instead of 3 arguments, it accepts a
single scala.Tuple3 argument.

* returns
  * a function `f` such that
     `f((x1, x2, x3)) == f(Tuple3(x1, x2, x3)) == apply(x1, x2, x3)`

* Annotations
  * @ unspecialized ()
(defined at scala.Function3)
