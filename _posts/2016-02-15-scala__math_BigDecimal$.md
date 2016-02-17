
#                            scala.math.BigDecimal                            #

```scala
object BigDecimal extends Serializable
```

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)
* Version
  * 1.1
* Since
  * 2.7


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object RoundingMode extends Enumeration`                                ###

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)


--------------------------------------------------------------------------------
              Deprecated Value Members From scala.math.BigDecimal
--------------------------------------------------------------------------------


### `def apply(x: Float): BigDecimal`                                        ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ The default conversion from Float may not do what you
    want. Use BigDecimal.decimal for a String representation, or explicitly
    convert the Float with.toDouble.

(defined at scala.math.BigDecimal)


### `def apply(x: Float, mc: MathContext): BigDecimal`                       ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ The default conversion from Float may not do what you
    want. Use BigDecimal.decimal for a String representation, or explicitly
    convert the Float with.toDouble.

(defined at scala.math.BigDecimal)


### `def apply(bd: java.math.BigDecimal, mc: MathContext): BigDecimal`       ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ This method appears to round a java.math.BigDecimal
    but actually doesn't. Use new BigDecimal(bd, mc) instead for no rounding, or
    BigDecimal.decimal(bd, mc) for rounding.

(defined at scala.math.BigDecimal)


### `def valueOf(d: Double, mc: MathContext): BigDecimal`                    ###

Constructs a `BigDecimal` using the java BigDecimal static valueOf constructor,
specifying a `MathContext` that is used for computations but isn't used for
rounding. Use `BigDecimal.decimal` to use `MathContext` for rounding, or
 `BigDecimal(java.math.BigDecimal.valueOf(d), mc)` for no rounding.

* d
  * the specified double value
* mc
  * the `MathContext` used for future computations
* returns
  * the constructed `BigDecimal`

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ MathContext is not applied to Doubles in valueOf. Use
    BigDecimal.decimal to use rounding, or java.math.BigDecimal.valueOf to avoid
    it.

(defined at scala.math.BigDecimal)


### `def valueOf(f: Float): BigDecimal`                                      ###

Constructs a `BigDecimal` using the java BigDecimal static valueOf constructor.
This is unlikely to do what you want; use `valueOf(f.toDouble)` or `decimal(f)`
instead.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ Float arguments to valueOf may not do what you wish.
    Use decimal or valueOf(f.toDouble).

(defined at scala.math.BigDecimal)


### `def valueOf(f: Float, mc: MathContext): BigDecimal`                     ###

Constructs a `BigDecimal` using the java BigDecimal static valueOf constructor.
This is unlikely to do what you want; use `valueOf(f.toDouble)` or `decimal(f)`
instead.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11)_ Float arguments to valueOf may not do what you wish.
    Use decimal or valueOf(f.toDouble).

(defined at scala.math.BigDecimal)


--------------------------------------------------------------------------------
                    Value Members From scala.math.BigDecimal
--------------------------------------------------------------------------------


### `def apply(x: Array[Char]): BigDecimal`                                  ###

Translates a character array representation of a `BigDecimal` into a
 `BigDecimal` .

(defined at scala.math.BigDecimal)


### `def apply(x: Array[Char], mc: MathContext): BigDecimal`                 ###

Translates a character array representation of a `BigDecimal` into a
 `BigDecimal` , rounding if necessary.

(defined at scala.math.BigDecimal)


### `def apply(x: BigInt): BigDecimal`                                       ###

Constructs a `BigDecimal` whose value is equal to that of the specified
 `BigInt` value.

* x
  * the specified `BigInt` value
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(unscaledVal: BigInt, scale: Int): BigDecimal`                 ###

Constructs a `BigDecimal` whose unscaled value is equal to that of the specified
 `BigInt` value.

* unscaledVal
  * the specified `BigInt` value
* scale
  * the scale
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(unscaledVal: BigInt, scale: Int, mc: MathContext): BigDecimal` ###

Constructs a `BigDecimal` whose unscaled value is equal to that of the specified
 `BigInt` value.

* unscaledVal
  * the specified `BigInt` value
* scale
  * the scale
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(x: BigInt, mc: MathContext): BigDecimal`                      ###

Constructs a `BigDecimal` whose value is equal to that of the specified
 `BigInt` value, rounding if necessary.

* x
  * the specified `BigInt` value
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(d: Double): BigDecimal`                                       ###

Constructs a `BigDecimal` whose value is equal to that of the specified double
value. Equivalent to `BigDecimal.decimal` .

* d
  * the specified `Double` value
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(d: Double, mc: MathContext): BigDecimal`                      ###

Constructs a `BigDecimal` whose value is equal to that of the specified double
value, but rounded if necessary. Equivalent to `BigDecimal.decimal` .

* d
  * the specified `Double` value
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(i: Int): BigDecimal`                                          ###

Constructs a `BigDecimal` whose value is equal to that of the specified
 `Integer` value.

* i
  * the specified integer value
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(i: Int, mc: MathContext): BigDecimal`                         ###

Constructs a `BigDecimal` whose value is equal to that of the specified
 `Integer` value, rounding if necessary.

* i
  * the specified integer value
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(l: Long): BigDecimal`                                         ###

Constructs a `BigDecimal` whose value is equal to that of the specified long
value.

* l
  * the specified long value
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(unscaledVal: Long, scale: Int): BigDecimal`                   ###

Constructs a `BigDecimal` whose unscaled value is equal to that of the specified
long value.

* unscaledVal
  * the value
* scale
  * the scale
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(unscaledVal: Long, scale: Int, mc: MathContext): BigDecimal`  ###

Constructs a `BigDecimal` whose unscaled value is equal to that of the specified
long value, but rounded if necessary.

* unscaledVal
  * the value
* scale
  * the scale
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(l: Long, mc: MathContext): BigDecimal`                        ###

Constructs a `BigDecimal` whose value is equal to that of the specified long
value, but rounded if necessary.

* l
  * the specified long value
* mc
  * the precision and rounding mode for creation of this value and future
    operations on it
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def apply(x: String): BigDecimal`                                       ###

Translates the decimal String representation of a `BigDecimal` into a
 `BigDecimal` .

(defined at scala.math.BigDecimal)


### `def apply(x: String, mc: MathContext): BigDecimal`                      ###

Translates the decimal String representation of a `BigDecimal` into a
 `BigDecimal` , rounding if necessary.

(defined at scala.math.BigDecimal)


### `def apply(bd: java.math.BigDecimal): BigDecimal`                        ###

Constructs a `BigDecimal` from a `java.math.BigDecimal` .

(defined at scala.math.BigDecimal)


### `def binary(d: Double): BigDecimal`                                      ###

Constructs a `BigDecimal` by expanding the binary fraction contained by
 `Double` value `d` into a decimal representation. Note: this also works
correctly on converted `Float` s.

(defined at scala.math.BigDecimal)


### `def binary(d: Double, mc: MathContext): BigDecimal`                     ###

Constructs a `BigDecimal` by expanding the binary fraction contained by
 `Double` value `d` into a decimal representation, rounding if necessary. When a
 `Float` is converted to a `Double` , the binary fraction is preserved, so this
method also works for converted `Float` s.

(defined at scala.math.BigDecimal)


### `def decimal(d: Double): BigDecimal`                                     ###

Constructs a `BigDecimal` using the decimal text representation of `Double`
value `d` .

(defined at scala.math.BigDecimal)


### `def decimal(d: Double, mc: MathContext): BigDecimal`                    ###

Constructs a `BigDecimal` using the decimal text representation of `Double`
value `d` , rounding if necessary.

(defined at scala.math.BigDecimal)


### `def decimal(f: Float): BigDecimal`                                      ###

Constructs a `BigDecimal` using the decimal text representation of `Float` value
 `f` . Note that `BigDecimal.decimal(0.1f) != 0.1f` since equality agrees with
the `Double` representation, and `0.1 != 0.1f` .

(defined at scala.math.BigDecimal)


### `def decimal(f: Float, mc: MathContext): BigDecimal`                     ###

Constructs a `BigDecimal` using the decimal text representation of `Float` value
 `f` , rounding if necessary. Note that `BigDecimal.decimal(0.1f) != 0.1f` since
equality agrees with the `Double` representation, and `0.1 != 0.1f` .

(defined at scala.math.BigDecimal)


### `def decimal(l: Long): BigDecimal`                                       ###

Constructs a `BigDecimal` from a `Long` . This is identical to `BigDecimal(l)` .

(defined at scala.math.BigDecimal)


### `def decimal(l: Long, mc: MathContext): BigDecimal`                      ###

Constructs a `BigDecimal` from a `Long` , rounding if necessary. This is
identical to `BigDecimal(l, mc)` .

(defined at scala.math.BigDecimal)


### `def decimal(bd: java.math.BigDecimal, mc: MathContext): BigDecimal`     ###

Constructs a `BigDecimal` using a `java.math.BigDecimal` , rounding if
necessary.

(defined at scala.math.BigDecimal)


### `val defaultMathContext: MathContext`                                    ###

(defined at scala.math.BigDecimal)


### `implicit def double2bigDecimal(d: Double): BigDecimal`                  ###

Implicit conversion from `Double` to `BigDecimal` .

(defined at scala.math.BigDecimal)


### `def exact(cs: Array[Char]): BigDecimal`                                 ###

Constructs a `BigDecimal` that exactly represents the number specified in base
10 in a character array.

(defined at scala.math.BigDecimal)


### `def exact(bi: BigInt): BigDecimal`                                      ###

Constructs a `BigDecimal` that exactly represents a `BigInt` .

(defined at scala.math.BigDecimal)


### `def exact(d: Double): BigDecimal`                                       ###

Constructs a `BigDecimal` by fully expanding the binary fraction contained by
 `Double` value `d` , adjusting the precision as necessary. Note: this works
correctly on converted `Float` s also.

(defined at scala.math.BigDecimal)


### `def exact(l: Long): BigDecimal`                                         ###

Constructs a `BigDecimal` that exactly represents a `Long` . Note that all
creation methods for `BigDecimal` that do not take a `MathContext` represent a
 `Long` ; this is equivalent to `apply` , `valueOf` , etc..

(defined at scala.math.BigDecimal)


### `def exact(s: String): BigDecimal`                                       ###

Constructs a `BigDecimal` that exactly represents the number specified in a
 `String` .

(defined at scala.math.BigDecimal)


### `def exact(repr: java.math.BigDecimal): BigDecimal`                      ###

Constructs a `BigDecimal` from a `java.math.BigDecimal` . The precision is the
default for `BigDecimal` or enough to represent the `java.math.BigDecimal`
exactly, whichever is greater.

(defined at scala.math.BigDecimal)


### `implicit def int2bigDecimal(i: Int): BigDecimal`                        ###

Implicit conversion from `Int` to `BigDecimal` .

(defined at scala.math.BigDecimal)


### `implicit def javaBigDecimal2bigDecimal(x: java.math.BigDecimal): BigDecimal` ###

Implicit conversion from `java.math.BigDecimal` to `scala.BigDecimal` .

(defined at scala.math.BigDecimal)


### `implicit def long2bigDecimal(l: Long): BigDecimal`                      ###

Implicit conversion from `Long` to `BigDecimal` .

(defined at scala.math.BigDecimal)


### `def valueOf(d: Double): BigDecimal`                                     ###

Constructs a `BigDecimal` using the java BigDecimal static valueOf constructor.
Equivalent to `BigDecimal.decimal` .

* d
  * the specified double value
* returns
  * the constructed `BigDecimal`

(defined at scala.math.BigDecimal)


### `def valueOf(x: Long): BigDecimal`                                       ###

Constructs a `BigDecimal` using the java BigDecimal static valueOf constructor.

* x
  * the specified `Long` value
* returns
  * the constructed `BigDecimal`
(defined at scala.math.BigDecimal)
