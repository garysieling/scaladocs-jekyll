
#                      scala.collection.mutable.HashTable                      #

```scala
trait HashTable[A, Entry >: Null <: HashEntry[A, Entry]] extends HashUtils[A]
```

This class can be used to construct data structures that are based on
hashtables. Class `HashTable[A]` implements a hashtable that maps keys of type
 `A` to values of the fully abstract member type `Entry` . Classes that make use
of `HashTable` have to provide an implementation for `Entry` .

There are mainly two parameters that affect the performance of a hashtable: the
 _initial size_ and the _load factor_ . The _size_ refers to the number of _
buckets_ in the hashtable, and the _load factor_ is a measure of how full the
hashtable is allowed to get before its size is automatically doubled. Both
parameters may be changed by overriding the corresponding values in class
 `HashTable` .

* A
  * type of the elements contained in this hash table.

* Source
  * [HashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/HashTable.scala#L1)
* Version
  * 2.0, 31/12/2006
* Since
  * 1


--------------------------------------------------------------------------------
         Abstract Value Members From scala.collection.mutable.HashTable
--------------------------------------------------------------------------------


### `abstract def createNewEntry[B](key: A, value: B): Entry`                ###

Creates new entry to be immediately inserted into the hashtable. This method is
guaranteed to be called only once and in case that the entry will be added. In
other words, an implementation may be side-effecting.

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.mutable.HashTable
--------------------------------------------------------------------------------


### `def addEntry(e: Entry): Unit`                                           ###

Add entry to table pre: no entry with same key exists

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def calcSizeMapSize(tableLength: Int): Int`                             ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def elemEquals(key1: A, key2: A): Boolean`                              ###

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `def findEntry(key: A): Entry`                                           ###

Find entry with given key in table, null if not found.

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def findOrAddEntry[B](key: A, value: B): Entry`                         ###

Find entry with given key in table, or add new one if not found. May be somewhat
faster then `findEntry` / `addEntry` pair as it computes entry's hash index only
once. Returns entry found in table or null. New entries are created by calling
 `createNewEntry` method.

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `def foreachEntry[U](f: (Entry) ⇒ U): Unit`                              ###

Avoid iterator for a 2x faster traversal.

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `final def index(hcode: Int): Int`                                       ###

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `def initWithContents(c: Contents[A, Entry]): Unit`                      ###

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapAdd(h: Int): Unit`                                         ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapRemove(h: Int): Unit`                                      ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def nnSizeMapReset(tableLength: Int): Unit`                             ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def removeEntry(key: A): Entry`                                         ###

Remove entry from table if present.

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.HashTable)


### `def sizeMapInit(tableLength: Int): Unit`                                ###

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


### `var table: Array[HashEntry[A, Entry]]`                                  ###

The actual hash table.

* Attributes
  * protected

(defined at scala.collection.mutable.HashTable)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.mutable.HashTable.HashUtils
--------------------------------------------------------------------------------


### `def elemHashCode(key: A): Int`                                          ###

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
