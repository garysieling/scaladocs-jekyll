
#                           scala.runtime.RichShort                           #

```scala
final class RichShort extends AnyVal with ScalaWholeNumberProxy[Short]
```

* Source
  * [RichShort.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/RichShort.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Any###
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


### `def <(that: Short): Boolean`                                            ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: Short): Boolean`                                           ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: Short): Boolean`                                            ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: Short): Boolean`                                           ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: Short): Int`                                        ###

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
                 Value Members From scala.runtime.OrderedProxy
--------------------------------------------------------------------------------


### `def compare(y: Short): Int`                                             ###

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
               Instance Constructors From scala.runtime.RichShort
--------------------------------------------------------------------------------


### `new RichShort(self: Short)`                                             ###

(defined at scala.runtime.RichShort)


--------------------------------------------------------------------------------
                   Value Members From scala.runtime.RichShort
--------------------------------------------------------------------------------


### `def max(that: Short): Short`                                            ###

Returns `this` if `this > that` or `that` otherwise.

* Definition Classes
  * RichShort → ScalaNumberProxy

(defined at scala.runtime.RichShort)


### `def min(that: Short): Short`                                            ###

Returns `this` if `this < that` or `that` otherwise.

* Definition Classes
  * RichShort → ScalaNumberProxy

(defined at scala.runtime.RichShort)


### `def num: ShortIsIntegral.type`                                          ###

* Attributes
  * protected
* Definition Classes
  * RichShort → ScalaNumberProxy
(defined at scala.runtime.RichShort)
