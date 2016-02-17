
#                     scala.math.Numeric.FloatIsFractional                     #

```scala
implicit object FloatIsFractional extends FloatIsFractional with FloatOrdering
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
                    Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[Float]`                                      ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: Float]): Comparator[Float]`     ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: Float]): Comparator[Float]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: Float]): Comparator[Float]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: Float]): Comparator[Float]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: Float, _ <: U]): Comparator[Float]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: Float, _ <: U], arg1: Comparator[_ >: U]): Comparator[Float]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                    Value Members From scala.math.Fractional
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: Float): FractionalOps`                   ###

* Definition Classes
  * Fractional → Numeric

(defined at scala.math.Fractional)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def one: Float`                                                         ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: Float): Int`                                              ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: Float`                                                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
            Value Members From scala.math.Numeric.FloatIsConflicted
--------------------------------------------------------------------------------


### `def abs(x: Float): Float`                                               ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def fromInt(x: Int): Float`                                             ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def minus(x: Float, y: Float): Float`                                   ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def negate(x: Float): Float`                                            ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def plus(x: Float, y: Float): Float`                                    ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def times(x: Float, y: Float): Float`                                   ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def toDouble(x: Float): Double`                                         ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def toFloat(x: Float): Float`                                           ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def toInt(x: Float): Int`                                               ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


### `def toLong(x: Float): Long`                                             ###

* Definition Classes
  * FloatIsConflicted → Numeric

(defined at scala.math.Numeric.FloatIsConflicted)


--------------------------------------------------------------------------------
            Value Members From scala.math.Numeric.FloatIsFractional
--------------------------------------------------------------------------------


### `def div(x: Float, y: Float): Float`                                     ###

* Definition Classes
  * FloatIsFractional → Fractional

(defined at scala.math.Numeric.FloatIsFractional)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `implicit def mkOrderingOps(lhs: Float): FloatIsFractional.Ops`          ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ Float): Ordering[U]`                                 ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def tryCompare(x: Float, y: Float): Some[Int]`                          ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
              Value Members From scala.math.Ordering.FloatOrdering
--------------------------------------------------------------------------------


### `def compare(x: Float, y: Float): Int`                                   ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * FloatOrdering → Ordering → Comparator

(defined at scala.math.Ordering.FloatOrdering)


### `def equiv(x: Float, y: Float): Boolean`                                 ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering.FloatOrdering)


### `def gt(x: Float, y: Float): Boolean`                                    ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.FloatOrdering)


### `def gteq(x: Float, y: Float): Boolean`                                  ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.FloatOrdering)


### `def lt(x: Float, y: Float): Boolean`                                    ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.FloatOrdering)


### `def lteq(x: Float, y: Float): Boolean`                                  ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.FloatOrdering)


### `def max(x: Float, y: Float): Float`                                     ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * FloatOrdering → Ordering

(defined at scala.math.Ordering.FloatOrdering)


### `def min(x: Float, y: Float): Float`                                     ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * FloatOrdering → Ordering

(defined at scala.math.Ordering.FloatOrdering)


### `def reverse: Ordering[Float]`                                           ###

Return the opposite ordering of this one.

* Definition Classes
  * FloatOrdering → Ordering → PartialOrdering
(defined at scala.math.Ordering.FloatOrdering)
