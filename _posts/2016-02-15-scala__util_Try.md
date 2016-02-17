
#                                scala.util.Try                                #

```scala
sealed abstract class Try[+T] extends Product with Serializable
```

The `Try` type represents a computation that may either result in an exception,
or return a successfully computed value. It's similar to, but semantically
different from the scala.util.Either type.

Instances of `Try[T]` , are either an instance of scala.util.Success [T] or
scala.util.Failure [T].

For example, `Try` can be used to perform division on a user-defined input,
without the need to do explicit exception-handling in all of the places that an
exception might occur.

Example:

```scala
import scala.io.StdIn
import scala.util.{Try, Success, Failure}

def divide: Try[Int] = {
  val dividend = Try(StdIn.readLine("Enter an Int that you'd like to divide:\n").toInt)
  val divisor = Try(StdIn.readLine("Enter an Int that you'd like to divide by:\n").toInt)
  val problem = dividend.flatMap(x => divisor.map(y => x/y))
  problem match {
    case Success(v) =>
      println("Result of " + dividend.get + "/"+ divisor.get +" is: " + v)
      Success(v)
    case Failure(e) =>
      println("You must've divided by zero or entered something that's not an Int. Try again!")
      println("Info from the exception: " + e.getMessage)
      divide
  }
}
```

An important property of `Try` shown in the above example is its ability to _
pipeline_ , or chain, operations, catching exceptions along the way. The
 `flatMap` and `map` combinators in the above example each essentially pass off
either their successfully completed value, wrapped in the `Success` type for it
to be further operated upon by the next combinator in the chain, or the
exception wrapped in the `Failure` type usually to be simply passed on down the
chain. Combinators such as `recover` and `recoverWith` are designed to provide
some type of default behavior in the case of failure.

 _Note_ : only non-fatal exceptions are caught by the combinators on `Try` (see
scala.util.control.NonFatal). Serious system errors, on the other hand, will be
thrown.

 _Note:_ : all Try combinators will catch exceptions and return failure unless
otherwise specified in the documentation.

 `Try` comes to the Scala standard library after years of use as an integral
part of Twitter's stack.

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WithFilter extends AnyRef`                                        ###

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.12")
* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


--------------------------------------------------------------------------------
                    Abstract Value Members From scala.Equals
--------------------------------------------------------------------------------


### `abstract def canEqual(that: Any): Boolean`                              ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* that
  * the value being probed for possible equality
* returns
  * true if this instance can possibly equal `that` , otherwise false

* Definition Classes
  * Equals

(defined at scala.Equals)


--------------------------------------------------------------------------------
                   Abstract Value Members From scala.Product
--------------------------------------------------------------------------------


### `abstract def productElement(n: Int): Any`                               ###

The n <sup>th</sup> element of this product, 0-based. In other words, for a
product `A(x1, ..., xk)` , returns `x(n+1)` where `0 < n < k` .

* n
  * the index of the element to return
* returns
  * the element `n` elements after the first element

* Definition Classes
  * Product
* Exceptions thrown
  *

(defined at scala.Product)


--------------------------------------------------------------------------------
                   Abstract Value Members From scala.util.Try
--------------------------------------------------------------------------------


### `abstract def collect[U](pf: PartialFunction[T, U]): Try[U]`             ###

Applies the given partial function to the value from this `Success` or returns
this if this is a `Failure` .

(defined at scala.util.Try)


### `abstract def failed: Try[Throwable]`                                    ###

Inverts this `Try` . If this is a `Failure` , returns its exception wrapped in a
 `Success` . If this is a `Success` , returns a `Failure` containing an
 `UnsupportedOperationException` .

(defined at scala.util.Try)


### `abstract def filter(p: (T) ⇒ Boolean): Try[T]`                          ###

Converts this to a `Failure` if the predicate is not satisfied.

(defined at scala.util.Try)


### `abstract def flatMap[U](f: (T) ⇒ Try[U]): Try[U]`                       ###

Returns the given function applied to the value from this `Success` or returns
this if this is a `Failure` .

(defined at scala.util.Try)


### `abstract def flatten[U](implicit ev: <:<[T, Try[U]]): Try[U]`           ###

Transforms a nested `Try` , ie, a `Try` of type `Try[Try[T]]` , into an
un-nested `Try` , ie, a `Try` of type `Try[T]` .

(defined at scala.util.Try)


### `abstract def fold[U](fa: (Throwable) ⇒ U, fb: (T) ⇒ U): U`              ###

Applies `fa` if this is a `Failure` or `fb` if this is a `Success` . If `fb` is
initially applied and throws an exception, then `fa` is applied with this
exception.

* fa
  * the function to apply if this is a `Failure`
* fb
  * the function to apply if this is a `Success`
* returns
  * the results of applying the function

Example:

```scala
val result: Try[Throwable, Int] = Try { string.toInt }
log(result.fold(
  ex => "Operation failed with " + ex,
  v => "Operation produced value: " + v
))
```

(defined at scala.util.Try)


### `abstract def foreach[U](f: (T) ⇒ U): Unit`                              ###

Applies the given function `f` if this is a `Success` , otherwise returns
 `Unit` if this is a `Failure` .

 _Note:_ If `f` throws, then this method may throw an exception.

(defined at scala.util.Try)


### `abstract def getOrElse[U >: T](default: ⇒ U): U`                        ###

Returns the value from this `Success` or the given `default` argument if this is
a `Failure` .

 _Note:_ : This will throw an exception if it is not a success and default
throws an exception.

(defined at scala.util.Try)


### `abstract def map[U](f: (T) ⇒ U): Try[U]`                                ###

Maps the given function to the value from this `Success` or returns this if this
is a `Failure` .

(defined at scala.util.Try)


### `abstract def orElse[U >: T](default: ⇒ Try[U]): Try[U]`                 ###

Returns this `Try` if it's a `Success` or the given `default` argument if this
is a `Failure` .

(defined at scala.util.Try)


### `abstract def recoverWith[U >: T](pf: PartialFunction[Throwable, Try[U]]): Try[U]` ###

Applies the given function `f` if this is a `Failure` , otherwise returns this
if this is a `Success` . This is like `flatMap` for the exception.

(defined at scala.util.Try)


### `abstract def recover[U >: T](pf: PartialFunction[Throwable, U]): Try[U]` ###

Applies the given function `f` if this is a `Failure` , otherwise returns this
if this is a `Success` . This is like map for the exception.

(defined at scala.util.Try)


### `abstract def toEither: Either[Throwable, T]`                            ###

Returns `Left` with `Throwable` if this is a `Failure` , otherwise returns
 `Right` with `Success` value.

(defined at scala.util.Try)


### `abstract def transform[U](s: (T) ⇒ Try[U], f: (Throwable) ⇒ Try[U]): Try[U]` ###

Completes this `Try` by applying the function `f` to this if this is of type
 `Failure` , or conversely, by applying `s` if this is a `Success` .

(defined at scala.util.Try)


--------------------------------------------------------------------------------
                   Concrete Value Members From scala.util.Try
--------------------------------------------------------------------------------


### `abstract def get: T`                                                    ###

Returns the value from this `Success` or throws the exception if this is a
 `Failure` .

(defined at scala.util.Try)


### `final def withFilter(p: (T) ⇒ Boolean): WithFilter`                     ###

Creates a non-strict filter, which eventually converts this to a `Failure` if
the predicate is not satisfied.

Note: unlike filter, withFilter does not create a new Try. Instead, it restricts
the domain of subsequent `map` , `flatMap` , `foreach` , and `withFilter`
operations.

As Try is a one-element collection, this may be a bit overkill, but it's
consistent with withFilter on Option and the other collections.

* p
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this Try which satisfy the predicate `p` .

* Annotations
  * @ inline ()
(defined at scala.util.Try)
