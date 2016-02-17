
#                          scala.beans.ScalaBeanInfo                          #

```scala
abstract class ScalaBeanInfo extends SimpleBeanInfo
```

Provides some simple runtime processing necessary to create JavaBean descriptors
for Scala entities. The compiler creates subclasses of this class automatically
when the BeanInfo annotation is attached to a class.

* Source
  * [ScalaBeanInfo.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/beans/ScalaBeanInfo.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From java.beans.SimpleBeanInfo
--------------------------------------------------------------------------------


### `def getBeanDescriptor(): BeanDescriptor`                                ###

* Definition Classes
  * SimpleBeanInfo → BeanInfo

(defined at java.beans.SimpleBeanInfo)


### `def getEventSetDescriptors(): Array[EventSetDescriptor]`                ###

* Definition Classes
  * SimpleBeanInfo → BeanInfo

(defined at java.beans.SimpleBeanInfo)


### `def getIcon(arg0: Int): Image`                                          ###

* Definition Classes
  * SimpleBeanInfo → BeanInfo

(defined at java.beans.SimpleBeanInfo)


### `def loadImage(arg0: String): Image`                                     ###

* Definition Classes
  * SimpleBeanInfo

(defined at java.beans.SimpleBeanInfo)


--------------------------------------------------------------------------------
              Instance Constructors From scala.beans.ScalaBeanInfo
--------------------------------------------------------------------------------


### `new ScalaBeanInfo(clazz: Class[_], props: Array[String], methods: Array[String])` ###

(defined at scala.beans.ScalaBeanInfo)


--------------------------------------------------------------------------------
                  Value Members From scala.beans.ScalaBeanInfo
--------------------------------------------------------------------------------


### `def getMethodDescriptors(): Array[MethodDescriptor]`                    ###

* Definition Classes
  * ScalaBeanInfo → SimpleBeanInfo → BeanInfo

(defined at scala.beans.ScalaBeanInfo)


### `def getPropertyDescriptors(): Array[PropertyDescriptor]`                ###

* Definition Classes
  * ScalaBeanInfo → SimpleBeanInfo → BeanInfo
(defined at scala.beans.ScalaBeanInfo)
