
#        scala.collection.parallel.ParIterableLike#BuilderOps#Otherwise        #

```scala
trait Otherwise[Cmb] extends AnyRef
```

* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.ParIterableLike.BuilderOps.Otherwise
--------------------------------------------------------------------------------


### `abstract def otherwise(notbody: ⇒ Unit)(implicit t: ClassTag[Cmb]): Unit` ###

(defined at scala.collection.parallel.ParIterableLike.BuilderOps.Otherwise)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Otherwise [Cmb] to
    CollectionsHaveToParArray [Otherwise [Cmb], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Otherwise [Cmb]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
