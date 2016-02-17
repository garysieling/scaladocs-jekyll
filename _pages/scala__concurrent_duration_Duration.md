
#                      scala.concurrent.duration.Duration                      #

```scala
sealed abstract class Duration extends Serializable with Ordered[Duration]
```

### Utility for working with java.util.concurrent.TimeUnit durations.

 * _This class is not meant as a general purpose representation of time, it is
optimized for the needs of `scala.concurrent` ._*

### Basic Usage

Examples:

```scala
import scala.concurrent.duration._

val duration = Duration(100, MILLISECONDS)
val duration = Duration(100, "millis")

duration.toNanos
duration < 1.second
duration <= Duration.Inf
```

 * _Invoking inexpressible conversions (like calling `toSeconds` on an infinite
duration) will throw an IllegalArgumentException._*

Implicits are also provided for Int, Long and Double. Example usage:

```scala
import scala.concurrent.duration._

val duration = 100 millis
```

 * _The DSL provided by the implicit conversions always allows construction of
finite durations, even for infinite Double inputs; use Duration.Inf instead._*

Extractors, parsing and arithmetic are also included:

```scala
val d = Duration("1.2 µs")
val Duration(length, unit) = 5 millis
val d2 = d * 2.5
val d3 = d2 + 1.millisecond
```

### Handling of Time Units

Calculations performed on finite durations always retain the more precise unit
of either operand, no matter whether a coarser unit would be able to exactly
express the same duration. This means that Duration can be used as a lossless
container for a (length, unit) pair if it is constructed using the corresponding
methods and no arithmetic is performed on it; adding/subtracting durations
should in that case be done with care.

### Correspondence to Double Semantics

The semantics of arithmetic operations on Duration are two-fold:

* exact addition/subtraction with nanosecond resolution for finite durations,
   independent of the summands' magnitude
* isomorphic to `java.lang.Double` when it comes to infinite or undefined values

The conversion between Duration and Double is done using Duration.toUnit (with
unit NANOSECONDS) and Duration.fromNanos(Double)

### Ordering

The default ordering is consistent with the ordering of Double numbers, which
means that Undefined is considered greater than all other durations, including
Duration.Inf.

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
         Abstract Value Members From scala.concurrent.duration.Duration
--------------------------------------------------------------------------------


### `abstract def *(factor: Double): Duration`                               ###

Return this duration multiplied by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `abstract def +(other: Duration): Duration`                              ###

Return the sum of that duration and this. When involving non-finite summands the
semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `abstract def -(other: Duration): Duration`                              ###

Return the difference of that duration and this. When involving non-finite
summands the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `abstract def /(divisor: Double): Duration`                              ###

Return this duration divided by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `abstract def /(divisor: Duration): Double`                              ###

Return the quotient of this and that duration as floating-point number. The
semantics are determined by Double as if calculating the quotient of the
nanosecond lengths of both factors.

(defined at scala.concurrent.duration.Duration)


### `abstract def toCoarsest: Duration`                                      ###

Return duration which is equal to this duration but with a coarsest Unit, or
self in case it is already the coarsest Unit

Examples:

```scala
Duration(60, MINUTES).toCoarsest // Duration(1, HOURS)
Duration(1000, MILLISECONDS).toCoarsest // Duration(1, SECONDS)
Duration(48, HOURS).toCoarsest // Duration(2, DAYS)
Duration(5, SECONDS).toCoarsest // Duration(5, SECONDS)
```

(defined at scala.concurrent.duration.Duration)


### `abstract def toUnit(unit: TimeUnit): Double`                            ###

Return the number of nanoseconds as floating point number, scaled down to the
given unit. The result may not precisely represent this duration due to the
Double datatype's inherent limitations (mantissa size effectively 53 bits).
Non-finite durations are represented as

* Duration.Undefined is mapped to Double.NaN
* Duration.Inf is mapped to Double.PositiveInfinity
* Duration.MinusInf is mapped to Double.NegativeInfinity

(defined at scala.concurrent.duration.Duration)


### `abstract def unary_-: Duration`                                         ###

Negate this duration. The only two values which are mapped to themselves are
Duration.Zero and Duration.Undefined.

(defined at scala.concurrent.duration.Duration)


### `abstract def unit: TimeUnit`                                            ###

Obtain the time unit in which the length of this duration is measured.

* Exceptions thrown
  * IllegalArgumentException when invoked on a non-finite duration

(defined at scala.concurrent.duration.Duration)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.concurrent.duration.Duration
--------------------------------------------------------------------------------


### `abstract def isFinite(): Boolean`                                       ###

This method returns whether this duration is finite, which is not the same as
 `!isInfinite` for Double because this method also returns `false` for
Duration.Undefined.

(defined at scala.concurrent.duration.Duration)


### `def div(divisor: Double): Duration`                                     ###

Return this duration divided by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def div(other: Duration): Double`                                       ###

Return the quotient of this and that duration as floating-point number. The
semantics are determined by Double as if calculating the quotient of the
nanosecond lengths of both factors.

(defined at scala.concurrent.duration.Duration)


### `def gt(other: Duration): Boolean`                                       ###

(defined at scala.concurrent.duration.Duration)


### `def gteq(other: Duration): Boolean`                                     ###

(defined at scala.concurrent.duration.Duration)


### `def lt(other: Duration): Boolean`                                       ###

(defined at scala.concurrent.duration.Duration)


### `def lteq(other: Duration): Boolean`                                     ###

(defined at scala.concurrent.duration.Duration)


### `def max(other: Duration): Duration`                                     ###

Return the larger of this and that duration as determined by the natural
ordering.

(defined at scala.concurrent.duration.Duration)


### `def min(other: Duration): Duration`                                     ###

Return the smaller of this and that duration as determined by the natural
ordering.

(defined at scala.concurrent.duration.Duration)


### `def minus(other: Duration): Duration`                                   ###

Return the difference of that duration and this. When involving non-finite
summands the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def mul(factor: Double): Duration`                                      ###

Return this duration multiplied by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def neg(): Duration`                                                    ###

Negate this duration. The only two values which are mapped to themselves are
Duration.Zero and Duration.Undefined.

(defined at scala.concurrent.duration.Duration)


### `def plus(other: Duration): Duration`                                    ###

Return the sum of that duration and this. When involving non-finite summands the
semantics match those of Double.

* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


--------------------------------------------------------------------------------
                 Abstract Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `abstract def compare(that: Duration): Int`                              ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: Duration): Boolean`                                         ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: Duration): Boolean`                                        ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: Duration): Boolean`                                         ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: Duration): Boolean`                                        ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: Duration): Int`                                     ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable

(defined at scala.math.Ordered)


--------------------------------------------------------------------------------
 Concrete Value Members From Implicit scala.concurrent.duration.durationToPair
--------------------------------------------------------------------------------


### `def productElement(n: Int): Any`                                        ###

Returns the n-th projection of this product if 0 < n <= productArity, otherwise
throws an `IndexOutOfBoundsException` .

* n
  * number of the projection to be returned
* returns
  * same as `._(n+1)` , for example `productElement(0)` is the same as `._1` .

* Implicit information
  * This member is added by an implicit conversion from Duration to (Long,
    TimeUnit) performed by method durationToPair in scala.concurrent.duration.
* Definition Classes
  * Product2 → Product
* Annotations
  * @ throws (clazz = classOf[IndexOutOfBoundsException])
* Exceptions thrown
  *

(added by implicit convertion: scala.concurrent.duration.durationToPair)


### `def swap: (TimeUnit, Long)`                                             ###

Swaps the elements of this `Tuple` .

* returns
  * a new Tuple where the first element is the second element of this Tuple and
    the second element is the first element of this Tuple.

* Implicit information
  * This member is added by an implicit conversion from Duration to (Long,
    TimeUnit) performed by method durationToPair in scala.concurrent.duration.
* Definition Classes
  * Tuple2
(added by implicit convertion: scala.concurrent.duration.durationToPair)
