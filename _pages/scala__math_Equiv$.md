
#                               scala.math.Equiv                               #

```scala
object Equiv extends LowPriorityEquiv with Serializable
```

* Source
  * [Equiv.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/Equiv.scala#L1)


--------------------------------------------------------------------------------
                      Value Members From scala.math.Equiv
--------------------------------------------------------------------------------


### `def apply[T](implicit arg0: Equiv[T]): Equiv[T]`                        ###

(defined at scala.math.Equiv)


### `def by[T, S](f: (T) ⇒ S)(implicit arg0: Equiv[S]): Equiv[T]`            ###

(defined at scala.math.Equiv)


### `def fromComparator[T](cmp: Comparator[T]): Equiv[T]`                    ###

(defined at scala.math.Equiv)


### `def fromFunction[T](cmp: (T, T) ⇒ Boolean): Equiv[T]`                   ###

(defined at scala.math.Equiv)


### `def reference[T <: AnyRef]: Equiv[T]`                                   ###

(defined at scala.math.Equiv)


### `def universal[T]: Equiv[T]`                                             ###

(defined at scala.math.Equiv)


--------------------------------------------------------------------------------
                 Value Members From scala.math.LowPriorityEquiv
--------------------------------------------------------------------------------


### `implicit def universalEquiv[T]: Equiv[T]`                               ###

* Definition Classes
  * LowPriorityEquiv
(defined at scala.math.LowPriorityEquiv)
