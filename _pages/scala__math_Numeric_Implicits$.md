
#                         scala.math.Numeric.Implicits                         #

```scala
object Implicits extends ExtraImplicits
```

* Source
  * [Numeric.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Numeric.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.math.Numeric.ExtraImplicits
--------------------------------------------------------------------------------


### `implicit def infixNumericOps[T](x: T)(implicit num: Numeric[T]): Ops`   ###

These implicits create conversions from a value for which an implicit Numeric
exists to the inner class which creates infix operations. Once imported, you can
write methods as follows:

```scala
def plus[T: Numeric](x: T, y: T) = x + y
```

* Definition Classes
  * ExtraImplicits
(defined at scala.math.Numeric.ExtraImplicits)
