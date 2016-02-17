
#                            scala.PartialFunction                            #

```scala
trait PartialFunction[-A, +B] extends (A) ⇒ B
```

A partial function of type `PartialFunction[A, B]` is a unary function where the
domain does not necessarily include all values of type `A` . The function
 `isDefinedAt` allows to test dynamically if a value is in the domain of the
function.

Even if `isDefinedAt` returns true for an `a: A` , calling `apply(a)` may still
throw an exception, so the following code is legal:

```scala
val f: PartialFunction[Int, Any] = { case _ => 1/0 }
```

It is the responsibility of the caller to call `isDefinedAt` before calling
 `apply` , because if `isDefinedAt` is false, it is not guaranteed `apply` will
throw an exception to indicate an error condition. If an exception is not
thrown, evaluation may result in an arbitrary value.

The main distinction between `PartialFunction` and scala.Function1 is that the
user of a `PartialFunction` may choose to do something different with input that
is declared to be outside its domain. For example:

```scala
val sample = 1 to 10
val isEven: PartialFunction[Int, String] = {
  case x if x % 2 == 0 => x+" is even"
}

// the method collect can use isDefinedAt to select which members to collect
val evenNumbers = sample collect isEven

val isOdd: PartialFunction[Int, String] = {
  case x if x % 2 == 1 => x+" is odd"
}

// the method orElse allows chaining another partial function to handle
// input outside the declared domain
val numbers = sample map (isEven orElse isOdd)
```

* Self Type
  * PartialFunction [A, B]
* Source
  * [PartialFunction.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/PartialFunction.scala#L1)
* Version
  * 1.0, 16/07/2003


--------------------------------------------------------------------------------
                  Abstract Value Members From scala.Function1
--------------------------------------------------------------------------------


### `abstract def apply(v1: A): B`                                           ###

Apply the body of this function to the argument.

* returns
  * the result of function application.

* Definition Classes
  * Function1

(defined at scala.Function1)


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def compose[A](g: (A) ⇒ A): (A) ⇒ B`                                    ###

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
               Abstract Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `abstract def isDefinedAt(x: A): Boolean`                                ###

Checks if a value is contained in the function's domain.

* x
  * the value to test
* returns
  * `true` , iff `x` is in the domain of this function, `false` otherwise.

(defined at scala.PartialFunction)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `def andThen[C](k: (B) ⇒ C): PartialFunction[A, C]`                      ###

Composes this partial function with a transformation function that gets applied
to results of this partial function.

* C
  * the result type of the transformation function.
* k
  * the transformation function
* returns
  * a partial function with the same domain as this partial function, which maps
    arguments `x` to `k(this(x))` .

* Definition Classes
  * PartialFunction → Function1

(defined at scala.PartialFunction)


### `def applyOrElse[A1 <: A, B1 >: B](x: A1, default: (A1) ⇒ B1): B1`       ###

Applies this partial function to the given argument when it is contained in the
function domain. Applies fallback function where this partial function is not
defined.

Note that expression `pf.applyOrElse(x, default)` is equivalent to

```scala
if(pf isDefinedAt x) pf(x) else default(x)
```

except that `applyOrElse` method can be implemented more efficiently. For all
partial function literals the compiler generates an `applyOrElse` implementation
which avoids double evaluation of pattern matchers and guards. This makes
 `applyOrElse` the basis for the efficient implementation for many operations
and scenarios, such as:

* combining partial functions into `orElse` / `andThen` chains does not lead to
   excessive `apply` / `isDefinedAt` evaluation
*  `lift` and `unlift` do not evaluate source functions twice on each invocation
*  `runWith` allows efficient imperative-style combining of partial functions
   with conditionally applied actions

For non-literal partial function classes with nontrivial `isDefinedAt` method it
is recommended to override `applyOrElse` with custom implementation that avoids
double `isDefinedAt` evaluation. This may result in better performance and more
predictable behavior w.r.t. side effects.

* x
  * the function argument
* default
  * the fallback function
* returns
  * the result of this function or fallback function application.

* Since
  * 2.10

(defined at scala.PartialFunction)


### `def lift: (A) ⇒ Option[B]`                                              ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: A, B1 >: B](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

Composes this partial function with a fallback partial function which gets
applied where this partial function is not defined.

* A1
  * the argument type of the fallback function
* B1
  * the result type of the fallback function
* that
  * the fallback function
* returns
  * a partial function which has as domain the union of the domains of this
    partial function and `that` . The resulting partial function takes `x` to
     `this(x)` where `this` is defined, and to `that(x)` where it is not.

(defined at scala.PartialFunction)


### `def runWith[U](action: (B) ⇒ U): (A) ⇒ Boolean`                         ###

Composes this partial function with an action function which gets applied to
results of this partial function. The action function is invoked only for its
side effects; its result is ignored.

Note that expression `pf.runWith(action)(x)` is equivalent to

```scala
if(pf isDefinedAt x) { action(pf(x)); true } else false
```

except that `runWith` is implemented via `applyOrElse` and thus potentially more
efficient. Using `runWith` avoids double evaluation of pattern matchers and
guards for partial function literals.

* action
  * the action function
* returns
  * a function which maps arguments `x` to `isDefinedAt(x)` . The resulting
    function runs `action(this(x))` where `this` is defined.

* Since
  * 2.10
* See also
  * `applyOrElse` .
(defined at scala.PartialFunction)
