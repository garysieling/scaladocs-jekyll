
#                                 scala.Short                                 #

```scala
abstract final class Short extends AnyVal
```

 `Short` , a 16-bit signed integer (equivalent to Java's `short` primitive type)
is a subtype of scala.AnyVal. Instances of `Short` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Short => scala.runtime.RichShort
which provides useful non-primitive operations.

* Source
  * [Short.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Short.scala#L1)


--------------------------------------------------------------------------------
                    Abstract Value Members From scala.Short
--------------------------------------------------------------------------------


### `abstract def !=(x: Byte): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Char): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Double): Boolean`                                    ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Float): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Int): Boolean`                                       ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Long): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def !=(x: Short): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def %(x: Byte): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Char): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Double): Double`                                      ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Float): Float`                                        ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Int): Int`                                            ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Long): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def %(x: Short): Int`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Short)


### `abstract def &(x: Byte): Int`                                           ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Short)


### `abstract def &(x: Char): Int`                                           ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Short)


### `abstract def &(x: Int): Int`                                            ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Short)


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

(defined at scala.Short)


### `abstract def &(x: Short): Int`                                          ###

Returns the bitwise AND of this value and `x` .

Example:

```scala
(0xf0 & 0xaa) == 0xa0
// in binary:   11110000
//            & 10101010
//              --------
//              10100000
```

(defined at scala.Short)


### `abstract def *(x: Byte): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Char): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Double): Double`                                      ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Float): Float`                                        ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Int): Int`                                            ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Long): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def *(x: Short): Int`                                          ###

Returns the product of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Byte): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Char): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Double): Double`                                      ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Float): Float`                                        ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Int): Int`                                            ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Long): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: Short): Int`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Short)


### `abstract def +(x: String): String`                                      ###

(defined at scala.Short)


### `abstract def -(x: Byte): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Char): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Double): Double`                                      ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Float): Float`                                        ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Int): Int`                                            ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Long): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def -(x: Short): Int`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Byte): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Char): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Double): Double`                                      ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Float): Float`                                        ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Int): Int`                                            ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Long): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def /(x: Short): Int`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Short)


### `abstract def <(x: Byte): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Char): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Double): Boolean`                                     ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Float): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Int): Boolean`                                        ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Long): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <(x: Short): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Short)


### `abstract def <<(x: Int): Int`                                           ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Short)


### `abstract def <<(x: Long): Int`                                          ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Short)


### `abstract def <=(x: Byte): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Char): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Double): Boolean`                                    ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Float): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Int): Boolean`                                       ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Long): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def <=(x: Short): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Byte): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Char): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Double): Boolean`                                    ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Float): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Int): Boolean`                                       ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Long): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def ==(x: Short): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Byte): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Char): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Double): Boolean`                                     ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Float): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Int): Boolean`                                        ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Long): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >(x: Short): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Byte): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Char): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Double): Boolean`                                    ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Float): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Int): Boolean`                                       ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Long): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >=(x: Short): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Short)


### `abstract def >>(x: Int): Int`                                           ###

Returns this value bit-shifted right by the specified number of bits, filling in
the left bits with the same value as the left-most bit of this. The effect of
this is to retain the sign of the value.

Example:

```scala
-21 >> 3 == -3
// in binary: 11111111 11111111 11111111 11101011 >> 3 ==
//            11111111 11111111 11111111 11111101
```

(defined at scala.Short)


### `abstract def >>(x: Long): Int`                                          ###

Returns this value bit-shifted right by the specified number of bits, filling in
the left bits with the same value as the left-most bit of this. The effect of
this is to retain the sign of the value.

Example:

```scala
-21 >> 3 == -3
// in binary: 11111111 11111111 11111111 11101011 >> 3 ==
//            11111111 11111111 11111111 11111101
```

(defined at scala.Short)


### `abstract def >>>(x: Int): Int`                                          ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Short)


### `abstract def >>>(x: Long): Int`                                         ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Short)


### `abstract def ^(x: Byte): Int`                                           ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Short)


### `abstract def ^(x: Char): Int`                                           ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Short)


### `abstract def ^(x: Int): Int`                                            ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Short)


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

(defined at scala.Short)


### `abstract def ^(x: Short): Int`                                          ###

Returns the bitwise XOR of this value and `x` .

Example:

```scala
(0xf0 ^ 0xaa) == 0x5a
// in binary:   11110000
//            ^ 10101010
//              --------
//              01011010
```

(defined at scala.Short)


### `abstract def |(x: Byte): Int`                                           ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Short)


### `abstract def |(x: Char): Int`                                           ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Short)


### `abstract def |(x: Int): Int`                                            ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Short)


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

(defined at scala.Short)


### `abstract def |(x: Short): Int`                                          ###

Returns the bitwise OR of this value and `x` .

Example:

```scala
(0xf0 | 0xaa) == 0xfa
// in binary:   11110000
//            | 10101010
//              --------
//              11111010
```

(defined at scala.Short)


--------------------------------------------------------------------------------
                    Concrete Value Members From scala.Short
--------------------------------------------------------------------------------


### `abstract def toByte: Byte`                                              ###

(defined at scala.Short)


--------------------------------------------------------------------------------
  Concrete Value Members From Implicit scala.LowPriorityImplicits.shortWrapper
--------------------------------------------------------------------------------


### `def compare(y: Short): Int`                                             ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Implicit information
  * This member is added by an implicit conversion from Short to RichShort
    performed by method shortWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * OrderedProxy → Ordered

(added by implicit convertion: scala.LowPriorityImplicits.shortWrapper)


### `def compareTo(that: Short): Int`                                        ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from Short to RichShort
    performed by method shortWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered → Comparable

(added by implicit convertion: scala.LowPriorityImplicits.shortWrapper)


### `def max(that: Short): Short`                                            ###

Returns `this` if `this > that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Short to RichShort
    performed by method shortWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichShort → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.shortWrapper)


### `def min(that: Short): Short`                                            ###

Returns `this` if `this < that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Short to RichShort
    performed by method shortWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichShort → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.shortWrapper)


--------------------------------------------------------------------------------
         Concrete Value Members From Implicit scala.Predef.short2Short
--------------------------------------------------------------------------------


### `def compareTo(arg0: java.lang.Short): Int`                              ###

* Implicit information
  * This member is added by an implicit conversion from Short to java.lang.Short
    performed by method short2Short in scala.Predef.
* Definition Classes
  * Short → Comparable
(added by implicit convertion: scala.Predef.short2Short)
