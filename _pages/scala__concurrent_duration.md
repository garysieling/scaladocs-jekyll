
#                          scala.concurrent.duration                          #

```scala
package duration
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `case class Deadline extends Ordered[Deadline] with Product with Serializable` ###

This class stores a deadline, as obtained via `Deadline.now` or the duration
DSL:

```scala
import scala.concurrent.duration._
3.seconds.fromNow
```

Its main purpose is to manage repeated attempts to achieve something (like
awaiting a condition) by offering the methods `hasTimeLeft` and `timeLeft` . All
durations are measured according to `System.nanoTime` aka wall-time; this does
not take into account changes to the system clock (such as leap seconds).

* Source
  * [Deadline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Deadline.scala#L1)


### `implicit final class DoubleMult extends AnyVal`                         ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `sealed abstract class Duration extends Serializable with Ordered[Duration]` ###

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


### `trait DurationConversions extends Any`                                  ###

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)


### `implicit final class DurationDouble extends AnyVal with DurationConversions` ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `implicit final class DurationInt extends AnyVal with DurationConversions` ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `implicit final class DurationLong extends AnyVal with DurationConversions` ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `final class FiniteDuration extends Duration`                            ###

This class represents a finite duration. Its addition and subtraction operators
are overloaded to retain this guarantee statically. The range of this class is
limited to +-(2^63-1)ns, which is roughly 292 years.

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


### `implicit final class IntMult extends AnyVal`                            ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `implicit final class LongMult extends AnyVal`                           ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `type TimeUnit = java.util.concurrent.TimeUnit`                          ###


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Deadline extends Serializable`                                   ###

* Source
  * [Deadline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Deadline.scala#L1)


### `object Duration extends Serializable`                                   ###

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


### `object DurationConversions`                                             ###

This object just holds some cogs which make the DSL machine work, not for direct
consumption.

* Source
  * [DurationConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/DurationConversions.scala#L1)


### `object FiniteDuration extends Serializable`                             ###

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


### `object fromNow`                                                         ###

This object can be used as closing token for declaring a deadline at some future
point in time:

```scala
import scala.concurrent.duration._

val deadline = 3 seconds fromNow
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


### `object span`                                                            ###

This object can be used as closing token if you prefer dot-less style but do not
want to enable language.postfixOps:

```scala
import scala.concurrent.duration._

val duration = 2 seconds span
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/package.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.concurrent.duration
--------------------------------------------------------------------------------


### `final val DAYS: java.util.concurrent.TimeUnit(DAYS)`                    ###

(defined at scala.concurrent.duration)


### `implicit def durationToPair(d: Duration): (Long, TimeUnit)`             ###

(defined at scala.concurrent.duration)


### `implicit def pairIntToDuration(p: (Int, TimeUnit)): Duration`           ###

(defined at scala.concurrent.duration)


### `implicit def pairLongToDuration(p: (Long, TimeUnit)): FiniteDuration`   ###
(defined at scala.concurrent.duration)
