
#                              scala.Enumeration                              #

```scala
abstract class Enumeration extends Serializable
```

Defines a finite set of values specific to the enumeration. Typically these
values enumerate all possible forms something can take and provide a lightweight
alternative to case classes.

Each call to a `Value` method adds a new unique value to the enumeration. To be
accessible, these values are usually defined as `val` members of the evaluation.

All values in an enumeration share a common, unique type defined as the `Value`
type member of the enumeration ( `Value` selected on the stable identifier path
of the enumeration instance).

* Self Type
  * Enumeration
* Annotations
  * @ SerialVersionUID ()
* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)

Example:

```scala
object Main extends App {
  object WeekDay extends Enumeration {
    type WeekDay = Value
    val Mon, Tue, Wed, Thu, Fri, Sat, Sun = Value
  }
  import WeekDay._
  def isWorkingDay(d: WeekDay) = ! (d == Sat || d == Sun)
  WeekDay.values filter isWorkingDay foreach println
}
// output:
// Mon
// Tue
// Wed
// Thu
// Fri
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Val extends Value with Serializable`                              ###

A class implementing the scala.Enumeration.Value type. This class can be
overridden to change the enumeration's naming and integer identification
behaviour.

* Attributes
  * protected
* Annotations
  * @ SerialVersionUID ()
* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


### `abstract class Value extends Ordered[Value] with Serializable`          ###

The type of the enumerated values.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


### `class ValueSet extends AbstractSet[Value] with SortedSet[Value] with SortedSetLike[Value, ValueSet] with Serializable` ###

A class for sets of values. Iterating through this set will yield values in
increasing order of their ids.

* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object ValueOrdering extends Ordering[Value]`                           ###

An ordering by id for values of this set

* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


### `object ValueSet extends Serializable`                                   ###

A factory object for value sets

* Source
  * [Enumeration.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Enumeration.scala#L1)


--------------------------------------------------------------------------------
                  Instance Constructors From scala.Enumeration
--------------------------------------------------------------------------------


### `new Enumeration()`                                                      ###

(defined at scala.Enumeration)


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

(defined at scala.Enumeration)


### `final def Value(name: String): Value`                                   ###

Creates a fresh value, part of this enumeration, called `name` .

* name
  * A human-readable name for that value.
* returns
  * Fresh value called `name` .

* Attributes
  * protected

(defined at scala.Enumeration)


### `final def Value: Value`                                                 ###

Creates a fresh value, part of this enumeration.

* Attributes
  * protected

(defined at scala.Enumeration)


### `final def apply(x: Int): Value`                                         ###

The value of this enumeration with given id `x`

(defined at scala.Enumeration)


### `def values: ValueSet`                                                   ###

The values of this enumeration as a set.

(defined at scala.Enumeration)


### `final def withName(s: String): Value`                                   ###

Return a `Value` from this `Enumeration` whose name matches the argument `s` .
The names are determined automatically via reflection.

* s
  * an `Enumeration` name
* returns
  * the `Value` of this `Enumeration` if its name matches `s`

* Exceptions thrown
  * NoSuchElementException if no `Value` with a matching name is in this
     `Enumeration`
(defined at scala.Enumeration)
