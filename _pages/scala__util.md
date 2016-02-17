
#                                  scala.util                                  #

```scala
package util
```


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object MurmurHash`                                                      ###

An object designed to generate well-distributed non-cryptographic hashes. It is
designed to hash a collection of integers; along with the integers to hash, it
generates two magic streams of integers to increase the distribution of
repetitive input sequences. Thus, three methods need to be called at each step
(to start and to incorporate a new integer) to update the values. Only one
method needs to be called to finalize the hash.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use the object MurmurHash3 instead.
* Source
  * [MurmurHash.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/MurmurHash.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class DynamicVariable[T] extends AnyRef`                                ###

 `DynamicVariables` provide a binding mechanism where the current value is found
through dynamic scope, but where access to the variable itself is resolved
through static scope.

The current value can be retrieved with the value method. New values should be
pushed using the `withValue` method. Values pushed via `withValue` only stay
valid while the `withValue` 's second argument, a parameterless closure,
executes. When the second argument finishes, the variable reverts to the
previous value.

```scala
someDynamicVariable.withValue(newValue) {
  // ... code called in here that calls value ...
  // ... will be given back the newValue ...
}
```

Each thread gets its own stack of bindings. When a new thread is created, the
 `DynamicVariable` gets a copy of the stack of bindings from the parent thread,
and from then on the bindings for the new thread are independent of those for
the original thread.

* Source
  * [DynamicVariable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/DynamicVariable.scala#L1)
* Version
  * 1.1, 2007-5-21


### `sealed abstract class Either[+A, +B] extends Product with Serializable` ###

Represents a value of one of two possible types (a disjoint union.) Instances of
Either are either an instance of scala.util.Left or scala.util.Right.

A common use of Either is as an alternative to scala.Option for dealing with
possible missing values. In this usage, scala.None is replaced with a
scala.util.Left which can contain useful information. scala.util.Right takes the
place of scala.Some. Convention dictates that Left is used for failure and Right
is used for success.

For example, you could use `Either[String, Int]` to detect whether a received
input is a String or an Int.

```scala
val in = Console.readLine("Type Either a string or an Int: ")
val result: Either[String,Int] = try {
    Right(in.toInt)
  } catch {
    case e: Exception =>
      Left(in)
}

println( result match {
  case Right(x) => "You passed me the Int: " + x + ", which I will increment. " + x + " + 1 = " + (x+1)
  case Left(x) => "You passed me the String: " + x
})
```

A _projection_ can be used to selectively operate on a value of type Either,
depending on whether it is of type Left or Right. For example, to transform an
Either using a function, in the case where it's a Left, one can first apply the
 `left` projection and invoke `map` on that projected Either. If a `right`
projection is applied to that Left, the original Left is returned, unmodified.

```scala
val l: Either[String, Int] = Left("flower")
val r: Either[String, Int] = Right(12)
l.left.map(_.size): Either[Int, Int] // Left(6)
r.left.map(_.size): Either[Int, Int] // Right(12)
l.right.map(_.toDouble): Either[String, Double] // Left("flower")
r.right.map(_.toDouble): Either[String, Double] // Right(12.0)
```

Like with other types which define a `map` method, the same can be achieved
using a for-comprehension:

```scala
for (s <- l.left) yield s.size // Left(6)
```

To support multiple projections as generators in for-comprehensions, the Either
type also defines a `flatMap` method.

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008
* Since
  * 2.7


### `final case class Failure[+T](exception: Throwable) extends Try[T] with Product with Serializable` ###

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


### `final case class Left[+A, +B](a: A) extends Either[A, B] with Product with Serializable` ###

The left side of the disjoint union, as opposed to the scala.util.Right side.

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008


### `class MurmurHash[T] extends (T) ⇒ Unit`                                 ###

A class designed to generate well-distributed non-cryptographic hashes. It is
designed to be passed to a collection's foreach method, or can take individual
hash values with append. Its own hash code is set equal to the hash code of
whatever it is hashing.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use the object MurmurHash3 instead.
* Source
  * [MurmurHash.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/MurmurHash.scala#L1)


### `class Random extends Serializable`                                      ###

* Source
  * [Random.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Random.scala#L1)


### `final case class Right[+A, +B](b: B) extends Either[A, B] with Product with Serializable` ###

The right side of the disjoint union, as opposed to the scala.util.Left side.

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)
* Version
  * 1.0, 11/10/2008


### `final case class Success[+T](value: T) extends Try[T] with Product with Serializable` ###

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


### `sealed abstract class Try[+T] extends Product with Serializable`        ###

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
                                 Value Members
--------------------------------------------------------------------------------


### `object Either extends Serializable`                                     ###

* Source
  * [Either.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Either.scala#L1)


### `object Properties extends PropertiesTrait`                              ###

Loads `library.properties` from the jar.

* Source
  * [Properties.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Properties.scala#L1)


### `object Random extends Random`                                           ###

The object `Random` offers a default implementation of scala.util.Random and
random-related convenience methods.

* Source
  * [Random.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Random.scala#L1)
* Since
  * 2.8


### `object Sorting`                                                         ###

The `Sorting` object provides convenience wrappers for `java.util.Arrays.sort` .
Methods that defer to `java.util.Arrays.sort` say that they do or under what
conditions that they do.

 `Sorting` also implements a general-purpose quicksort and stable (merge) sort
for those cases where `java.util.Arrays.sort` could only be used at the cost of
a large memory penalty. If performance rather than memory usage is the primary
concern, one may wish to find alternate strategies to use
 `java.util.Arrays.sort` directly e.g. by boxing primitives to use a custom
ordering on them.

 `Sorting` provides methods where you can provide a comparison function, or can
request a sort of items that are scala.math.Ordered or that otherwise have an
implicit or explicit scala.math.Ordering.

Note also that high-performance non-default sorts for numeric types are not
provided. If this is required, it is advisable to investigate other libraries
that cover this use case.

* Source
  * [Sorting.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Sorting.scala#L1)
* Version
  * 1.1


### `object Try extends Serializable`                                        ###

* Source
  * [Try.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Try.scala#L1)


### `package control`                                                        ###


### `package hashing`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/package.scala#L1)


### `package matching`                                                       ###

