
#                   scala.collection.immutable.NumericRange                   #

```scala
object NumericRange extends Serializable
```

A companion object for numeric ranges.

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Exclusive[T] extends NumericRange[T]`                             ###

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)


### `class Inclusive[T] extends NumericRange[T]`                             ###

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.immutable.NumericRange
--------------------------------------------------------------------------------


### `def apply[T](start: T, end: T, step: T)(implicit num: Integral[T]): Exclusive[T]` ###

(defined at scala.collection.immutable.NumericRange)


### `def count[T](start: T, end: T, step: T, isInclusive: Boolean)(implicit num: Integral[T]): Int` ###

Calculates the number of elements in a range given start, end, step, and whether
or not it is inclusive. Throws an exception if step == 0 or the number of
elements exceeds the maximum Int.

(defined at scala.collection.immutable.NumericRange)


### `def inclusive[T](start: T, end: T, step: T)(implicit num: Integral[T]): Inclusive[T]` ###
(defined at scala.collection.immutable.NumericRange)
