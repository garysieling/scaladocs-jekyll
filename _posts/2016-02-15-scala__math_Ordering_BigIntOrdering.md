
#                      scala.math.Ordering.BigIntOrdering                      #

```scala
trait BigIntOrdering extends Ordering[BigInt]
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


### `implicit def mkOrderingOps(lhs: BigInt): Ops`                           ###

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


--------------------------------------------------------------------------------
        Value Members From Implicit scala.math.Ordered.orderingToOrdered
--------------------------------------------------------------------------------


### `def <(that: BigIntOrdering): Boolean`                                   ###

Returns true if `this` is less than `that`

* Implicit information
  * This member is added by an implicit conversion from BigIntOrdering to
    Ordered [BigIntOrdering] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigIntOrdering] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def <=(that: BigIntOrdering): Boolean`                                  ###

Returns true if `this` is less than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from BigIntOrdering to
    Ordered [BigIntOrdering] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigIntOrdering] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def >(that: BigIntOrdering): Boolean`                                   ###

Returns true if `this` is greater than `that` .

* Implicit information
  * This member is added by an implicit conversion from BigIntOrdering to
    Ordered [BigIntOrdering] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigIntOrdering] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def >=(that: BigIntOrdering): Boolean`                                  ###

Returns true if `this` is greater than or equal to `that` .

* Implicit information
  * This member is added by an implicit conversion from BigIntOrdering to
    Ordered [BigIntOrdering] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigIntOrdering] is in scope.
* Definition Classes
  * Ordered

(added by implicit convertion: scala.math.Ordered.orderingToOrdered)


### `def compareTo(that: BigIntOrdering): Int`                               ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from BigIntOrdering to
    Ordered [BigIntOrdering] performed by method orderingToOrdered in
    scala.math.Ordered. This conversion will take place only if an implicit
    value of type Ordering [BigIntOrdering] is in scope.
* Definition Classes
  * Ordered → Comparable
(added by implicit convertion: scala.math.Ordered.orderingToOrdered)
