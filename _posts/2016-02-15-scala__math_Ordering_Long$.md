
#                           scala.math.Ordering.Long                           #

```scala
implicit object Long extends LongOrdering
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


### `implicit def mkOrderingOps(lhs: Long): Ops`                             ###

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
