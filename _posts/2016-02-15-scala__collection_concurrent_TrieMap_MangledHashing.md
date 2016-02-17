
#              scala.collection.concurrent.TrieMap.MangledHashing              #

```scala
class MangledHashing[K] extends Hashing[K]
```

* Source
  * [TrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/TrieMap.scala#L1)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.concurrent.TrieMap.MangledHashing
--------------------------------------------------------------------------------


### `new MangledHashing()`                                                   ###

(defined at scala.collection.concurrent.TrieMap.MangledHashing)


--------------------------------------------------------------------------------
     Value Members From scala.collection.concurrent.TrieMap.MangledHashing
--------------------------------------------------------------------------------


### `def hash(k: K): Int`                                                    ###

* Definition Classes
  * MangledHashing → Hashing

(defined at scala.collection.concurrent.TrieMap.MangledHashing)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from MangledHashing [K] to
    CollectionsHaveToParArray [MangledHashing [K], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (MangledHashing [K]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
