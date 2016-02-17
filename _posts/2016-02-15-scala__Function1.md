
#                               scala.Function1                               #

```scala
trait Function1[-T1, +R] extends AnyRef
```

A function of 1 parameter.

In the following example, the definition of succ is a shorthand for the
anonymous class definition anonfun1:

```scala
object Main extends App {
   val succ = (x: Int) => x + 1
   val anonfun1 = new Function1[Int, Int] {
     def apply(x: Int): Int = x + 1
   }
   assert(succ(0) == anonfun1(0))
}
```

Note that the difference between `Function1` and scala.PartialFunction is that
the latter can specify inputs which it will not handle.

* Self Type
  * (T1) ⇒ R
* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Function1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function1.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function1
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1): R`                                          ###

Apply the body of this function to the argument.

* returns
  * the result of function application.

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

* Annotations
  * @ unspecialized ()
(defined at scala.Function1)
