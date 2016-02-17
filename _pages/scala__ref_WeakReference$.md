
#                           scala.ref.WeakReference                           #

```scala
object WeakReference
```

An extractor for weak reference values

* Source
  * [WeakReference.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/ref/WeakReference.scala#L1)


--------------------------------------------------------------------------------
                   Value Members From scala.ref.WeakReference
--------------------------------------------------------------------------------


### `def apply[T <: AnyRef](value: T): WeakReference[T]`                     ###

Creates a weak reference pointing to `value`

(defined at scala.ref.WeakReference)


### `def unapply[T <: AnyRef](wr: WeakReference[T]): Option[T]`              ###

Optionally returns the referenced value, or `None` if that value no longer
exists
(defined at scala.ref.WeakReference)
