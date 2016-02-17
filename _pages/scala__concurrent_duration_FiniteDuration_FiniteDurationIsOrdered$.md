
#       scala.concurrent.duration.FiniteDuration.FiniteDurationIsOrdered       #

```scala
implicit object FiniteDurationIsOrdered extends Ordering[FiniteDuration]
```

* Source
  * [Duration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/duration/Duration.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Ops extends AnyRef`                                               ###

This inner class defines comparison operators available for `T` .

* Definition Classes
  * Ordering


--------------------------------------------------------------------------------
                    Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[FiniteDuration]`                             ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: FiniteDuration]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: FiniteDuration]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: FiniteDuration]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: FiniteDuration]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: FiniteDuration, _ <: U]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: FiniteDuration, _ <: U], arg1: Comparator[_ >: U]): Comparator[FiniteDuration]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
Value Members From scala.concurrent.duration.FiniteDuration.FiniteDurationIsOrdered
--------------------------------------------------------------------------------


### `def compare(a: FiniteDuration, b: FiniteDuration): Int`                 ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * FiniteDurationIsOrdered → Ordering → Comparator

(defined at scala.concurrent.duration.FiniteDuration.FiniteDurationIsOrdered)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: FiniteDuration, y: FiniteDuration): Boolean`               ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: FiniteDuration, y: FiniteDuration): Boolean`                  ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: FiniteDuration, y: FiniteDuration): Boolean`                ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: FiniteDuration, y: FiniteDuration): Boolean`                  ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: FiniteDuration, y: FiniteDuration): Boolean`                ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: FiniteDuration, y: FiniteDuration): FiniteDuration`          ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: FiniteDuration, y: FiniteDuration): FiniteDuration`          ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: FiniteDuration): Ops`                   ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ FiniteDuration): math.Ordering[U]`                   ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: math.Ordering[FiniteDuration]`                             ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: FiniteDuration, y: FiniteDuration): Some[Int]`        ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering
(defined at scala.math.Ordering)
