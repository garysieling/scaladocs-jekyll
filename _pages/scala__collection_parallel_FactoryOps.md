
#                     scala.collection.parallel.FactoryOps                     #

```scala
trait FactoryOps[From, Elem, To] extends AnyRef
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
        Abstract Value Members From scala.collection.parallel.FactoryOps
--------------------------------------------------------------------------------


### `abstract def asParallel: CanCombineFrom[From, Elem, To]`                ###

(defined at scala.collection.parallel.FactoryOps)


### `abstract def ifParallel[R](isbody: (CanCombineFrom[From, Elem, To]) ⇒ R): Otherwise[R]` ###

(defined at scala.collection.parallel.FactoryOps)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.parallel.FactoryOps
--------------------------------------------------------------------------------


### `abstract def isParallel: Boolean`                                       ###

(defined at scala.collection.parallel.FactoryOps)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from FactoryOps [From, Elem,
    To] to CollectionsHaveToParArray [FactoryOps [From, Elem, To], T] performed
    by method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (FactoryOps [
    From, Elem, To]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
