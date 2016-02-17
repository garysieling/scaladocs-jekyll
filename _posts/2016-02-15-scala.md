
#                                    scala                                    #

```scala
package scala
```

Core Scala types. They are always available without an explicit import.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/package.scala#L1)


--------------------------------------------------------------------------------

--------------------------------------------------------------------------------


### `class AnyRef extends Any`                                               ###

Class `AnyRef` is the root class of all _reference types_ . All types except the
value types descend from this class.


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object Responder extends Serializable`                                  ###

This object contains utility methods to build responders.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This object will be removed
* Source
  * [Responder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Responder.scala#L1)
* Version
  * 1.0
* Since
  * 2.1
* See also
  * class Responder


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type ::[A] = scala.collection.immutable.::[A]`                          ###


### `type AbstractMethodError = java.lang.AbstractMethodError`               ###


### `abstract class Any`                                                     ###

Class `Any` is the root of the Scala class hierarchy. Every class in a Scala
execution environment inherits directly or indirectly from this class.

Starting with Scala 2.10 it is possible to directly extend `Any` using _
universal traits_ . A _universal trait_ is a trait that extends `Any` , only has
 `def` s as members, and does no initialization.

The main use case for universal traits is to allow basic inheritance of methods
for value classes. For example,

```scala
trait Printable extends Any {
  def print(): Unit = println(this)
}
class Wrapper(val underlying: Int) extends AnyVal with Printable

val w = new Wrapper(3)
w.print()
```

See the
[Value Classes and Universal Traits](http://docs.scala-lang.org/overviews/core/value-classes.html)
for more details on the interplay of universal traits and value classes.


### `abstract class AnyVal extends Any`                                      ###

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


### `trait App extends DelayedInit`                                          ###

The `App` trait can be used to quickly turn objects into executable programs.
Here is an example:

```scala
object Main extends App {
  Console.println("Hello World: " + (args mkString ", "))
}
```

Here, object `Main` inherits the `main` method of `App` .

 `args` returns the current command line arguments as an array.

### Caveats

 * _It should be noted that this trait is implemented using the DelayedInit
functionality, which means that fields of the object will not have been
initialized before the main method has been executed._*

It should also be noted that the `main` method should not be overridden: the
whole class body becomes the “main method”.

Future versions of this trait will no longer extend `DelayedInit` .

* Source
  * [App.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/App.scala#L1)
* Version
  * 2.1, 15/02/2011


### `final class Array[T] extends java.io.Serializable with java.lang.Cloneable` ###

Arrays are mutable, indexed collections of values. `Array[T]` is Scala's
representation for Java's `T[]` .

```scala
val numbers = Array(1, 2, 3, 4)
val first = numbers(0) // read the first element
numbers(3) = 100 // replace the 4th array element with 100
val biggerNumbers = numbers.map(_ * 2) // multiply all numbers by two
```

Arrays make use of two common pieces of Scala syntactic sugar, shown on lines 2
and 3 of the above example code. Line 2 is translated into a call to
 `apply(Int)` , while line 3 is translated into a call to `update(Int, T)` .

Two implicit conversions exist in scala.Predef that are frequently applied to
arrays: a conversion to scala.collection.mutable.ArrayOps (shown on line 4 of
the example above) and a conversion to scala.collection.mutable.WrappedArray (a
subtype of scala.collection.Seq). Both types make available many of the standard
operations found in the Scala collections API. The conversion to `ArrayOps` is
temporary, as all operations defined on `ArrayOps` return an `Array` , while the
conversion to `WrappedArray` is permanent as all operations return a
 `WrappedArray` .

The conversion to `ArrayOps` takes priority over the conversion to
 `WrappedArray` . For instance, consider the following code:

```scala
val arr = Array(1, 2, 3)
val arrReversed = arr.reverse
val seqReversed : Seq[Int] = arr.reverse
```

Value `arrReversed` will be of type `Array[Int]` , with an implicit conversion
to `ArrayOps` occurring to perform the `reverse` operation. The value of
 `seqReversed` , on the other hand, will be computed by converting to
 `WrappedArray` first and invoking the variant of `reverse` that returns another
 `WrappedArray` .

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)
* Version
  * 1.0
* See also
  * ["The Scala 2.8 Collections' API"](http://docs.scala-lang.org/overviews/collections/arrays.html)
    section on `Array` by Martin Odersky for more information.
    ["Scala 2.8 Arrays"](http://docs.scala-lang.org/sips/completed/scala-2-8-arrays.html)
    the Scala Improvement Document detailing arrays since Scala 2.8.
    [Scala Language Specification](http://www.scala-lang.org/files/archive/spec/2.11/),
    for in-depth information on the transformations the Scala compiler makes on
    Arrays (Sections 6.6 and 6.15 respectively.)


### `type ArrayIndexOutOfBoundsException = java.lang.ArrayIndexOutOfBoundsException` ###


### `type BigDecimal = scala.math.BigDecimal`                                ###


### `type BigInt = scala.math.BigInt`                                        ###


### `abstract final class Boolean extends AnyVal`                            ###

 `Boolean` (equivalent to Java's `boolean` primitive type) is a subtype of
scala.AnyVal. Instances of `Boolean` are not represented by an object in the
underlying runtime system.

There is an implicit conversion from scala.Boolean => scala.runtime.RichBoolean
which provides useful non-primitive operations.

* Source
  * [Boolean.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Boolean.scala#L1)


### `type BufferedIterator[+A] = scala.collection.BufferedIterator[A]`       ###


### `abstract final class Byte extends AnyVal`                               ###

 `Byte` , a 8-bit signed integer (equivalent to Java's `byte` primitive type) is
a subtype of scala.AnyVal. Instances of `Byte` are not represented by an object
in the underlying runtime system.

There is an implicit conversion from scala.Byte => scala.runtime.RichByte which
provides useful non-primitive operations.

* Source
  * [Byte.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Byte.scala#L1)


### `abstract final class Char extends AnyVal`                               ###

 `Char` , a 16-bit unsigned integer (equivalent to Java's `char` primitive type)
is a subtype of scala.AnyVal. Instances of `Char` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Char => scala.runtime.RichChar which
provides useful non-primitive operations.

* Source
  * [Char.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Char.scala#L1)


### `type ClassCastException = java.lang.ClassCastException`                 ###


### `trait Cloneable extends java.lang.Cloneable`                            ###

Classes extending this trait are cloneable across platforms (Java,.NET).

* Source
  * [Cloneable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Cloneable.scala#L1)


### `trait DelayedInit extends AnyRef`                                       ###

Classes and objects (but note, not traits) inheriting the `DelayedInit` marker
trait will have their initialization code rewritten as follows: `code` becomes
 `delayedInit(code)` .

Initialization code comprises all statements and all value definitions that are
executed during initialization.

Example:

```scala
trait Helper extends DelayedInit {
  def delayedInit(body: => Unit) = {
    println("dummy text, printed before initialization of C")
    body // evaluates the initialization code of C
  }
}

class C extends Helper {
  println("this is the initialization code of C")
}

object Test extends App {
  val c = new C
}
```

Should result in the following being printed:

```scala
dummy text, printed before initialization of C
this is the initialization code of C
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ DelayedInit semantics can be surprising. Support
    for `App` will continue. See the release notes for more details:
    https://github.com/scala/scala/releases/tag/v2.11.0-RC1
* Source
  * [DelayedInit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/DelayedInit.scala#L1)
* See also
  * "Delayed Initialization" subsection of the Scala Language Specification
    (section 5.1)


### `abstract final class Double extends AnyVal`                             ###

 `Double` , a 64-bit IEEE-754 floating point number (equivalent to Java's
 `double` primitive type) is a subtype of scala.AnyVal. Instances of `Double`
are not represented by an object in the underlying runtime system.

There is an implicit conversion from scala.Double => scala.runtime.RichDouble
which provides useful non-primitive operations.

* Source
  * [Double.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Double.scala#L1)


### `trait Dynamic extends Any`                                              ###

A marker trait that enables dynamic invocations. Instances `x` of this trait
allow method invocations `x.meth(args)` for arbitrary method names `meth` and
argument lists `args` as well as field accesses `x.field` for arbitrary field
names `field` .

If a call is not natively supported by `x` (i.e. if type checking fails), it is
rewritten according to the following rules:

```scala
foo.method("blah")      ~~> foo.applyDynamic("method")("blah")
foo.method(x = "blah")  ~~> foo.applyDynamicNamed("method")(("x", "blah"))
foo.method(x = 1, 2)    ~~> foo.applyDynamicNamed("method")(("x", 1), ("", 2))
foo.field           ~~> foo.selectDynamic("field")
foo.varia = 10      ~~> foo.updateDynamic("varia")(10)
foo.arr(10) = 13    ~~> foo.selectDynamic("arr").update(10, 13)
foo.arr(10)         ~~> foo.applyDynamic("arr")(10)
```

As of Scala 2.10, defining direct or indirect subclasses of this trait is only
possible if the language feature `dynamics` is enabled.

* Source
  * [Dynamic.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Dynamic.scala#L1)


### `type Either[+A, +B] = scala.util.Either[A, B]`                          ###


### `abstract class Enumeration extends Serializable`                        ###

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


### `trait Equals extends Any`                                               ###

An interface containing operations for equality. The only method not already
present in class `AnyRef` is `canEqual` .

* Source
  * [Equals.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Equals.scala#L1)


### `type Equiv[T] = scala.math.Equiv[T]`                                    ###


### `type Error = java.lang.Error`                                           ###


### `type Exception = java.lang.Exception`                                   ###


### `class FallbackArrayBuilding extends AnyRef`                             ###

Contains a fallback builder for arrays when the element type does not have a
class tag. In that case a generic array is built.

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)


### `abstract final class Float extends AnyVal`                              ###

 `Float` , a 32-bit IEEE-754 floating point number (equivalent to Java's
 `float` primitive type) is a subtype of scala.AnyVal. Instances of `Float` are
not represented by an object in the underlying runtime system.

There is an implicit conversion from scala.Float => scala.runtime.RichFloat
which provides useful non-primitive operations.

* Source
  * [Float.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Float.scala#L1)


### `type Fractional[T] = scala.math.Fractional[T]`                          ###


### `trait Function0[+R] extends AnyRef`                                     ###

A function of 0 parameters.

In the following example, the definition of javaVersion is a shorthand for the
anonymous class definition anonfun0:

```scala
object Main extends App {
   val javaVersion = () => sys.props("java.version")

   val anonfun0 = new Function0[String] {
     def apply(): String = sys.props("java.version")
   }
   assert(javaVersion() == anonfun0())
}
```

* Self Type
  * () ⇒ R
* Source
  * [Function0.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function0.scala#L1)


### `trait Function1[-T1, +R] extends AnyRef`                                ###

A function of 1 parameter.

In the following example, the definition of succ is a shorthand for the
anonymous class definition anonfun1:

```scala
object Main extends App {
   val succ = (x: Int) => x + 1
   val anonfun1 = new Function1[Int, Int] {
     def apply(x: Int): Int = x + 1
   }
   assert(succ(0) == anonfun1(0))
}
```

Note that the difference between `Function1` and scala.PartialFunction is that
the latter can specify inputs which it will not handle.

* Self Type
  * (T1) ⇒ R
* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Function1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function1.scala#L1)


### `trait Function10[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, +R] extends AnyRef` ###

A function of 10 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10) ⇒ R
* Source
  * [Function10.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function10.scala#L1)


### `trait Function11[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, +R] extends AnyRef` ###

A function of 11 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11) ⇒ R
* Source
  * [Function11.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function11.scala#L1)


### `trait Function12[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, +R] extends AnyRef` ###

A function of 12 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12) ⇒ R
* Source
  * [Function12.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function12.scala#L1)


### `trait Function13[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, +R] extends AnyRef` ###

A function of 13 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13) ⇒ R
* Source
  * [Function13.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function13.scala#L1)


### `trait Function14[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, +R] extends AnyRef` ###

A function of 14 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14) ⇒ R
* Source
  * [Function14.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function14.scala#L1)


### `trait Function15[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, +R] extends AnyRef` ###

A function of 15 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15) ⇒ R
* Source
  * [Function15.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function15.scala#L1)


### `trait Function16[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, +R] extends AnyRef` ###

A function of 16 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16) ⇒ R
* Source
  * [Function16.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function16.scala#L1)


### `trait Function17[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, +R] extends AnyRef` ###

A function of 17 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17)
    ⇒ R
* Source
  * [Function17.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function17.scala#L1)


### `trait Function18[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, +R] extends AnyRef` ###

A function of 18 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17,
    T18) ⇒ R
* Source
  * [Function18.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function18.scala#L1)


### `trait Function19[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, -T19, +R] extends AnyRef` ###

A function of 19 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17,
    T18, T19) ⇒ R
* Source
  * [Function19.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function19.scala#L1)


### `trait Function2[-T1, -T2, +R] extends AnyRef`                           ###

A function of 2 parameters.

In the following example, the definition of max is a shorthand for the anonymous
class definition anonfun2:

```scala
object Main extends App {
   val max = (x: Int, y: Int) => if (x < y) y else x

   val anonfun2 = new Function2[Int, Int, Int] {
     def apply(x: Int, y: Int): Int = if (x < y) y else x
   }
   assert(max(0, 1) == anonfun2(0, 1))
}
```

* Self Type
  * (T1, T2) ⇒ R
* Source
  * [Function2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function2.scala#L1)


### `trait Function20[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, -T19, -T20, +R] extends AnyRef` ###

A function of 20 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17,
    T18, T19, T20) ⇒ R
* Source
  * [Function20.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function20.scala#L1)


### `trait Function21[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, -T19, -T20, -T21, +R] extends AnyRef` ###

A function of 21 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17,
    T18, T19, T20, T21) ⇒ R
* Source
  * [Function21.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function21.scala#L1)


### `trait Function22[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, -T10, -T11, -T12, -T13, -T14, -T15, -T16, -T17, -T18, -T19, -T20, -T21, -T22, +R] extends AnyRef` ###

A function of 22 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17,
    T18, T19, T20, T21, T22) ⇒ R
* Source
  * [Function22.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function22.scala#L1)


### `trait Function3[-T1, -T2, -T3, +R] extends AnyRef`                      ###

A function of 3 parameters.

* Self Type
  * (T1, T2, T3) ⇒ R
* Source
  * [Function3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function3.scala#L1)


### `trait Function4[-T1, -T2, -T3, -T4, +R] extends AnyRef`                 ###

A function of 4 parameters.

* Self Type
  * (T1, T2, T3, T4) ⇒ R
* Source
  * [Function4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function4.scala#L1)


### `trait Function5[-T1, -T2, -T3, -T4, -T5, +R] extends AnyRef`            ###

A function of 5 parameters.

* Self Type
  * (T1, T2, T3, T4, T5) ⇒ R
* Source
  * [Function5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function5.scala#L1)


### `trait Function6[-T1, -T2, -T3, -T4, -T5, -T6, +R] extends AnyRef`       ###

A function of 6 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6) ⇒ R
* Source
  * [Function6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function6.scala#L1)


### `trait Function7[-T1, -T2, -T3, -T4, -T5, -T6, -T7, +R] extends AnyRef`  ###

A function of 7 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7) ⇒ R
* Source
  * [Function7.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function7.scala#L1)


### `trait Function8[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, +R] extends AnyRef` ###

A function of 8 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8) ⇒ R
* Source
  * [Function8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function8.scala#L1)


### `trait Function9[-T1, -T2, -T3, -T4, -T5, -T6, -T7, -T8, -T9, +R] extends AnyRef` ###

A function of 9 parameters.

* Self Type
  * (T1, T2, T3, T4, T5, T6, T7, T8, T9) ⇒ R
* Source
  * [Function9.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function9.scala#L1)


### `type IllegalArgumentException = java.lang.IllegalArgumentException`     ###


### `trait Immutable extends AnyRef`                                         ###

A marker trait for all immutable datastructures such as immutable collections.

* Source
  * [Immutable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Immutable.scala#L1)
* Since
  * 2.8


### `type IndexOutOfBoundsException = java.lang.IndexOutOfBoundsException`   ###


### `type IndexedSeq[+A] = scala.collection.IndexedSeq[A]`                   ###


### `abstract final class Int extends AnyVal`                                ###

 `Int` , a 32-bit signed integer (equivalent to Java's `int` primitive type) is
a subtype of scala.AnyVal. Instances of `Int` are not represented by an object
in the underlying runtime system.

There is an implicit conversion from scala.Int => scala.runtime.RichInt which
provides useful non-primitive operations.

* Source
  * [Int.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Int.scala#L1)


### `type Integral[T] = scala.math.Integral[T]`                              ###


### `type InterruptedException = java.lang.InterruptedException`             ###


### `type Iterable[+A] = scala.collection.Iterable[A]`                       ###


### `type Iterator[+A] = scala.collection.Iterator[A]`                       ###


### `type Left[+A, +B] = scala.util.Left[A, B]`                              ###


### `type List[+A] = scala.collection.immutable.List[A]`                     ###


### `abstract final class Long extends AnyVal`                               ###

 `Long` , a 64-bit signed integer (equivalent to Java's `long` primitive type)
is a subtype of scala.AnyVal. Instances of `Long` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Long => scala.runtime.RichLong which
provides useful non-primitive operations.

* Source
  * [Long.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Long.scala#L1)


### `final class MatchError extends RuntimeException`                        ###

This class implements errors which are thrown whenever an object doesn't match
any pattern of a pattern matching expression.

* Source
  * [MatchError.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/MatchError.scala#L1)
* Version
  * 1.1, 05/03/2004
* Since
  * 2.0


### `trait Mutable extends AnyRef`                                           ###

A marker trait for mutable data structures such as mutable collections

* Source
  * [Mutable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Mutable.scala#L1)
* Since
  * 2.8


### `type NoSuchElementException = java.util.NoSuchElementException`         ###


### `final class NotImplementedError extends Error`                          ###

Throwing this exception can be a temporary replacement for a method body that
remains to be implemented. For instance, the exception is thrown by
 `Predef.???` .

* Source
  * [NotImplementedError.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/NotImplementedError.scala#L1)


### `trait NotNull extends Any`                                              ###

A marker trait for things that are not allowed to be null

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This trait will be removed
* Source
  * [NotNull.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/NotNull.scala#L1)
* Since
  * 2.5


### `abstract final class Nothing extends Any`                               ###

 `Nothing` is - together with scala.Null - at the bottom of Scala's type
hierarchy.

 `Nothing` is a subtype of every other type (including scala.Null); there exist
 _no instances_ of this type. Although type `Nothing` is uninhabited, it is
nevertheless useful in several ways. For instance, the Scala library defines a
value scala.collection.immutable.Nil of type `List[Nothing]` . Because lists are
covariant in Scala, this makes scala.collection.immutable.Nil an instance of
 `List[T]` , for any element of type `T` .

Another usage for Nothing is the return type for methods which never return
normally. One example is method error in scala.sys, which always throws an
exception.


### `abstract final class Null extends AnyRef`                               ###

 `Null` is - together with scala.Nothing - at the bottom of the Scala type
hierarchy.

 `Null` is a subtype of all reference types; its only instance is the `null`
reference. Since `Null` is not a subtype of value types, `null` is not a member
of any such type. For instance, it is not possible to assign `null` to a
variable of type scala.Int.


### `type NullPointerException = java.lang.NullPointerException`             ###


### `type NumberFormatException = java.lang.NumberFormatException`           ###


### `type Numeric[T] = scala.math.Numeric[T]`                                ###


### `sealed abstract class Option[+A] extends Product with Serializable`     ###

Represents optional values. Instances of `Option` are either an instance of
scala.Some or the object `None` .

The most idiomatic way to use an scala.Option instance is to treat it as a
collection or monad and use `map` , `flatMap` , `filter` , or `foreach` :

```scala
val name: Option[String] = request getParameter "name"
val upper = name map { _.trim } filter { _.length != 0 } map { _.toUpperCase }
println(upper getOrElse "")
```

Note that this is equivalent to

```scala
val upper = for {
  name <- request getParameter "name"
  trimmed <- Some(name.trim)
  upper <- Some(trimmed.toUpperCase) if trimmed.length != 0
} yield upper
println(upper getOrElse "")
```

Because of how for comprehension works, if `None` is returned from
 `request.getParameter` , the entire expression results in `None`

This allows for sophisticated chaining of scala.Option values without having to
check for the existence of a value.

A less-idiomatic way to use scala.Option values is via pattern matching:

```scala
val nameMaybe = request getParameter "name"
nameMaybe match {
  case Some(name) =>
    println(name.trim.toUppercase)
  case None =>
    println("No name value")
}
```

* Self Type
  * Option [A]
* Annotations
  * @ SerialVersionUID ()
* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)
* Version
  * 1.1, 16/01/2007
* Note
  * Many of the methods in here are duplicative with those in the Traversable
    hierarchy, but they are duplicated for a reason: the implicit conversion
    tends to leave one with an Iterable in situations where one could have
    retained an Option.


### `type Ordered[T] = scala.math.Ordered[T]`                                ###


### `type Ordering[T] = scala.math.Ordering[T]`                              ###


### `trait PartialFunction[-A, +B] extends (A) ⇒ B`                          ###

A partial function of type `PartialFunction[A, B]` is a unary function where the
domain does not necessarily include all values of type `A` . The function
 `isDefinedAt` allows to test dynamically if a value is in the domain of the
function.

Even if `isDefinedAt` returns true for an `a: A` , calling `apply(a)` may still
throw an exception, so the following code is legal:

```scala
val f: PartialFunction[Int, Any] = { case _ => 1/0 }
```

It is the responsibility of the caller to call `isDefinedAt` before calling
 `apply` , because if `isDefinedAt` is false, it is not guaranteed `apply` will
throw an exception to indicate an error condition. If an exception is not
thrown, evaluation may result in an arbitrary value.

The main distinction between `PartialFunction` and scala.Function1 is that the
user of a `PartialFunction` may choose to do something different with input that
is declared to be outside its domain. For example:

```scala
val sample = 1 to 10
val isEven: PartialFunction[Int, String] = {
  case x if x % 2 == 0 => x+" is even"
}

// the method collect can use isDefinedAt to select which members to collect
val evenNumbers = sample collect isEven

val isOdd: PartialFunction[Int, String] = {
  case x if x % 2 == 1 => x+" is odd"
}

// the method orElse allows chaining another partial function to handle
// input outside the declared domain
val numbers = sample map (isEven orElse isOdd)
```

* Self Type
  * PartialFunction [A, B]
* Source
  * [PartialFunction.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/PartialFunction.scala#L1)
* Version
  * 1.0, 16/07/2003


### `type PartialOrdering[T] = scala.math.PartialOrdering[T]`                ###


### `type PartiallyOrdered[T] = scala.math.PartiallyOrdered[T]`              ###


### `trait Product extends Equals`                                           ###

Base trait for all products, which in the standard library include at least
scala.Product1 through scala.Product22 and therefore also their subclasses
scala.Tuple1 through scala.Tuple22. In addition, all case classes implement
 `Product` with synthetically generated methods.

* Source
  * [Product.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product.scala#L1)
* Version
  * 1.0
* Since
  * 2.3


### `trait Product1[+T1] extends Product`                                    ###

Product1 is a cartesian product of 1 component.

* Source
  * [Product1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product1.scala#L1)
* Since
  * 2.3


### `trait Product10[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10] extends Product` ###

Product10 is a cartesian product of 10 components.

* Source
  * [Product10.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product10.scala#L1)
* Since
  * 2.3


### `trait Product11[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11] extends Product` ###

Product11 is a cartesian product of 11 components.

* Source
  * [Product11.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product11.scala#L1)
* Since
  * 2.3


### `trait Product12[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12] extends Product` ###

Product12 is a cartesian product of 12 components.

* Source
  * [Product12.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product12.scala#L1)
* Since
  * 2.3


### `trait Product13[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13] extends Product` ###

Product13 is a cartesian product of 13 components.

* Source
  * [Product13.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product13.scala#L1)
* Since
  * 2.3


### `trait Product14[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14] extends Product` ###

Product14 is a cartesian product of 14 components.

* Source
  * [Product14.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product14.scala#L1)
* Since
  * 2.3


### `trait Product15[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15] extends Product` ###

Product15 is a cartesian product of 15 components.

* Source
  * [Product15.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product15.scala#L1)
* Since
  * 2.3


### `trait Product16[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16] extends Product` ###

Product16 is a cartesian product of 16 components.

* Source
  * [Product16.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product16.scala#L1)
* Since
  * 2.3


### `trait Product17[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17] extends Product` ###

Product17 is a cartesian product of 17 components.

* Source
  * [Product17.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product17.scala#L1)
* Since
  * 2.3


### `trait Product18[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18] extends Product` ###

Product18 is a cartesian product of 18 components.

* Source
  * [Product18.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product18.scala#L1)
* Since
  * 2.3


### `trait Product19[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19] extends Product` ###

Product19 is a cartesian product of 19 components.

* Source
  * [Product19.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product19.scala#L1)
* Since
  * 2.3


### `trait Product2[+T1, +T2] extends Product`                               ###

Product2 is a cartesian product of 2 components.

* Source
  * [Product2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product2.scala#L1)
* Since
  * 2.3


### `trait Product20[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20] extends Product` ###

Product20 is a cartesian product of 20 components.

* Source
  * [Product20.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product20.scala#L1)
* Since
  * 2.3


### `trait Product21[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20, +T21] extends Product` ###

Product21 is a cartesian product of 21 components.

* Source
  * [Product21.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product21.scala#L1)
* Since
  * 2.3


### `trait Product22[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20, +T21, +T22] extends Product` ###

Product22 is a cartesian product of 22 components.

* Source
  * [Product22.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product22.scala#L1)
* Since
  * 2.3


### `trait Product3[+T1, +T2, +T3] extends Product`                          ###

Product3 is a cartesian product of 3 components.

* Source
  * [Product3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product3.scala#L1)
* Since
  * 2.3


### `trait Product4[+T1, +T2, +T3, +T4] extends Product`                     ###

Product4 is a cartesian product of 4 components.

* Source
  * [Product4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product4.scala#L1)
* Since
  * 2.3


### `trait Product5[+T1, +T2, +T3, +T4, +T5] extends Product`                ###

Product5 is a cartesian product of 5 components.

* Source
  * [Product5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product5.scala#L1)
* Since
  * 2.3


### `trait Product6[+T1, +T2, +T3, +T4, +T5, +T6] extends Product`           ###

Product6 is a cartesian product of 6 components.

* Source
  * [Product6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product6.scala#L1)
* Since
  * 2.3


### `trait Product7[+T1, +T2, +T3, +T4, +T5, +T6, +T7] extends Product`      ###

Product7 is a cartesian product of 7 components.

* Source
  * [Product7.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product7.scala#L1)
* Since
  * 2.3


### `trait Product8[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8] extends Product` ###

Product8 is a cartesian product of 8 components.

* Source
  * [Product8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product8.scala#L1)
* Since
  * 2.3


### `trait Product9[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9] extends Product` ###

Product9 is a cartesian product of 9 components.

* Source
  * [Product9.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product9.scala#L1)
* Since
  * 2.3


### `trait Proxy extends Any`                                                ###

This class implements a simple proxy that forwards all calls to the public,
non-final methods defined in class `Any` to another object self. Those methods
are:

```scala
def hashCode(): Int
def equals(other: Any): Boolean
def toString(): String
```

 *Note:* forwarding methods in this way will most likely create an asymmetric
equals method, which is not generally recommended.

* Source
  * [Proxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Proxy.scala#L1)
* Version
  * 1.0, 26/04/2004


### `type Range = scala.collection.immutable.Range`                          ###


### `abstract class Responder[+A] extends Serializable`                      ###

Instances of responder are the building blocks of small programs written in
continuation passing style. By using responder classes in for comprehensions,
one can embed domain-specific languages in Scala while giving the impression
that programs in these DSLs are written in direct style.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This class will be removed
* Source
  * [Responder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Responder.scala#L1)
* Version
  * 1.0
* Since
  * 2.1


### `type Right[+A, +B] = scala.util.Right[A, B]`                            ###


### `type RuntimeException = java.lang.RuntimeException`                     ###


### `case class ScalaReflectionException(msg: String) extends Exception with Product with Serializable` ###

An exception that indicates an error during Scala reflection

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/package.scala#L1)


### `type Seq[+A] = scala.collection.Seq[A]`                                 ###


### `class SerialVersionUID extends Annotation with ClassfileAnnotation`     ###

Annotation for specifying the `static SerialVersionUID` field of a serializable
class.

* Source
  * [SerialVersionUID.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/SerialVersionUID.scala#L1)


### `trait Serializable extends java.io.Serializable`                        ###

Classes extending this trait are serializable across platforms (Java,.NET).

* Source
  * [Serializable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Serializable.scala#L1)


### `abstract final class Short extends AnyVal`                              ###

 `Short` , a 16-bit signed integer (equivalent to Java's `short` primitive type)
is a subtype of scala.AnyVal. Instances of `Short` are not represented by an
object in the underlying runtime system.

There is an implicit conversion from scala.Short => scala.runtime.RichShort
which provides useful non-primitive operations.

* Source
  * [Short.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Short.scala#L1)


### `final case class Some[+A](x: A) extends Option[A] with Product with Serializable` ###

Class `Some[A]` represents existing values of type `A` .

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)
* Version
  * 1.0, 16/07/2003


### `trait Specializable extends AnyRef`                                     ###

A common supertype for companions of specializable types. Should not be extended
in user code.

* Source
  * [Specializable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Specializable.scala#L1)


### `type Stream[+A] = scala.collection.immutable.Stream[A]`                 ###


### `type StringBuilder = scala.collection.mutable.StringBuilder`            ###


### `case class StringContext(parts: String*) extends Product with Serializable` ###

This class provides the basic mechanism to do String Interpolation. String
Interpolation allows users to embed variable references directly in *processed*
string literals. Here's an example:

```scala
val name = "James"
println(s"Hello, $name")  // Hello, James
```

Any processed string literal is rewritten as an instantiation and method call
against this class. For example:

```scala
s"Hello, $name"
```

is rewritten to be:

```scala
StringContext("Hello, ", "").s(name)
```

By default, this class provides the `raw` , `s` and `f` methods as available
interpolators.

To provide your own string interpolator, create an implicit class which adds a
method to `StringContext` . Here's an example:

```scala
implicit class JsonHelper(private val sc: StringContext) extends AnyVal {
  def json(args: Any*): JSONObject = ...
}
val x: JSONObject = json"{ a: $a }"
```

Here the `JsonHelper` extension class implicitly adds the `json` method to
 `StringContext` which can be used for `json` string literals.

* parts
  * The parts that make up the interpolated string, without the expressions that
    get inserted by interpolation.

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)
* Since
  * 2.10.0


### `type StringIndexOutOfBoundsException = java.lang.StringIndexOutOfBoundsException` ###


### `final class Symbol extends Serializable`                                ###

This class provides a simple way to get unique objects for equal strings. Since
symbols are interned, they can be compared using reference equality. Instances
of `Symbol` can be created easily with Scala's built-in quote mechanism.

For instance, the [Scala](http://scala-lang.org/#_top) term `'mysym` will invoke
the constructor of the `Symbol` class in the following way: `Symbol("mysym")` .

* Source
  * [Symbol.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Symbol.scala#L1)
* Version
  * 1.8


### `type Throwable = java.lang.Throwable`                                   ###


### `type Traversable[+A] = scala.collection.Traversable[A]`                 ###


### `type TraversableOnce[+A] = scala.collection.TraversableOnce[A]`         ###


### `case class Tuple1[+T1](_1: T1) extends Product1[T1] with Product with Serializable` ###

A tuple of 1 elements; the canonical representation of a scala.Product1.

* _1
  * Element 1 of this Tuple1

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple1.scala#L1)


### `case class Tuple10[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10) extends Product10[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10] with Product with Serializable` ###

A tuple of 10 elements; the canonical representation of a scala.Product10.

* _1
  * Element 1 of this Tuple10
* _2
  * Element 2 of this Tuple10
* _3
  * Element 3 of this Tuple10
* _4
  * Element 4 of this Tuple10
* _5
  * Element 5 of this Tuple10
* _6
  * Element 6 of this Tuple10
* _7
  * Element 7 of this Tuple10
* _8
  * Element 8 of this Tuple10
* _9
  * Element 9 of this Tuple10
* _10
  * Element 10 of this Tuple10

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple10.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple10.scala#L1)


### `case class Tuple11[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11) extends Product11[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11] with Product with Serializable` ###

A tuple of 11 elements; the canonical representation of a scala.Product11.

* _1
  * Element 1 of this Tuple11
* _2
  * Element 2 of this Tuple11
* _3
  * Element 3 of this Tuple11
* _4
  * Element 4 of this Tuple11
* _5
  * Element 5 of this Tuple11
* _6
  * Element 6 of this Tuple11
* _7
  * Element 7 of this Tuple11
* _8
  * Element 8 of this Tuple11
* _9
  * Element 9 of this Tuple11
* _10
  * Element 10 of this Tuple11
* _11
  * Element 11 of this Tuple11

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple11.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple11.scala#L1)


### `case class Tuple12[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12) extends Product12[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12] with Product with Serializable` ###

A tuple of 12 elements; the canonical representation of a scala.Product12.

* _1
  * Element 1 of this Tuple12
* _2
  * Element 2 of this Tuple12
* _3
  * Element 3 of this Tuple12
* _4
  * Element 4 of this Tuple12
* _5
  * Element 5 of this Tuple12
* _6
  * Element 6 of this Tuple12
* _7
  * Element 7 of this Tuple12
* _8
  * Element 8 of this Tuple12
* _9
  * Element 9 of this Tuple12
* _10
  * Element 10 of this Tuple12
* _11
  * Element 11 of this Tuple12
* _12
  * Element 12 of this Tuple12

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple12.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple12.scala#L1)


### `case class Tuple13[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13) extends Product13[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13] with Product with Serializable` ###

A tuple of 13 elements; the canonical representation of a scala.Product13.

* _1
  * Element 1 of this Tuple13
* _2
  * Element 2 of this Tuple13
* _3
  * Element 3 of this Tuple13
* _4
  * Element 4 of this Tuple13
* _5
  * Element 5 of this Tuple13
* _6
  * Element 6 of this Tuple13
* _7
  * Element 7 of this Tuple13
* _8
  * Element 8 of this Tuple13
* _9
  * Element 9 of this Tuple13
* _10
  * Element 10 of this Tuple13
* _11
  * Element 11 of this Tuple13
* _12
  * Element 12 of this Tuple13
* _13
  * Element 13 of this Tuple13

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple13.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple13.scala#L1)


### `case class Tuple14[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14) extends Product14[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14] with Product with Serializable` ###

A tuple of 14 elements; the canonical representation of a scala.Product14.

* _1
  * Element 1 of this Tuple14
* _2
  * Element 2 of this Tuple14
* _3
  * Element 3 of this Tuple14
* _4
  * Element 4 of this Tuple14
* _5
  * Element 5 of this Tuple14
* _6
  * Element 6 of this Tuple14
* _7
  * Element 7 of this Tuple14
* _8
  * Element 8 of this Tuple14
* _9
  * Element 9 of this Tuple14
* _10
  * Element 10 of this Tuple14
* _11
  * Element 11 of this Tuple14
* _12
  * Element 12 of this Tuple14
* _13
  * Element 13 of this Tuple14
* _14
  * Element 14 of this Tuple14

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple14.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple14.scala#L1)


### `case class Tuple15[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15) extends Product15[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15] with Product with Serializable` ###

A tuple of 15 elements; the canonical representation of a scala.Product15.

* _1
  * Element 1 of this Tuple15
* _2
  * Element 2 of this Tuple15
* _3
  * Element 3 of this Tuple15
* _4
  * Element 4 of this Tuple15
* _5
  * Element 5 of this Tuple15
* _6
  * Element 6 of this Tuple15
* _7
  * Element 7 of this Tuple15
* _8
  * Element 8 of this Tuple15
* _9
  * Element 9 of this Tuple15
* _10
  * Element 10 of this Tuple15
* _11
  * Element 11 of this Tuple15
* _12
  * Element 12 of this Tuple15
* _13
  * Element 13 of this Tuple15
* _14
  * Element 14 of this Tuple15
* _15
  * Element 15 of this Tuple15

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple15.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple15.scala#L1)


### `case class Tuple16[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16) extends Product16[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16] with Product with Serializable` ###

A tuple of 16 elements; the canonical representation of a scala.Product16.

* _1
  * Element 1 of this Tuple16
* _2
  * Element 2 of this Tuple16
* _3
  * Element 3 of this Tuple16
* _4
  * Element 4 of this Tuple16
* _5
  * Element 5 of this Tuple16
* _6
  * Element 6 of this Tuple16
* _7
  * Element 7 of this Tuple16
* _8
  * Element 8 of this Tuple16
* _9
  * Element 9 of this Tuple16
* _10
  * Element 10 of this Tuple16
* _11
  * Element 11 of this Tuple16
* _12
  * Element 12 of this Tuple16
* _13
  * Element 13 of this Tuple16
* _14
  * Element 14 of this Tuple16
* _15
  * Element 15 of this Tuple16
* _16
  * Element 16 of this Tuple16

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple16.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple16.scala#L1)


### `case class Tuple17[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17) extends Product17[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17] with Product with Serializable` ###

A tuple of 17 elements; the canonical representation of a scala.Product17.

* _1
  * Element 1 of this Tuple17
* _2
  * Element 2 of this Tuple17
* _3
  * Element 3 of this Tuple17
* _4
  * Element 4 of this Tuple17
* _5
  * Element 5 of this Tuple17
* _6
  * Element 6 of this Tuple17
* _7
  * Element 7 of this Tuple17
* _8
  * Element 8 of this Tuple17
* _9
  * Element 9 of this Tuple17
* _10
  * Element 10 of this Tuple17
* _11
  * Element 11 of this Tuple17
* _12
  * Element 12 of this Tuple17
* _13
  * Element 13 of this Tuple17
* _14
  * Element 14 of this Tuple17
* _15
  * Element 15 of this Tuple17
* _16
  * Element 16 of this Tuple17
* _17
  * Element 17 of this Tuple17

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple17.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple17.scala#L1)


### `case class Tuple18[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18) extends Product18[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18] with Product with Serializable` ###

A tuple of 18 elements; the canonical representation of a scala.Product18.

* _1
  * Element 1 of this Tuple18
* _2
  * Element 2 of this Tuple18
* _3
  * Element 3 of this Tuple18
* _4
  * Element 4 of this Tuple18
* _5
  * Element 5 of this Tuple18
* _6
  * Element 6 of this Tuple18
* _7
  * Element 7 of this Tuple18
* _8
  * Element 8 of this Tuple18
* _9
  * Element 9 of this Tuple18
* _10
  * Element 10 of this Tuple18
* _11
  * Element 11 of this Tuple18
* _12
  * Element 12 of this Tuple18
* _13
  * Element 13 of this Tuple18
* _14
  * Element 14 of this Tuple18
* _15
  * Element 15 of this Tuple18
* _16
  * Element 16 of this Tuple18
* _17
  * Element 17 of this Tuple18
* _18
  * Element 18 of this Tuple18

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple18.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple18.scala#L1)


### `case class Tuple19[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19) extends Product19[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19] with Product with Serializable` ###

A tuple of 19 elements; the canonical representation of a scala.Product19.

* _1
  * Element 1 of this Tuple19
* _2
  * Element 2 of this Tuple19
* _3
  * Element 3 of this Tuple19
* _4
  * Element 4 of this Tuple19
* _5
  * Element 5 of this Tuple19
* _6
  * Element 6 of this Tuple19
* _7
  * Element 7 of this Tuple19
* _8
  * Element 8 of this Tuple19
* _9
  * Element 9 of this Tuple19
* _10
  * Element 10 of this Tuple19
* _11
  * Element 11 of this Tuple19
* _12
  * Element 12 of this Tuple19
* _13
  * Element 13 of this Tuple19
* _14
  * Element 14 of this Tuple19
* _15
  * Element 15 of this Tuple19
* _16
  * Element 16 of this Tuple19
* _17
  * Element 17 of this Tuple19
* _18
  * Element 18 of this Tuple19
* _19
  * Element 19 of this Tuple19

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple19.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple19.scala#L1)


### `case class Tuple2[+T1, +T2](_1: T1, _2: T2) extends Product2[T1, T2] with Product with Serializable` ###

A tuple of 2 elements; the canonical representation of a scala.Product2.

* _1
  * Element 1 of this Tuple2
* _2
  * Element 2 of this Tuple2

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple2.scala#L1)


### `case class Tuple20[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19, _20: T20) extends Product20[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20] with Product with Serializable` ###

A tuple of 20 elements; the canonical representation of a scala.Product20.

* _1
  * Element 1 of this Tuple20
* _2
  * Element 2 of this Tuple20
* _3
  * Element 3 of this Tuple20
* _4
  * Element 4 of this Tuple20
* _5
  * Element 5 of this Tuple20
* _6
  * Element 6 of this Tuple20
* _7
  * Element 7 of this Tuple20
* _8
  * Element 8 of this Tuple20
* _9
  * Element 9 of this Tuple20
* _10
  * Element 10 of this Tuple20
* _11
  * Element 11 of this Tuple20
* _12
  * Element 12 of this Tuple20
* _13
  * Element 13 of this Tuple20
* _14
  * Element 14 of this Tuple20
* _15
  * Element 15 of this Tuple20
* _16
  * Element 16 of this Tuple20
* _17
  * Element 17 of this Tuple20
* _18
  * Element 18 of this Tuple20
* _19
  * Element 19 of this Tuple20
* _20
  * Element 20 of this Tuple20

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple20.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple20.scala#L1)


### `case class Tuple21[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20, +T21](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19, _20: T20, _21: T21) extends Product21[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21] with Product with Serializable` ###

A tuple of 21 elements; the canonical representation of a scala.Product21.

* _1
  * Element 1 of this Tuple21
* _2
  * Element 2 of this Tuple21
* _3
  * Element 3 of this Tuple21
* _4
  * Element 4 of this Tuple21
* _5
  * Element 5 of this Tuple21
* _6
  * Element 6 of this Tuple21
* _7
  * Element 7 of this Tuple21
* _8
  * Element 8 of this Tuple21
* _9
  * Element 9 of this Tuple21
* _10
  * Element 10 of this Tuple21
* _11
  * Element 11 of this Tuple21
* _12
  * Element 12 of this Tuple21
* _13
  * Element 13 of this Tuple21
* _14
  * Element 14 of this Tuple21
* _15
  * Element 15 of this Tuple21
* _16
  * Element 16 of this Tuple21
* _17
  * Element 17 of this Tuple21
* _18
  * Element 18 of this Tuple21
* _19
  * Element 19 of this Tuple21
* _20
  * Element 20 of this Tuple21
* _21
  * Element 21 of this Tuple21

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple21.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple21.scala#L1)


### `case class Tuple22[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9, +T10, +T11, +T12, +T13, +T14, +T15, +T16, +T17, +T18, +T19, +T20, +T21, +T22](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9, _10: T10, _11: T11, _12: T12, _13: T13, _14: T14, _15: T15, _16: T16, _17: T17, _18: T18, _19: T19, _20: T20, _21: T21, _22: T22) extends Product22[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22] with Product with Serializable` ###

A tuple of 22 elements; the canonical representation of a scala.Product22.

* _1
  * Element 1 of this Tuple22
* _2
  * Element 2 of this Tuple22
* _3
  * Element 3 of this Tuple22
* _4
  * Element 4 of this Tuple22
* _5
  * Element 5 of this Tuple22
* _6
  * Element 6 of this Tuple22
* _7
  * Element 7 of this Tuple22
* _8
  * Element 8 of this Tuple22
* _9
  * Element 9 of this Tuple22
* _10
  * Element 10 of this Tuple22
* _11
  * Element 11 of this Tuple22
* _12
  * Element 12 of this Tuple22
* _13
  * Element 13 of this Tuple22
* _14
  * Element 14 of this Tuple22
* _15
  * Element 15 of this Tuple22
* _16
  * Element 16 of this Tuple22
* _17
  * Element 17 of this Tuple22
* _18
  * Element 18 of this Tuple22
* _19
  * Element 19 of this Tuple22
* _20
  * Element 20 of this Tuple22
* _21
  * Element 21 of this Tuple22
* _22
  * Element 22 of this Tuple22

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple22.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple22.scala#L1)


### `case class Tuple3[+T1, +T2, +T3](_1: T1, _2: T2, _3: T3) extends Product3[T1, T2, T3] with Product with Serializable` ###

A tuple of 3 elements; the canonical representation of a scala.Product3.

* _1
  * Element 1 of this Tuple3
* _2
  * Element 2 of this Tuple3
* _3
  * Element 3 of this Tuple3

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple3.scala#L1)


### `case class Tuple4[+T1, +T2, +T3, +T4](_1: T1, _2: T2, _3: T3, _4: T4) extends Product4[T1, T2, T3, T4] with Product with Serializable` ###

A tuple of 4 elements; the canonical representation of a scala.Product4.

* _1
  * Element 1 of this Tuple4
* _2
  * Element 2 of this Tuple4
* _3
  * Element 3 of this Tuple4
* _4
  * Element 4 of this Tuple4

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple4.scala#L1)


### `case class Tuple5[+T1, +T2, +T3, +T4, +T5](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5) extends Product5[T1, T2, T3, T4, T5] with Product with Serializable` ###

A tuple of 5 elements; the canonical representation of a scala.Product5.

* _1
  * Element 1 of this Tuple5
* _2
  * Element 2 of this Tuple5
* _3
  * Element 3 of this Tuple5
* _4
  * Element 4 of this Tuple5
* _5
  * Element 5 of this Tuple5

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple5.scala#L1)


### `case class Tuple6[+T1, +T2, +T3, +T4, +T5, +T6](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6) extends Product6[T1, T2, T3, T4, T5, T6] with Product with Serializable` ###

A tuple of 6 elements; the canonical representation of a scala.Product6.

* _1
  * Element 1 of this Tuple6
* _2
  * Element 2 of this Tuple6
* _3
  * Element 3 of this Tuple6
* _4
  * Element 4 of this Tuple6
* _5
  * Element 5 of this Tuple6
* _6
  * Element 6 of this Tuple6

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple6.scala#L1)


### `case class Tuple7[+T1, +T2, +T3, +T4, +T5, +T6, +T7](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7) extends Product7[T1, T2, T3, T4, T5, T6, T7] with Product with Serializable` ###

A tuple of 7 elements; the canonical representation of a scala.Product7.

* _1
  * Element 1 of this Tuple7
* _2
  * Element 2 of this Tuple7
* _3
  * Element 3 of this Tuple7
* _4
  * Element 4 of this Tuple7
* _5
  * Element 5 of this Tuple7
* _6
  * Element 6 of this Tuple7
* _7
  * Element 7 of this Tuple7

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple7.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple7.scala#L1)


### `case class Tuple8[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8) extends Product8[T1, T2, T3, T4, T5, T6, T7, T8] with Product with Serializable` ###

A tuple of 8 elements; the canonical representation of a scala.Product8.

* _1
  * Element 1 of this Tuple8
* _2
  * Element 2 of this Tuple8
* _3
  * Element 3 of this Tuple8
* _4
  * Element 4 of this Tuple8
* _5
  * Element 5 of this Tuple8
* _6
  * Element 6 of this Tuple8
* _7
  * Element 7 of this Tuple8
* _8
  * Element 8 of this Tuple8

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple8.scala#L1)


### `case class Tuple9[+T1, +T2, +T3, +T4, +T5, +T6, +T7, +T8, +T9](_1: T1, _2: T2, _3: T3, _4: T4, _5: T5, _6: T6, _7: T7, _8: T8, _9: T9) extends Product9[T1, T2, T3, T4, T5, T6, T7, T8, T9] with Product with Serializable` ###

A tuple of 9 elements; the canonical representation of a scala.Product9.

* _1
  * Element 1 of this Tuple9
* _2
  * Element 2 of this Tuple9
* _3
  * Element 3 of this Tuple9
* _4
  * Element 4 of this Tuple9
* _5
  * Element 5 of this Tuple9
* _6
  * Element 6 of this Tuple9
* _7
  * Element 7 of this Tuple9
* _8
  * Element 8 of this Tuple9
* _9
  * Element 9 of this Tuple9

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [Tuple9.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Tuple9.scala#L1)


### `final class UninitializedError extends RuntimeException`                ###

This class represents uninitialized variable/value errors.

* Source
  * [UninitializedError.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/UninitializedError.scala#L1)
* Since
  * 2.5


### `final case class UninitializedFieldError(msg: String) extends RuntimeException with Product with Serializable` ###

This class implements errors which are thrown whenever a field is used before it
has been initialized.

Such runtime checks are not emitted by default. They can be enabled by the
 `-Xcheckinit` compiler option.

* Source
  * [UninitializedFieldError.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/UninitializedFieldError.scala#L1)
* Since
  * 2.7


### `abstract final class Unit extends AnyVal`                               ###

 `Unit` is a subtype of scala.AnyVal. There is only one value of type `Unit` ,
 `()` , and it is not represented by any object in the underlying runtime
system. A method with return type `Unit` is analogous to a Java method which is
declared `void` .

* Source
  * [Unit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Unit.scala#L1)


### `type UnsupportedOperationException = java.lang.UnsupportedOperationException` ###


### `type Vector[+A] = scala.collection.immutable.Vector[A]`                 ###


### `class deprecated extends Annotation with StaticAnnotation`              ###

An annotation that designates that a definition is deprecated. Access to the
member then generates a deprecated warning.

* Annotations
  * @ getter () @ setter () @ beanGetter () @ beanSetter ()
* Source
  * [deprecated.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecated.scala#L1)
* Since
  * 2.3


### `class deprecatedInheritance extends Annotation with StaticAnnotation`   ###

An annotation that designates that inheriting from a class is deprecated.

This is usually done to warn about a non-final class being made final in a
future version. Sub-classing such a class then generates a warning. No warnings
are generated if the subclass is in the same compilation unit.

* Source
  * [deprecatedInheritance.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedInheritance.scala#L1)
* Since
  * 2.10
* See also
  * scala.deprecatedOverriding


### `class deprecatedName extends Annotation with StaticAnnotation`          ###

An annotation that designates the name of the parameter to which it is applied
as deprecated. Using that name in a named argument generates a deprecation
warning.

For instance, evaluating the code below in the Scala interpreter

```scala
def inc(x: Int, @deprecatedName('y) n: Int): Int = x + n
inc(1, y = 2)
```

will produce the following output:

```scala
warning: there were 1 deprecation warnings; re-run with -deprecation for details
res0: Int = 3
```

* Annotations
  * @ param ()
* Source
  * [deprecatedName.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedName.scala#L1)
* Since
  * 2.8.1


### `class deprecatedOverriding extends Annotation with StaticAnnotation`    ###

An annotation that designates that overriding a member is deprecated.

Overriding such a member in a sub-class then generates a warning.

* Source
  * [deprecatedOverriding.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedOverriding.scala#L1)
* Since
  * 2.10
* See also
  * scala.deprecatedInheritance


### `class inline extends Annotation with StaticAnnotation`                  ###

An annotation on methods that requests that the compiler should try especially
hard to inline the annotated method. The annotation can be used at definition
site or at callsite.

```scala
@inline   final def f1(x: Int) = x
@noinline final def f2(x: Int) = x
          final def f3(x: Int) = x

 def t1 = f1(1)              // inlined if possible
 def t2 = f2(1)              // not inlined
 def t3 = f3(1)              // may be inlined (heuristics)
 def t4 = f1(1): @noinline   // not inlined (override at callsite)
 def t5 = f2(1): @inline     // not inlined (cannot override the @noinline at f2's definition)
 def t6 = f3(1): @inline     // inlined if possible
 def t7 = f3(1): @noinline   // not inlined
}
```

Note: parentheses are required when annotating a callsite withing a larger
expression.

```scala
def t1 = f1(1) + f1(1): @noinline   // equivalent to (f1(1) + f1(1)): @noinline
def t2 = f1(1) + (f1(1): @noinline) // the second call to f1 is not inlined
```

* Source
  * [inline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/inline.scala#L1)
* Version
  * 1.0, 2007-5-21


### `class native extends Annotation with StaticAnnotation`                  ###

Marker for native methods.

```scala
@native def f(x: Int, y: List[Long]): String = ...
```

Method body is not generated if method is marked with `@native` , but it is type
checked when present.

* Source
  * [native.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/native.scala#L1)
* Since
  * 2.6


### `class noinline extends Annotation with StaticAnnotation`                ###

An annotation on methods that forbids the compiler to inline the method, no
matter how safe the inlining appears to be. The annotation can be used at
definition site or at callsite.

```scala
@inline   final def f1(x: Int) = x
@noinline final def f2(x: Int) = x
          final def f3(x: Int) = x

 def t1 = f1(1)              // inlined if possible
 def t2 = f2(1)              // not inlined
 def t3 = f3(1)              // may be inlined (heuristics)
 def t4 = f1(1): @noinline   // not inlined (override at callsite)
 def t5 = f2(1): @inline     // not inlined (cannot override the @noinline at f2's definition)
 def t6 = f3(1): @inline     // inlined if possible
 def t7 = f3(1): @noinline   // not inlined
}
```

Note: parentheses are required when annotating a callsite withing a larger
expression.

```scala
def t1 = f1(1) + f1(1): @noinline   // equivalent to (f1(1) + f1(1)): @noinline
def t2 = f1(1) + (f1(1): @noinline) // the second call to f1 is not inlined
```

* Source
  * [noinline.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/noinline.scala#L1)
* Version
  * 1.0, 2007-5-21
* Since
  * 2.5


### `class remote extends Annotation with StaticAnnotation`                  ###

An annotation that designates the class to which it is applied as remotable.

For instance, the Scala code

```scala
@remote trait Hello {
  def sayHello(): String
}
```

is equivalent to the following Java code:

```scala
public interface Hello extends java.rmi.Remote {
    String sayHello() throws java.rmi.RemoteException;
}
```

* Source
  * [remote.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/remote.scala#L1)


### `class specialized extends Annotation with StaticAnnotation`             ###

Annotate type parameters on which code should be automatically specialized. For
example:

```scala
class MyList[@specialized T] ...
```

Type T can be specialized on a subset of the primitive types by specifying a
list of primitive types to specialize at:

```scala
class MyList[@specialized(Int, Double, Boolean) T] ..
```

* Source
  * [specialized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/specialized.scala#L1)
* Since
  * 2.8


### `class throws[T <: Throwable] extends Annotation with StaticAnnotation`  ###

Annotation for specifying the exceptions thrown by a method. For example:

```scala
class Reader(fname: String) {
  private val in = new BufferedReader(new FileReader(fname))
  @throws[IOException]("if the file doesn't exist")
  def read() = in.read()
}
```

* Source
  * [throws.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/throws.scala#L1)
* Version
  * 1.0, 19/05/2006
* Since
  * 2.1


### `class transient extends Annotation with StaticAnnotation`               ###

* Annotations
  * @ field ()
* Source
  * [transient.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/transient.scala#L1)


### `class unchecked extends Annotation`                                     ###

An annotation to designate that the annotated entity should not be considered
for additional compiler checks. Specific applications include annotating the
subject of a match expression to suppress exhaustiveness warnings, and
annotating a type argument in a match case to suppress unchecked warnings.

Such suppression should be used with caution, without which one may encounter
scala.MatchError or java.lang.ClassCastException at runtime. In most cases one
can and should address the warning instead of suppressing it.

```scala
object Test extends App {
  // This would normally warn "match is not exhaustive"
  // because `None` is not covered.
  def f(x: Option[String]) = (x: @unchecked) match { case Some(y) => y }
  // This would normally warn "type pattern is unchecked"
  // but here will blindly cast the head element to String.
  def g(xs: Any) = xs match { case x: List[String @unchecked] => x.head }
}
```

* Source
  * [unchecked.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/unchecked.scala#L1)
* Since
  * 2.4


### `class volatile extends Annotation with StaticAnnotation`                ###

* Annotations
  * @ field ()
* Source
  * [volatile.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/volatile.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object Array extends FallbackArrayBuilding with Serializable`           ###

Utility methods for operating on arrays. For example:

```scala
val a = Array(1, 2)
val b = Array.ofDim[Int](2)
val c = Array.concat(a, b)
```

where the array objects `a` , `b` and `c` have respectively the values
 `Array(1, 2)` , `Array(0, 0)` and `Array(1, 2, 0, 0)` .

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)
* Version
  * 1.0


### `object Boolean extends AnyValCompanion`                                 ###

* Source
  * [Boolean.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Boolean.scala#L1)


### `object Byte extends AnyValCompanion`                                    ###

* Source
  * [Byte.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Byte.scala#L1)


### `object Char extends AnyValCompanion`                                    ###

* Source
  * [Char.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Char.scala#L1)


### `object Console extends DeprecatedConsole with AnsiColor`                ###

Implements functionality for printing Scala values on the terminal as well as
reading specific values. Also defines constants for marking up text on ANSI
terminals.

* Source
  * [Console.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Console.scala#L1)
* Version
  * 1.0, 03/09/2003


### `object Double extends AnyValCompanion`                                  ###

* Source
  * [Double.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Double.scala#L1)


### `object Float extends AnyValCompanion`                                   ###

* Source
  * [Float.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Float.scala#L1)


### `object Function`                                                        ###

A module defining utility methods for higher-order functional programming.

* Source
  * [Function.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Function.scala#L1)
* Version
  * 1.0, 29/11/2006


### `object Int extends AnyValCompanion`                                     ###

* Source
  * [Int.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Int.scala#L1)


### `object Long extends AnyValCompanion`                                    ###

* Source
  * [Long.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Long.scala#L1)


### `object None extends Option[Nothing] with Product with Serializable`     ###

This case object represents non-existent values.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)
* Version
  * 1.0, 16/07/2003


### `object Option extends Serializable`                                     ###

* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)


### `object PartialFunction`                                                 ###

A few handy operations which leverage the extra bit of information available in
partial functions. Examples:

```scala
import PartialFunction._

def strangeConditional(other: Any): Boolean = cond(other) {
  case x: String if x == "abc" || x == "def"  => true
  case x: Int => true
}
def onlyInt(v: Any): Option[Int] = condOpt(v) { case x: Int => x }
```

* Source
  * [PartialFunction.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/PartialFunction.scala#L1)
* Since
  * 2.8


### `object Predef extends LowPriorityImplicits with DeprecatedPredef`       ###

The `Predef` object provides definitions that are accessible in all Scala
compilation units without explicit qualification.

### Commonly Used Types

Predef provides type aliases for types which are commonly used, such as the
immutable collection types scala.collection.immutable.Map,
scala.collection.immutable.Set, and the scala.collection.immutable.List
constructors (scala.collection.immutable.:: and scala.collection.immutable.Nil).

### Console I/O

Predef provides a number of simple functions for console I/O, such as `print` ,
 `println` , `readLine` , `readInt` , etc. These functions are all aliases of
the functions provided by scala.Console.

### Assertions

A set of `assert` functions are provided for use as a way to document and
dynamically check invariants in code. Invocations of `assert` can be elided at
compile time by providing the command line option `-Xdisable-assertions` , which
raises `-Xelide-below` above `elidable.ASSERTION` , to the `scalac` command.

Variants of `assert` intended for use with static analysis tools are also
provided: `assume` , `require` and `ensuring` . `require` and `ensuring` are
intended for use as a means of design-by-contract style specification of pre-
and post-conditions on functions, with the intention that these specifications
could be consumed by a static analysis tool. For instance,

```scala
def addNaturals(nats: List[Int]): Int = {
  require(nats forall (_ >= 0), "List contains negative numbers")
  nats.foldLeft(0)(_ + _)
} ensuring(_ >= 0)
```

The declaration of `addNaturals` states that the list of integers passed should
only contain natural numbers (i.e. non-negative), and that the result returned
will also be natural. `require` is distinct from `assert` in that if the
condition fails, then the caller of the function is to blame rather than a
logical error having been made within `addNaturals` itself. `ensuring` is a form
of `assert` that declares the guarantee the function is providing with regards
to its return value.

### Implicit Conversions

A number of commonly applied implicit conversions are also defined here, and in
the parent type scala.LowPriorityImplicits. Implicit conversions are provided
for the "widening" of numeric values, for instance, converting a Short value to
a Long value as required, and to add additional higher-order functions to Array
values. These are described in more detail in the documentation of scala.Array.

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `object Product1`                                                        ###

* Source
  * [Product1.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product1.scala#L1)


### `object Product10`                                                       ###

* Source
  * [Product10.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product10.scala#L1)


### `object Product11`                                                       ###

* Source
  * [Product11.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product11.scala#L1)


### `object Product12`                                                       ###

* Source
  * [Product12.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product12.scala#L1)


### `object Product13`                                                       ###

* Source
  * [Product13.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product13.scala#L1)


### `object Product14`                                                       ###

* Source
  * [Product14.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product14.scala#L1)


### `object Product15`                                                       ###

* Source
  * [Product15.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product15.scala#L1)


### `object Product16`                                                       ###

* Source
  * [Product16.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product16.scala#L1)


### `object Product17`                                                       ###

* Source
  * [Product17.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product17.scala#L1)


### `object Product18`                                                       ###

* Source
  * [Product18.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product18.scala#L1)


### `object Product19`                                                       ###

* Source
  * [Product19.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product19.scala#L1)


### `object Product2`                                                        ###

* Source
  * [Product2.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product2.scala#L1)


### `object Product20`                                                       ###

* Source
  * [Product20.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product20.scala#L1)


### `object Product21`                                                       ###

* Source
  * [Product21.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product21.scala#L1)


### `object Product22`                                                       ###

* Source
  * [Product22.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product22.scala#L1)


### `object Product3`                                                        ###

* Source
  * [Product3.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product3.scala#L1)


### `object Product4`                                                        ###

* Source
  * [Product4.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product4.scala#L1)


### `object Product5`                                                        ###

* Source
  * [Product5.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product5.scala#L1)


### `object Product6`                                                        ###

* Source
  * [Product6.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product6.scala#L1)


### `object Product7`                                                        ###

* Source
  * [Product7.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product7.scala#L1)


### `object Product8`                                                        ###

* Source
  * [Product8.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product8.scala#L1)


### `object Product9`                                                        ###

* Source
  * [Product9.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Product9.scala#L1)


### `object Proxy`                                                           ###

* Source
  * [Proxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Proxy.scala#L1)


### `object Short extends AnyValCompanion`                                   ###

* Source
  * [Short.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Short.scala#L1)


### `object Specializable`                                                   ###

* Source
  * [Specializable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Specializable.scala#L1)


### `object StringContext extends Serializable`                              ###

* Source
  * [StringContext.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/StringContext.scala#L1)


### `object Symbol extends UniquenessCache[String, Symbol] with Serializable` ###

* Source
  * [Symbol.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Symbol.scala#L1)


### `object Unit extends AnyValCompanion`                                    ###

* Source
  * [Unit.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Unit.scala#L1)


### `package annotation`                                                     ###


### `package beans`                                                          ###


### `package collection`                                                     ###

Contains the base traits and objects needed to use and extend Scala's collection
library.

### Guide

A detailed guide for using the collections library is available at
[http://docs.scala-lang.org/overviews/collections/introduction.html](http://docs.scala-lang.org/overviews/collections/introduction.html).
Developers looking to extend the collections library can find a description of
its architecture at
[http://docs.scala-lang.org/overviews/core/architecture-of-scala-collections.html](http://docs.scala-lang.org/overviews/core/architecture-of-scala-collections.html).

### Using Collections

It is convenient to treat all collections as either a
scala.collection.Traversable or scala.collection.Iterable, as these traits
define the vast majority of operations on a collection.

Collections can, of course, be treated as specifically as needed, and the
library is designed to ensure that the methods that transform collections will
return a collection of the same type:

```scala
scala> val array = Array(1,2,3,4,5,6)
array: Array[Int] = Array(1, 2, 3, 4, 5, 6)

scala> array map { _.toString }
res0: Array[String] = Array(1, 2, 3, 4, 5, 6)

scala> val list = List(1,2,3,4,5,6)
list: List[Int] = List(1, 2, 3, 4, 5, 6)

scala> list map { _.toString }
res1: List[String] = List(1, 2, 3, 4, 5, 6)
```

### Creating Collections

The most common way to create a collection is to use its companion object as a
factory. The three most commonly used collections are scala.collection.Seq,
scala.collection.immutable.Set, and scala.collection.immutable.Map. They can be
used directly as shown below since their companion objects are all available as
type aliases in either the scala package or in `scala.Predef` . New collections
are created like this:

```scala
scala> val seq = Seq(1,2,3,4,1)
seq: Seq[Int] = List(1, 2, 3, 4, 1)

scala> val set = Set(1,2,3,4,1)
set: scala.collection.immutable.Set[Int] = Set(1, 2, 3, 4)

scala> val map = Map(1 -> "one", 2 -> "two", 3 -> "three", 2 -> "too")
map: scala.collection.immutable.Map[Int,String] = Map(1 -> one, 2 -> too, 3 -> three)
```

It is also typical to prefer the scala.collection.immutable collections over
those in scala.collection.mutable; the types aliased in the `scala.Predef`
object are the immutable versions.

Also note that the collections library was carefully designed to include several
implementations of each of the three basic collection types. These
implementations have specific performance characteristics which are described in
[the guide](http://docs.scala-lang.org/overviews/collections/performance-characteristics.html).

The concrete parallel collections also have specific performance characteristics
which are described in
[the parallel collections guide](http://docs.scala-lang.org/overviews/parallel-collections/concrete-parallel-collections.html#performance-characteristics)

### Converting between Java Collections

The scala.collection.JavaConversions object provides implicit defs that will
allow mostly seamless integration between APIs using Java Collections and the
Scala collections library.

Alternatively the scala.collection.JavaConverters object provides a collection
of decorators that allow converting between Scala and Java collections using
 `asScala` and `asJava` methods.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/package.scala#L1)


### `package compat`                                                         ###


### `package concurrent`                                                     ###

This package object contains primitives for concurrent and parallel programming.

### Guide

A more detailed guide to Futures and Promises, including discussion and examples
can be found at
[http://docs.scala-lang.org/overviews/core/futures.html](http://docs.scala-lang.org/overviews/core/futures.html).

### Common Imports

When working with Futures, you will often find that importing the whole
concurrent package is convenient, furthermore you are likely to need an implicit
ExecutionContext in scope for many operations involving Futures and Promises:

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global
```

### Specifying Durations

Operations often require a duration to be specified. A duration DSL is available
to make defining these easier:

```scala
import scala.concurrent.duration._
val d: Duration = 10.seconds
```

### Using Futures For Non-blocking Computation

Basic use of futures is easy with the factory method on Future, which executes a
provided function asynchronously, handing you back a future result of that
function without blocking the current thread. In order to create the Future you
will need either an implicit or explicit ExecutionContext to be provided:

```scala
import scala.concurrent._
import ExecutionContext.Implicits.global  // implicit execution context

val firstZebra: Future[Int] = Future {
  val source = scala.io.Source.fromFile("/etc/dictionaries-common/words")
  source.toSeq.indexOfSlice("zebra")
}
```

### Avoid Blocking

Although blocking is possible in order to await results (with a mandatory
timeout duration):

```scala
import scala.concurrent.duration._
Await.result(firstZebra, 10.seconds)
```

and although this is sometimes necessary to do, in particular for testing
purposes, blocking in general is discouraged when working with Futures and
concurrency in order to avoid potential deadlocks and improve performance.
Instead, use callbacks or combinators to remain in the future domain:

```scala
val animalRange: Future[Int] = for {
  aardvark <- firstAardvark
  zebra <- firstZebra
} yield zebra - aardvark

animalRange.onSuccess {
  case x if x > 500000 => println("It's a long way from Aardvark to Zebra")
}
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/package.scala#L1)


### `package io`                                                             ###


### `object language`                                                        ###

The `scala.language` object controls the language features available to the
programmer, as proposed in the
[SIP-18 document](https://docs.google.com/document/d/1nlkvpoIRkx7at1qJEZafJwthZ3GeIklTFhqmXMvTX9Q/edit).

Each of these features has to be explicitly imported into the current scope to
become available:

```scala
import language.postfixOps // or language._
List(1, 2, 3) reverse
```

The language features are:

* dynamics enables defining calls rewriting using the Dynamic trait
* postfixOps enables postfix operators
* reflectiveCalls enables using structural types
* implicitConversions enables defining implicit methods and members
* higherKinds enables writing higher-kinded types
* existentials enables writing existential types
* experimental contains newer features that have not yet been tested in
   production

* Source
  * [language.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/language.scala#L1)


### `object languageFeature`                                                 ###

* Source
  * [languageFeature.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/languageFeature.scala#L1)


### `package math`                                                           ###

The package object `scala.math` contains methods for performing basic numeric
operations such as elementary exponential, logarithmic, root and trigonometric
functions.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/math/package.scala#L1)


### `package ref`                                                            ###


### `package reflect`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/reflect/package.scala#L1)


### `package runtime`                                                        ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/package.scala#L1)


### `package sys`                                                            ###

The package object `scala.sys` contains methods for reading and altering core
aspects of the virtual machine as well as the world outside of it.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/sys/package.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


### `package text`                                                           ###


### `package util`                                                           ###


--------------------------------------------------------------------------------
                            Value Members From scala
--------------------------------------------------------------------------------


### `val AnyRef: Specializable`                                              ###

(defined at scala)


### `val +:: scala.collection.+:.type`                                       ###

(defined at scala)


### `val :+: scala.collection.:+.type`                                       ###

(defined at scala)


### `val ::: scala.collection.immutable.::.type`                             ###

(defined at scala)


### `val BigDecimal: scala.math.BigDecimal.type`                             ###

(defined at scala)


### `val BigInt: scala.math.BigInt.type`                                     ###

(defined at scala)


### `val Either: scala.util.Either.type`                                     ###

(defined at scala)


### `val Equiv: scala.math.Equiv.type`                                       ###

(defined at scala)


### `val Fractional: scala.math.Fractional.type`                             ###

(defined at scala)


### `val IndexedSeq: scala.collection.IndexedSeq.type`                       ###

(defined at scala)


### `val Integral: scala.math.Integral.type`                                 ###

(defined at scala)


### `val Iterable: scala.collection.Iterable.type`                           ###

(defined at scala)


### `val Iterator: scala.collection.Iterator.type`                           ###

(defined at scala)


### `val Left: scala.util.Left.type`                                         ###

(defined at scala)


### `val List: scala.collection.immutable.List.type`                         ###

(defined at scala)


### `val Nil: scala.collection.immutable.Nil.type`                           ###

(defined at scala)


### `val Numeric: scala.math.Numeric.type`                                   ###

(defined at scala)


### `val Ordered: scala.math.Ordered.type`                                   ###

(defined at scala)


### `val Ordering: scala.math.Ordering.type`                                 ###

(defined at scala)


### `val Range: scala.collection.immutable.Range.type`                       ###

(defined at scala)


### `val Right: scala.util.Right.type`                                       ###

(defined at scala)


### `val Seq: scala.collection.Seq.type`                                     ###

(defined at scala)


### `val Stream: scala.collection.immutable.Stream.type`                     ###

(defined at scala)


### `val StringBuilder: scala.collection.mutable.StringBuilder.type`         ###

(defined at scala)


### `val Traversable: scala.collection.Traversable.type`                     ###

(defined at scala)


### `val Vector: scala.collection.immutable.Vector.type`                     ###

(defined at scala)


--------------------------------------------------------------------------------
                           Value Members From scala#
--------------------------------------------------------------------------------


### `val #::: scala.collection.immutable.Stream.#::.type`                    ###
(defined at scala#)
