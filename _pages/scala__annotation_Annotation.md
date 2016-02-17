
#                         scala.annotation.Annotation                         #

```scala
abstract class Annotation extends AnyRef
```

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


--------------------------------------------------------------------------------
             Instance Constructors From scala.annotation.Annotation
--------------------------------------------------------------------------------


### `new Annotation()`                                                       ###
(defined at scala.annotation.Annotation)
