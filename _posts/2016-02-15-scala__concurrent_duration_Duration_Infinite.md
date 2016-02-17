
#                 scala.concurrent.duration.Duration.Infinite                 #

```scala
sealed abstract class Infinite extends Duration
```

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
         Abstract Value Members From scala.concurrent.duration.Duration
--------------------------------------------------------------------------------


### `abstract def toUnit(unit: TimeUnit): Double`                            ###

Return the number of nanoseconds as floating point number, scaled down to the
given unit. The result may not precisely represent this duration due to the
Double datatype's inherent limitations (mantissa size effectively 53 bits).
Non-finite durations are represented as

* Duration.Undefined is mapped to Double.NaN
* Duration.Inf is mapped to Double.PositiveInfinity
* Duration.MinusInf is mapped to Double.NegativeInfinity

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `abstract def unary_-: Duration`                                         ###

Negate this duration. The only two values which are mapped to themselves are
Duration.Zero and Duration.Undefined.

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.concurrent.duration.Duration
--------------------------------------------------------------------------------


### `def div(divisor: Double): Duration`                                     ###

Return this duration divided by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Definition Classes
  * Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def div(other: Duration): Double`                                       ###

Return the quotient of this and that duration as floating-point number. The
semantics are determined by Double as if calculating the quotient of the
nanosecond lengths of both factors.

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def gt(other: Duration): Boolean`                                       ###

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def gteq(other: Duration): Boolean`                                     ###

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def lt(other: Duration): Boolean`                                       ###

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def lteq(other: Duration): Boolean`                                     ###

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def max(other: Duration): Duration`                                     ###

Return the larger of this and that duration as determined by the natural
ordering.

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def min(other: Duration): Duration`                                     ###

Return the smaller of this and that duration as determined by the natural
ordering.

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def minus(other: Duration): Duration`                                   ###

Return the difference of that duration and this. When involving non-finite
summands the semantics match those of Double.

* Definition Classes
  * Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def mul(factor: Double): Duration`                                      ###

Return this duration multiplied by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Definition Classes
  * Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


### `def neg(): Duration`                                                    ###

Negate this duration. The only two values which are mapped to themselves are
Duration.Zero and Duration.Undefined.

* Definition Classes
  * Duration

(defined at scala.concurrent.duration.Duration)


### `def plus(other: Duration): Duration`                                    ###

Return the sum of that duration and this. When involving non-finite summands the
semantics match those of Double.

* Definition Classes
  * Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.concurrent.duration.Duration.Infinite
--------------------------------------------------------------------------------


### `def *(factor: Double): Duration`                                        ###

Return this duration multiplied by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Definition Classes
  * Infinite → Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration.Infinite)


### `def +(other: Duration): Duration`                                       ###

Return the sum of that duration and this. When involving non-finite summands the
semantics match those of Double.

* Definition Classes
  * Infinite → Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration.Infinite)


### `def -(other: Duration): Duration`                                       ###

Return the difference of that duration and this. When involving non-finite
summands the semantics match those of Double.

* Definition Classes
  * Infinite → Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration.Infinite)


### `def /(divisor: Double): Duration`                                       ###

Return this duration divided by the scalar factor. When involving non-finite
factors the semantics match those of Double.

* Definition Classes
  * Infinite → Duration
* Exceptions thrown
  * IllegalArgumentException in case of a finite overflow: the range of a finite
    duration is +-(2^63-1)ns, and no conversion to infinite durations takes
    place.

(defined at scala.concurrent.duration.Duration.Infinite)


### `def /(divisor: Duration): Double`                                       ###

Return the quotient of this and that duration as floating-point number. The
semantics are determined by Double as if calculating the quotient of the
nanosecond lengths of both factors.

* Definition Classes
  * Infinite → Duration

(defined at scala.concurrent.duration.Duration.Infinite)


### `final def toCoarsest: Duration`                                         ###

Return duration which is equal to this duration but with a coarsest Unit, or
self in case it is already the coarsest Unit

Examples:

```scala
Duration(60, MINUTES).toCoarsest // Duration(1, HOURS)
Duration(1000, MILLISECONDS).toCoarsest // Duration(1, SECONDS)
Duration(48, HOURS).toCoarsest // Duration(2, DAYS)
Duration(5, SECONDS).toCoarsest // Duration(5, SECONDS)
```

* Definition Classes
  * Infinite → Duration

(defined at scala.concurrent.duration.Duration.Infinite)


### `final def unit: TimeUnit`                                               ###

Obtain the time unit in which the length of this duration is measured.

* Definition Classes
  * Infinite → Duration
* Exceptions thrown
  * IllegalArgumentException when invoked on a non-finite duration

(defined at scala.concurrent.duration.Duration.Infinite)


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
  * This member is added by an implicit conversion from Infinite to (Long,
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
  * This member is added by an implicit conversion from Infinite to (Long,
    TimeUnit) performed by method durationToPair in scala.concurrent.duration.
* Definition Classes
  * Tuple2
(added by implicit convertion: scala.concurrent.duration.durationToPair)
