
#                       scala.math.Numeric.IntIsIntegral                       #

```scala
implicit object IntIsIntegral extends IntIsIntegral with IntOrdering
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


### `def reversed(): Comparator[Int]`                                        ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Int]): Comparator[Int]`         ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Int]): Comparator[Int]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Int]): Comparator[Int]`   ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Int]): Comparator[Int]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Int, _ <: U]): Comparator[Int]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Int, _ <: U], arg1: Comparator[_ >: U]): Comparator[Int]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Int): IntegralOps`                       ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: Int): Int`                                                   ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: Int`                                                           ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Int): Int`                                                ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Int`                                                          ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
              Value Members From scala.math.Numeric.IntIsIntegral
--------------------------------------------------------------------------------


### `def fromInt(x: Int): Int`                                               ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def minus(x: Int, y: Int): Int`                                         ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def negate(x: Int): Int`                                                ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def plus(x: Int, y: Int): Int`                                          ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def quot(x: Int, y: Int): Int`                                          ###

* Definition Classes
  * IntIsIntegral → Integral

(defined at scala.math.Numeric.IntIsIntegral)


### `def rem(x: Int, y: Int): Int`                                           ###

* Definition Classes
  * IntIsIntegral → Integral

(defined at scala.math.Numeric.IntIsIntegral)


### `def times(x: Int, y: Int): Int`                                         ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def toDouble(x: Int): Double`                                           ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def toFloat(x: Int): Float`                                             ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def toInt(x: Int): Int`                                                 ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


### `def toLong(x: Int): Long`                                               ###

* Definition Classes
  * IntIsIntegral → Numeric

(defined at scala.math.Numeric.IntIsIntegral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: Int, y: Int): Boolean`                                     ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: Int, y: Int): Boolean`                                        ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: Int, y: Int): Boolean`                                      ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: Int, y: Int): Boolean`                                        ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: Int, y: Int): Boolean`                                      ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: Int, y: Int): Int`                                           ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: Int, y: Int): Int`                                           ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: Int): IntIsIntegral.Ops`                ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Int): Ordering[U]`                                   ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[Int]`                                             ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: Int, y: Int): Some[Int]`                              ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
               Value Members From scala.math.Ordering.IntOrdering
--------------------------------------------------------------------------------


### `def compare(x: Int, y: Int): Int`                                       ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * IntOrdering → Ordering → Comparator
(defined at scala.math.Ordering.IntOrdering)
