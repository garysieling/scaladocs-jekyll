
#              scala.collection.parallel.ParIterableLike#ScanTree              #

```scala
trait ScanTree[U >: T] extends AnyRef
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.parallel.ParIterableLike.ScanTree
--------------------------------------------------------------------------------


### `abstract def leftmost: ScanLeaf[U]`                                     ###

(defined at scala.collection.parallel.ParIterableLike.ScanTree)


### `abstract def print(depth: Int = 0): Unit`                               ###

(defined at scala.collection.parallel.ParIterableLike.ScanTree)


### `abstract def pushdown(v: U): Unit`                                      ###

(defined at scala.collection.parallel.ParIterableLike.ScanTree)


### `abstract def rightmost: ScanLeaf[U]`                                    ###

(defined at scala.collection.parallel.ParIterableLike.ScanTree)


--------------------------------------------------------------------------------
 Concrete Value Members From scala.collection.parallel.ParIterableLike.ScanTree
--------------------------------------------------------------------------------


### `abstract def beginsAt: Int`                                             ###

(defined at scala.collection.parallel.ParIterableLike.ScanTree)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ScanTree [U] to
    CollectionsHaveToParArray [ScanTree [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ScanTree [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
