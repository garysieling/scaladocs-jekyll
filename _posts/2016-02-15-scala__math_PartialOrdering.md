
#                          scala.math.PartialOrdering                          #

```scala
trait PartialOrdering[T] extends Equiv[T]
```

A trait for representing partial orderings. It is important to distinguish
between a type that has a partial order and a representation of partial ordering
on some type. This trait is for representing the latter.

A [partial ordering](http://en.wikipedia.org/wiki/Partial_order) is a binary
relation on a type `T` , exposed as the `lteq` method of this trait. This
relation must be:

* reflexive: `lteq(x, x) == true` , for any `x` of type `T` .
* anti-symmetric: if `lteq(x, y) == true` and `lteq(y, x) == true` then
    `equiv(x, y) == true` , for any `x` and `y` of type `T` .
* transitive: if `lteq(x, y) == true` and `lteq(y, z) == true` then
    `lteq(x, z) == true` , for any `x` , `y` , and `z` of type `T` .

Additionally, a partial ordering induces an
[equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) on a
type `T` : `x` and `y` of type `T` are equivalent if and only if
 `lteq(x, y) && lteq(y, x) == true` . This equivalence relation is exposed as
the `equiv` method, inherited from the Equiv trait.

* Self Type
  * PartialOrdering [T]
* Source
  * [PartialOrdering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/PartialOrdering.scala#L1)
* Version
  * 1.0, 2008-04-0-3
* Since
  * 2.7


--------------------------------------------------------------------------------
             Abstract Value Members From scala.math.PartialOrdering
--------------------------------------------------------------------------------


### `abstract def lteq(x: T, y: T): Boolean`                                 ###

Returns `true` iff `x` comes before `y` in the ordering.

(defined at scala.math.PartialOrdering)


### `abstract def tryCompare(x: T, y: T): Option[Int]`                       ###

Result of comparing `x` with operand `y` . Returns `None` if operands are not
comparable. If operands are comparable, returns `Some(r)` where

*  `r < 0` iff `x < y`
*  `r == 0` iff `x == y`
*  `r > 0` iff `x > y`

(defined at scala.math.PartialOrdering)


--------------------------------------------------------------------------------
             Concrete Value Members From scala.math.PartialOrdering
--------------------------------------------------------------------------------


### `def equiv(x: T, y: T): Boolean`                                         ###

Returns `true` iff `x` is equivalent to `y` in the ordering.

* Definition Classes
  * PartialOrdering → Equiv

(defined at scala.math.PartialOrdering)


### `def gt(x: T, y: T): Boolean`                                            ###

Returns `true` iff `y` comes before `x` in the ordering and is not the same as
 `x` .

(defined at scala.math.PartialOrdering)


### `def gteq(x: T, y: T): Boolean`                                          ###

Returns `true` iff `y` comes before `x` in the ordering.

(defined at scala.math.PartialOrdering)


### `def lt(x: T, y: T): Boolean`                                            ###

Returns `true` iff `x` comes before `y` in the ordering and is not the same as
 `y` .

(defined at scala.math.PartialOrdering)


### `def reverse: PartialOrdering[T]`                                        ###
(defined at scala.math.PartialOrdering)
