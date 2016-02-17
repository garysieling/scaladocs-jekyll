
#                             scala.beans.BeanInfo                             #

```scala
class BeanInfo extends Annotation
```

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


--------------------------------------------------------------------------------
                Instance Constructors From scala.beans.BeanInfo
--------------------------------------------------------------------------------


### `new BeanInfo()`                                                         ###
(defined at scala.beans.BeanInfo)
