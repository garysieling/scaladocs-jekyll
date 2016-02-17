
#                         scala.math.PartiallyOrdered                         #

```scala
trait PartiallyOrdered[+A] extends AnyRef
```

A class for partially ordered data.

* Source
  * [PartiallyOrdered.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/PartiallyOrdered.scala#L1)
* Version
  * 1.0, 23/04/2004


--------------------------------------------------------------------------------
            Abstract Value Members From scala.math.PartiallyOrdered
--------------------------------------------------------------------------------


### `abstract def tryCompareTo[B >: A](that: B)(implicit arg0: (B) ⇒ PartiallyOrdered[B]): Option[Int]` ###

Result of comparing `this` with operand `that` . Returns `None` if operands are
not comparable. If operands are comparable, returns `Some(x)` where

*  `x < 0` iff `this < that`
*  `x == 0` iff `this == that`
*  `x > 0` iff `this > that`

(defined at scala.math.PartiallyOrdered)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.math.PartiallyOrdered
--------------------------------------------------------------------------------


### `def <=[B >: A](that: B)(implicit arg0: (B) ⇒ PartiallyOrdered[B]): Boolean` ###

(defined at scala.math.PartiallyOrdered)


### `def <[B >: A](that: B)(implicit arg0: (B) ⇒ PartiallyOrdered[B]): Boolean` ###

(defined at scala.math.PartiallyOrdered)


### `def >=[B >: A](that: B)(implicit arg0: (B) ⇒ PartiallyOrdered[B]): Boolean` ###

(defined at scala.math.PartiallyOrdered)


### `def >[B >: A](that: B)(implicit arg0: (B) ⇒ PartiallyOrdered[B]): Boolean` ###
(defined at scala.math.PartiallyOrdered)
