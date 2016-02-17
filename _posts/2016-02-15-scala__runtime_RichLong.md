
#                            scala.runtime.RichLong                            #

```scala
final class RichLong extends AnyVal with IntegralProxy[Long]
```

* Source
  * [RichLong.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/RichLong.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type ResultWithoutStep = NumericRange[Long]`                            ###

* Definition Classes
  * IntegralProxy → RangedProxy


--------------------------------------------------------------------------------
                   Deprecated Value Members From scala.Any###
--------------------------------------------------------------------------------


### `final def ##(): Int`                                                    ###

Equivalent to `x.hashCode` except for boxed numeric types and `null` . For
numerics, it returns a hash value which is consistent with value equality: if
two value type instances compare as true, then ## will produce the same hash
value for each of them. For `null` returns a hashcode where `null.hashCode`
throws a `NullPointerException` .

* returns
  * a hash value consistent with ==

* Definition Classes
  * Any

(defined at scala.Any###)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: Long): Boolean`                                             ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: Long): Boolean`                                            ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: Long): Boolean`                                             ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: Long): Boolean`                                            ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: Long): Int`                                         ###

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


--------------------------------------------------------------------------------
                 Value Members From scala.runtime.IntegralProxy
--------------------------------------------------------------------------------


### `def to(end: Long): Inclusive[Long]`                                     ###

* Definition Classes
  * IntegralProxy → RangedProxy

(defined at scala.runtime.IntegralProxy)


### `def to(end: Long, step: Long): Inclusive[Long]`                         ###

* Definition Classes
  * IntegralProxy → RangedProxy

(defined at scala.runtime.IntegralProxy)


### `def until(end: Long): Exclusive[Long]`                                  ###

* Definition Classes
  * IntegralProxy → RangedProxy

(defined at scala.runtime.IntegralProxy)


### `def until(end: Long, step: Long): Exclusive[Long]`                      ###

* Definition Classes
  * IntegralProxy → RangedProxy

(defined at scala.runtime.IntegralProxy)


--------------------------------------------------------------------------------
                 Value Members From scala.runtime.OrderedProxy
--------------------------------------------------------------------------------


### `def compare(y: Long): Int`                                              ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Definition Classes
  * OrderedProxy → Ordered

(defined at scala.runtime.OrderedProxy)


--------------------------------------------------------------------------------
               Instance Constructors From scala.runtime.RichLong
--------------------------------------------------------------------------------


### `new RichLong(self: Long)`                                               ###

(defined at scala.runtime.RichLong)


--------------------------------------------------------------------------------
                   Value Members From scala.runtime.RichLong
--------------------------------------------------------------------------------


### `def max(that: Long): Long`                                              ###

Returns `this` if `this > that` or `that` otherwise.

* Definition Classes
  * RichLong → ScalaNumberProxy

(defined at scala.runtime.RichLong)


### `def min(that: Long): Long`                                              ###

Returns `this` if `this < that` or `that` otherwise.

* Definition Classes
  * RichLong → ScalaNumberProxy

(defined at scala.runtime.RichLong)


### `def num: LongIsIntegral.type`                                           ###

* Attributes
  * protected
* Definition Classes
  * RichLong → IntegralProxy → ScalaNumberProxy
(defined at scala.runtime.RichLong)
