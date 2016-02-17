
#                             scala.math.Ordering                             #

```scala
object Ordering extends LowPriorityOrderingImplicits with Serializable
```

This is the companion object for the scala.math.Ordering trait.

It contains many implicit orderings as well as well as methods to construct new
orderings.

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait BigDecimalOrdering extends Ordering[BigDecimal]`                  ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait BigIntOrdering extends Ordering[BigInt]`                          ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait BooleanOrdering extends Ordering[Boolean]`                        ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait ByteOrdering extends Ordering[Byte]`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait CharOrdering extends Ordering[Char]`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait DoubleOrdering extends Ordering[Double]`                          ###

* Self Type
  * DoubleOrdering
* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait ExtraImplicits extends AnyRef`                                    ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait FloatOrdering extends Ordering[Float]`                            ###

* Self Type
  * FloatOrdering
* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait IntOrdering extends Ordering[Int]`                                ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait LongOrdering extends Ordering[Long]`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait OptionOrdering[T] extends Ordering[Option[T]]`                    ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait ShortOrdering extends Ordering[Short]`                            ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait StringOrdering extends Ordering[String]`                          ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `trait UnitOrdering extends Ordering[Unit]`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `implicit object BigDecimal extends BigDecimalOrdering`                  ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object BigInt extends BigIntOrdering`                          ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Boolean extends BooleanOrdering`                        ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Byte extends ByteOrdering`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Char extends CharOrdering`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Double extends DoubleOrdering`                          ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Float extends FloatOrdering`                            ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `object Implicits extends ExtraImplicits`                                ###

An object containing implicits which are not in the default scope.

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Int extends IntOrdering`                                ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Long extends LongOrdering`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Short extends ShortOrdering`                            ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object String extends StringOrdering`                          ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


### `implicit object Unit extends UnitOrdering`                              ###

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.math.LowPriorityOrderingImplicits
--------------------------------------------------------------------------------


### `implicit def comparatorToOrdering[A](implicit cmp: Comparator[A]): Ordering[A]` ###

* Definition Classes
  * LowPriorityOrderingImplicits

(defined at scala.math.LowPriorityOrderingImplicits)


### `implicit def ordered[A](implicit arg0: (A) ⇒ Comparable[A]): Ordering[A]` ###

This would conflict with all the nice implicit Orderings available, but thanks
to the magic of prioritized implicits via subclassing we can make
 `Ordered[A] => Ordering[A]` only turn up if nothing else works. Since
 `Ordered[A]` extends `Comparable[A]` anyway, we can throw in some Java interop
too.

* Definition Classes
  * LowPriorityOrderingImplicits

(defined at scala.math.LowPriorityOrderingImplicits)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordering
--------------------------------------------------------------------------------


### `implicit def Iterable[T](implicit ord: Ordering[T]): Ordering[Iterable[T]]` ###

(defined at scala.math.Ordering)


### `implicit def Option[T](implicit ord: Ordering[T]): Ordering[Option[T]]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple2[T1, T2](implicit ord1: Ordering[T1], ord2: Ordering[T2]): Ordering[(T1, T2)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple3[T1, T2, T3](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3]): Ordering[(T1, T2, T3)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple4[T1, T2, T3, T4](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4]): Ordering[(T1, T2, T3, T4)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple5[T1, T2, T3, T4, T5](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4], ord5: Ordering[T5]): Ordering[(T1, T2, T3, T4, T5)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple6[T1, T2, T3, T4, T5, T6](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4], ord5: Ordering[T5], ord6: Ordering[T6]): Ordering[(T1, T2, T3, T4, T5, T6)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple7[T1, T2, T3, T4, T5, T6, T7](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4], ord5: Ordering[T5], ord6: Ordering[T6], ord7: Ordering[T7]): Ordering[(T1, T2, T3, T4, T5, T6, T7)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple8[T1, T2, T3, T4, T5, T6, T7, T8](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4], ord5: Ordering[T5], ord6: Ordering[T6], ord7: Ordering[T7], ord8: Ordering[T8]): Ordering[(T1, T2, T3, T4, T5, T6, T7, T8)]` ###

(defined at scala.math.Ordering)


### `implicit def Tuple9[T1, T2, T3, T4, T5, T6, T7, T8, T9](implicit ord1: Ordering[T1], ord2: Ordering[T2], ord3: Ordering[T3], ord4: Ordering[T4], ord5: Ordering[T5], ord6: Ordering[T6], ord7: Ordering[T7], ord8: Ordering[T8], ord9: Ordering[T9]): Ordering[(T1, T2, T3, T4, T5, T6, T7, T8, T9)]` ###

(defined at scala.math.Ordering)


### `def apply[T](implicit ord: Ordering[T]): Ordering[T]`                   ###

(defined at scala.math.Ordering)


### `def by[T, S](f: (T) ⇒ S)(implicit ord: Ordering[S]): Ordering[T]`       ###

Given f, a function from T into S, creates an Ordering[T] whose compare function
is equivalent to:

```scala
def compare(x:T, y:T) = Ordering[S].compare(f(x), f(y))
```

This function is an analogue to Ordering.on where the Ordering[S] parameter is
passed implicitly.

(defined at scala.math.Ordering)


### `def fromLessThan[T](cmp: (T, T) ⇒ Boolean): Ordering[T]`                ###

Construct an Ordering[T] given a function `lt` .
(defined at scala.math.Ordering)
