
#                                scala.Function                                #

```scala
object Function
```

A module defining utility methods for higher-order functional programming.

* Source
  * [Function.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function.scala#L1)
* Version
  * 1.0, 29/11/2006


--------------------------------------------------------------------------------
                       Value Members From scala.Function
--------------------------------------------------------------------------------


### `def chain[a](fs: Seq[(a) ⇒ a]): (a) ⇒ a`                                ###

Given a sequence of functions `f1` ,..., `fn` , return the function
 `f1 andThen ... andThen fn` .

* fs
  * The given sequence of functions

(defined at scala.Function)


### `def const[T, U](x: T)(y: U): T`                                         ###

The constant function

(defined at scala.Function)


### `def tupled[a1, a2, a3, a4, a5, b](f: (a1, a2, a3, a4, a5) ⇒ b): ((a1, a2, a3, a4, a5)) ⇒ b` ###

Tupling for functions of arity 5. This transforms a function of arity 5 into a
unary function that takes a 5-tuple of arguments.

(defined at scala.Function)


### `def tupled[a1, a2, a3, a4, b](f: (a1, a2, a3, a4) ⇒ b): ((a1, a2, a3, a4)) ⇒ b` ###

Tupling for functions of arity 4. This transforms a function of arity 4 into a
unary function that takes a 4-tuple of arguments.

(defined at scala.Function)


### `def tupled[a1, a2, a3, b](f: (a1, a2, a3) ⇒ b): ((a1, a2, a3)) ⇒ b`     ###

Tupling for functions of arity 3. This transforms a function of arity 3 into a
unary function that takes a triple of arguments.

(defined at scala.Function)


### `def tupled[a1, a2, b](f: (a1, a2) ⇒ b): ((a1, a2)) ⇒ b`                 ###

Tupling for functions of arity 2. This transforms a function of arity 2 into a
unary function that takes a pair of arguments.

* Note
  * These functions are slotted for deprecation, but it is on hold pending
    superior type inference for tupling anonymous functions.

(defined at scala.Function)


### `def uncurried[a1, a2, a3, a4, a5, b](f: (a1) ⇒ (a2) ⇒ (a3) ⇒ (a4) ⇒ (a5) ⇒ b): (a1, a2, a3, a4, a5) ⇒ b` ###

Uncurrying for functions of arity 5.

(defined at scala.Function)


### `def uncurried[a1, a2, a3, a4, b](f: (a1) ⇒ (a2) ⇒ (a3) ⇒ (a4) ⇒ b): (a1, a2, a3, a4) ⇒ b` ###

Uncurrying for functions of arity 4.

(defined at scala.Function)


### `def uncurried[a1, a2, a3, b](f: (a1) ⇒ (a2) ⇒ (a3) ⇒ b): (a1, a2, a3) ⇒ b` ###

Uncurrying for functions of arity 3.

(defined at scala.Function)


### `def uncurried[a1, a2, b](f: (a1) ⇒ (a2) ⇒ b): (a1, a2) ⇒ b`             ###

Uncurrying for functions of arity 2. This transforms a unary function returning
another unary function into a function of arity 2.

(defined at scala.Function)


### `def unlift[T, R](f: (T) ⇒ Option[R]): PartialFunction[T, R]`            ###

Turns a function `A => Option[B]` into a `PartialFunction[A, B]` .

 *Important note* : this transformation implies the original function may be
called 2 or more times on each logical invocation, because the only way to
supply an implementation of `isDefinedAt` is to call the function and examine
the return value. See also scala.PartialFunction, method `applyOrElse` .

* f
  * a function `T => Option[R]`
* returns
  * a partial function defined for those inputs where f returns `Some(_)` and
    undefined where `f` returns `None` .

* See also
  * scala.PartialFunction, method `lift` .

(defined at scala.Function)


### `def untupled[a1, a2, a3, a4, a5, b](f: ((a1, a2, a3, a4, a5)) ⇒ b): (a1, a2, a3, a4, a5) ⇒ b` ###

Un-tupling for functions of arity 5. This transforms a function taking a 5-tuple
of arguments into a function of arity 5 which takes each argument separately.

(defined at scala.Function)


### `def untupled[a1, a2, a3, a4, b](f: ((a1, a2, a3, a4)) ⇒ b): (a1, a2, a3, a4) ⇒ b` ###

Un-tupling for functions of arity 4. This transforms a function taking a 4-tuple
of arguments into a function of arity 4 which takes each argument separately.

(defined at scala.Function)


### `def untupled[a1, a2, a3, b](f: ((a1, a2, a3)) ⇒ b): (a1, a2, a3) ⇒ b`   ###

Un-tupling for functions of arity 3. This transforms a function taking a triple
of arguments into a ternary function which takes each argument separately.

(defined at scala.Function)


### `def untupled[a1, a2, b](f: ((a1, a2)) ⇒ b): (a1, a2) ⇒ b`               ###

Un-tupling for functions of arity 2. This transforms a function taking a pair of
arguments into a binary function which takes each argument separately.
(defined at scala.Function)
