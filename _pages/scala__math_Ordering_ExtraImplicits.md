
#                      scala.math.Ordering.ExtraImplicits                      #

```scala
trait ExtraImplicits extends AnyRef
```

* Source
  * [Ordering.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Ordering.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.math.Ordering.ExtraImplicits
--------------------------------------------------------------------------------


### `implicit def infixOrderingOps[T](x: T)(implicit ord: Ordering[T]): Ops` ###

This implicit creates a conversion from any value for which an implicit
 `Ordering` exists to the class which creates infix operations. With it
imported, you can write methods as follows:

```scala
def lessThan[T: Ordering](x: T, y: T) = x < y
```

(defined at scala.math.Ordering.ExtraImplicits)


### `implicit def seqDerivedOrdering[CC[X] <: collection.Seq[X], T](implicit ord: Ordering[T]): Ordering[CC[T]]` ###

Not in the standard scope due to the potential for divergence: For instance
 `implicitly[Ordering[Any]]` diverges in its presence.
(defined at scala.math.Ordering.ExtraImplicits)
