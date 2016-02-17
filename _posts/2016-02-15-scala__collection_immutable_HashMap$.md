
#                      scala.collection.immutable.HashMap                      #

```scala
object HashMap extends ImmutableMapFactory[HashMap] with generic.BitOperations.Int with Serializable
```

This object provides a set of operations needed to create `immutable.HashMap`
values.

* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = HashMap[_, _]`                                              ###

The type constructor of the collection that can be built by this factory

* Definition Classes
  * GenMapFactory


### `class HashMap1[A, +B] extends HashMap[A, B]`                            ###

* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashMap.scala#L1)


### `class HashTrieMap[A, +B] extends HashMap[A, B]`                         ###

* Source
  * [HashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/HashMap.scala#L1)


### `type Int = scala.Int`                                                   ###

* Definition Classes
  * Int


### `class MapCanBuildFrom[A, B] extends CanBuildFrom[Coll, (A, B), CC[A, B]]` ###

The standard `CanBuildFrom` class for maps.

* Definition Classes
  * GenMapFactory


--------------------------------------------------------------------------------
         Value Members From scala.collection.generic.BitOperations.Int
--------------------------------------------------------------------------------


### `def bitString(num: Int, sep: String = ""): String`                      ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def bits(num: Int): IndexedSeq[Boolean]`                                ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def complement(i: Int): scala.Int`                                      ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def hasMatch(key: Int, prefix: Int, m: Int): Boolean`                   ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def highestOneBit(j: Int): scala.Int`                                   ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def mask(i: Int, mask: Int): scala.Int`                                 ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def shorter(m1: Int, m2: Int): Boolean`                                 ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def unsignedCompare(i: Int, j: Int): Boolean`                           ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


### `def zero(i: Int, mask: Int): Boolean`                                   ###

* Definition Classes
  * Int

(defined at scala.collection.generic.BitOperations.Int)


--------------------------------------------------------------------------------
           Value Members From scala.collection.generic.GenMapFactory
--------------------------------------------------------------------------------


### `def apply[A, B](elems: (A, B)*): HashMap[A, B]`                         ###

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


### `def newBuilder[A, B]: Builder[(A, B), HashMap[A, B]]`                   ###

The default builder for `Map` objects.

* A
  * the type of the keys
* B
  * the type of the associated values

* Definition Classes
  * GenMapFactory

(defined at scala.collection.generic.GenMapFactory)


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.HashMap
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A, B]: CanBuildFrom[Coll, (A, B), HashMap[A, B]]` ###

The standard `CanBuildFrom` instance for `immutable.HashMap` objects. The
created value is an instance of class `MapCanBuildFrom` .

(defined at scala.collection.immutable.HashMap)


### `def empty[A, B]: HashMap[A, B]`                                         ###

An empty `immutable.HashMap`

* Definition Classes
  * HashMap → MapFactory → GenMapFactory
(defined at scala.collection.immutable.HashMap)
