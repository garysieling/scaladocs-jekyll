
#                               scala.Function2                               #

```scala
trait Function2[-T1, -T2, +R] extends AnyRef
```

A function of 2 parameters.

In the following example, the definition of max is a shorthand for the anonymous
class definition anonfun2:

```scala
object Main extends App {
   val max = (x: Int, y: Int) => if (x < y) y else x

   val anonfun2 = new Function2[Int, Int, Int] {
     def apply(x: Int, y: Int): Int = if (x < y) y else x
   }
   assert(max(0, 1) == anonfun2(0, 1))
}
```

* Self Type
  * (T1, T2) ⇒ R
* Source
  * [Function2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function2.scala#L1)


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function2
--------------------------------------------------------------------------------


### `abstract def apply(v1: T1, v2: T2): R`                                  ###

Apply the body of this function to the arguments.

* returns
  * the result of function application.

(defined at scala.Function2)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function2
--------------------------------------------------------------------------------


### `def curried: (T1) ⇒ (T2) ⇒ R`                                           ###

Creates a curried version of this function.

* returns
  * a function `f` such that `f(x1)(x2) == apply(x1, x2)`

* Annotations
  * @ unspecialized ()

(defined at scala.Function2)


### `def tupled: ((T1, T2)) ⇒ R`                                             ###

Creates a tupled version of this function: instead of 2 arguments, it accepts a
single scala.Tuple2 argument.

* returns
  * a function `f` such that
     `f((x1, x2)) == f(Tuple2(x1, x2)) == apply(x1, x2)`

* Annotations
  * @ unspecialized ()
(defined at scala.Function2)
