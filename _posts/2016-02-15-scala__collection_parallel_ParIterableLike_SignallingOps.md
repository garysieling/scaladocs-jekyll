
#           scala.collection.parallel.ParIterableLike#SignallingOps           #

```scala
trait SignallingOps[PI <: DelegatedSignalling] extends AnyRef
```

* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.ParIterableLike.SignallingOps
--------------------------------------------------------------------------------


### `abstract def assign(cntx: Signalling): PI`                              ###

(defined at scala.collection.parallel.ParIterableLike.SignallingOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SignallingOps [PI] to
    CollectionsHaveToParArray [SignallingOps [PI], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (SignallingOps [PI]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
