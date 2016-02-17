
#                scala.collection.parallel.mutable.ParHashTable                #

```scala
trait ParHashTable[K, Entry >: Null <: HashEntry[K, Entry]] extends HashTable[K, Entry]
```

Provides functionality for hash tables with linked list buckets, enriching the
data structure by fulfilling certain requirements for their parallel
construction and iteration.

* Source
  * [ParHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashTable.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class EntryIterator[T, +IterRepr <: IterableSplitter[T]] extends IterableSplitter[T] with SizeMapUtils` ###

A parallel iterator returning all the entries.

* Source
  * [ParHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashTable.scala#L1)


--------------------------------------------------------------------------------
         Abstract Value Members From scala.collection.mutable.HashTable
--------------------------------------------------------------------------------


### `abstract def createNewEntry[B](key: K, value: B): Entry`                ###

Creates new entry to be immediately inserted into the hashtable. This method is
guaranteed to be called only once and in case that the entry will be added. In
other words, an implementation may be side-effecting.

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.mutable.HashTable
--------------------------------------------------------------------------------


### `def addEntry(e: Entry): Unit`                                           ###

Add entry to table pre: no entry with same key exists

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def calcSizeMapSize(tableLength: Int): Int`                             ###

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def elemEquals(key1: K, key2: K): Boolean`                              ###

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `def findEntry(key: K): Entry`                                           ###

Find entry with given key in table, null if not found.

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def findOrAddEntry[B](key: K, value: B): Entry`                         ###

Find entry with given key in table, or add new one if not found. May be somewhat
faster then `findEntry` / `addEntry` pair as it computes entry's hash index only
once. Returns entry found in table or null. New entries are created by calling
 `createNewEntry` method.

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `def foreachEntry[U](f: (Entry) ⇒ U): Unit`                              ###

Avoid iterator for a 2x faster traversal.

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `final def index(hcode: Int): Int`                                       ###

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `def initWithContents(c: Contents[K, Entry]): Unit`                      ###

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapAdd(h: Int): Unit`                                         ###

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapRemove(h: Int): Unit`                                      ###

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapReset(tableLength: Int): Unit`                             ###

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def removeEntry(key: K): Entry`                                         ###

Remove entry from table if present.

* Attributes
  * protected
* Definition Classes
  * HashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def sizeMapInit(tableLength: Int): Unit`                                ###

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


### `var table: Array[HashEntry[K, Entry]]`                                  ###

The actual hash table.

* Attributes
  * protected
* Definition Classes
  * HashTable

(defined at scala.collection.mutable.HashTable)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.mutable.HashTable.HashUtils
--------------------------------------------------------------------------------


### `def elemHashCode(key: K): Int`                                          ###

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.HashTable.HashUtils)


### `final def improve(hcode: Int, seed: Int): Int`                          ###

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.HashTable.HashUtils)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParHashTable [K, Entry]
    to CollectionsHaveToParArray [ParHashTable [K, Entry], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (ParHashTable [
    K, Entry]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
