
#              scala.collection.parallel.ParIterableLike#ScanNode              #

```scala
case class ScanNode[U >: T](left: ScanTree[U], right: ScanTree[U]) extends ScanTree[U] with scala.Product with Serializable
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.ScanNode
--------------------------------------------------------------------------------


### `new ScanNode(left: ScanTree[U], right: ScanTree[U])`                    ###

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.ScanNode
--------------------------------------------------------------------------------


### `val left: ScanTree[U]`                                                  ###

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


### `val leftmost: ScanLeaf[U]`                                              ###

* Definition Classes
  * ScanNode → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


### `def print(depth: Int): Unit`                                            ###

* Definition Classes
  * ScanNode → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


### `def pushdown(v: U): Unit`                                               ###

* Definition Classes
  * ScanNode → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


### `val right: ScanTree[U]`                                                 ###

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


### `val rightmost: ScanLeaf[U]`                                             ###

* Definition Classes
  * ScanNode → ScanTree

(defined at scala.collection.parallel.ParIterableLike.ScanNode)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ScanNode [U] to
    CollectionsHaveToParArray [ScanNode [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ScanNode [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
