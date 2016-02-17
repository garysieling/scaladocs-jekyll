
#                      scala.concurrent.duration.Duration                      #

```scala
object Duration extends Serializable
```

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `sealed abstract class Infinite extends Duration`                        ###

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `implicit object DurationIsOrdered extends Ordering[Duration]`           ###

The natural ordering of durations matches the natural ordering for Double,
including non-finite values.

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.concurrent.duration.Duration
--------------------------------------------------------------------------------


### `val Inf: Infinite`                                                      ###

Infinite duration: greater than any other (apart from Undefined) and not equal
to any other but itself. This value closely corresponds to
Double.PositiveInfinity, matching its semantics in arithmetic operations.

(defined at scala.concurrent.duration.Duration)


### `val MinusInf: Infinite`                                                 ###

Infinite duration: less than any other and not equal to any other but itself.
This value closely corresponds to Double.NegativeInfinity, matching its
semantics in arithmetic operations.

(defined at scala.concurrent.duration.Duration)


### `val Undefined: Infinite`                                                ###

The Undefined value corresponds closely to Double.NaN:

* it is the result of otherwise invalid operations
* it does not equal itself (according to `equals()` )
* it compares greater than any other Duration apart from itself (for which
    `compare` returns 0)

The particular comparison semantics mirror those of Double.NaN.

 * _Use `eq` when checking an input of a method against this value._*

(defined at scala.concurrent.duration.Duration)


### `val Zero: FiniteDuration`                                               ###

Preconstructed value of `0.days` .

(defined at scala.concurrent.duration.Duration)


### `def apply(length: Double, unit: TimeUnit): Duration`                    ###

Construct a Duration from the given length and unit. Observe that nanosecond
precision may be lost if

* the unit is NANOSECONDS
* and the length has an absolute value greater than 2^53

Infinite inputs (and NaN) are converted into Duration.Inf, Duration.MinusInf and
Duration.Undefined, respectively.

* Exceptions thrown
  * IllegalArgumentException if the length was finite but the resulting duration
    cannot be expressed as a FiniteDuration

(defined at scala.concurrent.duration.Duration)


### `def apply(length: Long, unit: String): FiniteDuration`                  ###

Construct a finite duration from the given length and time unit, where the
latter is looked up in a list of string representation. Valid choices are:

 `d, day, h, hour, min, minute, s, sec, second, ms, milli, millisecond, µs, micro, microsecond, ns, nano, nanosecond`
and their pluralized forms (for every but the first mentioned form of each unit,
i.e. no "ds", but "days").

(defined at scala.concurrent.duration.Duration)


### `def apply(length: Long, unit: TimeUnit): FiniteDuration`                ###

Construct a finite duration from the given length and time unit. The unit given
is retained throughout calculations as long as possible, so that it can be
retrieved later.

(defined at scala.concurrent.duration.Duration)


### `def apply(s: String): Duration`                                         ###

Parse String into Duration. Format is `"<length><unit>"` , where whitespace is
allowed before, between and after the parts. Infinities are designated by
 `"Inf"` , `"PlusInf"` , `"+Inf"` and `"-Inf"` or `"MinusInf"` .

* Exceptions thrown
  * NumberFormatException if format is not parseable

(defined at scala.concurrent.duration.Duration)


### `def create(length: Double, unit: TimeUnit): Duration`                   ###

Construct a Duration from the given length and unit. Observe that nanosecond
precision may be lost if

* the unit is NANOSECONDS
* and the length has an absolute value greater than 2^53

Infinite inputs (and NaN) are converted into Duration.Inf, Duration.MinusInf and
Duration.Undefined, respectively.

* Exceptions thrown
  * IllegalArgumentException if the length was finite but the resulting duration
    cannot be expressed as a FiniteDuration

(defined at scala.concurrent.duration.Duration)


### `def create(length: Long, unit: String): FiniteDuration`                 ###

Construct a finite duration from the given length and time unit, where the
latter is looked up in a list of string representation. Valid choices are:

 `d, day, h, hour, min, minute, s, sec, second, ms, milli, millisecond, µs, micro, microsecond, ns, nano, nanosecond`
and their pluralized forms (for every but the first mentioned form of each unit,
i.e. no "ds", but "days").

(defined at scala.concurrent.duration.Duration)


### `def create(length: Long, unit: TimeUnit): FiniteDuration`               ###

Construct a finite duration from the given length and time unit. The unit given
is retained throughout calculations as long as possible, so that it can be
retrieved later.

(defined at scala.concurrent.duration.Duration)


### `def create(s: String): Duration`                                        ###

Parse String into Duration. Format is `"<length><unit>"` , where whitespace is
allowed before, between and after the parts. Infinities are designated by
 `"Inf"` , `"PlusInf"` , `"+Inf"` and `"-Inf"` or `"MinusInf"` .

* Exceptions thrown
  * NumberFormatException if format is not parseable

(defined at scala.concurrent.duration.Duration)


### `def fromNanos(nanos: Double): Duration`                                 ###

Construct a possibly infinite or undefined Duration from the given number of
nanoseconds.

*  `Double.PositiveInfinity` is mapped to Duration.Inf
*  `Double.NegativeInfinity` is mapped to Duration.MinusInf
*  `Double.NaN` is mapped to Duration.Undefined
*  `-0d` is mapped to Duration.Zero (exactly like `0d` )

The semantics of the resulting Duration objects matches the semantics of their
Double counterparts with respect to arithmetic operations.

* Exceptions thrown
  * IllegalArgumentException if the length was finite but the resulting duration
    cannot be expressed as a FiniteDuration

(defined at scala.concurrent.duration.Duration)


### `def fromNanos(nanos: Long): FiniteDuration`                             ###

Construct a finite duration from the given number of nanoseconds. The result
will have the coarsest possible time unit which can exactly express this
duration.

* Exceptions thrown
  * IllegalArgumentException for `Long.MinValue` since that would lead to
    inconsistent behavior afterwards (cannot be negated)

(defined at scala.concurrent.duration.Duration)


### `val timeUnit: Map[String, TimeUnit]`                                    ###

* Attributes
  * protected[scala.concurrent.duration]

(defined at scala.concurrent.duration.Duration)


### `val timeUnitName: Map[TimeUnit, String]`                                ###

* Attributes
  * protected[scala.concurrent.duration]

(defined at scala.concurrent.duration.Duration)


### `def unapply(d: Duration): Option[(Long, TimeUnit)]`                     ###

Extract length and time unit out of a duration, if it is finite.

(defined at scala.concurrent.duration.Duration)


### `def unapply(s: String): Option[(Long, TimeUnit)]`                       ###

Extract length and time unit out of a string, where the format must match the
description for apply(String). The extractor will not match for malformed
strings or non-finite durations.
(defined at scala.concurrent.duration.Duration)
