
#                   scala.collection.parallel.TraversableOps                   #

```scala
trait TraversableOps[T] extends AnyRef
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Otherwise[R] extends AnyRef`                                      ###

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
      Abstract Value Members From scala.collection.parallel.TraversableOps
--------------------------------------------------------------------------------


### `abstract def asParIterable: ParIterable[T]`                             ###

(defined at scala.collection.parallel.TraversableOps)


### `abstract def asParSeq: ParSeq[T]`                                       ###

(defined at scala.collection.parallel.TraversableOps)


### `abstract def ifParSeq[R](isbody: (ParSeq[T]) ⇒ R): Otherwise[R]`        ###

(defined at scala.collection.parallel.TraversableOps)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.parallel.TraversableOps
--------------------------------------------------------------------------------


### `abstract def isParIterable: Boolean`                                    ###

(defined at scala.collection.parallel.TraversableOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from TraversableOps [T] to
    CollectionsHaveToParArray [TraversableOps [T], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (TraversableOps [T]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
