
#                                  scala.Long                                  #

```scala
abstract final class Long extends AnyVal
```

 `Long` , a 64-bit signed integer (equivalent to Java's `long` primitive type)
is a subtype of scala.AnyVal. Instances of `Long` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Long => scala.runtime.RichLong which
provides useful non-primitive operations.

* Source
  * [Long.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Long.scala#L1)


--------------------------------------------------------------------------------
                     Abstract Value Members From scala.Long
--------------------------------------------------------------------------------


### `abstract def !=(x: Byte): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Char): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Double): Boolean`                                    ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Float): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Int): Boolean`                                       ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Long): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def !=(x: Short): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def %(x: Byte): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Char): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Double): Double`                                      ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Float): Float`                                        ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Int): Long`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Long): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def %(x: Short): Long`                                         ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Long)


### `abstract def &(x: Byte): Long`                                          ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Long)


### `abstract def &(x: Char): Long`                                          ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Long)


### `abstract def &(x: Int): Long`                                           ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Long)


### `abstract def &(x: Long): Long`                                          ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Long)


### `abstract def &(x: Short): Long`                                         ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Long)


### `abstract def *(x: Byte): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Char): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Double): Double`                                      ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Float): Float`                                        ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Int): Long`                                           ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Long): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def *(x: Short): Long`                                         ###

Returns the product of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Byte): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Char): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Double): Double`                                      ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Float): Float`                                        ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Int): Long`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Long): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: Short): Long`                                         ###

Returns the sum of this value and `x` .

(defined at scala.Long)


### `abstract def +(x: String): String`                                      ###

(defined at scala.Long)


### `abstract def -(x: Byte): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Char): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Double): Double`                                      ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Float): Float`                                        ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Int): Long`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Long): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def -(x: Short): Long`                                         ###

Returns the difference of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Byte): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Char): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Double): Double`                                      ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Float): Float`                                        ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Int): Long`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Long): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def /(x: Short): Long`                                         ###

Returns the quotient of this value and `x` .

(defined at scala.Long)


### `abstract def <(x: Byte): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Char): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Double): Boolean`                                     ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Float): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Int): Boolean`                                        ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Long): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <(x: Short): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Long)


### `abstract def <<(x: Int): Long`                                          ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Long)


### `abstract def <<(x: Long): Long`                                         ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Long)


### `abstract def <=(x: Byte): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Char): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Double): Boolean`                                    ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Float): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Int): Boolean`                                       ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Long): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def <=(x: Short): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Byte): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Char): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Double): Boolean`                                    ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Float): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Int): Boolean`                                       ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Long): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def ==(x: Short): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Byte): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Char): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Double): Boolean`                                     ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Float): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Int): Boolean`                                        ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Long): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >(x: Short): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Byte): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Char): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Double): Boolean`                                    ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Float): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Int): Boolean`                                       ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Long): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >=(x: Short): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Long)


### `abstract def >>(x: Int): Long`                                          ###

Returns this value bit-shifted right by the specified number of bits, filling in
the left bits with the same value as the left-most bit of this. The effect of
this is to retain the sign of the value.

Example:

```scala
-21 >> 3 == -3
// in binary: 11111111 11111111 11111111 11101011 >> 3 ==
//            11111111 11111111 11111111 11111101
```

(defined at scala.Long)


### `abstract def >>(x: Long): Long`                                         ###

Returns this value bit-shifted right by the specified number of bits, filling in
the left bits with the same value as the left-most bit of this. The effect of
this is to retain the sign of the value.

Example:

```scala
-21 >> 3 == -3
// in binary: 11111111 11111111 11111111 11101011 >> 3 ==
//            11111111 11111111 11111111 11111101
```

(defined at scala.Long)


### `abstract def >>>(x: Int): Long`                                         ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Long)


### `abstract def >>>(x: Long): Long`                                        ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Long)


### `abstract def ^(x: Byte): Long`                                          ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Long)


### `abstract def ^(x: Char): Long`                                          ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Long)


### `abstract def ^(x: Int): Long`                                           ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Long)


### `abstract def ^(x: Long): Long`                                          ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Long)


### `abstract def ^(x: Short): Long`                                         ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Long)


### `abstract def |(x: Byte): Long`                                          ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Long)


### `abstract def |(x: Char): Long`                                          ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Long)


### `abstract def |(x: Int): Long`                                           ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Long)


### `abstract def |(x: Long): Long`                                          ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Long)


### `abstract def |(x: Short): Long`                                         ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Long)


--------------------------------------------------------------------------------
                    Deprecated Value Members From scala.Long
--------------------------------------------------------------------------------


### `abstract def toByte: Byte`                                              ###

(defined at scala.Long)


--------------------------------------------------------------------------------
  Concrete Value Members From Implicit scala.LowPriorityImplicits.longWrapper
--------------------------------------------------------------------------------


### `def compare(y: Long): Int`                                              ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * OrderedProxy → Ordered

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def compareTo(that: Long): Int`                                         ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered → Comparable

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def max(that: Long): Long`                                              ###

Returns `this` if `this > that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichLong → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def min(that: Long): Long`                                              ###

Returns `this` if `this < that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichLong → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def to(end: Long): Inclusive[Long]`                                     ###

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def to(end: Long, step: Long): Inclusive[Long]`                         ###

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def until(end: Long): Exclusive[Long]`                                  ###

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


### `def until(end: Long, step: Long): Exclusive[Long]`                      ###

* Implicit information
  * This member is added by an implicit conversion from Long to RichLong
    performed by method longWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.longWrapper)


--------------------------------------------------------------------------------
          Concrete Value Members From Implicit scala.Predef.long2Long
--------------------------------------------------------------------------------


### `def compareTo(arg0: java.lang.Long): Int`                               ###

* Implicit information
  * This member is added by an implicit conversion from Long to java.lang.Long
    performed by method long2Long in scala.Predef.
* Definition Classes
  * Long → Comparable
(added by implicit convertion: scala.Predef.long2Long)
