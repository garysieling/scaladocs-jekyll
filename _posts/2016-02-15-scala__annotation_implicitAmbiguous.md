
#                      scala.annotation.implicitAmbiguous                      #

```scala
final class implicitAmbiguous extends Annotation with StaticAnnotation
```

To customize the error message that's emitted when an implicit search finds
multiple ambiguous values, annotate at least one of the implicit values
 `@implicitAmbiguous` . Assuming the implicit value is a method with type
parameters `X1,..., XN` , the error message will be the result of replacing all
occurrences of `${Xi}` in the string `msg` with the string representation of the
corresponding type argument `Ti` .

If more than one `@implicitAmbiguous` annotation is collected, the compiler is
free to pick any of them to display.

Nice errors can direct users to fix imports or even tell them why code
intentionally doesn't compile.

```scala
trait =!=[C, D]

implicit def neq[E, F] : E =!= F = null

@annotation.implicitAmbiguous("Could not prove ${J} =!= ${J}")
implicit def neqAmbig1[G, H, J] : J =!= J = null
implicit def neqAmbig2[I] : I =!= I = null

implicitly[Int =!= Int]
```

* Source
  * [implicitAmbiguous.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/annotation/implicitAmbiguous.scala#L1)
* Since
  * 2.12.0


--------------------------------------------------------------------------------
         Instance Constructors From scala.annotation.implicitAmbiguous
--------------------------------------------------------------------------------


### `new implicitAmbiguous(msg: String)`                                     ###
(defined at scala.annotation.implicitAmbiguous)
