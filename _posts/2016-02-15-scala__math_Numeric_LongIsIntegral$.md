
#                      scala.math.Numeric.LongIsIntegral                      #

```scala
implicit object LongIsIntegral extends LongIsIntegral with LongOrdering
```

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class IntegralOps extends Ops`                                          ###

* Definition Classes
  * Integral


### `class Ops extends AnyRef`                                               ###

* Definition Classes
  * Numeric


--------------------------------------------------------------------------------
                    Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[Long]`                                       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Long]): Comparator[Long]`       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Long]): Comparator[Long]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Long]): Comparator[Long]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Long]): Comparator[Long]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Long, _ <: U]): Comparator[Long]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Long, _ <: U], arg1: Comparator[_ >: U]): Comparator[Long]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Long): IntegralOps`                      ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: Long): Long`                                                 ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: Long`                                                          ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Long): Int`                                               ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Long`                                                         ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
              Value Members From scala.math.Numeric.LongIsIntegral
--------------------------------------------------------------------------------


### `def fromInt(x: Int): Long`                                              ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def minus(x: Long, y: Long): Long`                                      ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def negate(x: Long): Long`                                              ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def plus(x: Long, y: Long): Long`                                       ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def quot(x: Long, y: Long): Long`                                       ###

* Definition Classes
  * LongIsIntegral → Integral

(defined at scala.math.Numeric.LongIsIntegral)


### `def rem(x: Long, y: Long): Long`                                        ###

* Definition Classes
  * LongIsIntegral → Integral

(defined at scala.math.Numeric.LongIsIntegral)


### `def times(x: Long, y: Long): Long`                                      ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def toDouble(x: Long): Double`                                          ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def toFloat(x: Long): Float`                                            ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def toInt(x: Long): Int`                                                ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


### `def toLong(x: Long): Long`                                              ###

* Definition Classes
  * LongIsIntegral → Numeric

(defined at scala.math.Numeric.LongIsIntegral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: Long, y: Long): Boolean`                                   ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: Long, y: Long): Boolean`                                      ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: Long, y: Long): Boolean`                                    ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: Long, y: Long): Boolean`                                      ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: Long, y: Long): Boolean`                                    ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: Long, y: Long): Long`                                        ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: Long, y: Long): Long`                                        ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: Long): LongIsIntegral.Ops`              ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Long): Ordering[U]`                                  ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[Long]`                                            ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: Long, y: Long): Some[Int]`                            ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
              Value Members From scala.math.Ordering.LongOrdering
--------------------------------------------------------------------------------


### `def compare(x: Long, y: Long): Int`                                     ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * LongOrdering → Ordering → Comparator
(defined at scala.math.Ordering.LongOrdering)
