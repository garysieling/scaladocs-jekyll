
#                     scala.annotation.meta.companionClass                     #

```scala
final class companionClass extends Annotation with StaticAnnotation
```

When defining an implicit class, the Scala compiler creates an implicit
conversion method for it. Annotations `@companionClass` and `@companionMethod`
control where an annotation on the implicit class will go. By default,
annotations on an implicit class end up only on the class.

* Source
  * [companionClass.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/companionClass.scala#L1)


--------------------------------------------------------------------------------
        Instance Constructors From scala.annotation.meta.companionClass
--------------------------------------------------------------------------------


### `new companionClass()`                                                   ###
(defined at scala.annotation.meta.companionClass)
