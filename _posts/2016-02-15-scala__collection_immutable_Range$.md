
#                       scala.collection.immutable.Range                       #

```scala
object Range extends Serializable
```

A companion object for the `Range` class.

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Inclusive extends Range`                                          ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `class Partial[T, U] extends AnyRef`                                     ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object BigDecimal`                                                      ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `object BigInt`                                                          ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `object Double`                                                          ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `object Int`                                                             ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


### `object Long`                                                            ###

* Source
  * [Range.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Range.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.immutable.Range
--------------------------------------------------------------------------------


### `def apply(start: Int, end: Int): Range`                                 ###

Make a range from `start` until `end` (exclusive) with step value 1.

(defined at scala.collection.immutable.Range)


### `def apply(start: Int, end: Int, step: Int): Range`                      ###

Make a range from `start` until `end` (exclusive) with given step value.

* Note
  * step != 0

(defined at scala.collection.immutable.Range)


### `def count(start: Int, end: Int, step: Int): Int`                        ###

(defined at scala.collection.immutable.Range)


### `def count(start: Int, end: Int, step: Int, isInclusive: Boolean): Int`  ###

Counts the number of range elements.

(defined at scala.collection.immutable.Range)


### `def inclusive(start: Int, end: Int): Inclusive`                         ###

Make an inclusive range from `start` to `end` with step value 1.

(defined at scala.collection.immutable.Range)


### `def inclusive(start: Int, end: Int, step: Int): Inclusive`              ###

Make an inclusive range from `start` to `end` with given step value.

* Note
  * step != 0
(defined at scala.collection.immutable.Range)
