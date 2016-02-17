
#                         scala.util.control.TailCalls                         #

```scala
object TailCalls
```

Methods exported by this object implement tail calls via trampolining. Tail
calling methods have to return their result using `done` or call the next method
using `tailcall` . Both return a `TailRec` object. The result of evaluating a
tailcalling function can be retrieved from a `Tailrec` value using method
 `result` . Implemented as described in "Stackless Scala with Free Monads"
http://blog.higher-order.com/assets/trampolines.pdf

Here's a usage example:

```scala
import scala.util.control.TailCalls._

def isEven(xs: List[Int]): TailRec[Boolean] =
  if (xs.isEmpty) done(true) else tailcall(isOdd(xs.tail))

def isOdd(xs: List[Int]): TailRec[Boolean] =
 if (xs.isEmpty) done(false) else tailcall(isEven(xs.tail))

isEven((1 to 100000).toList).result

def fib(n: Int): TailRec[Int] =
  if (n < 2) done(n) else for {
    x <- tailcall(fib(n - 1))
    y <- tailcall(fib(n - 2))
  } yield (x + y)

fib(40).result
```

* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `case class Call[A](rest: () ⇒ TailRec[A]) extends TailRec[A] with Product with Serializable` ###

Internal class representing a tailcall

* Attributes
  * protected
* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


### `case class Cont[A, B](a: TailRec[A], f: (A) ⇒ TailRec[B]) extends TailRec[B] with Product with Serializable` ###

Internal class representing a continuation with function A => TailRec[B]. It is
needed for the flatMap to be implemented.

* Attributes
  * protected
* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


### `case class Done[A](value: A) extends TailRec[A] with Product with Serializable` ###

Internal class representing the final result returned from a tailcalling
computation

* Attributes
  * protected
* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


### `abstract class TailRec[+A] extends AnyRef`                              ###

This class represents a tailcalling computation

* Source
  * [TailCalls.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/control/TailCalls.scala#L1)


--------------------------------------------------------------------------------
                Value Members From scala.util.control.TailCalls
--------------------------------------------------------------------------------


### `def done[A](result: A): TailRec[A]`                                     ###

Used to return final result from tailcalling computation

* returns
  * a `TailRec` object representing a computation which immediately returns
     `result`

(defined at scala.util.control.TailCalls)


### `def tailcall[A](rest: ⇒ TailRec[A]): TailRec[A]`                        ###

Performs a tailcall

* rest
  * the expression to be evaluated in the tailcall
* returns
  * a `TailRec` object representing the expression `rest`
(defined at scala.util.control.TailCalls)
