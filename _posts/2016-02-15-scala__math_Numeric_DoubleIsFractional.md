
#                    scala.math.Numeric.DoubleIsFractional                    #

```scala
trait DoubleIsFractional extends DoubleIsConflicted with Fractional[Double]
```

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class FractionalOps extends Ops`                                        ###

* Definition Classes
  * Fractional


### `class Ops extends AnyRef`                                               ###

* Definition Classes
  * Numeric


--------------------------------------------------------------------------------
                Concrete Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[Double]`                                     ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Double]): Comparator[Double]`   ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Double]): Comparator[Double]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Double]): Comparator[Double]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Double]): Comparator[Double]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Double, _ <: U]): Comparator[Double]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Double, _ <: U], arg1: Comparator[_ >: U]): Comparator[Double]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.math.Fractional
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Double): FractionalOps`                  ###

* Definition Classes
  * Fractional → Numeric

(defined at scala.math.Fractional)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def one: Double`                                                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Double): Int`                                             ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Double`                                                       ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.math.Numeric.DoubleIsConflicted
--------------------------------------------------------------------------------


### `def abs(x: Double): Double`                                             ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def fromInt(x: Int): Double`                                            ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def minus(x: Double, y: Double): Double`                                ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def negate(x: Double): Double`                                          ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def plus(x: Double, y: Double): Double`                                 ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def times(x: Double, y: Double): Double`                                ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def toDouble(x: Double): Double`                                        ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def toFloat(x: Double): Float`                                          ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def toInt(x: Double): Int`                                              ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


### `def toLong(x: Double): Long`                                            ###

* Definition Classes
  * DoubleIsConflicted → Numeric

(defined at scala.math.Numeric.DoubleIsConflicted)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.math.Numeric.DoubleIsFractional
--------------------------------------------------------------------------------


### `def div(x: Double, y: Double): Double`                                  ###

* Definition Classes
  * DoubleIsFractional → Fractional

(defined at scala.math.Numeric.DoubleIsFractional)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `abstract def compare(x: Double, y: Double): Int`                        ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * Ordering → Comparator

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
                Concrete Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: Double, y: Double): Boolean`                               ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: Double, y: Double): Boolean`                                  ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: Double, y: Double): Boolean`                                ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: Double, y: Double): Boolean`                                  ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: Double, y: Double): Boolean`                                ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: Double, y: Double): Double`                                  ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: Double, y: Double): Double`                                  ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: Double): DoubleIsFractional.Ops`        ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Double): Ordering[U]`                                ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[Double]`                                          ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: Double, y: Double): Some[Int]`                        ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering
(defined at scala.math.Ordering)
