
#                              scala.util.Either                              #

```scala
sealed abstract class Either[+A, +B] extends Product with Serializable
```

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
                 Concrete Value Members From scala.util.Either
--------------------------------------------------------------------------------


### `abstract def isLeft: Boolean`                                           ###

Returns `true` if this is a `Left` , `false` otherwise.

```scala
Left("tulip").isLeft // true
Right("venus fly-trap").isLeft // false
```

(defined at scala.util.Either)


### `def fold[X](fa: (A) ⇒ X, fb: (B) ⇒ X): X`                               ###

Applies `fa` if this is a `Left` or `fb` if this is a `Right` .

* fa
  * the function to apply if this is a `Left`
* fb
  * the function to apply if this is a `Right`
* returns
  * the results of applying the function

Example:

```scala
val result: Either[Exception, Value] = possiblyFailingOperation()
log(result.fold(
  ex => "Operation failed with " + ex,
  v => "Operation produced value: " + v
))
```

(defined at scala.util.Either)


### `def joinLeft[A1 >: A, B1 >: B, C](implicit ev: <:<[A1, Either[C, B1]]): Either[C, B1]` ###

Joins an `Either` through `Left` .

This method requires that the left side of this Either is itself an Either type.
That is, this must be some type like:

```scala
Either[Either[C, B], B]
```

(which respects the type parameter bounds, shown below.)

If this instance is a Left[Either[C, B]] then the contained Either[C, B] will be
returned, otherwise this value will be returned unmodified.

```scala
Left[Either[Int, String], String](Right("flower")).joinLeft // Result: Right("flower")
Left[Either[Int, String], String](Left(12)).joinLeft // Result: Left(12)
Right[Either[Int, String], String]("daisy").joinLeft // Result: Right("daisy")
```

This method, and `joinRight` , are analogous to `Option#flatten`

(defined at scala.util.Either)


### `def joinRight[A1 >: A, B1 >: B, C](implicit ev: <:<[B1, Either[A1, C]]): Either[A1, C]` ###

Joins an `Either` through `Right` .

This method requires that the right side of this Either is itself an Either
type. That is, this must be some type like:

```scala
Either[A, Either[A, C]]
```

(which respects the type parameter bounds, shown below.)

If this instance is a Right[Either[A, C]] then the contained Either[A, C] will
be returned, otherwise this value will be returned unmodified.

Example:

```scala
joinLeft
```

(defined at scala.util.Either)


### `def left: LeftProjection[A, B]`                                         ###

Projects this `Either` as a `Left` .

(defined at scala.util.Either)


### `def right: RightProjection[A, B]`                                       ###

Projects this `Either` as a `Right` .

(defined at scala.util.Either)


### `def swap: Either[B, A]`                                                 ###

If this is a `Left` , then return the left value in `Right` or vice versa.

Example:

```scala
val l: Either[String, Int] = Left("left")
val r: Either[Int, String] = l.swap // Result: Right("left")
```

(defined at scala.util.Either)


--------------------------------------------------------------------------------
     Concrete Value Members From Implicit scala.util.Either.MergeableEither
--------------------------------------------------------------------------------


### `def merge: B`                                                           ###

* Implicit information
  * This member is added by an implicit conversion from Either [A, B] to
    MergeableEither [B] performed by method MergeableEither in scala.util.Either.
* Definition Classes
  * MergeableEither
(added by implicit convertion: scala.util.Either.MergeableEither)
