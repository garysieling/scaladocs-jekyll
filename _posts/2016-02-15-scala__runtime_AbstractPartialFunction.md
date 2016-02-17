
#                    scala.runtime.AbstractPartialFunction                    #

```scala
abstract class AbstractPartialFunction[-T1, +R] extends (T1) ⇒ R with PartialFunction[T1, R]
```

 `AbstractPartialFunction` reformulates all operations of its supertrait
 `PartialFunction` in terms of `isDefinedAt` and `applyOrElse` .

This allows more efficient implementations in many cases:

* optimized `orElse` method supports chained `orElse` in linear time, and with
   no slow-down if the `orElse` part is not needed.
* optimized `lift` method helps to avoid double evaluation of pattern matchers &
   guards of partial function literals.

This trait is used as a basis for implementation of all partial function
literals.

* Self Type
  * AbstractPartialFunction [T1, R]
* Source
  * [AbstractPartialFunction.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/AbstractPartialFunction.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


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
               Abstract Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `abstract def isDefinedAt(x: T1): Boolean`                               ###

Checks if a value is contained in the function's domain.

* x
  * the value to test
* returns
  * `true` , iff `x` is in the domain of this function, `false` otherwise.

* Definition Classes
  * PartialFunction

(defined at scala.PartialFunction)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `def andThen[C](k: (R) ⇒ C): PartialFunction[T1, C]`                     ###

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


### `def applyOrElse[A1 <: T1, B1 >: R](x: A1, default: (A1) ⇒ B1): B1`      ###

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

* Definition Classes
  * PartialFunction
* Since
  * 2.10

(defined at scala.PartialFunction)


### `def lift: (T1) ⇒ Option[R]`                                             ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: T1, B1 >: R](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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

* Definition Classes
  * PartialFunction

(defined at scala.PartialFunction)


### `def runWith[U](action: (R) ⇒ U): (T1) ⇒ Boolean`                        ###

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

* Definition Classes
  * PartialFunction
* Since
  * 2.10
* See also
  * `applyOrElse` .

(defined at scala.PartialFunction)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.runtime.AbstractPartialFunction
--------------------------------------------------------------------------------


### `def apply(x: T1): R`                                                    ###

Apply the body of this function to the argument.

* returns
  * the result of function application.

* Definition Classes
  * AbstractPartialFunction → Function1

(defined at scala.runtime.AbstractPartialFunction)


--------------------------------------------------------------------------------
        Instance Constructors From scala.runtime.AbstractPartialFunction
--------------------------------------------------------------------------------


### `new AbstractPartialFunction()`                                          ###
(defined at scala.runtime.AbstractPartialFunction)
