
#                      scala.math.BigDecimal.RoundingMode                      #

```scala
object RoundingMode extends Enumeration
```

* Source
  * [BigDecimal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/BigDecimal.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type RoundingMode = Value`                                              ###


### `class Val extends Value with Serializable`                              ###

A class implementing the scala.Enumeration.Value type. This class can be
overridden to change the enumeration's naming and integer identification
behaviour.

* Attributes
  * protected
* Definition Classes
  * Enumeration
* Annotations
  * @ SerialVersionUID ()


### `abstract class Value extends Ordered[Value] with Serializable`          ###

The type of the enumerated values.

* Definition Classes
  * Enumeration
* Annotations
  * @ SerialVersionUID ()


### `class ValueSet extends AbstractSet[Value] with SortedSet[Value] with SortedSetLike[Value, ValueSet] with Serializable` ###

A class for sets of values. Iterating through this set will yield values in
increasing order of their ids.

* Definition Classes
  * Enumeration


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object ValueOrdering extends Ordering[Value]`                           ###

An ordering by id for values of this set

* Definition Classes
  * Enumeration


### `object ValueSet extends Serializable`                                   ###

A factory object for value sets

* Definition Classes
  * Enumeration


--------------------------------------------------------------------------------
                      Value Members From scala.Enumeration
--------------------------------------------------------------------------------


### `final def Value(i: Int): Value`                                         ###

Creates a fresh value, part of this enumeration, identified by the integer `i` .

* i
  * An integer that identifies this value at run-time. It must be unique amongst
    all values of the enumeration.
* returns
  * Fresh value identified by `i` .

* Attributes
  * protected
* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `final def Value(i: Int, name: String): Value`                           ###

Creates a fresh value, part of this enumeration, called `name` and identified by
the integer `i` .

* i
  * An integer that identifies this value at run-time. It must be unique amongst
    all values of the enumeration.
* name
  * A human-readable name for that value.
* returns
  * Fresh value with the provided identifier `i` and name `name` .

* Attributes
  * protected
* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `final def Value(name: String): Value`                                   ###

Creates a fresh value, part of this enumeration, called `name` .

* name
  * A human-readable name for that value.
* returns
  * Fresh value called `name` .

* Attributes
  * protected
* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `final def Value: Value`                                                 ###

Creates a fresh value, part of this enumeration.

* Attributes
  * protected
* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `final def apply(x: Int): Value`                                         ###

The value of this enumeration with given id `x`

* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `def values: ValueSet`                                                   ###

The values of this enumeration as a set.

* Definition Classes
  * Enumeration

(defined at scala.Enumeration)


### `final def withName(s: String): Value`                                   ###

Return a `Value` from this `Enumeration` whose name matches the argument `s` .
The names are determined automatically via reflection.

* s
  * an `Enumeration` name
* returns
  * the `Value` of this `Enumeration` if its name matches `s`

* Definition Classes
  * Enumeration
* Exceptions thrown
  * NoSuchElementException if no `Value` with a matching name is in this
     `Enumeration`

(defined at scala.Enumeration)


--------------------------------------------------------------------------------
             Value Members From scala.math.BigDecimal.RoundingMode
--------------------------------------------------------------------------------


### `val CEILING: Value`                                                     ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val DOWN: Value`                                                        ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val FLOOR: Value`                                                       ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val HALF_DOWN: Value`                                                   ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val HALF_EVEN: Value`                                                   ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val HALF_UP: Value`                                                     ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val UNNECESSARY: Value`                                                 ###

(defined at scala.math.BigDecimal.RoundingMode)


### `val UP: Value`                                                          ###
(defined at scala.math.BigDecimal.RoundingMode)
