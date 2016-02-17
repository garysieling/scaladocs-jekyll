
#                     scala.math.Numeric.BigIntIsIntegral                     #

```scala
implicit object BigIntIsIntegral extends BigIntIsIntegral with BigIntOrdering
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


### `def reversed(): Comparator[BigInt]`                                     ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: BigInt]): Comparator[BigInt]`   ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: BigInt]): Comparator[BigInt]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: BigInt]): Comparator[BigInt]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: BigInt]): Comparator[BigInt]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: BigInt, _ <: U]): Comparator[BigInt]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: BigInt, _ <: U], arg1: Comparator[_ >: U]): Comparator[BigInt]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: BigInt): IntegralOps`                    ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: BigInt): BigInt`                                             ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: BigInt`                                                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: BigInt): Int`                                             ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: BigInt`                                                       ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
             Value Members From scala.math.Numeric.BigIntIsIntegral
--------------------------------------------------------------------------------


### `def fromInt(x: Int): BigInt`                                            ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def minus(x: BigInt, y: BigInt): BigInt`                                ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def negate(x: BigInt): BigInt`                                          ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def plus(x: BigInt, y: BigInt): BigInt`                                 ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def quot(x: BigInt, y: BigInt): BigInt`                                 ###

* Definition Classes
  * BigIntIsIntegral → Integral

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def rem(x: BigInt, y: BigInt): BigInt`                                  ###

* Definition Classes
  * BigIntIsIntegral → Integral

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def times(x: BigInt, y: BigInt): BigInt`                                ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def toDouble(x: BigInt): Double`                                        ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def toFloat(x: BigInt): Float`                                          ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def toInt(x: BigInt): Int`                                              ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


### `def toLong(x: BigInt): Long`                                            ###

* Definition Classes
  * BigIntIsIntegral → Numeric

(defined at scala.math.Numeric.BigIntIsIntegral)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: BigInt, y: BigInt): Boolean`                               ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: BigInt, y: BigInt): Boolean`                                  ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: BigInt, y: BigInt): Boolean`                                ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: BigInt, y: BigInt): Boolean`                                  ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: BigInt, y: BigInt): Boolean`                                ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: BigInt, y: BigInt): BigInt`                                  ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: BigInt, y: BigInt): BigInt`                                  ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: BigInt): BigIntIsIntegral.Ops`          ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ BigInt): Ordering[U]`                                ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[BigInt]`                                          ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: BigInt, y: BigInt): Some[Int]`                        ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
             Value Members From scala.math.Ordering.BigIntOrdering
--------------------------------------------------------------------------------


### `def compare(x: BigInt, y: BigInt): Int`                                 ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * BigIntOrdering → Ordering → Comparator
(defined at scala.math.Ordering.BigIntOrdering)
