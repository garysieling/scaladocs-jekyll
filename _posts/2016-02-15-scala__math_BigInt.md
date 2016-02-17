
#                              scala.math.BigInt                              #

```scala
final class BigInt extends ScalaNumber with ScalaNumericConversions with Serializable with Ordered[BigInt]
```

* Source
  * [BigInt.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigInt.scala#L1)
* Version
  * 1.0, 15/07/2003


--------------------------------------------------------------------------------
                  Instance Constructors From scala.math.BigInt
--------------------------------------------------------------------------------


### `new BigInt(bigInteger: BigInteger)`                                     ###

(defined at scala.math.BigInt)


--------------------------------------------------------------------------------
                      Value Members From scala.math.BigInt
--------------------------------------------------------------------------------


### `def %(that: BigInt): BigInt`                                            ###

Remainder of BigInts

(defined at scala.math.BigInt)


### `def &(that: BigInt): BigInt`                                            ###

Bitwise and of BigInts

(defined at scala.math.BigInt)


### `def &~(that: BigInt): BigInt`                                           ###

Bitwise and-not of BigInts. Returns a BigInt whose value is (this & ~that).

(defined at scala.math.BigInt)


### `def *(that: BigInt): BigInt`                                            ###

Multiplication of BigInts

(defined at scala.math.BigInt)


### `def +(that: BigInt): BigInt`                                            ###

Addition of BigInts

(defined at scala.math.BigInt)


### `def -(that: BigInt): BigInt`                                            ###

Subtraction of BigInts

(defined at scala.math.BigInt)


### `def /%(that: BigInt): (BigInt, BigInt)`                                 ###

Returns a pair of two BigInts containing (this / that) and (this % that).

(defined at scala.math.BigInt)


### `def /(that: BigInt): BigInt`                                            ###

Division of BigInts

(defined at scala.math.BigInt)


### `def <<(n: Int): BigInt`                                                 ###

Leftshift of BigInt

(defined at scala.math.BigInt)


### `def >>(n: Int): BigInt`                                                 ###

(Signed) rightshift of BigInt

(defined at scala.math.BigInt)


### `def ^(that: BigInt): BigInt`                                            ###

Bitwise exclusive-or of BigInts

(defined at scala.math.BigInt)


### `def abs: BigInt`                                                        ###

Returns the absolute value of this BigInt

(defined at scala.math.BigInt)


### `val bigInteger: BigInteger`                                             ###

(defined at scala.math.BigInt)


### `def clearBit(n: Int): BigInt`                                           ###

Returns a BigInt whose value is equivalent to this BigInt with the designated
bit cleared.

(defined at scala.math.BigInt)


### `def compare(that: BigInt): Int`                                         ###

Compares this BigInt with the specified BigInt

* Definition Classes
  * BigInt → Ordered

(defined at scala.math.BigInt)


### `def equals(that: Any): Boolean`                                         ###

Compares this BigInt with the specified value for equality.

* that
  * the object to compare against this object for equality.
* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * BigInt → AnyRef → Any

(defined at scala.math.BigInt)


### `def equals(that: BigInt): Boolean`                                      ###

Compares this BigInt with the specified BigInt for equality.

(defined at scala.math.BigInt)


### `def flipBit(n: Int): BigInt`                                            ###

Returns a BigInt whose value is equivalent to this BigInt with the designated
bit flipped.

(defined at scala.math.BigInt)


### `def gcd(that: BigInt): BigInt`                                          ###

Returns the greatest common divisor of abs(this) and abs(that)

(defined at scala.math.BigInt)


### `def isProbablePrime(certainty: Int): Boolean`                           ###

Returns true if this BigInt is probably prime, false if it's definitely
composite.

* certainty
  * a measure of the uncertainty that the caller is willing to tolerate: if the
    call returns true the probability that this BigInt is prime exceeds (1 - 1/2
    ^ certainty). The execution time of this method is proportional to the value
    of this parameter.

(defined at scala.math.BigInt)


### `def max(that: BigInt): BigInt`                                          ###

Returns the maximum of this and that

(defined at scala.math.BigInt)


### `def min(that: BigInt): BigInt`                                          ###

Returns the minimum of this and that

(defined at scala.math.BigInt)


### `def mod(that: BigInt): BigInt`                                          ###

Returns a BigInt whose value is (this mod that). This method differs from `%` in
that it always returns a non-negative BigInt.

(defined at scala.math.BigInt)


### `def modInverse(m: BigInt): BigInt`                                      ###

Returns a BigInt whose value is (the inverse of `this` modulo `m` ).

(defined at scala.math.BigInt)


### `def modPow(exp: BigInt, m: BigInt): BigInt`                             ###

Returns a BigInt whose value is ( `this` raised to the power of `exp` modulo
 `m` ).

(defined at scala.math.BigInt)


### `def pow(exp: Int): BigInt`                                              ###

Returns a BigInt whose value is ( `this` raised to the power of `exp` ).

(defined at scala.math.BigInt)


### `def setBit(n: Int): BigInt`                                             ###

Returns a BigInt whose value is equivalent to this BigInt with the designated
bit set.

(defined at scala.math.BigInt)


### `def testBit(n: Int): Boolean`                                           ###

Returns true if and only if the designated bit is set.

(defined at scala.math.BigInt)


### `def to(end: BigInt, step: BigInt = BigInt(1)): Inclusive[scala.BigInt]` ###

Like until, but inclusive of the end value.

(defined at scala.math.BigInt)


### `def toString(radix: Int): String`                                       ###

Returns the String representation in the specified radix of this BigInt.

(defined at scala.math.BigInt)


### `def unary_-: BigInt`                                                    ###

Returns a BigInt whose value is the negation of this BigInt

(defined at scala.math.BigInt)


### `def unary_~: BigInt`                                                    ###

Returns the bitwise complement of this BigInt

(defined at scala.math.BigInt)


### `def underlying(): BigInteger`                                           ###

* Definition Classes
  * BigInt → ScalaNumericConversions → ScalaNumericAnyConversions → ScalaNumber

(defined at scala.math.BigInt)


### `def until(end: BigInt, step: BigInt = BigInt(1)): Exclusive[scala.BigInt]` ###

Create a `NumericRange[BigInt]` in range `[start;end)` with the specified step,
where start is the target BigInt.

* end
  * the end value of the range (exclusive)
* step
  * the distance between elements (defaults to 1)
* returns
  * the range

(defined at scala.math.BigInt)


### `def |(that: BigInt): BigInt`                                            ###

Bitwise or of BigInts

(defined at scala.math.BigInt)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: BigInt): Boolean`                                           ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: BigInt): Boolean`                                          ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: BigInt): Boolean`                                           ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: BigInt): Boolean`                                          ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: BigInt): Int`                                       ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable

(defined at scala.math.Ordered)


--------------------------------------------------------------------------------
            Value Members From scala.math.ScalaNumericAnyConversions
--------------------------------------------------------------------------------


### `def unifiedPrimitiveEquals(x: Any): Boolean`                            ###

Should only be called after all known non-primitive types have been excluded.
This method won't dispatch anywhere else after checking against the primitives
to avoid infinite recursion between equals and this on unknown "Number"
variants.

Additionally, this should only be called if the numeric type is happy to be
converted to Long, Float, and Double. If for instance a BigInt much larger than
the Long range is sent here, it will claim equality with whatever Long is left
in its lower 64 bits. Or a BigDecimal with more precision than Double can hold:
same thing. There's no way given the interface available here to prevent this
error.

* Attributes
  * protected
* Definition Classes
  * ScalaNumericAnyConversions
(defined at scala.math.ScalaNumericAnyConversions)
