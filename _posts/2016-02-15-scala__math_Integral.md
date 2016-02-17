
#                             scala.math.Integral                             #

```scala
trait Integral[T] extends Numeric[T]
```

* Source
  * [Integral.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Integral.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class IntegralOps extends Ops`                                          ###

* Source
  * [Integral.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Integral.scala#L1)


### `class Ops extends AnyRef`                                               ###

* Definition Classes
  * Numeric


--------------------------------------------------------------------------------
                Concrete Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[T]`                                          ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: T]): Comparator[T]`             ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: T]): Comparator[T]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: T]): Comparator[T]`       ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: T]): Comparator[T]`     ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: T, _ <: U]): Comparator[T]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: T, _ <: U], arg1: Comparator[_ >: U]): Comparator[T]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `abstract def quot(x: T, y: T): T`                                       ###

(defined at scala.math.Integral)


### `abstract def rem(x: T, y: T): T`                                        ###

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                Concrete Value Members From scala.math.Integral
--------------------------------------------------------------------------------


### `implicit def mkNumericOps(lhs: T): IntegralOps`                         ###

* Definition Classes
  * Integral → Numeric

(defined at scala.math.Integral)


--------------------------------------------------------------------------------
                 Abstract Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `abstract def fromInt(x: Int): T`                                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def minus(x: T, y: T): T`                                      ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def negate(x: T): T`                                           ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def plus(x: T, y: T): T`                                       ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def times(x: T, y: T): T`                                      ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def toDouble(x: T): Double`                                    ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def toFloat(x: T): Float`                                      ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def toInt(x: T): Int`                                          ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `abstract def toLong(x: T): Long`                                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: T): T`                                                       ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: T): Int`                                                  ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `abstract def compare(x: T, y: T): Int`                                  ###

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


### `def equiv(x: T, y: T): Boolean`                                         ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: T, y: T): Boolean`                                            ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: T, y: T): Boolean`                                          ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: T, y: T): Boolean`                                            ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: T, y: T): Boolean`                                          ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: T, y: T): T`                                                 ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: T, y: T): T`                                                 ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: T): Integral.Ops`                       ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ T): Ordering[U]`                                     ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[T]`                                               ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: T, y: T): Some[Int]`                                  ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering
(defined at scala.math.Ordering)
