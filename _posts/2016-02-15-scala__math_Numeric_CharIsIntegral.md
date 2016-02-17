
#                      scala.math.Numeric.CharIsIntegral                      #

```scala
trait CharIsIntegral extends Integral[Char]
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


### `def reversed(): Comparator[Char]`                                       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Char]): Comparator[Char]`       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Char]): Comparator[Char]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Char]): Comparator[Char]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Char]): Comparator[Char]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Char, _ <: U]): Comparator[Char]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Char, _ <: U], arg1: Comparator[_ >: U]): Comparator[Char]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                Concrete Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Char): IntegralOps`                      ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: Char): Char`                                                 ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: Char`                                                          ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Char): Int`                                               ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Char`                                                         ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.math.Numeric.CharIsIntegral
--------------------------------------------------------------------------------


### `def fromInt(x: Int): Char`                                              ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def minus(x: Char, y: Char): Char`                                      ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def negate(x: Char): Char`                                              ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def plus(x: Char, y: Char): Char`                                       ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def quot(x: Char, y: Char): Char`                                       ###

* Definition Classes
  * CharIsIntegral → Integral

(defined at scala.math.Numeric.CharIsIntegral)


### `def rem(x: Char, y: Char): Char`                                        ###

* Definition Classes
  * CharIsIntegral → Integral

(defined at scala.math.Numeric.CharIsIntegral)


### `def times(x: Char, y: Char): Char`                                      ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def toDouble(x: Char): Double`                                          ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def toFloat(x: Char): Float`                                            ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def toInt(x: Char): Int`                                                ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


### `def toLong(x: Char): Long`                                              ###

* Definition Classes
  * CharIsIntegral → Numeric

(defined at scala.math.Numeric.CharIsIntegral)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `abstract def compare(x: Char, y: Char): Int`                            ###

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


### `def equiv(x: Char, y: Char): Boolean`                                   ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: Char, y: Char): Boolean`                                      ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: Char, y: Char): Boolean`                                    ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: Char, y: Char): Boolean`                                      ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: Char, y: Char): Boolean`                                    ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: Char, y: Char): Char`                                        ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: Char, y: Char): Char`                                        ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: Char): CharIsIntegral.Ops`              ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Char): Ordering[U]`                                  ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[Char]`                                            ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: Char, y: Char): Some[Int]`                            ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering
(defined at scala.math.Ordering)
