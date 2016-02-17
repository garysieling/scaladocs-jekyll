
#                            scala.Enumeration#Val                            #

```scala
class Val extends Value with Serializable
```

A class implementing the scala.Enumeration.Value type. This class can be
overridden to change the enumeration's naming and integer identification
behaviour.

* Attributes
  * protected
* Annotations
  * @ SerialVersionUID ()
* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


--------------------------------------------------------------------------------
                Instance Constructors From scala.Enumeration.Val
--------------------------------------------------------------------------------


### `new Val()`                                                              ###

(defined at scala.Enumeration.Val)


--------------------------------------------------------------------------------
                   Value Members From scala.Enumeration.Value
--------------------------------------------------------------------------------


### `def +(v: Value): ValueSet`                                              ###

Create a ValueSet which contains this value and another one

* Definition Classes
  * Value

(defined at scala.Enumeration.Value)


### `def compare(that: Value): Int`                                          ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Definition Classes
  * Value → Ordered

(defined at scala.Enumeration.Value)


### `def equals(other: Any): Boolean`                                        ###

The equality method for reference types. Default implementation delegates to
 `eq` .

See also `equals` in scala.Any.

* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * Value → AnyRef → Any

(defined at scala.Enumeration.Value)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: Value): Boolean`                                            ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: Value): Boolean`                                           ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: Value): Boolean`                                            ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: Value): Boolean`                                           ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: Value): Int`                                        ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable
(defined at scala.math.Ordered)
