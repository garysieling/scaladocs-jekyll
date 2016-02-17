
#                           scala.ref.SoftReference                           #

```scala
object SoftReference
```

A companion object that implements an extractor for `SoftReference` values

* Source
  * [SoftReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/SoftReference.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From scala.ref.SoftReference
--------------------------------------------------------------------------------


### `def apply[T <: AnyRef](value: T): SoftReference[T]`                     ###

Creates a `SoftReference` pointing to `value`

(defined at scala.ref.SoftReference)


### `def unapply[T <: AnyRef](sr: SoftReference[T]): Option[T]`              ###

Optionally returns the referenced value, or `None` if that value no longer
exists
(defined at scala.ref.SoftReference)
