
#                  scala.collection.parallel.CombinerFactory                  #

```scala
trait CombinerFactory[U, Repr] extends AnyRef
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.parallel.CombinerFactory
--------------------------------------------------------------------------------


### `abstract def apply(): Combiner[U, Repr]`                                ###

Provides a combiner used to construct a collection.

(defined at scala.collection.parallel.CombinerFactory)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.parallel.CombinerFactory
--------------------------------------------------------------------------------


### `abstract def doesShareCombiners: Boolean`                               ###

The call to the `apply` method can create a new combiner each time. If it does,
this method returns `false` . The same combiner factory may be used each time
(typically, this is the case for concurrent collections, which are thread safe).
If so, the method returns `true` .

(defined at scala.collection.parallel.CombinerFactory)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from CombinerFactory [U, Repr]
    to CollectionsHaveToParArray [CombinerFactory [U, Repr], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    CombinerFactory [U, Repr]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
