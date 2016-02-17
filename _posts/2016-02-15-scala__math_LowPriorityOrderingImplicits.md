
#                   scala.math.LowPriorityOrderingImplicits                   #

```scala
trait LowPriorityOrderingImplicits extends AnyRef
```

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.math.LowPriorityOrderingImplicits
--------------------------------------------------------------------------------


### `implicit def comparatorToOrdering[A](implicit cmp: Comparator[A]): Ordering[A]` ###

(defined at scala.math.LowPriorityOrderingImplicits)


### `implicit def ordered[A](implicit arg0: (A) ⇒ Comparable[A]): Ordering[A]` ###

This would conflict with all the nice implicit Orderings available, but thanks
to the magic of prioritized implicits via subclassing we can make
 `Ordered[A] => Ordering[A]` only turn up if nothing else works. Since
 `Ordered[A]` extends `Comparable[A]` anyway, we can throw in some Java interop
too.
(defined at scala.math.LowPriorityOrderingImplicits)
