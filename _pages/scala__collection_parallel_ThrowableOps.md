
#                    scala.collection.parallel.ThrowableOps                    #

```scala
trait ThrowableOps extends AnyRef
```

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This trait will be removed.
* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.parallel.ThrowableOps
--------------------------------------------------------------------------------


### `abstract def alongWith(that: Throwable): Throwable`                     ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ This method will be removed.

(defined at scala.collection.parallel.ThrowableOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ThrowableOps to
    CollectionsHaveToParArray [ThrowableOps, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ThrowableOps) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
