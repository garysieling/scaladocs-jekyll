
#                                 scala.AnyVal                                 #

```scala
abstract class AnyVal extends Any
```

 `AnyVal` is the root class of all _value types_ , which describe values not
implemented as objects in the underlying host system. Value classes are
specified in Scala Language Specification, section 12.2.

The standard implementation includes nine `AnyVal` subtypes:

scala.Double, scala.Float, scala.Long, scala.Int, scala.Char, scala.Short, and
scala.Byte are the _numeric value types_ .

scala.Unit and scala.Boolean are the _non-numeric value types_ .

Other groupings:

* The _subrange types_ are scala.Byte, scala.Short, and scala.Char.
* The _integer types_ include the subrange types as well as scala.Int and
   scala.Long.
* The _floating point types_ are scala.Float and scala.Double.

Prior to Scala 2.10, `AnyVal` was a sealed trait. Beginning with Scala 2.10,
however, it is possible to define a subclass of `AnyVal` called a _user-defined
value class_ which is treated specially by the compiler. Properly-defined user
value classes provide a way to improve performance on user-defined types by
avoiding object allocation at runtime, and by replacing virtual method
invocations with static method invocations.

User-defined value classes which avoid object allocation...

* must have a single `val` parameter that is the underlying runtime
   representation.
* can define `def` s, but no `val` s, `var` s, or nested `traits` s, `class` es
   or `object` s.
* typically extend no other trait apart from `AnyVal` .
* cannot be used in type tests or pattern matching.
* may not override `equals` or `hashCode` methods.

A minimal example:

```scala
class Wrapper(val underlying: Int) extends AnyVal {
  def foo: Wrapper = new Wrapper(underlying * 19)
}
```

It's important to note that user-defined value classes are limited, and in some
circumstances, still must allocate a value class instance at runtime. These
limitations and circumstances are explained in greater detail in the
[Value Classes and Universal Traits](http://docs.scala-lang.org/overviews/core/value-classes.html).

* Source
  * [AnyVal.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/AnyVal.scala#L1)


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
                    Instance Constructors From scala.AnyVal
--------------------------------------------------------------------------------


### `new AnyVal()`                                                           ###
(defined at scala.AnyVal)
