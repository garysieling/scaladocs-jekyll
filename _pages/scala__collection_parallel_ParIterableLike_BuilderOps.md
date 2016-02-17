
#             scala.collection.parallel.ParIterableLike#BuilderOps             #

```scala
trait BuilderOps[Elem, To] extends AnyRef
```

* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Otherwise[Cmb] extends AnyRef`                                    ###

* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.ParIterableLike.BuilderOps
--------------------------------------------------------------------------------


### `abstract def asCombiner: Combiner[Elem, To]`                            ###

(defined at scala.collection.parallel.ParIterableLike.BuilderOps)


### `abstract def ifIs[Cmb](isbody: (Cmb) ⇒ Unit): Otherwise[Cmb]`           ###

(defined at scala.collection.parallel.ParIterableLike.BuilderOps)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.ParIterableLike.BuilderOps
--------------------------------------------------------------------------------


### `abstract def isCombiner: Boolean`                                       ###

(defined at scala.collection.parallel.ParIterableLike.BuilderOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from BuilderOps [Elem, To] to
    CollectionsHaveToParArray [BuilderOps [Elem, To], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (BuilderOps [Elem, To]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
