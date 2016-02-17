
#                              scala.util.hashing                              #

```scala
package hashing
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final class ByteswapHashing[T] extends Hashing[T]`                      ###

A fast multiplicative hash by Phil Bagwell.

* Source
  * [ByteswapHashing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/ByteswapHashing.scala#L1)


### `trait Hashing[T] extends Serializable`                                  ###

 `Hashing` is a trait whose instances each represent a strategy for hashing
instances of a type.

 `Hashing` 's companion object defines a default hashing strategy for all
objects - it calls their `##` method.

Note: when using a custom `Hashing` , make sure to use it with the `Equiv` such
that if any two objects are equal, then their hash codes must be equal.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Hashing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/Hashing.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object ByteswapHashing extends Serializable`                            ###

* Source
  * [ByteswapHashing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/ByteswapHashing.scala#L1)


### `object Hashing extends Serializable`                                    ###

* Source
  * [Hashing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/Hashing.scala#L1)


### `object MurmurHash3 extends MurmurHash3`                                 ###

An implementation of Austin Appleby's MurmurHash 3 algorithm
(MurmurHash3_x86_32). This object contains methods that hash values of various
types as well as means to construct `Hashing` objects.

This algorithm is designed to generate well-distributed non-cryptographic
hashes. It is designed to hash data in 32 bit chunks (ints).

The mix method needs to be called at each step to update the intermediate hash
value. For the last chunk to incorporate into the hash mixLast may be used
instead, which is slightly faster. Finally finalizeHash needs to be called to
compute the final hash value.

This is based on the earlier MurmurHash3 code by Rex Kerr, but the MurmurHash3
algorithm was since changed by its creator Austin Appleby to remedy some
weaknesses and improve performance. This represents the latest and supposedly
final version of the algorithm (revision 136).

* Source
  * [MurmurHash3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/MurmurHash3.scala#L1)
* See also
  * [http://code.google.com/p/smhasher](http://code.google.com/p/smhasher)


--------------------------------------------------------------------------------
                     Value Members From scala.util.hashing
--------------------------------------------------------------------------------


### `def byteswap32(v: Int): Int`                                            ###

Fast multiplicative hash with a nice distribution.

(defined at scala.util.hashing)


### `def byteswap64(v: Long): Long`                                          ###

Fast multiplicative hash with a nice distribution for 64-bit values.
(defined at scala.util.hashing)
