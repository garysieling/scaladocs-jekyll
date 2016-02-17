
#                                 scala.beans                                 #

```scala
package beans
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class BeanDescription extends Annotation`                               ###

Provides a short description that will be included when generating bean
information. This annotation can be attached to the bean itself, or to any
member.

* Source
  * [BeanDescription.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BeanDescription.scala#L1)


### `class BeanDisplayName extends Annotation`                               ###

Provides a display name when generating bean information. This annotation can be
attached to the bean itself, or to any member.

* Source
  * [BeanDisplayName.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BeanDisplayName.scala#L1)


### `class BeanInfo extends Annotation`                                      ###

This annotation indicates that a JavaBean-compliant `BeanInfo` class should be
generated for this annotated Scala class.

* A `val` becomes a read-only property.
* A `var` becomes a read-write property.
* A `def` becomes a method.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12.0)_ the generation of BeanInfo classes is no longer
    supported
* Source
  * [BeanInfo.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BeanInfo.scala#L1)


### `class BeanInfoSkip extends Annotation`                                  ###

This annotation indicates that bean information should *not* be generated for
the val, var, or def that it is attached to.

* Source
  * [BeanInfoSkip.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BeanInfoSkip.scala#L1)


### `class BeanProperty extends Annotation with StaticAnnotation`            ###

When attached to a field, this annotation adds a setter and a getter method
following the Java Bean convention. For example:

```scala
@BeanProperty
var status = ""
```

adds the following methods to the class:

```scala
def setStatus(s: String) { this.status = s }
def getStatus: String = this.status
```

For fields of type `Boolean` , if you need a getter named `isStatus` , use the
 `scala.beans.BooleanBeanProperty` annotation instead.

* Annotations
  * @ field ()
* Source
  * [BeanProperty.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BeanProperty.scala#L1)


### `class BooleanBeanProperty extends Annotation with StaticAnnotation`     ###

This annotation has the same functionality as `scala.beans.BeanProperty` , but
the generated Bean getter will be named `isFieldName` instead of `getFieldName` .

* Annotations
  * @ field ()
* Source
  * [BooleanBeanProperty.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/BooleanBeanProperty.scala#L1)


### `abstract class ScalaBeanInfo extends SimpleBeanInfo`                    ###

Provides some simple runtime processing necessary to create JavaBean descriptors
for Scala entities. The compiler creates subclasses of this class automatically
when the BeanInfo annotation is attached to a class.

* Source
  * [ScalaBeanInfo.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/ScalaBeanInfo.scala#L1)

