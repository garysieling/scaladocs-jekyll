
#                              scala.math.BigInt                              #

```scala
object BigInt extends Serializable
```

* Source
  * [BigInt.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigInt.scala#L1)
* Version
  * 1.0, 15/07/2003
* Since
  * 2.1


--------------------------------------------------------------------------------
                      Value Members From scala.math.BigInt
--------------------------------------------------------------------------------


### `def apply(x: Array[Byte]): BigInt`                                      ###

Translates a byte array containing the two's-complement binary representation of
a BigInt into a BigInt.

(defined at scala.math.BigInt)


### `def apply(x: BigInteger): BigInt`                                       ###

Translates a `java.math.BigInteger` into a BigInt.

(defined at scala.math.BigInt)


### `def apply(i: Int): BigInt`                                              ###

Constructs a `BigInt` whose value is equal to that of the specified integer
value.

* i
  * the specified integer value
* returns
  * the constructed `BigInt`

(defined at scala.math.BigInt)


### `def apply(signum: Int, magnitude: Array[Byte]): BigInt`                 ###

Translates the sign-magnitude representation of a BigInt into a BigInt.

(defined at scala.math.BigInt)


### `def apply(bitlength: Int, certainty: Int, rnd: Random): BigInt`         ###

Constructs a randomly generated positive BigInt that is probably prime, with the
specified bitLength.

(defined at scala.math.BigInt)


### `def apply(numbits: Int, rnd: Random): BigInt`                           ###

Constructs a randomly generated BigInt, uniformly distributed over the range
 `0` to `(2 ^ numBits - 1), inclusive.`

(defined at scala.math.BigInt)


### `def apply(l: Long): BigInt`                                             ###

Constructs a `BigInt` whose value is equal to that of the specified long value.

* l
  * the specified long value
* returns
  * the constructed `BigInt`

(defined at scala.math.BigInt)


### `def apply(x: String): BigInt`                                           ###

Translates the decimal String representation of a BigInt into a BigInt.

(defined at scala.math.BigInt)


### `def apply(x: String, radix: Int): BigInt`                               ###

Translates the string representation of a `BigInt` in the specified `radix` into
a BigInt.

(defined at scala.math.BigInt)


### `implicit def int2bigInt(i: Int): BigInt`                                ###

Implicit conversion from `Int` to `BigInt` .

(defined at scala.math.BigInt)


### `implicit def javaBigInteger2bigInt(x: BigInteger): BigInt`              ###

Implicit conversion from `java.math.BigInteger` to `scala.BigInt` .

(defined at scala.math.BigInt)


### `implicit def long2bigInt(l: Long): BigInt`                              ###

Implicit conversion from `Long` to `BigInt` .

(defined at scala.math.BigInt)


### `def probablePrime(bitLength: Int, rnd: Random): BigInt`                 ###

Returns a positive BigInt that is probably prime, with the specified bitLength.
(defined at scala.math.BigInt)
