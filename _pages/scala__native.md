
#                                 scala.native                                 #

```scala
class native extends Annotation with StaticAnnotation
```

Marker for native methods.

```scala
@native def f(x: Int, y: List[Long]): String = ...
```

Method body is not generated if method is marked with `@native` , but it is type
checked when present.

* Source
  * [native.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/native.scala#L1)
* Since
  * 2.6


--------------------------------------------------------------------------------
                    Instance Constructors From scala.native
--------------------------------------------------------------------------------


### `new native()`                                                           ###
(defined at scala.native)
