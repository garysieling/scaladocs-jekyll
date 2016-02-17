
#                       scala.runtime.AbstractFunction1                       #

```scala
abstract class AbstractFunction1[-T1, +R] extends (T1) ⇒ R
```

* Source
  * [AbstractFunction1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractFunction1.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function1
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1): R`                                          ###

Apply the body of this function to the argument.

* returns
  * the result of function application.

* Definition Classes
  * Function1

(defined at scala.Function1)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def andThen[A](g: (R) ⇒ A): (T1) ⇒ A`                                   ###

Composes two instances of Function1 in a new Function1, with this function
applied first.

* A
  * the result type of function `g`
* g
  * a function R => A
* returns
  * a new function `f` such that `f(x) == g(apply(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


### `def compose[A](g: (A) ⇒ T1): (A) ⇒ R`                                   ###

Composes two instances of Function1 in a new Function1, with this function
applied last.

* A
  * the type to which function `g` can be applied
* g
  * a function A => T1
* returns
  * a new function `f` such that `f(x) == apply(g(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


--------------------------------------------------------------------------------
           Instance Constructors From scala.runtime.AbstractFunction1
--------------------------------------------------------------------------------


### `new AbstractFunction1()`                                                ###
(defined at scala.runtime.AbstractFunction1)
