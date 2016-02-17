
#                    scala.annotation.meta.companionMethod                    #

```scala
final class companionMethod extends Annotation with StaticAnnotation
```

When defining an implicit class, the Scala compiler creates an implicit
conversion method for it. Annotations `@companionClass` and `@companionMethod`
control where an annotation on the implicit class will go. By default,
annotations on an implicit class end up only on the class.

* Source
  * [companionMethod.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/meta/companionMethod.scala#L1)


--------------------------------------------------------------------------------
        Instance Constructors From scala.annotation.meta.companionMethod
--------------------------------------------------------------------------------


### `new companionMethod()`                                                  ###
(defined at scala.annotation.meta.companionMethod)
