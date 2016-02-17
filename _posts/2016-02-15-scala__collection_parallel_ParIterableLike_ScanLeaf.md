
#              scala.collection.parallel.ParIterableLike#ScanLeaf              #

```scala
case class ScanLeaf[U >: T](pit: IterableSplitter[U], op: (U, U) ⇒ U, from: Int, len: Int, prev: Option[ScanLeaf[U]], acc: U) extends ScanTree[U] with scala.Product with Serializable
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.ScanLeaf
--------------------------------------------------------------------------------


### `new ScanLeaf(pit: IterableSplitter[U], op: (U, U) ⇒ U, from: Int, len: Int, prev: Option[ScanLeaf[U]], acc: U)` ###

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.ScanLeaf
--------------------------------------------------------------------------------


### `def leftmost: ScanLeaf[U]`                                              ###

* Definition Classes
  * ScanLeaf → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `val op: (U, U) ⇒ U`                                                     ###

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `val pit: IterableSplitter[U]`                                           ###

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `var prev: Option[ScanLeaf[U]]`                                          ###

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `def print(depth: Int): Unit`                                            ###

* Definition Classes
  * ScanLeaf → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `def pushdown(v: U): Unit`                                               ###

* Definition Classes
  * ScanLeaf → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


### `def rightmost: ScanLeaf[U]`                                             ###

* Definition Classes
  * ScanLeaf → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanLeaf)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ScanLeaf [U] to
    CollectionsHaveToParArray [ScanLeaf [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ScanLeaf [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
