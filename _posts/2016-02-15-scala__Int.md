
#                                  scala.Int                                  #

```scala
abstract final class Int extends AnyVal
```

 `Int` , a 32-bit signed integer (equivalent to Java's `int` primitive type) is
a subtype of scala.AnyVal. Instances of `Int` are not represented by an object
in the underlying runtime system.

There is an implicit conversion from scala.Int => scala.runtime.RichInt which
provides useful non-primitive operations.

* Source
  * [Int.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Int.scala#L1)


--------------------------------------------------------------------------------
                     Abstract Value Members From scala.Int
--------------------------------------------------------------------------------


### `abstract def !=(x: Byte): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Char): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Double): Boolean`                                    ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Float): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Int): Boolean`                                       ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Long): Boolean`                                      ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def !=(x: Short): Boolean`                                     ###

Returns `true` if this value is not equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def %(x: Byte): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Char): Int`                                           ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Double): Double`                                      ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Float): Float`                                        ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Int): Int`                                            ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Long): Long`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


### `abstract def %(x: Short): Int`                                          ###

Returns the remainder of the division of this value by `x` .

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


### `abstract def *(x: Byte): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Char): Int`                                           ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Double): Double`                                      ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Float): Float`                                        ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Int): Int`                                            ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Long): Long`                                          ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def *(x: Short): Int`                                          ###

Returns the product of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Byte): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Char): Int`                                           ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Double): Double`                                      ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Float): Float`                                        ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Int): Int`                                            ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Long): Long`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: Short): Int`                                          ###

Returns the sum of this value and `x` .

(defined at scala.Int)


### `abstract def +(x: String): String`                                      ###

(defined at scala.Int)


### `abstract def -(x: Byte): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Char): Int`                                           ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Double): Double`                                      ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Float): Float`                                        ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Int): Int`                                            ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Long): Long`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def -(x: Short): Int`                                          ###

Returns the difference of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Byte): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Char): Int`                                           ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Double): Double`                                      ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Float): Float`                                        ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Int): Int`                                            ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Long): Long`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def /(x: Short): Int`                                          ###

Returns the quotient of this value and `x` .

(defined at scala.Int)


### `abstract def <(x: Byte): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Char): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Double): Boolean`                                     ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Float): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Int): Boolean`                                        ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Long): Boolean`                                       ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <(x: Short): Boolean`                                      ###

Returns `true` if this value is less than x, `false` otherwise.

(defined at scala.Int)


### `abstract def <<(x: Int): Int`                                           ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Int)


### `abstract def <<(x: Long): Int`                                          ###

Returns this value bit-shifted left by the specified number of bits, filling in
the new right bits with zeroes.

Example:

```scala
6 << 3 == 48 // in binary: 0110 << 3 == 0110000
```

(defined at scala.Int)


### `abstract def <=(x: Byte): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Char): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Double): Boolean`                                    ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Float): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Int): Boolean`                                       ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Long): Boolean`                                      ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def <=(x: Short): Boolean`                                     ###

Returns `true` if this value is less than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Byte): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Char): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Double): Boolean`                                    ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Float): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Int): Boolean`                                       ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Long): Boolean`                                      ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def ==(x: Short): Boolean`                                     ###

Returns `true` if this value is equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Byte): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Char): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Double): Boolean`                                     ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Float): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Int): Boolean`                                        ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Long): Boolean`                                       ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >(x: Short): Boolean`                                      ###

Returns `true` if this value is greater than x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Byte): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Char): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Double): Boolean`                                    ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Float): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Int): Boolean`                                       ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Long): Boolean`                                      ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


### `abstract def >=(x: Short): Boolean`                                     ###

Returns `true` if this value is greater than or equal to x, `false` otherwise.

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


### `abstract def >>>(x: Int): Int`                                          ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Int)


### `abstract def >>>(x: Long): Int`                                         ###

Returns this value bit-shifted right by the specified number of bits, filling
the new left bits with zeroes.

Examples:

```scala
-21 >>> 3 == 536870909
// in binary: 11111111 11111111 11111111 11101011 >>> 3 ==
//            00011111 11111111 11111111 11111101 21 >>> 3 == 2 // in binary: 010101 >>> 3 == 010
```

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


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

(defined at scala.Int)


--------------------------------------------------------------------------------
                    Deprecated Value Members From scala.Int
--------------------------------------------------------------------------------


### `abstract def toByte: Byte`                                              ###

(defined at scala.Int)


--------------------------------------------------------------------------------
   Concrete Value Members From Implicit scala.LowPriorityImplicits.intWrapper
--------------------------------------------------------------------------------


### `def compare(y: Int): Int`                                               ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * OrderedProxy → Ordered

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def compareTo(that: Int): Int`                                          ###

Result of comparing `this` with operand `that` .

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * Ordered → Comparable

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def max(that: Int): Int`                                                ###

Returns `this` if `this > that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def min(that: Int): Int`                                                ###

Returns `this` if `this < that` or `that` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → ScalaNumberProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def to(end: Int): Inclusive`                                            ###

* end
  * The final bound of the range to make.
* returns
  * A scala.collection.immutable.Range from `this` up to and including `end` .

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def to(end: Int, step: Int): Inclusive`                                 ###

* end
  * The final bound of the range to make.
* step
  * The number to increase by for each step of the range.
* returns
  * A scala.collection.immutable.Range from `this` up to and including `end` .

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def until(end: Int): collection.immutable.Range`                        ###

* end
  * The final bound of the range to make.
* returns
  * A scala.collection.immutable.Range from `this` up to but not including
     `end` .

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


### `def until(end: Int, step: Int): collection.immutable.Range`             ###

* end
  * The final bound of the range to make.
* step
  * The number to increase by for each step of the range.
* returns
  * A scala.collection.immutable.Range from `this` up to but not including
     `end` .

* Implicit information
  * This member is added by an implicit conversion from Int to RichInt performed
    by method intWrapper in scala.LowPriorityImplicits.
* Definition Classes
  * RichInt → RangedProxy

(added by implicit convertion: scala.LowPriorityImplicits.intWrapper)


--------------------------------------------------------------------------------
         Concrete Value Members From Implicit scala.Predef.int2Integer
--------------------------------------------------------------------------------


### `def compareTo(arg0: Integer): Int`                                      ###

* Implicit information
  * This member is added by an implicit conversion from Int to Integer performed
    by method int2Integer in scala.Predef.
* Definition Classes
  * Integer → Comparable
(added by implicit convertion: scala.Predef.int2Integer)
