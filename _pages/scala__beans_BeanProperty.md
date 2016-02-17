
#                           scala.beans.BeanProperty                           #

```scala
class BeanProperty extends Annotation with StaticAnnotation
```

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


--------------------------------------------------------------------------------
              Instance Constructors From scala.beans.BeanProperty
--------------------------------------------------------------------------------


### `new BeanProperty()`                                                     ###
(defined at scala.beans.BeanProperty)
