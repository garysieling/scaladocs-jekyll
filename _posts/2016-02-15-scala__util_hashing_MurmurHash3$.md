
#                        scala.util.hashing.MurmurHash3                        #

```scala
object MurmurHash3 extends MurmurHash3
```

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
                                  Type Members
--------------------------------------------------------------------------------


### `class ArrayHashing[T] extends Hashing[Array[T]]`                        ###

* Source
  * [MurmurHash3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/MurmurHash3.scala#L1)


--------------------------------------------------------------------------------
               Value Members From scala.util.hashing.MurmurHash3
--------------------------------------------------------------------------------


### `def arrayHash[T](a: Array[T]): Int`                                     ###

(defined at scala.util.hashing.MurmurHash3)


### `final def arrayHash[T](a: Array[T], seed: Int): Int`                    ###

Compute the hash of an array.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def arrayHashing[T]: ArrayHashing[T]`                                   ###

(defined at scala.util.hashing.MurmurHash3)


### `def bytesHash(data: Array[Byte]): Int`                                  ###

(defined at scala.util.hashing.MurmurHash3)


### `final def bytesHash(data: Array[Byte], seed: Int): Int`                 ###

Compute the hash of a byte array. Faster than arrayHash, because it hashes 4
bytes at once.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def bytesHashing: Hashing[Array[Byte]]`                                 ###

(defined at scala.util.hashing.MurmurHash3)


### `final def finalizeHash(hash: Int, length: Int): Int`                    ###

Finalize a hash to incorporate the length and make sure all bits avalanche.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `final def listHash(xs: collection.immutable.List[_], seed: Int): Int`   ###

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def mapHash(xs: Map[_, _]): Int`                                        ###

(defined at scala.util.hashing.MurmurHash3)


### `final def mix(hash: Int, data: Int): Int`                               ###

Mix in a block of data into an intermediate hash value.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `final def mixLast(hash: Int, data: Int): Int`                           ###

May optionally be used as the last mixing step. Is a little bit faster than mix,
as it does no further mixing of the resulting hash. For the last element this is
not necessary as the hash is thoroughly mixed during finalization anyway.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def orderedHash(xs: TraversableOnce[Any]): Int`                         ###

(defined at scala.util.hashing.MurmurHash3)


### `final def orderedHash(xs: TraversableOnce[Any], seed: Int): Int`        ###

Compute a hash that depends on the order of its arguments.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def orderedHashing: Hashing[TraversableOnce[Any]]`                      ###

(defined at scala.util.hashing.MurmurHash3)


### `def productHash(x: Product): Int`                                       ###

(defined at scala.util.hashing.MurmurHash3)


### `final def productHash(x: Product, seed: Int): Int`                      ###

Compute the hash of a product

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def productHashing: Hashing[Product]`                                   ###

(defined at scala.util.hashing.MurmurHash3)


### `def seqHash(xs: collection.Seq[_]): Int`                                ###

To offer some potential for optimization.

(defined at scala.util.hashing.MurmurHash3)


### `def setHash(xs: Set[_]): Int`                                           ###

(defined at scala.util.hashing.MurmurHash3)


### `def stringHash(x: String): Int`                                         ###

(defined at scala.util.hashing.MurmurHash3)


### `final def stringHash(str: String, seed: Int): Int`                      ###

Compute the hash of a string

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def stringHashing: Hashing[String]`                                     ###

(defined at scala.util.hashing.MurmurHash3)


### `def unorderedHash(xs: TraversableOnce[Any]): Int`                       ###

(defined at scala.util.hashing.MurmurHash3)


### `final def unorderedHash(xs: TraversableOnce[Any], seed: Int): Int`      ###

Compute a hash that is symmetric in its arguments - that is a hash where the
order of appearance of elements does not matter. This is useful for hashing
sets, for example.

* Definition Classes
  * MurmurHash3

(defined at scala.util.hashing.MurmurHash3)


### `def unorderedHashing: Hashing[TraversableOnce[Any]]`                    ###
(defined at scala.util.hashing.MurmurHash3)
