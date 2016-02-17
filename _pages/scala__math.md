
#                                  scala.math                                  #

```scala
package math
```

The package object `scala.math` contains methods for performing basic numeric
operations such as elementary exponential, logarithmic, root and trigonometric
functions.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final class BigDecimal extends ScalaNumber with ScalaNumericConversions with Serializable with Ordered[BigDecimal]` ###

 `BigDecimal` represents decimal floating-point numbers of arbitrary precision.
By default, the precision approximately matches that of IEEE 128-bit floating
point numbers (34 decimal digits, `HALF_EVEN` rounding mode). Within the range
of IEEE binary128 numbers, `BigDecimal` will agree with `BigInt` for both
equality and hash codes (and will agree with primitive types as well). Beyond
that range--numbers with more than 4934 digits when written out in full--the
 `hashCode` of `BigInt` and `BigDecimal` is allowed to diverge due to difficulty
in efficiently computing both the decimal representation in `BigDecimal` and the
binary representation in `BigInt` .

When creating a `BigDecimal` from a `Double` or `Float` , care must be taken as
the binary fraction representation of `Double` and `Float` does not easily
convert into a decimal representation. Three explicit schemes are available for
conversion. `BigDecimal.decimal` will convert the floating-point number to a
decimal text representation, and build a `BigDecimal` based on that.
 `BigDecimal.binary` will expand the binary fraction to the requested or default
precision. `BigDecimal.exact` will expand the binary fraction to the full number
of digits, thus producing the exact decimal value corresponding to the binary
fraction of that floating-point number. `BigDecimal` equality matches the
decimal expansion of `Double` : `BigDecimal.decimal(0.1) == 0.1` . Note that
since `0.1f != 0.1` , the same is not true for `Float` . Instead,
 `0.1f == BigDecimal.decimal((0.1f).toDouble)` .

To test whether a `BigDecimal` number can be converted to a `Double` or `Float`
and then back without loss of information by using one of these methods, test
with `isDecimalDouble` , `isBinaryDouble` , or `isExactDouble` or the
corresponding `Float` versions. Note that `BigInt` 's `isValidDouble` will agree
with `isExactDouble` , not the `isDecimalDouble` used by default.

 `BigDecimal` uses the decimal representation of binary floating-point numbers
to determine equality and hash codes. This yields different answers than
conversion between `Long` and `Double` values, where the exact form is used. As
always, since floating-point is a lossy representation, it is advisable to take
care when assuming identity will be maintained across multiple conversions.

 `BigDecimal` maintains a `MathContext` that determines the rounding that is
applied to certain calculations. In most cases, the value of the `BigDecimal` is
also rounded to the precision specified by the `MathContext` . To create a
 `BigDecimal` with a different precision than its `MathContext` , use
 `new BigDecimal(new java.math.BigDecimal(...), mc)` . Rounding will be applied
on those mathematical operations that can dramatically change the number of
digits in a full representation, namely multiplication, division, and powers.
The left-hand argument's `MathContext` always determines the degree of rounding,
if any, and is the one propagated through arithmetic operations that do not
apply rounding themselves.

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)
* Version
  * 1.1


### `final class BigInt extends ScalaNumber with ScalaNumericConversions with Serializable with Ordered[BigInt]` ###

* Source
  * [BigInt.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigInt.scala#L1)
* Version
  * 1.0, 15/07/2003


### `trait Equiv[T] extends Serializable`                                    ###

A trait for representing equivalence relations. It is important to distinguish
between a type that can be compared for equality or equivalence and a
representation of equivalence on some type. This trait is for representing the
latter.

An [equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) is
a binary relation on a type. This relation is exposed as the `equiv` method of
the `Equiv` trait. The relation must be:

1. reflexive: `equiv(x, x) == true` for any x of type `T` .
2. symmetric: `equiv(x, y) == equiv(y, x)` for any `x` and `y` of type `T` .
3. transitive: if `equiv(x, y) == true` and `equiv(y, z) == true` , then
    `equiv(x, z) == true` for any `x` , `y` , and `z` of type `T` .

* Source
  * [Equiv.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Equiv.scala#L1)
* Version
  * 1.0, 2008-04-03
* Since
  * 2.7


### `trait Fractional[T] extends Numeric[T]`                                 ###

* Source
  * [Fractional.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Fractional.scala#L1)
* Since
  * 2.8


### `trait Integral[T] extends Numeric[T]`                                   ###

* Source
  * [Integral.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Integral.scala#L1)
* Since
  * 2.8


### `trait LowPriorityEquiv extends AnyRef`                                  ###

* Self Type
  * Equiv.type
* Source
  * [Equiv.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Equiv.scala#L1)


### `trait LowPriorityOrderingImplicits extends AnyRef`                      ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait Numeric[T] extends Ordering[T]`                                   ###

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)


### `trait Ordered[A] extends Comparable[A]`                                 ###

A trait for data that have a single, natural ordering. See scala.math.Ordering
before using this trait for more information about whether to use
scala.math.Ordering instead.

Classes that implement this trait can be sorted with scala.util.Sorting and can
be compared with standard comparison operators (e.g. > and <).

Ordered should be used for data with a single, natural ordering (like integers)
while Ordering allows for multiple ordering implementations. An Ordering
instance will be implicitly created if necessary.

scala.math.Ordering is an alternative to this trait that allows multiple
orderings to be defined for the same type.

scala.math.PartiallyOrdered is an alternative to this trait for partially
ordered data.

For example, create a simple class that implements `Ordered` and then sort it
with scala.util.Sorting :

```scala
case class OrderedClass(n:Int) extends Ordered[OrderedClass] {
	def compare(that: OrderedClass) =  this.n - that.n
}

val x = Array(OrderedClass(1), OrderedClass(5), OrderedClass(3))
scala.util.Sorting.quickSort(x)
x
```

It is important that the `equals` method for an instance of `Ordered[A]` be
consistent with the compare method. However, due to limitations inherent in the
type erasure semantics, there is no reasonable way to provide a default
implementation of equality for instances of `Ordered[A]` . Therefore, if you
need to be able to use equality on an instance of `Ordered[A]` you must provide
it yourself either when inheriting or instantiating.

It is important that the `hashCode` method for an instance of `Ordered[A]` be
consistent with the `compare` method. However, it is not possible to provide a
sensible default implementation. Therefore, if you need to be able compute the
hash of an instance of `Ordered[A]` you must provide it yourself either when
inheriting or instantiating.

* Source
  * [Ordered.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordered.scala#L1)
* Version
  * 1.1, 2006-07-24
* See also
  * scala.math.Ordering, scala.math.PartiallyOrdered


### `trait Ordering[T] extends Comparator[T] with PartialOrdering[T] with Serializable` ###

Ordering is a trait whose instances each represent a strategy for sorting
instances of a type.

Ordering's companion object defines many implicit objects to deal with subtypes
of AnyVal (e.g. Int, Double), String, and others.

To sort instances by one or more member variables, you can take advantage of
these built-in orderings using Ordering.by and Ordering.on:

```scala
import scala.util.Sorting
val pairs = Array(("a", 5, 2), ("c", 3, 1), ("b", 1, 3))

// sort by 2nd element
Sorting.quickSort(pairs)(Ordering.by[(String, Int, Int), Int](_._2))

// sort by the 3rd element, then 1st
Sorting.quickSort(pairs)(Ordering[(Int, String)].on(x => (x._3, x._1)))
```

An Ordering[T] is implemented by specifying compare(a:T, b:T), which decides how
to order two instances a and b. Instances of Ordering[T] can be used by things
like scala.util.Sorting to sort collections like Array[T].

For example:

```scala
import scala.util.Sorting

case class Person(name:String, age:Int)
val people = Array(Person("bob", 30), Person("ann", 32), Person("carl", 19))

// sort by age
object AgeOrdering extends Ordering[Person] {
  def compare(a:Person, b:Person) = a.age compare b.age
}
Sorting.quickSort(people)(AgeOrdering)
```

This trait and scala.math.Ordered both provide this same functionality, but in
different ways. A type T can be given a single way to order itself by extending
Ordered. Using Ordering, this same type may be sorted in many other ways.
Ordered and Ordering both provide implicits allowing them to be used
interchangeably.

You can import scala.math.Ordering.Implicits to gain access to other implicit
orderings.

* Self Type
  * Ordering [T]
* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)
* Version
  * 0.9.5, 2008-04-15
* Since
  * 2.7
* See also
  * scala.math.Ordered, scala.util.Sorting


### `trait PartialOrdering[T] extends Equiv[T]`                              ###

A trait for representing partial orderings. It is important to distinguish
between a type that has a partial order and a representation of partial ordering
on some type. This trait is for representing the latter.

A [partial ordering](http://en.wikipedia.org/wiki/Partial_order) is a binary
relation on a type `T` , exposed as the `lteq` method of this trait. This
relation must be:

* reflexive: `lteq(x, x) == true` , for any `x` of type `T` .
* anti-symmetric: if `lteq(x, y) == true` and `lteq(y, x) == true` then
    `equiv(x, y) == true` , for any `x` and `y` of type `T` .
* transitive: if `lteq(x, y) == true` and `lteq(y, z) == true` then
    `lteq(x, z) == true` , for any `x` , `y` , and `z` of type `T` .

Additionally, a partial ordering induces an
[equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) on a
type `T` : `x` and `y` of type `T` are equivalent if and only if
 `lteq(x, y) && lteq(y, x) == true` . This equivalence relation is exposed as
the `equiv` method, inherited from the Equiv trait.

* Self Type
  * PartialOrdering [T]
* Source
  * [PartialOrdering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/PartialOrdering.scala#L1)
* Version
  * 1.0, 2008-04-0-3
* Since
  * 2.7


### `trait PartiallyOrdered[+A] extends AnyRef`                              ###

A class for partially ordered data.

* Source
  * [PartiallyOrdered.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/PartiallyOrdered.scala#L1)
* Version
  * 1.0, 23/04/2004


### `trait ScalaNumericAnyConversions extends Any`                           ###

Conversions which present a consistent conversion interface across all the
numeric types, suitable for use in value classes.

* Source
  * [ScalaNumericConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/ScalaNumericConversions.scala#L1)


### `trait ScalaNumericConversions extends ScalaNumber with ScalaNumericAnyConversions` ###

A slightly more specific conversion trait for classes which extend ScalaNumber
(which excludes value classes.)

* Source
  * [ScalaNumericConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/ScalaNumericConversions.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object BigDecimal extends Serializable`                                 ###

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)
* Version
  * 1.1
* Since
  * 2.7


### `object BigInt extends Serializable`                                     ###

* Source
  * [BigInt.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigInt.scala#L1)
* Version
  * 1.0, 15/07/2003
* Since
  * 2.1


### `object Equiv extends LowPriorityEquiv with Serializable`                ###

* Source
  * [Equiv.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Equiv.scala#L1)


### `object Fractional extends Serializable`                                 ###

* Source
  * [Fractional.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Fractional.scala#L1)


### `object Integral extends Serializable`                                   ###

* Source
  * [Integral.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Integral.scala#L1)


### `object Numeric extends Serializable`                                    ###

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)
* Since
  * 2.8


### `object Ordered`                                                         ###

* Source
  * [Ordered.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordered.scala#L1)


### `object Ordering extends LowPriorityOrderingImplicits with Serializable` ###

This is the companion object for the scala.math.Ordering trait.

It contains many implicit orderings as well as well as methods to construct new
orderings.

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
                    Deprecated Value Members From scala.math
--------------------------------------------------------------------------------


### `def round(x: Long): Long`                                               ###

There is no reason to round a `Long` , but this method prevents unintended
conversion to `Float` followed by rounding to `Int` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This is an integer type; there is no reason to
    round it. Perhaps you meant to call this with a floating-point value?

(defined at scala.math)


--------------------------------------------------------------------------------
                         Value Members From scala.math
--------------------------------------------------------------------------------


### `final val E: Double(2.718281828459045)`                                 ###

The `double` value that is closer than any other to `e` , the base of the
natural logarithms.

(defined at scala.math)


### `def IEEEremainder(x: Double, y: Double): Double`                        ###

(defined at scala.math)


### `def abs(x: Double): Double`                                             ###

(defined at scala.math)


### `def abs(x: Float): Float`                                               ###

(defined at scala.math)


### `def abs(x: Int): Int`                                                   ###

(defined at scala.math)


### `def abs(x: Long): Long`                                                 ###

(defined at scala.math)


### `def acos(x: Double): Double`                                            ###

(defined at scala.math)


### `def asin(x: Double): Double`                                            ###

(defined at scala.math)


### `def atan(x: Double): Double`                                            ###

(defined at scala.math)


### `def atan2(y: Double, x: Double): Double`                                ###

Converts rectangular coordinates `(x, y)` to polar `(r, theta)` .

* y
  * the abscissa coordinate
* x
  * the ordinate coordinate
* returns
  * the _theta_ component of the point `(r, theta)` in polar coordinates that
    corresponds to the point `(x, y)` in Cartesian coordinates.

(defined at scala.math)


### `def cbrt(x: Double): Double`                                            ###

Returns the cube root of the given `Double` value.

(defined at scala.math)


### `def ceil(x: Double): Double`                                            ###

(defined at scala.math)


### `def cos(x: Double): Double`                                             ###

(defined at scala.math)


### `def cosh(x: Double): Double`                                            ###

Returns the hyperbolic cosine of the given `Double` value.

(defined at scala.math)


### `def exp(x: Double): Double`                                             ###

Returns Euler's number `e` raised to the power of a `double` value.

* x
  * the exponent to raise `e` to.
* returns
  * the value `ea` , where `e` is the base of the natural logarithms.

(defined at scala.math)


### `def expm1(x: Double): Double`                                           ###

Returns `exp(x) - 1` .

(defined at scala.math)


### `def floor(x: Double): Double`                                           ###

(defined at scala.math)


### `def hypot(x: Double, y: Double): Double`                                ###

Returns the square root of the sum of the squares of both given `Double` values
without intermediate underflow or overflow.

(defined at scala.math)


### `def log(x: Double): Double`                                             ###

Returns the natural logarithm of a `double` value.

* x
  * the number to take the natural logarithm of
* returns
  * the value `logₑ(x)` where `e` is Eulers number

(defined at scala.math)


### `def log10(x: Double): Double`                                           ###

Returns the base 10 logarithm of the given `Double` value.

(defined at scala.math)


### `def log1p(x: Double): Double`                                           ###

Returns the natural logarithm of the sum of the given `Double` value and 1.

(defined at scala.math)


### `def max(x: Double, y: Double): Double`                                  ###

(defined at scala.math)


### `def max(x: Float, y: Float): Float`                                     ###

(defined at scala.math)


### `def max(x: Int, y: Int): Int`                                           ###

(defined at scala.math)


### `def max(x: Long, y: Long): Long`                                        ###

(defined at scala.math)


### `def min(x: Double, y: Double): Double`                                  ###

(defined at scala.math)


### `def min(x: Float, y: Float): Float`                                     ###

(defined at scala.math)


### `def min(x: Int, y: Int): Int`                                           ###

(defined at scala.math)


### `def min(x: Long, y: Long): Long`                                        ###

(defined at scala.math)


### `def pow(x: Double, y: Double): Double`                                  ###

Returns the value of the first argument raised to the power of the second
argument.

* x
  * the base.
* y
  * the exponent.
* returns
  * the value `xy` .

(defined at scala.math)


### `def rint(x: Double): Double`                                            ###

Returns the `double` value that is closest in value to the argument and is equal
to a mathematical integer.

* x
  * a `double` value
* returns
  * the closest floating-point value to a that is equal to a mathematical
    integer.

(defined at scala.math)


### `def round(x: Double): Long`                                             ###

Returns the closest `Long` to the argument.

* x
  * a floating-point value to be rounded to a `Long` .
* returns
  * the value of the argument rounded to the nearest `long` value.

(defined at scala.math)


### `def round(x: Float): Int`                                               ###

Returns the closest `Int` to the argument.

* x
  * a floating-point value to be rounded to a `Int` .
* returns
  * the value of the argument rounded to the nearest `Int` value.

(defined at scala.math)


### `def signum(x: Double): Double`                                          ###

(defined at scala.math)


### `def signum(x: Float): Float`                                            ###

(defined at scala.math)


### `def signum(x: Int): Int`                                                ###

Note that these are not pure forwarders to the java versions. In particular, the
return type of java.lang.Long.signum is Int, but here it is widened to Long so
that each overloaded variant will return the same numeric type it is passed.

(defined at scala.math)


### `def signum(x: Long): Long`                                              ###

(defined at scala.math)


### `def sin(x: Double): Double`                                             ###

(defined at scala.math)


### `def sinh(x: Double): Double`                                            ###

Returns the hyperbolic sine of the given `Double` value.

(defined at scala.math)


### `def sqrt(x: Double): Double`                                            ###

Returns the square root of a `double` value.

* x
  * the number to take the square root of
* returns
  * the value √x

(defined at scala.math)


### `def tan(x: Double): Double`                                             ###

(defined at scala.math)


### `def tanh(x: Double): Double`                                            ###

Returns the hyperbolic tangent of the given `Double` value.

(defined at scala.math)


### `def toDegrees(x: Double): Double`                                       ###

Converts an angle measured in radians to an approximately equivalent angle
measured in degrees.

* x
  * angle, in radians
* returns
  * the measurement of the angle `x` in degrees.

(defined at scala.math)


### `def toRadians(x: Double): Double`                                       ###

Converts an angle measured in degrees to an approximately equivalent angle
measured in radians.

* x
  * an angle, in degrees
* returns
  * the measurement of the angle `x` in radians.

(defined at scala.math)


### `def ulp(x: Double): Double`                                             ###

Returns the size of an ulp of the given `Double` value.

(defined at scala.math)


### `def ulp(x: Float): Float`                                               ###

Returns the size of an ulp of the given `Float` value.
(defined at scala.math)
