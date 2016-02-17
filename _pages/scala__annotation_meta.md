
#                            scala.annotation.meta                            #

```scala
package meta
```

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


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `final class beanGetter extends Annotation with StaticAnnotation`        ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [beanGetter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/beanGetter.scala#L1)


### `final class beanSetter extends Annotation with StaticAnnotation`        ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [beanSetter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/beanSetter.scala#L1)


### `final class companionClass extends Annotation with StaticAnnotation`    ###

When defining an implicit class, the Scala compiler creates an implicit
conversion method for it. Annotations `@companionClass` and `@companionMethod`
control where an annotation on the implicit class will go. By default,
annotations on an implicit class end up only on the class.

* Source
  * [companionClass.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/companionClass.scala#L1)


### `final class companionMethod extends Annotation with StaticAnnotation`   ###

When defining an implicit class, the Scala compiler creates an implicit
conversion method for it. Annotations `@companionClass` and `@companionMethod`
control where an annotation on the implicit class will go. By default,
annotations on an implicit class end up only on the class.

* Source
  * [companionMethod.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/companionMethod.scala#L1)


### `final class companionObject extends Annotation with StaticAnnotation`   ###

Currently unused; intended as an annotation target for classes such as case
classes that automatically generate a companion object

* Source
  * [companionObject.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/companionObject.scala#L1)


### `final class field extends Annotation with StaticAnnotation`             ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [field.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/field.scala#L1)


### `final class getter extends Annotation with StaticAnnotation`            ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [getter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/getter.scala#L1)


### `final class languageFeature extends Annotation with StaticAnnotation`   ###

An annotation giving particulars for a language feature in object
 `scala.language` .

* Source
  * [languageFeature.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/languageFeature.scala#L1)


### `final class param extends Annotation with StaticAnnotation`             ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [param.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/param.scala#L1)


### `final class setter extends Annotation with StaticAnnotation`            ###

Consult the documentation in package scala.annotation.meta.

* Source
  * [setter.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/setter.scala#L1)

