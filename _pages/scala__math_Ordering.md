
#                             scala.math.Ordering                             #

```scala
trait Ordering[T] extends Comparator[T] with PartialOrdering[T] with Serializable
```

Ordering is a trait whose instances each represent a strategy for sorting
instances of a type.

Ordering's companion object defines many implicit objects to deal with subtypes
of AnyVal (e.g. Int, Double), String, and others.

To sort instances by one or more member variables, you can take advantage of
these built-in orderings using Ordering.by and Ordering.on:

```scala
import scala.util.Sorting
val pairs = Array(("a", 5, 2), ("c", 3, 1), ("b", 1, 3))

// sort by 2nd element
Sorting.quickSort(pairs)(Ordering.by[(String, Int, Int), Int](_._2))

// sort by the 3rd element, then 1st
Sorting.quickSort(pairs)(Ordering[(Int, String)].on(x => (x._3, x._1)))
```

An Ordering[T] is implemented by specifying compare(a:T, b:T), which decides how
to order two instances a and b. Instances of Ordering[T] can be used by things
like scala.util.Sorting to sort collections like Array[T].

For example:

```scala
import scala.util.Sorting

case class Person(name:String, age:Int)
val people = Array(Person("bob", 30), Person("ann", 32), Person("carl", 19))

// sort by age
object AgeOrdering extends Ordering[Person] {
  def compare(a:Person, b:Person) = a.age compare b.age
}
Sorting.quickSort(people)(AgeOrdering)
```

This trait and scala.math.Ordered both provide this same functionality, but in
different ways. A type T can be given a single way to order itself by extending
Ordered. Using Ordering, this same type may be sorted in many other ways.
Ordered and Ordering both provide implicits allowing them to be used
interchangeably.

You can import scala.math.Ordering.Implicits to gain access to other implicit
orderings.

* Self Type
  * Ordering [T]
* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)
* Version
  * 0.9.5, 2008-04-15
* Since
  * 2.7
* See also
  * scala.math.Ordered, scala.util.Sorting


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Ops extends AnyRef`                                               ###

This inner class defines comparison operators available for `T` .

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


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

(defined at scala.math.Ordering)


### `def min(x: T, y: T): T`                                                 ###

Return `x` if `x` <= `y` , otherwise `y` .

(defined at scala.math.Ordering)


### `implicit def mkOrderingOps(lhs: T): Ops`                                ###

This implicit method augments `T` with the comparison operators defined in
 `scala.math.Ordering.Ops` .

(defined at scala.math.Ordering)


### `def on[U](f: (U) ⇒ T): Ordering[U]`                                     ###

Given f, a function from U into T, creates an Ordering[U] whose compare function
is equivalent to:

```scala
def compare(x:U, y:U) = Ordering[T].compare(f(x), f(y))
```

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
