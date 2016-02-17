
#              scala.collection.parallel.TraversableOps#Otherwise              #

```scala
trait Otherwise[R] extends AnyRef
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
 Abstract Value Members From scala.collection.parallel.TraversableOps.Otherwise
--------------------------------------------------------------------------------


### `abstract def otherwise(notbody: ⇒ R): R`                                ###

(defined at scala.collection.parallel.TraversableOps.Otherwise)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Otherwise [R] to
    CollectionsHaveToParArray [Otherwise [R], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Otherwise [R]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
