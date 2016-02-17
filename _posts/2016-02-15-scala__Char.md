
#                                  scala.Char                                  #

```scala
abstract final class Char extends AnyVal
```

 `Char` , a 16-bit unsigned integer (equivalent to Java's `char` primitive type)
is a subtype of scala.AnyVal. Instances of `Char` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Char => scala.runtime.RichChar which
provides useful non-primitive operations.

* Source
  * [Char.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Char.scala#L1)


--------------------------------------------------------------------------------
                     Abstract Value Members From scala.Char
--------------------------------------------------------------------------------


### `abstract def !=(x: Byte): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Char): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Double): Boolean`                                    ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Float): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Int): Boolean`                                       ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Long): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def !=(x: Short): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def %(x: Byte): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Char): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Double): Double`                                      ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Float): Float`                                        ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Int): Int`                                            ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Long): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


### `abstract def %(x: Short): Int`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


### `abstract def *(x: Byte): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Char): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Double): Double`                                      ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Float): Float`                                        ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Int): Int`                                            ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Long): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def *(x: Short): Int`                                          ###

Returns the product of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Byte): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Char): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Double): Double`                                      ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Float): Float`                                        ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Int): Int`                                            ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Long): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: Short): Int`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Char)


### `abstract def +(x: String): String`                                      ###

(defined at scala.Char)


### `abstract def -(x: Byte): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Char): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Double): Double`                                      ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Float): Float`                                        ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Int): Int`                                            ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Long): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def -(x: Short): Int`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Byte): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Char): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Double): Double`                                      ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Float): Float`                                        ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Int): Int`                                            ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Long): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def /(x: Short): Int`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Char)


### `abstract def <(x: Byte): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Char): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Double): Boolean`                                     ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Float): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Int): Boolean`                                        ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Long): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <(x: Short): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Char)


### `abstract def <<(x: Int): Int`                                           ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Char)


### `abstract def <<(x: Long): Int`                                          ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Char)


### `abstract def <=(x: Byte): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Char): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Double): Boolean`                                    ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Float): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Int): Boolean`                                       ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Long): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def <=(x: Short): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Byte): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Char): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Double): Boolean`                                    ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Float): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Int): Boolean`                                       ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Long): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def ==(x: Short): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Byte): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Char): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Double): Boolean`                                     ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Float): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Int): Boolean`                                        ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Long): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >(x: Short): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Byte): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Char): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Double): Boolean`                                    ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Float): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Int): Boolean`                                       ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Long): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


### `abstract def >=(x: Short): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


### `abstract def >>>(x: Int): Int`                                          ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Char)


### `abstract def >>>(x: Long): Int`                                         ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


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

(defined at scala.Char)


--------------------------------------------------------------------------------
                     Concrete Value Members From scala.Char
--------------------------------------------------------------------------------


### `abstract def toByte: Byte`                                              ###

(defined at scala.Char)


--------------------------------------------------------------------------------
  Concrete Value Members From Implicit scala.LowPriorityImplicits.charWrapper
--------------------------------------------------------------------------------


### `def compare(y: Char): Int`                                              ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * OrderedProxy → Ordered

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def compareTo(that: Char): Int`                                         ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered → Comparable

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def max(that: Char): Char`                                              ###

Returns `this` if `this > that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichChar → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def min(that: Char): Char`                                              ###

Returns `this` if `this < that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichChar → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def to(end: Char): Inclusive[Char]`                                     ###

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def to(end: Char, step: Char): Inclusive[Char]`                         ###

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def until(end: Char): Exclusive[Char]`                                  ###

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


### `def until(end: Char, step: Char): Exclusive[Char]`                      ###

* Implicit information
  * This member is added by an implicit conversion from Char to RichChar
    performed by method charWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * IntegralProxy → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.charWrapper)


--------------------------------------------------------------------------------
        Concrete Value Members From Implicit scala.Predef.char2Character
--------------------------------------------------------------------------------


### `def compareTo(arg0: Character): Int`                                    ###

* Implicit information
  * This member is added by an implicit conversion from Char to Character
    performed by method char2Character in scala.Predef.
* Definition Classes
  * Character → Comparable
(added by implicit convertion: scala.Predef.char2Character)
