
#                      scala.math.Numeric.ByteIsIntegral                      #

```scala
trait ByteIsIntegral extends Integral[Byte]
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
                Concrete Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[Byte]`                                       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Byte]): Comparator[Byte]`       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Byte]): Comparator[Byte]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Byte]): Comparator[Byte]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Byte]): Comparator[Byte]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Byte, _ <: U]): Comparator[Byte]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Byte, _ <: U], arg1: Comparator[_ >: U]): Comparator[Byte]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                Concrete Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Byte): IntegralOps`                      ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: Byte): Byte`                                                 ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: Byte`                                                          ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Byte): Int`                                               ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Byte`                                                         ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.math.Numeric.ByteIsIntegral
--------------------------------------------------------------------------------


### `def fromInt(x: Int): Byte`                                              ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def minus(x: Byte, y: Byte): Byte`                                      ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def negate(x: Byte): Byte`                                              ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def plus(x: Byte, y: Byte): Byte`                                       ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def quot(x: Byte, y: Byte): Byte`                                       ###

* Definition Classes
  * ByteIsIntegral → Integral

(defined at scala.math.Numeric.ByteIsIntegral)


### `def rem(x: Byte, y: Byte): Byte`                                        ###

* Definition Classes
  * ByteIsIntegral → Integral

(defined at scala.math.Numeric.ByteIsIntegral)


### `def times(x: Byte, y: Byte): Byte`                                      ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def toDouble(x: Byte): Double`                                          ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def toFloat(x: Byte): Float`                                            ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def toInt(x: Byte): Int`                                                ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


### `def toLong(x: Byte): Long`                                              ###

* Definition Classes
  * ByteIsIntegral → Numeric

(defined at scala.math.Numeric.ByteIsIntegral)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `abstract def compare(x: Byte, y: Byte): Int`                            ###

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


### `def equiv(x: Byte, y: Byte): Boolean`                                   ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: Byte, y: Byte): Boolean`                                      ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: Byte, y: Byte): Boolean`                                    ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: Byte, y: Byte): Boolean`                                      ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: Byte, y: Byte): Boolean`                                    ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: Byte, y: Byte): Byte`                                        ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: Byte, y: Byte): Byte`                                        ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: Byte): ByteIsIntegral.Ops`              ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Byte): Ordering[U]`                                  ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[Byte]`                                            ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: Byte, y: Byte): Some[Int]`                            ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering
(defined at scala.math.Ordering)
