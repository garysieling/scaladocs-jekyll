
#                      scala.annotation.implicitNotFound                      #

```scala
final class implicitNotFound extends Annotation with StaticAnnotation
```

To customize the error message that's emitted when an implicit of type C[T1,...,
TN] cannot be found, annotate the class C with @implicitNotFound. Assuming C has
type parameters X1,..., XN, the error message will be the result of replacing
all occurrences of ${Xi} in the string msg with the string representation of the
corresponding type argument Ti. *

* Source
  * [implicitNotFound.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/implicitNotFound.scala#L1)
* Since
  * 2.8.1


--------------------------------------------------------------------------------
          Instance Constructors From scala.annotation.implicitNotFound
--------------------------------------------------------------------------------


### `new implicitNotFound(msg: String)`                                      ###
(defined at scala.annotation.implicitNotFound)
