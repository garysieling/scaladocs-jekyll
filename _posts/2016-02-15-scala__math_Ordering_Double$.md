
#                          scala.math.Ordering.Double                          #

```scala
implicit object Double extends DoubleOrdering
```

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


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
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `implicit def mkOrderingOps(lhs: Double): Ops`                           ###

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


### `def tryCompare(x: Double, y: Double): Some[Int]`                        ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
             Value Members From scala.math.Ordering.DoubleOrdering
--------------------------------------------------------------------------------


### `def compare(x: Double, y: Double): Int`                                 ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * DoubleOrdering → Ordering → Comparator

(defined at scala.math.Ordering.DoubleOrdering)


### `def equiv(x: Double, y: Double): Boolean`                               ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering.DoubleOrdering)


### `def gt(x: Double, y: Double): Boolean`                                  ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.DoubleOrdering)


### `def gteq(x: Double, y: Double): Boolean`                                ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.DoubleOrdering)


### `def lt(x: Double, y: Double): Boolean`                                  ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.DoubleOrdering)


### `def lteq(x: Double, y: Double): Boolean`                                ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering

(defined at scala.math.Ordering.DoubleOrdering)


### `def max(x: Double, y: Double): Double`                                  ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * DoubleOrdering → Ordering

(defined at scala.math.Ordering.DoubleOrdering)


### `def min(x: Double, y: Double): Double`                                  ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * DoubleOrdering → Ordering

(defined at scala.math.Ordering.DoubleOrdering)


### `def reverse: Ordering[Double]`                                          ###

Return the opposite ordering of this one.

* Definition Classes
  * DoubleOrdering → Ordering → PartialOrdering
(defined at scala.math.Ordering.DoubleOrdering)
