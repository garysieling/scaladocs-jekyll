
#                         scala.deprecatedInheritance                         #

```scala
class deprecatedInheritance extends Annotation with StaticAnnotation
```

An annotation that designates that inheriting from a class is deprecated.

This is usually done to warn about a non-final class being made final in a
future version. Sub-classing such a class then generates a warning. No warnings
are generated if the subclass is in the same compilation unit.

* Source
  * [deprecatedInheritance.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedInheritance.scala#L1)
* Since
  * 2.10
* See also
  * scala.deprecatedOverriding


--------------------------------------------------------------------------------
             Instance Constructors From scala.deprecatedInheritance
--------------------------------------------------------------------------------


### `new deprecatedInheritance(message: String = "", since: String = "")`    ###

* message
  * the message to print during compilation if the class was sub-classed
* since
  * a string identifying the first version in which inheritance was deprecated
(defined at scala.deprecatedInheritance)
