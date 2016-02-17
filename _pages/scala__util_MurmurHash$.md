
#                            scala.util.MurmurHash                            #

```scala
object MurmurHash
```

An object designed to generate well-distributed non-cryptographic hashes. It is
designed to hash a collection of integers; along with the integers to hash, it
generates two magic streams of integers to increase the distribution of
repetitive input sequences. Thus, three methods need to be called at each step
(to start and to incorporate a new integer) to update the values. Only one
method needs to be called to finalize the hash.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use the object MurmurHash3 instead.
* Source
  * [MurmurHash.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/MurmurHash.scala#L1)


--------------------------------------------------------------------------------
                    Value Members From scala.util.MurmurHash
--------------------------------------------------------------------------------


### `def arrayHash[T](a: Array[T]): Int`                                     ###

Compute a high-quality hash of an array

(defined at scala.util.MurmurHash)


### `def extendHash(hash: Int, value: Int, magicA: Int, magicB: Int): Int`   ###

Incorporates a new value into an existing hash.

* hash
  * the prior hash value
* value
  * the new value to incorporate
* magicA
  * a magic integer from the stream
* magicB
  * a magic integer from a different stream
* returns
  * the updated hash value

(defined at scala.util.MurmurHash)


### `def finalizeHash(hash: Int): Int`                                       ###

Once all hashes have been incorporated, this performs a final mixing

(defined at scala.util.MurmurHash)


### `def nextMagicA(magicA: Int): Int`                                       ###

Given a magic integer from the first stream, compute the next

(defined at scala.util.MurmurHash)


### `def nextMagicB(magicB: Int): Int`                                       ###

Given a magic integer from the second stream, compute the next

(defined at scala.util.MurmurHash)


### `def startHash(seed: Int): Int`                                          ###

Begin a new hash with a seed value.

(defined at scala.util.MurmurHash)


### `def stringHash(s: String): Int`                                         ###

Compute a high-quality hash of a string

(defined at scala.util.MurmurHash)


### `def symmetricHash[T](xs: collection.TraversableOnce[T], seed: Int): Int` ###

Compute a hash that is symmetric in its arguments--that is, where the order of
appearance of elements does not matter. This is useful for hashing sets, for
example.
(defined at scala.util.MurmurHash)
