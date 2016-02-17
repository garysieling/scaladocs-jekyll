
#                               scala.deprecated                               #

```scala
class deprecated extends Annotation with StaticAnnotation
```

An annotation that designates that a definition is deprecated. Access to the
member then generates a deprecated warning.

* Annotations
  * @ getter () @ setter () @ beanGetter () @ beanSetter ()
* Source
  * [deprecated.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/deprecated.scala#L1)
* Since
  * 2.3


--------------------------------------------------------------------------------
                  Instance Constructors From scala.deprecated
--------------------------------------------------------------------------------


### `new deprecated(message: String = "", since: String = "")`               ###

* message
  * the message to print during compilation if the definition is accessed
* since
  * a string identifying the first version in which the definition was
    deprecated
(defined at scala.deprecated)
