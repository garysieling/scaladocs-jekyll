
#                      scala.math.ScalaNumericConversions                      #

```scala
trait ScalaNumericConversions extends ScalaNumber with ScalaNumericAnyConversions
```

A slightly more specific conversion trait for classes which extend ScalaNumber
(which excludes value classes.)

* Source
  * [ScalaNumericConversions.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/ScalaNumericConversions.scala#L1)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.math.ScalaNumericAnyConversions
--------------------------------------------------------------------------------


### `abstract def doubleValue(): Double`                                     ###

* Definition Classes
  * ScalaNumericAnyConversions

(defined at scala.math.ScalaNumericAnyConversions)


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
         Abstract Value Members From scala.math.ScalaNumericConversions
--------------------------------------------------------------------------------


### `abstract def underlying(): AnyRef`                                      ###

* Definition Classes
  * ScalaNumericConversions → ScalaNumericAnyConversions → ScalaNumber
(defined at scala.math.ScalaNumericConversions)
