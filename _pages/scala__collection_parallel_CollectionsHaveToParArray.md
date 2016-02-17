
#             scala.collection.parallel.CollectionsHaveToParArray             #

```scala
implicit class CollectionsHaveToParArray[C, T] extends AnyRef
```

Adds toParArray method to collection classes.

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/package.scala#L1)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `new CollectionsHaveToParArray(c: C)(implicit asGto: (C) ⇒ GenTraversableOnce[T])` ###

(defined at scala.collection.parallel.CollectionsHaveToParArray)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###
(defined at scala.collection.parallel.CollectionsHaveToParArray)
