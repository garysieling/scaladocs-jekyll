
#                        scala.math.Integral.Implicits                        #

```scala
object Implicits extends ExtraImplicits
```

* Source
  * [Integral.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Integral.scala#L1)


--------------------------------------------------------------------------------
             Value Members From scala.math.Integral.ExtraImplicits
--------------------------------------------------------------------------------


### `implicit def infixIntegralOps[T](x: T)(implicit num: Integral[T]): IntegralOps` ###

The regrettable design of Numeric/Integral/Fractional has them all bumping into
one another when searching for this implicit, so they are exiled into their own
companions.

* Definition Classes
  * ExtraImplicits
(defined at scala.math.Integral.ExtraImplicits)
