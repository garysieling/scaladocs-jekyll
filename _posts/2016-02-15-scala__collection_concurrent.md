
#                         scala.collection.concurrent                         #

```scala
package concurrent
```


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Map[A, B] extends mutable.Map[A, B]`                              ###

A template trait for mutable maps that allow concurrent access.

This is a base trait for all Scala concurrent map implementations. It provides
all of the methods a `Map` does, with the difference that all the changes are
atomic. It also describes methods specific to concurrent maps.

 *Note* : The concurrent maps do not accept `null` for keys or values.

* A
  * the key type of the map
* B
  * the value type of the map

* Source
  * [Map.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/Map.scala#L1)
* Since
  * 2.8
* See also
  * ["Scala's Collection Library overview"](http://docs.scala-lang.org/overviews/collections/concrete-mutable-collection-classes.html#concurrent_maps)
    section on `Concurrent Maps` for more information.


### `final class TrieMap[K, V] extends Map[K, V] with mutable.MapLike[K, V, TrieMap[K, V]] with CustomParallelizable[(K, V), ParTrieMap[K, V]] with Serializable` ###

A concurrent hash-trie or TrieMap is a concurrent thread-safe lock-free
implementation of a hash array mapped trie. It is used to implement the
concurrent map abstraction. It has particularly scalable concurrent insert and
remove operations and is memory-efficient. It supports O(1), atomic, lock-free
snapshots which are used to implement linearizable lock-free size, iterator and
clear operations. The cost of evaluating the (lazy) snapshot is distributed
across subsequent updates, thus making snapshot evaluation horizontally
scalable.

For details, see: http://lampwww.epfl.ch/~prokopec/ctries-snapshot.pdf

* Annotations
  * @ SerialVersionUID ()
* Source
  * [TrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/TrieMap.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object TrieMap extends MutableMapFactory[TrieMap] with Serializable`    ###

* Source
  * [TrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/TrieMap.scala#L1)

