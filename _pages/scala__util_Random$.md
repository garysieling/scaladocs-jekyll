
#                              scala.util.Random                              #

```scala
object Random extends Random
```

The object `Random` offers a default implementation of scala.util.Random and
random-related convenience methods.

* Source
  * [Random.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Random.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
                Deprecated Value Members From scala.util.Random
--------------------------------------------------------------------------------


### `final def isAlphaNum$1(c: Char): Boolean`                               ###

* Definition Classes
  * Random
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.6)_ Preserved for backwards binary compatibility. To
    remove in 2.12.x.

(defined at scala.util.Random)


--------------------------------------------------------------------------------
                      Value Members From scala.util.Random
--------------------------------------------------------------------------------


### `def alphanumeric: collection.immutable.Stream[Char]`                    ###

Returns a Stream of pseudorandomly chosen alphanumeric characters, equally
chosen from A-Z, a-z, and 0-9.

* Definition Classes
  * Random
* Since
  * 2.8

(defined at scala.util.Random)


### `implicit def javaRandomToRandom(r: java.util.Random): Random`           ###

(defined at scala.util.Random)


### `def nextBytes(bytes: Array[Byte]): Unit`                                ###

Generates random bytes and places them into a user-supplied byte array.

* Definition Classes
  * Random

(defined at scala.util.Random)


### `def nextInt(n: Int): Int`                                               ###

Returns a pseudorandom, uniformly distributed int value between 0 (inclusive)
and the specified value (exclusive), drawn from this random number generator's
sequence.

* Definition Classes
  * Random

(defined at scala.util.Random)


### `def nextString(length: Int): String`                                    ###

Returns a pseudorandomly generated String. This routine does not take any
measures to preserve the randomness of the distribution in the face of factors
like unicode's variable-length encoding, so please don't use this for anything
important. It's primarily intended for generating test data.

* length
  * the desired length of the String
* returns
  * the String

* Definition Classes
  * Random

(defined at scala.util.Random)


### `def setSeed(seed: Long): Unit`                                          ###

* Definition Classes
  * Random

(defined at scala.util.Random)


### `def shuffle[T, CC[X] <: TraversableOnce[X]](xs: CC[T])(implicit bf: CanBuildFrom[CC[T], T, CC[T]]): CC[T]` ###

Returns a new collection of the same type in a randomly chosen order.

* returns
  * the shuffled collection

* Definition Classes
  * Random
(defined at scala.util.Random)
