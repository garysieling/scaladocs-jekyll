
#                                 scala.Predef                                 #

```scala
object Predef extends LowPriorityImplicits with DeprecatedPredef
```

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


--------------------------------------------------------------------------------
                            Deprecated Value Members
--------------------------------------------------------------------------------


### `object Pair`                                                            ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use built-in tuple syntax or Tuple2 instead
* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `object Triple`                                                          ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use built-in tuple syntax or Tuple3 instead
* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `sealed abstract class <:<[-From, +To] extends (From) ⇒ To with Serializable` ###

An instance of `A <:< B` witnesses that `A` is a subtype of `B` . Requiring an
implicit argument of the type `A <:< B` encodes the generalized constraint
 `A <: B` .

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)
* Note
  * we need a new type constructor `<:<` and evidence `conforms` , as reusing
     `Function1` and `identity` leads to ambiguities in case of type errors (
     `any2stringadd` is inferred) To constrain any abstract type T that's in
    scope in a method's argument list (not just the method's own type
    parameters) simply add an implicit argument of type `T <:< U` , where `U` is
    the required upper bound; or for lower-bounds, use: `L <:< T` , where `L` is
    the required lower bound. In part contributed by Jason Zaugg.


### `sealed abstract class =:=[From, To] extends (From) ⇒ To with Serializable` ###

An instance of `A =:= B` witnesses that the types `A` and `B` are equal.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)
* See also
  * `<:<` for expressing subtyping constraints


### `implicit final class ArrayCharSequence extends CharSequence`            ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `implicit final class ArrowAssoc[A] extends AnyVal`                      ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `type Class[T] = java.lang.Class[T]`                                     ###


### `type ClassManifest[T] = ClassTag[T]`                                    ###

* Annotations
  * @ implicitNotFound (msg =...) @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use `scala.reflect.ClassTag` instead


### `class DummyImplicit extends AnyRef`                                     ###

A type for which there is always an implicit value.

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)
* See also
  * scala.Array$, method `fallbackCanBuildFrom`


### `implicit final class Ensuring[A] extends AnyVal`                        ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `type Function[-A, +B] = (A) ⇒ B`                                        ###


### `type Manifest[T] = reflect.Manifest[T]`                                 ###

* Annotations
  * @ implicitNotFound (msg = "No Manifest available for ${T}.")


### `type Map[A, +B] = collection.immutable.Map[A, B]`                       ###


### `type OptManifest[T] = reflect.OptManifest[T]`                           ###


### `type Pair[+A, +B] = (A, B)`                                             ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use built-in tuple syntax or Tuple2 instead


### `implicit final class RichException extends AnyVal`                      ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `implicit final class SeqCharSequence extends CharSequence`              ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `type Set[A] = collection.immutable.Set[A]`                              ###


### `type String = java.lang.String`                                         ###

The `String` type in Scala has methods that come either from the underlying Java
String (see the documentation corresponding to your Java version, for example
[http://docs.oracle.com/javase/8/docs/api/java/lang/String.html](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html))
or are added implicitly through scala.collection.immutable.StringOps.


### `implicit final class StringFormat[A] extends AnyVal`                    ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `type Triple[+A, +B, +C] = (A, B, C)`                                    ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use built-in tuple syntax or Tuple3 instead


### `implicit final class any2stringadd[A] extends AnyVal`                   ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object =:= extends Serializable`                                        ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


### `object DummyImplicit`                                                   ###

* Source
  * [Predef.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Predef.scala#L1)


--------------------------------------------------------------------------------
              Deprecated Value Members From scala.DeprecatedPredef
--------------------------------------------------------------------------------


### `def any2ArrowAssoc[A](x: A): ArrowAssoc[A]`                             ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ArrowAssoc`

(defined at scala.DeprecatedPredef)


### `def any2Ensuring[A](x: A): Ensuring[A]`                                 ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `Ensuring`

(defined at scala.DeprecatedPredef)


### `def any2stringfmt(x: Any): StringFormat[Any]`                           ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `StringFormat`

(defined at scala.DeprecatedPredef)


### `def arrayToCharSequence(xs: Array[Char]): CharSequence`                 ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `ArrayCharSequence`

(defined at scala.DeprecatedPredef)


### `def exceptionWrapper(exc: scala.Throwable): RichException`              ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `Throwable` directly

(defined at scala.DeprecatedPredef)


### `def readLine(): String`                                                 ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def readLine(text: String, args: Any*): String`                         ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def readf(format: String): List[Any]`                                   ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def readf1(format: String): Any`                                        ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def readf2(format: String): (Any, Any)`                                 ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def readf3(format: String): (Any, Any, Any)`                            ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use the method in `scala.io.StdIn`

(defined at scala.DeprecatedPredef)


### `def seqToCharSequence(xs: collection.IndexedSeq[Char]): CharSequence`   ###

* Definition Classes
  * DeprecatedPredef
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Use `SeqCharSequence`

(defined at scala.DeprecatedPredef)


--------------------------------------------------------------------------------
                 Value Members From scala.LowPriorityImplicits
--------------------------------------------------------------------------------


### `implicit def booleanWrapper(x: Boolean): RichBoolean`                   ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def byteWrapper(x: Byte): RichByte`                            ###

We prefer the java.lang.* boxed types to these wrappers in any potential
conflicts. Conflicts do exist because the wrappers need to implement ScalaNumber
in order to have a symmetric equals method, but that implies implementing
java.lang.Number as well.

Note - these are inlined because they are value classes, but the call to
xxxWrapper is not eliminated even though it does nothing. Even inlined, every
call site does a no-op retrieval of Predef's MODULE$ because maybe loading
Predef has side effects!

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def charWrapper(c: Char): RichChar`                            ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def doubleWrapper(x: Double): RichDouble`                      ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def fallbackStringCanBuildFrom[T]: CanBuildFrom[String, T, collection.immutable.IndexedSeq[T]]` ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def floatWrapper(x: Float): RichFloat`                         ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def genericWrapArray[T](xs: Array[T]): WrappedArray[T]`        ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def intWrapper(x: Int): RichInt`                               ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def longWrapper(x: Long): RichLong`                            ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def shortWrapper(x: Short): RichShort`                         ###

* Definition Classes
  * LowPriorityImplicits
* Annotations
  * @ inline ()

(defined at scala.LowPriorityImplicits)


### `implicit def unwrapString(ws: WrappedString): String`                   ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapBooleanArray(xs: Array[Boolean]): WrappedArray[Boolean]` ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapByteArray(xs: Array[Byte]): WrappedArray[Byte]`        ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapCharArray(xs: Array[Char]): WrappedArray[Char]`        ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapDoubleArray(xs: Array[Double]): WrappedArray[Double]`  ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapFloatArray(xs: Array[Float]): WrappedArray[Float]`     ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapIntArray(xs: Array[Int]): WrappedArray[Int]`           ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapLongArray(xs: Array[Long]): WrappedArray[Long]`        ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapRefArray[T <: AnyRef](xs: Array[T]): WrappedArray[T]`  ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapShortArray(xs: Array[Short]): WrappedArray[Short]`     ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapString(s: String): WrappedString`                      ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


### `implicit def wrapUnitArray(xs: Array[Unit]): WrappedArray[Unit]`        ###

* Definition Classes
  * LowPriorityImplicits

(defined at scala.LowPriorityImplicits)


--------------------------------------------------------------------------------
                   Deprecated Value Members From scala.Predef
--------------------------------------------------------------------------------


### `val ClassManifest: ClassManifestFactory.type`                           ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use `scala.reflect.ClassTag` instead

(defined at scala.Predef)


### `def booleanArrayOps(xs: Array[Boolean]): ArrayOps[Boolean]`             ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def byteArrayOps(xs: Array[Byte]): ArrayOps[Byte]`                      ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def charArrayOps(xs: Array[Char]): ArrayOps[Char]`                      ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def classManifest[T](implicit m: ClassManifest[T]): ClassManifest[T]`   ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ Use scala.reflect.classTag[T] instead

(defined at scala.Predef)


### `def doubleArrayOps(xs: Array[Double]): ArrayOps[Double]`                ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def error(message: String): Nothing`                                    ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.9.0)_ Use `sys.error(message)` instead

(defined at scala.Predef)


### `def floatArrayOps(xs: Array[Float]): ArrayOps[Float]`                   ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def intArrayOps(xs: Array[Int]): ArrayOps[Int]`                         ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def longArrayOps(xs: Array[Long]): ArrayOps[Long]`                      ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def refArrayOps[T <: AnyRef](xs: Array[T]): ArrayOps[T]`                ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def shortArrayOps(xs: Array[Short]): ArrayOps[Short]`                   ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


### `def unitArrayOps(xs: Array[Unit]): ArrayOps[Unit]`                      ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0-M2)_ For binary compatibility only. Release new
    partest and remove in M3.

(defined at scala.Predef)


--------------------------------------------------------------------------------
                        Value Members From scala.Predef
--------------------------------------------------------------------------------


### `implicit def Boolean2boolean(x: java.lang.Boolean): Boolean`            ###

(defined at scala.Predef)


### `implicit def Byte2byte(x: java.lang.Byte): Byte`                        ###

(defined at scala.Predef)


### `implicit def Character2char(x: Character): Char`                        ###

(defined at scala.Predef)


### `implicit def Double2double(x: java.lang.Double): Double`                ###

(defined at scala.Predef)


### `implicit def Float2float(x: java.lang.Float): Float`                    ###

(defined at scala.Predef)


### `implicit def Integer2int(x: Integer): Int`                              ###

(defined at scala.Predef)


### `implicit def Long2long(x: java.lang.Long): Long`                        ###

(defined at scala.Predef)


### `val Manifest: ManifestFactory.type`                                     ###

(defined at scala.Predef)


### `val Map: collection.immutable.Map.type`                                 ###

(defined at scala.Predef)


### `val Set: collection.immutable.Set.type`                                 ###

(defined at scala.Predef)


### `implicit def Short2short(x: java.lang.Short): Short`                    ###

(defined at scala.Predef)


### `implicit val StringCanBuildFrom: CanBuildFrom[String, Char, String]`    ###

(defined at scala.Predef)


### `implicit def _booleanArrayOps(xs: Array[Boolean]): ofBoolean`           ###

(defined at scala.Predef)


### `implicit def _byteArrayOps(xs: Array[Byte]): ofByte`                    ###

(defined at scala.Predef)


### `implicit def _charArrayOps(xs: Array[Char]): ofChar`                    ###

(defined at scala.Predef)


### `implicit def _doubleArrayOps(xs: Array[Double]): ofDouble`              ###

(defined at scala.Predef)


### `implicit def _floatArrayOps(xs: Array[Float]): ofFloat`                 ###

(defined at scala.Predef)


### `implicit def _intArrayOps(xs: Array[Int]): ofInt`                       ###

(defined at scala.Predef)


### `implicit def _longArrayOps(xs: Array[Long]): ofLong`                    ###

(defined at scala.Predef)


### `implicit def _refArrayOps[T <: AnyRef](xs: Array[T]): ofRef[T]`         ###

(defined at scala.Predef)


### `implicit def _shortArrayOps(xs: Array[Short]): ofShort`                 ###

(defined at scala.Predef)


### `implicit def _unitArrayOps(xs: Array[Unit]): ofUnit`                    ###

(defined at scala.Predef)


### `def assert(assertion: Boolean): Unit`                                   ###

Tests an expression, throwing an `AssertionError` if false. Calls to this method
will not be generated if `-Xelide-below` is at least `ASSERTION` .

* assertion
  * the expression to test

* Annotations
  * @ elidable (level = ASSERTION)
* See also
  * elidable

(defined at scala.Predef)


### `final def assert(assertion: Boolean, message: ⇒ Any): Unit`             ###

Tests an expression, throwing an `AssertionError` if false. Calls to this method
will not be generated if `-Xelide-below` is at least `ASSERTION` .

* assertion
  * the expression to test
* message
  * a String to include in the failure message

* Annotations
  * @ elidable (level = ASSERTION) @ inline ()
* See also
  * elidable

(defined at scala.Predef)


### `def assume(assumption: Boolean): Unit`                                  ###

Tests an expression, throwing an `AssertionError` if false. This method differs
from assert only in the intent expressed: assert contains a predicate which
needs to be proven, while assume contains an axiom for a static checker. Calls
to this method will not be generated if `-Xelide-below` is at least `ASSERTION` .

* assumption
  * the expression to test

* Annotations
  * @ elidable (level = ASSERTION)
* See also
  * elidable

(defined at scala.Predef)


### `final def assume(assumption: Boolean, message: ⇒ Any): Unit`            ###

Tests an expression, throwing an `AssertionError` if false. This method differs
from assert only in the intent expressed: assert contains a predicate which
needs to be proven, while assume contains an axiom for a static checker. Calls
to this method will not be generated if `-Xelide-below` is at least `ASSERTION` .

* assumption
  * the expression to test
* message
  * a String to include in the failure message

* Annotations
  * @ elidable (level = ASSERTION) @ inline ()
* See also
  * elidable

(defined at scala.Predef)


### `implicit def augmentString(x: String): StringOps`                       ###

* Annotations
  * @ inline ()

(defined at scala.Predef)


### `implicit def boolean2Boolean(x: Boolean): java.lang.Boolean`            ###

(defined at scala.Predef)


### `implicit def byte2Byte(x: Byte): java.lang.Byte`                        ###

(defined at scala.Predef)


### `implicit def char2Character(x: Char): Character`                        ###

(defined at scala.Predef)


### `implicit def double2Double(x: Double): java.lang.Double`                ###

(defined at scala.Predef)


### `implicit def float2Float(x: Float): java.lang.Float`                    ###

(defined at scala.Predef)


### `implicit def genericArrayOps[T](xs: Array[T]): ArrayOps[T]`             ###

(defined at scala.Predef)


### `def identity[A](x: A): A`                                               ###

* Annotations
  * @ inline ()

(defined at scala.Predef)


### `def implicitly[T](implicit e: T): T`                                    ###

* Annotations
  * @ inline ()

(defined at scala.Predef)


### `implicit def int2Integer(x: Int): Integer`                              ###

(defined at scala.Predef)


### `def locally[T](x: T): T`                                                ###

* Annotations
  * @ inline ()

(defined at scala.Predef)


### `implicit def long2Long(x: Long): java.lang.Long`                        ###

(defined at scala.Predef)


### `def manifest[T](implicit m: Manifest[T]): Manifest[T]`                  ###

(defined at scala.Predef)


### `def optManifest[T](implicit m: OptManifest[T]): OptManifest[T]`         ###

(defined at scala.Predef)


### `def print(x: Any): Unit`                                                ###

(defined at scala.Predef)


### `def printf(text: String, xs: Any*): Unit`                               ###

(defined at scala.Predef)


### `def println(x: Any): Unit`                                              ###

(defined at scala.Predef)


### `def require(requirement: Boolean): Unit`                                ###

Tests an expression, throwing an `IllegalArgumentException` if false. This
method is similar to `assert` , but blames the caller of the method for
violating the condition.

* requirement
  * the expression to test

(defined at scala.Predef)


### `final def require(requirement: Boolean, message: ⇒ Any): Unit`          ###

Tests an expression, throwing an `IllegalArgumentException` if false. This
method is similar to `assert` , but blames the caller of the method for
violating the condition.

* requirement
  * the expression to test
* message
  * a String to include in the failure message

* Annotations
  * @ inline ()

(defined at scala.Predef)


### `implicit def short2Short(x: Short): java.lang.Short`                    ###

(defined at scala.Predef)


### `implicit def tuple2ToZippedOps[T1, T2](x: (T1, T2)): Ops[T1, T2]`       ###

(defined at scala.Predef)


### `implicit def tuple3ToZippedOps[T1, T2, T3](x: (T1, T2, T3)): Ops[T1, T2, T3]` ###

(defined at scala.Predef)


### `implicit def unaugmentString(x: StringOps): String`                     ###

* Annotations
  * @ inline ()
(defined at scala.Predef)
