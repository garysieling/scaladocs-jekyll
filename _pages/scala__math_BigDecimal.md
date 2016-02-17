
#                            scala.math.BigDecimal                            #

```scala
final class BigDecimal extends ScalaNumber with ScalaNumericConversions with Serializable with Ordered[BigDecimal]
```

 `BigDecimal` represents decimal floating-point numbers of arbitrary precision.
By default, the precision approximately matches that of IEEE 128-bit floating
point numbers (34 decimal digits, `HALF_EVEN` rounding mode). Within the range
of IEEE binary128 numbers, `BigDecimal` will agree with `BigInt` for both
equality and hash codes (and will agree with primitive types as well). Beyond
that range--numbers with more than 4934 digits when written out in full--the
 `hashCode` of `BigInt` and `BigDecimal` is allowed to diverge due to difficulty
in efficiently computing both the decimal representation in `BigDecimal` and the
binary representation in `BigInt` .

When creating a `BigDecimal` from a `Double` or `Float` , care must be taken as
the binary fraction representation of `Double` and `Float` does not easily
convert into a decimal representation. Three explicit schemes are available for
conversion. `BigDecimal.decimal` will convert the floating-point number to a
decimal text representation, and build a `BigDecimal` based on that.
 `BigDecimal.binary` will expand the binary fraction to the requested or default
precision. `BigDecimal.exact` will expand the binary fraction to the full number
of digits, thus producing the exact decimal value corresponding to the binary
fraction of that floating-point number. `BigDecimal` equality matches the
decimal expansion of `Double` : `BigDecimal.decimal(0.1) == 0.1` . Note that
since `0.1f != 0.1` , the same is not true for `Float` . Instead,
 `0.1f == BigDecimal.decimal((0.1f).toDouble)` .

To test whether a `BigDecimal` number can be converted to a `Double` or `Float`
and then back without loss of information by using one of these methods, test
with `isDecimalDouble` , `isBinaryDouble` , or `isExactDouble` or the
corresponding `Float` versions. Note that `BigInt` 's `isValidDouble` will agree
with `isExactDouble` , not the `isDecimalDouble` used by default.

 `BigDecimal` uses the decimal representation of binary floating-point numbers
to determine equality and hash codes. This yields different answers than
conversion between `Long` and `Double` values, where the exact form is used. As
always, since floating-point is a lossy representation, it is advisable to take
care when assuming identity will be maintained across multiple conversions.

 `BigDecimal` maintains a `MathContext` that determines the rounding that is
applied to certain calculations. In most cases, the value of the `BigDecimal` is
also rounded to the precision specified by the `MathContext` . To create a
 `BigDecimal` with a different precision than its `MathContext` , use
 `new BigDecimal(new java.math.BigDecimal(...), mc)` . Rounding will be applied
on those mathematical operations that can dramatically change the number of
digits in a full representation, namely multiplication, division, and powers.
The left-hand argument's `MathContext` always determines the degree of rounding,
if any, and is the one propagated through arithmetic operations that do not
apply rounding themselves.

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)
* Version
  * 1.1


--------------------------------------------------------------------------------
                Instance Constructors From scala.math.BigDecimal
--------------------------------------------------------------------------------


### `new BigDecimal(bigDecimal: java.math.BigDecimal)`                       ###

(defined at scala.math.BigDecimal)


--------------------------------------------------------------------------------
                    Value Members From scala.math.BigDecimal
--------------------------------------------------------------------------------


### `def %(that: BigDecimal): BigDecimal`                                    ###

Remainder after dividing this by that.

(defined at scala.math.BigDecimal)


### `def *(that: BigDecimal): BigDecimal`                                    ###

Multiplication of BigDecimals

(defined at scala.math.BigDecimal)


### `def +(that: BigDecimal): BigDecimal`                                    ###

Addition of BigDecimals

(defined at scala.math.BigDecimal)


### `def -(that: BigDecimal): BigDecimal`                                    ###

Subtraction of BigDecimals

(defined at scala.math.BigDecimal)


### `def /%(that: BigDecimal): (BigDecimal, BigDecimal)`                     ###

Division and Remainder - returns tuple containing the result of
divideToIntegralValue and the remainder. The computation is exact: no rounding
is applied.

(defined at scala.math.BigDecimal)


### `def /(that: BigDecimal): BigDecimal`                                    ###

Division of BigDecimals

(defined at scala.math.BigDecimal)


### `def abs: BigDecimal`                                                    ###

Returns the absolute value of this BigDecimal

(defined at scala.math.BigDecimal)


### `def apply(mc: MathContext): BigDecimal`                                 ###

Returns a new BigDecimal based on the supplied MathContext, rounded as needed.

(defined at scala.math.BigDecimal)


### `def compare(that: BigDecimal): Int`                                     ###

Compares this BigDecimal with the specified BigDecimal

* Definition Classes
  * BigDecimal → Ordered

(defined at scala.math.BigDecimal)


### `def equals(that: Any): Boolean`                                         ###

Compares this BigDecimal with the specified value for equality. Where `Float`
and `Double` disagree, `BigDecimal` will agree with the `Double` value

* that
  * the object to compare against this object for equality.
* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * BigDecimal → AnyRef → Any

(defined at scala.math.BigDecimal)


### `def equals(that: BigDecimal): Boolean`                                  ###

Compares this BigDecimal with the specified BigDecimal for equality.

(defined at scala.math.BigDecimal)


### `def max(that: BigDecimal): BigDecimal`                                  ###

Returns the maximum of this and that, or this if the two are equal

(defined at scala.math.BigDecimal)


### `val mc: MathContext`                                                    ###

(defined at scala.math.BigDecimal)


### `def min(that: BigDecimal): BigDecimal`                                  ###

Returns the minimum of this and that, or this if the two are equal

(defined at scala.math.BigDecimal)


### `def pow(n: Int): BigDecimal`                                            ###

Returns a BigDecimal whose value is this ** n.

(defined at scala.math.BigDecimal)


### `def quot(that: BigDecimal): BigDecimal`                                 ###

Divide to Integral value.

(defined at scala.math.BigDecimal)


### `def remainder(that: BigDecimal): BigDecimal`                            ###

Remainder after dividing this by that.

(defined at scala.math.BigDecimal)


### `def round(mc: MathContext): BigDecimal`                                 ###

Returns a BigDecimal rounded according to the supplied MathContext settings, but
preserving its own MathContext for future operations.

(defined at scala.math.BigDecimal)


### `def rounded: BigDecimal`                                                ###

Returns a `BigDecimal` rounded according to its own `MathContext`

(defined at scala.math.BigDecimal)


### `def setScale(scale: Int): BigDecimal`                                   ###

Returns a `BigDecimal` whose scale is the specified value, and whose value is
numerically equal to this BigDecimal's.

(defined at scala.math.BigDecimal)


### `def setScale(scale: Int, mode: RoundingMode): BigDecimal`               ###

(defined at scala.math.BigDecimal)


### `def to(end: BigDecimal): Partial[BigDecimal, Inclusive[BigDecimal]]`    ###

Like `until` , but inclusive of the end value.

(defined at scala.math.BigDecimal)


### `def to(end: BigDecimal, step: BigDecimal): Inclusive[scala.BigDecimal]` ###

Like `until` , but inclusive of the end value.

(defined at scala.math.BigDecimal)


### `def toBigInt(): BigInt`                                                 ###

Converts this `BigDecimal` to a scala.BigInt.

(defined at scala.math.BigDecimal)


### `def toBigIntExact(): Option[BigInt]`                                    ###

Converts this `BigDecimal` to a scala.BigInt if it can be done losslessly,
returning Some(BigInt) or None.

(defined at scala.math.BigDecimal)


### `def ulp: BigDecimal`                                                    ###

Returns the size of an ulp, a unit in the last place, of this BigDecimal.

(defined at scala.math.BigDecimal)


### `def unary_-: BigDecimal`                                                ###

Returns a BigDecimal whose value is the negation of this BigDecimal

(defined at scala.math.BigDecimal)


### `def until(end: BigDecimal): Partial[BigDecimal, Exclusive[BigDecimal]]` ###

Creates a partially constructed NumericRange[BigDecimal] in range `[start;end)` ,
where start is the target BigDecimal. The step must be supplied via the "by"
method of the returned object in order to receive the fully constructed range.
For example:

```scala
val partial = BigDecimal(1.0) to 2.0       // not usable yet
val range = partial by 0.01                // now a NumericRange
val range2 = BigDecimal(0) to 1.0 by 0.01  // all at once of course is fine too
```

* end
  * the end value of the range (exclusive)
* returns
  * the partially constructed NumericRange

(defined at scala.math.BigDecimal)


### `def until(end: BigDecimal, step: BigDecimal): Exclusive[scala.BigDecimal]` ###

Same as the one-argument `until` , but creates the range immediately.

(defined at scala.math.BigDecimal)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: BigDecimal): Boolean`                                       ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: BigDecimal): Boolean`                                      ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: BigDecimal): Boolean`                                       ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: BigDecimal): Boolean`                                      ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: BigDecimal): Int`                                   ###

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
