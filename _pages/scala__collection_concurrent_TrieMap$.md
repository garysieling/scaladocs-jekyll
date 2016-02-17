
#                     scala.collection.concurrent.TrieMap                     #

```scala
object TrieMap extends MutableMapFactory[TrieMap] with Serializable
```

* Source
  * [TrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/TrieMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = TrieMap[_, _]`                                              ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class MangledHashing[K] extends Hashing[K]`                             ###

* Source
  * [TrieMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/concurrent/TrieMap.scala#L1)


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


--------------------------------------------------------------------------------
             Value Members From scala.collection.concurrent.TrieMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[K, V]: CanBuildFrom[Coll, (K, V), TrieMap[K, V]]` ###

(defined at scala.collection.concurrent.TrieMap)


### `def empty[K, V]: TrieMap[K, V]`                                         ###

An empty Map

* Definition Classes
  * TrieMap → MapFactory → GenMapFactory

(defined at scala.collection.concurrent.TrieMap)


### `val inodeupdater: AtomicReferenceFieldUpdater[INodeBase[_, _], MainNode[_, _]]` ###

(defined at scala.collection.concurrent.TrieMap)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): TrieMap[A, B]`                         ###

A collection of type `Map` that contains given key/value bindings.

* A
  * the type of the keys
* B
  * the type of the associated values
* elems
  * the key/value pairs that make up the map
* returns
  * a new map consisting key/value pairs given by `elems` .

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.MutableMapFactory
--------------------------------------------------------------------------------


### `def newBuilder[A, B]: Builder[(A, B), TrieMap[A, B]]`                   ###

The default builder for Map objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * MutableMapFactory → GenMapFactory
(defined at scala.collection.generic.MutableMapFactory)
