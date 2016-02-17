
#                         scala.FallbackArrayBuilding                         #

```scala
class FallbackArrayBuilding extends AnyRef
```

Contains a fallback builder for arrays when the element type does not have a
class tag. In that case a generic array is built.

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)


--------------------------------------------------------------------------------
             Instance Constructors From scala.FallbackArrayBuilding
--------------------------------------------------------------------------------


### `new FallbackArrayBuilding()`                                            ###

(defined at scala.FallbackArrayBuilding)


--------------------------------------------------------------------------------
                 Value Members From scala.FallbackArrayBuilding
--------------------------------------------------------------------------------


### `implicit def fallbackCanBuildFrom[T](implicit m: DummyImplicit): CanBuildFrom[Array[_], T, ArraySeq[T]]` ###

A builder factory that generates a generic array. Called instead of
 `Array.newBuilder` if the element type of an array does not have a class tag.
Note that fallbackBuilder factory needs an implicit parameter (otherwise it
would not be dominated in implicit search by `Array.canBuildFrom` ). We make
sure that implicit search is always successful.
(defined at scala.FallbackArrayBuilding)
