
#                          scala.deprecatedOverriding                          #

```scala
class deprecatedOverriding extends Annotation with StaticAnnotation
```

An annotation that designates that overriding a member is deprecated.

Overriding such a member in a sub-class then generates a warning.

* Source
  * [deprecatedOverriding.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecatedOverriding.scala#L1)
* Since
  * 2.10
* See also
  * scala.deprecatedInheritance


--------------------------------------------------------------------------------
             Instance Constructors From scala.deprecatedOverriding
--------------------------------------------------------------------------------


### `new deprecatedOverriding(message: String = "", since: String = "")`     ###

* message
  * the message to print during compilation if the member was overridden
* since
  * a string identifying the first version in which overriding was deprecated
(defined at scala.deprecatedOverriding)
