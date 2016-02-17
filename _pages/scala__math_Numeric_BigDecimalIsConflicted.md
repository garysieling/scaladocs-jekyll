
#                  scala.math.Numeric.BigDecimalIsConflicted                  #

```scala
trait BigDecimalIsConflicted extends Numeric[BigDecimal]
```

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Ops extends AnyRef`                                               ###

* Definition Classes
  * Numeric


--------------------------------------------------------------------------------
                Concrete Value Members From java.util.Comparator
--------------------------------------------------------------------------------


### `def reversed(): Comparator[BigDecimal]`                                 ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: BigDecimal]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: BigDecimal]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: BigDecimal]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: BigDecimal]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: BigDecimal, _ <: U]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: BigDecimal, _ <: U], arg1: Comparator[_ >: U]): Comparator[BigDecimal]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Numeric
--------------------------------------------------------------------------------


### `def abs(x: BigDecimal): BigDecimal`                                     ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `implicit def mkNumericOps(lhs: BigDecimal): Ops`                        ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def one: BigDecimal`                                                    ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def signum(x: BigDecimal): Int`                                         ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


### `def zero: BigDecimal`                                                   ###

* Definition Classes
  * Numeric

(defined at scala.math.Numeric)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.math.Numeric.BigDecimalIsConflicted
--------------------------------------------------------------------------------


### `def fromInt(x: Int): BigDecimal`                                        ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def minus(x: BigDecimal, y: BigDecimal): BigDecimal`                    ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def negate(x: BigDecimal): BigDecimal`                                  ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def plus(x: BigDecimal, y: BigDecimal): BigDecimal`                     ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def times(x: BigDecimal, y: BigDecimal): BigDecimal`                    ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def toDouble(x: BigDecimal): Double`                                    ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def toFloat(x: BigDecimal): Float`                                      ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def toInt(x: BigDecimal): Int`                                          ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


### `def toLong(x: BigDecimal): Long`                                        ###

* Definition Classes
  * BigDecimalIsConflicted → Numeric

(defined at scala.math.Numeric.BigDecimalIsConflicted)


--------------------------------------------------------------------------------
                Abstract Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `abstract def compare(x: BigDecimal, y: BigDecimal): Int`                ###

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


### `def equiv(x: BigDecimal, y: BigDecimal): Boolean`                       ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: BigDecimal, y: BigDecimal): Boolean`                          ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: BigDecimal, y: BigDecimal): Boolean`                        ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: BigDecimal, y: BigDecimal): Boolean`                          ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: BigDecimal, y: BigDecimal): Boolean`                        ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: BigDecimal, y: BigDecimal): BigDecimal`                      ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: BigDecimal, y: BigDecimal): BigDecimal`                      ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: BigDecimal): BigDecimalIsConflicted.Ops` ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ BigDecimal): Ordering[U]`                            ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[BigDecimal]`                                      ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: BigDecimal, y: BigDecimal): Some[Int]`                ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
   Concrete Value Members From Implicit scala.math.Ordered.orderingToOrdered
--------------------------------------------------------------------------------


### `def <(that: BigDecimalIsConflicted): Boolean`                           ###

Returns true if `this` is less than `that`

* Implicit information
  * This member is added by an implicit conversion from BigDecimalIsConflicted
    to Ordered [BigDecimalIsConflicted] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigDecimalIsConflicted] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def <=(that: BigDecimalIsConflicted): Boolean`                          ###

Returns true if `this` is less than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from BigDecimalIsConflicted
    to Ordered [BigDecimalIsConflicted] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigDecimalIsConflicted] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def >(that: BigDecimalIsConflicted): Boolean`                           ###

Returns true if `this` is greater than `that` .

* Implicit information
  * This member is added by an implicit conversion from BigDecimalIsConflicted
    to Ordered [BigDecimalIsConflicted] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigDecimalIsConflicted] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def >=(that: BigDecimalIsConflicted): Boolean`                          ###

Returns true if `this` is greater than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from BigDecimalIsConflicted
    to Ordered [BigDecimalIsConflicted] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigDecimalIsConflicted] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def compareTo(that: BigDecimalIsConflicted): Int`                       ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from BigDecimalIsConflicted
    to Ordered [BigDecimalIsConflicted] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigDecimalIsConflicted] is in scope.
* Definition Classes
  * Ordered → Comparable
(added by implicit convertion: scala.math.Ordered.orderingToOrdered)
