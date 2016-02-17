
#                          scala.math.Ordering.String                          #

```scala
implicit object String extends StringOrdering
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


### `def reversed(): Comparator[String]`                                     ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing(arg0: Comparator[_ >: String]): Comparator[String]`   ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingDouble(arg0: ToDoubleFunction[_ >: String]): Comparator[String]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingInt(arg0: ToIntFunction[_ >: String]): Comparator[String]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparingLong(arg0: ToLongFunction[_ >: String]): Comparator[String]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U <: Comparable[_ >: U]](arg0: java.util.function.Function[_ >: String, _ <: U]): Comparator[String]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


### `def thenComparing[U](arg0: java.util.function.Function[_ >: String, _ <: U], arg1: Comparator[_ >: U]): Comparator[String]` ###

* Definition Classes
  * Comparator

(defined at java.util.Comparator)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `def equiv(x: String, y: String): Boolean`                               ###

Return true if `x` == `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering → Equiv

(defined at scala.math.Ordering)


### `def gt(x: String, y: String): Boolean`                                  ###

Return true if `x` > `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def gteq(x: String, y: String): Boolean`                                ###

Return true if `x` >= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lt(x: String, y: String): Boolean`                                  ###

Return true if `x` < `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def lteq(x: String, y: String): Boolean`                                ###

Return true if `x` <= `y` in the ordering.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def max(x: String, y: String): String`                                  ###

Return `x` if `x` >= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def min(x: String, y: String): String`                                  ###

Return `x` if `x` <= `y` , otherwise `y` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: String): Ops`                           ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ String): Ordering[U]`                                ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

* Definition Classes
  * Ordering

(defined at scala.math.Ordering)


### `def reverse: Ordering[String]`                                          ###

Return the opposite ordering of this one.

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


### `def tryCompare(x: String, y: String): Some[Int]`                        ###

Returns whether a comparison between `x` and `y` is defined, and if so the
result of `compare(x, y)` .

* Definition Classes
  * Ordering → PartialOrdering

(defined at scala.math.Ordering)


--------------------------------------------------------------------------------
             Value Members From scala.math.Ordering.StringOrdering
--------------------------------------------------------------------------------


### `def compare(x: String, y: String): Int`                                 ###

Returns an integer whose sign communicates how x compares to y.

The result sign has the following meaning:

* negative if x < y
* positive if x > y
* zero otherwise (if x == y)

* Definition Classes
  * StringOrdering → Ordering → Comparator
(defined at scala.math.Ordering.StringOrdering)
