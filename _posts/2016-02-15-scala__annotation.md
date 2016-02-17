
#                               scala.annotation                               #

```scala
package annotation
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class Annotation extends AnyRef`                               ###

A base class for annotations. Annotations extending this class directly are not
preserved for the Scala type checker and are also not stored as Java annotations
in classfiles. To enable either or both of these, one needs to inherit from
scala.annotation.StaticAnnotation or/and scala.annotation.ClassfileAnnotation.

* Source
  * [Annotation.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/Annotation.scala#L1)
* Version
  * 1.1, 2/02/2007
* Since
  * 2.4


### `trait ClassfileAnnotation extends Annotation with StaticAnnotation`     ###

A base class for classfile annotations. These are stored as
[Java annotations](http://docs.oracle.com/javase/7/docs/technotes/guides/language/annotations.html#_top)]
in classfiles.

* Source
  * [ClassfileAnnotation.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/ClassfileAnnotation.scala#L1)
* Version
  * 1.1, 2/02/2007
* Since
  * 2.4


### `trait StaticAnnotation extends Annotation`                              ###

A base class for static annotations. These are available to the Scala type
checker, even across different compilation units.

* Source
  * [StaticAnnotation.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/StaticAnnotation.scala#L1)
* Version
  * 1.1, 2/02/2007
* Since
  * 2.4


### `trait TypeConstraint extends Annotation`                                ###

A marker for annotations that, when applied to a type, should be treated as a
constraint on the annotated type.

A proper constraint should restrict the type based only on information mentioned
within the type. A Scala compiler can use this assumption to rewrite the
contents of the constraint as necessary. To contrast, a type annotation whose
meaning depends on the context where it is written down is not a proper
constrained type, and this marker should not be applied. A Scala compiler will
drop such annotations in cases where it would rewrite a type constraint.

* Source
  * [TypeConstraint.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/TypeConstraint.scala#L1)
* Version
  * 1.1, 2007-11-5
* Since
  * 2.6


### `final class compileTimeOnly extends Annotation with StaticAnnotation`   ###

An annotation that designates that an annottee should not be referred to after
type checking (which includes macro expansion).

Examples of potential use: 1) The annottee can only appear in the arguments of
some other macro that will eliminate it from the AST during expansion. 2) The
annottee is a macro and should have been expanded away, so if hasn't, something
wrong has happened. (Comes in handy to provide better support for new macro
flavors, e.g. macro annotations, that can't be expanded by the vanilla
compiler).

* Annotations
  * @ getter () @ setter () @ beanGetter () @ beanSetter () @ companionClass ()
    @ companionMethod ()
* Source
  * [compileTimeOnly.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/compileTimeOnly.scala#L1)
* Since
  * 2.11.0


### `final class elidable extends Annotation with StaticAnnotation`          ###

An annotation for methods whose bodies may be excluded from compiler-generated
bytecode.

Behavior is influenced by passing `-Xelide-below <arg>` to `scalac` . Calls to
methods marked elidable (as well as the method body) will be omitted from
generated code if the priority given the annotation is lower than that given on
the command line.

```scala
@elidable(123)           // annotation priority
scalac -Xelide-below 456 // command line priority
```

The method call will be replaced with an expression which depends on the type of
the elided expression. In decreasing order of precedence:

```scala
Unit            ()
Boolean         false
T <: AnyVal     0
T >: Null       null
T >: Nothing    Predef.???
```

Complete example:

```scala
import scala.annotation._, elidable._
object Test extends App {
  def expensiveComputation(): Int = { Thread.sleep(1000) ; 172 }

  @elidable(WARNING) def warning(msg: String) = println(msg)
  @elidable(FINE) def debug(msg: String)      = println(msg)
  @elidable(FINE) def computedValue           = expensiveComputation()

  warning("Warning! Danger! Warning!")
  debug("Debug! Danger! Debug!")
  println("I computed a value: " + computedValue)
}
% scalac example.scala && scala Test
Warning! Danger! Warning!
Debug! Danger! Debug!
I computed a value: 172

// INFO lies between WARNING and FINE
% scalac -Xelide-below INFO example.scala && scala Test
Warning! Danger! Warning!
I computed a value: 0
```

* Source
  * [elidable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/elidable.scala#L1)
* Since
  * 2.8


### `final class implicitAmbiguous extends Annotation with StaticAnnotation` ###

To customize the error message that's emitted when an implicit search finds
multiple ambiguous values, annotate at least one of the implicit values
 `@implicitAmbiguous` . Assuming the implicit value is a method with type
parameters `X1,..., XN` , the error message will be the result of replacing all
occurrences of `${Xi}` in the string `msg` with the string representation of the
corresponding type argument `Ti` .

If more than one `@implicitAmbiguous` annotation is collected, the compiler is
free to pick any of them to display.

Nice errors can direct users to fix imports or even tell them why code
intentionally doesn't compile.

```scala
trait =!=[C, D]

implicit def neq[E, F] : E =!= F = null

@annotation.implicitAmbiguous("Could not prove ${J} =!= ${J}")
implicit def neqAmbig1[G, H, J] : J =!= J = null
implicit def neqAmbig2[I] : I =!= I = null

implicitly[Int =!= Int]
```

* Source
  * [implicitAmbiguous.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/implicitAmbiguous.scala#L1)
* Since
  * 2.12.0


### `final class implicitNotFound extends Annotation with StaticAnnotation`  ###

To customize the error message that's emitted when an implicit of type C[T1,...,
TN] cannot be found, annotate the class C with @implicitNotFound. Assuming C has
type parameters X1,..., XN, the error message will be the result of replacing
all occurrences of ${Xi} in the string msg with the string representation of the
corresponding type argument Ti. *

* Source
  * [implicitNotFound.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/implicitNotFound.scala#L1)
* Since
  * 2.8.1


### `class strictfp extends Annotation with StaticAnnotation`                ###

If this annotation is present on a method or its enclosing class, the strictfp
flag will be emitted.

* Source
  * [strictfp.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/strictfp.scala#L1)
* Version
  * 2.9
* Since
  * 2.9


### `final class switch extends Annotation with StaticAnnotation`            ###

An annotation to be applied to a match expression. If present, the compiler will
verify that the match has been compiled to a
[tableswitch or lookupswitch](http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-3.html#jvms-3.10)
and issue an error if it instead compiles into a series of conditional
expressions. Example usage:

```scala
val Constant = 'Q'
def tokenMe(ch: Char) = (ch: @switch) match {
  case ' ' | '\t' | '\n'  => 1
  case 'A' | 'Z' | '$'    => 2
  case '5' | Constant     => 3  // a non-literal may prevent switch generation: this would not compile
  case _                  => 4
}
```

Note: for pattern matches with one or two cases, the compiler generates jump
instructions. Annotating such a match with `@switch` does not issue any warning.

* Source
  * [switch.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/switch.scala#L1)
* Since
  * 2.8


### `final class tailrec extends Annotation with StaticAnnotation`           ###

A method annotation which verifies that the method will be compiled with tail
call optimization.

If it is present, the compiler will issue an error if the method cannot be
optimized into a loop.

* Source
  * [tailrec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/tailrec.scala#L1)
* Since
  * 2.8


### `class unspecialized extends Annotation with StaticAnnotation`           ###

A method annotation which suppresses the creation of additional specialized
forms based on enclosing specialized type parameters.

* Source
  * [unspecialized.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/unspecialized.scala#L1)
* Since
  * 2.10


### `final class varargs extends Annotation with StaticAnnotation`           ###

A method annotation which instructs the compiler to generate a Java
varargs-style forwarder method for interop. This annotation can only be applied
to methods with repeated parameters.

* Source
  * [varargs.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/varargs.scala#L1)
* Since
  * 2.9


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object elidable`                                                        ###

This useless appearing code was necessary to allow people to use named constants
for the elidable annotation. This is what it takes to convince the compiler to
fold the constants: otherwise when it's time to check an elision level it's
staring at a tree like

```scala
(Select(Level, Select(FINEST, Apply(intValue, Nil))))
```

instead of the number `300` .

* Source
  * [elidable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/elidable.scala#L1)
* Since
  * 2.8


### `package meta`                                                           ###

When defining a field, the Scala compiler creates up to four accessors for it: a
getter, a setter, and if the field is annotated with `@BeanProperty` , a bean
getter and a bean setter.

For instance in the following class definition

```scala
class C(@myAnnot @BeanProperty var c: Int)
```

there are six entities which can carry the annotation `@myAnnot` : the
constructor parameter, the generated field and the four accessors.

By default, annotations on ( `val` -, `var` - or plain) constructor parameters
end up on the parameter, not on any other entity. Annotations on fields by
default only end up on the field.

The meta-annotations in package `scala.annotation.meta` are used to control
where annotations on fields and class parameters are copied. This is done by
annotating either the annotation type or the annotation class with one or
several of the meta-annotations in this package.

### Annotating the annotation type

The target meta-annotations can be put on the annotation type when instantiating
the annotation. In the following example, the annotation `@Id` will be added
only to the bean getter `getX` .

```scala
import javax.persistence.Id
class A {
  @(Id @beanGetter) @BeanProperty val x = 0
}
```

In order to annotate the field as well, the meta-annotation `@field` would need
to be added.

The syntax can be improved using a type alias:

```scala
object ScalaJPA {
  type Id = javax.persistence.Id @beanGetter
}
import ScalaJPA.Id
class A {
  @Id @BeanProperty val x = 0
}
```

### Annotating the annotation class

For annotations defined in Scala, a default target can be specified in the
annotation class itself, for example

```scala
@getter
class myAnnotation extends Annotation
```

This only changes the default target for the annotation `myAnnotation` . When
instantiating the annotation, the target can still be specified as described in
the last section.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/package.scala#L1)


### `package unchecked`                                                      ###

