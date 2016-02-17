
#                      scala.concurrent.duration.Deadline                      #

```scala
case class Deadline extends Ordered[Deadline] with Product with Serializable
```

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


--------------------------------------------------------------------------------
             Value Members From scala.concurrent.duration.Deadline
--------------------------------------------------------------------------------


### `def +(other: FiniteDuration): Deadline`                                 ###

Return a deadline advanced (i.e., moved into the future) by the given duration.

(defined at scala.concurrent.duration.Deadline)


### `def -(other: Deadline): FiniteDuration`                                 ###

Calculate time difference between this and the other deadline, where the result
is directed (i.e., may be negative).

(defined at scala.concurrent.duration.Deadline)


### `def -(other: FiniteDuration): Deadline`                                 ###

Return a deadline moved backwards (i.e., towards the past) by the given
duration.

(defined at scala.concurrent.duration.Deadline)


### `def compare(other: Deadline): Int`                                      ###

The natural ordering for deadline is determined by the natural order of the
underlying (finite) duration.

* Definition Classes
  * Deadline → Ordered

(defined at scala.concurrent.duration.Deadline)


### `val time: FiniteDuration`                                               ###

(defined at scala.concurrent.duration.Deadline)


### `def timeLeft: FiniteDuration`                                           ###

Calculate time difference between this duration and now; the result is negative
if the deadline has passed.

 * _Note that on some systems this operation is costly because it entails a
system call._* Check `System.nanoTime` for your platform.

(defined at scala.concurrent.duration.Deadline)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: Deadline): Boolean`                                         ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: Deadline): Boolean`                                        ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: Deadline): Boolean`                                         ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: Deadline): Boolean`                                        ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: Deadline): Int`                                     ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable
(defined at scala.math.Ordered)
