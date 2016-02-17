
#                           scala.annotation.tailrec                           #

```scala
final class tailrec extends Annotation with StaticAnnotation
```

A method annotation which verifies that the method will be compiled with tail
call optimization.

If it is present, the compiler will issue an error if the method cannot be
optimized into a loop.

* Source
  * [tailrec.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/tailrec.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
              Instance Constructors From scala.annotation.tailrec
--------------------------------------------------------------------------------


### `new tailrec()`                                                          ###
(defined at scala.annotation.tailrec)
