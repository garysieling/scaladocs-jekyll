
#                        scala.runtime.FractionalProxy                        #

```scala
trait FractionalProxy[T] extends ScalaNumberProxy[T] with RangedProxy[T]
```

* Source
  * [ScalaNumberProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/ScalaNumberProxy.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type ResultWithoutStep = Partial[T, NumericRange[T]]`                   ###

In order to supply predictable ranges, we require an Integral[T] which provides
us with discrete operations on the (otherwise fractional) T. See
Numeric.DoubleAsIfIntegral for an example.

* Definition Classes
  * FractionalProxy → RangedProxy


--------------------------------------------------------------------------------
                    Concrete Value Members From scala.Proxy
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

Compares the receiver object ( `this` ) with the argument object ( `that` ) for
equivalence.

Any implementation of this method should be an
[equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) :

* It is reflexive: for any instance `x` of type `Any` , `x.equals(x)` should
   return `true` .
* It is symmetric: for any instances `x` and `y` of type `Any` , `x.equals(y)`
   should return `true` if and only if `y.equals(x)` returns `true` .
* It is transitive: for any instances `x` , `y` , and `z` of type `Any` if
    `x.equals(y)` returns `true` and `y.equals(z)` returns `true` , then
    `x.equals(z)` should return `true` .

If you override this method, you should verify that your implementation remains
an equivalence relation. Additionally, when overriding this method it is usually
necessary to override `hashCode` to ensure that objects which are "equal" (
 `o1.equals(o2)` returns `true` ) hash to the same scala.Int. (
 `o1.hashCode.equals(o2.hashCode)` ).

* that
  * the object to compare against this object for equality.
* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * Proxy → Any

(defined at scala.Proxy)


--------------------------------------------------------------------------------
                 Concrete Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: T): Boolean`                                                ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: T): Boolean`                                               ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: T): Boolean`                                                ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: T): Boolean`                                               ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: T): Int`                                            ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable

(defined at scala.math.Ordered)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.math.ScalaNumericAnyConversions
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
           Concrete Value Members From scala.runtime.FractionalProxy
--------------------------------------------------------------------------------


### `def to(end: T): ResultWithoutStep`                                      ###

* Definition Classes
  * FractionalProxy → RangedProxy

(defined at scala.runtime.FractionalProxy)


### `def to(end: T, step: T): Inclusive[T]`                                  ###

* Definition Classes
  * FractionalProxy → RangedProxy

(defined at scala.runtime.FractionalProxy)


### `def until(end: T): ResultWithoutStep`                                   ###

* Definition Classes
  * FractionalProxy → RangedProxy

(defined at scala.runtime.FractionalProxy)


### `def until(end: T, step: T): Exclusive[T]`                               ###

* Definition Classes
  * FractionalProxy → RangedProxy

(defined at scala.runtime.FractionalProxy)


--------------------------------------------------------------------------------
             Concrete Value Members From scala.runtime.OrderedProxy
--------------------------------------------------------------------------------


### `def compare(y: T): Int`                                                 ###

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
           Concrete Value Members From scala.runtime.ScalaNumberProxy
--------------------------------------------------------------------------------


### `def max(that: T): T`                                                    ###

Returns `this` if `this > that` or `that` otherwise.

* Definition Classes
  * ScalaNumberProxy

(defined at scala.runtime.ScalaNumberProxy)


### `def min(that: T): T`                                                    ###

Returns `this` if `this < that` or `that` otherwise.

* Definition Classes
  * ScalaNumberProxy
(defined at scala.runtime.ScalaNumberProxy)
