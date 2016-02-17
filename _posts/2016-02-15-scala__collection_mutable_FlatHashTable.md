
#                    scala.collection.mutable.FlatHashTable                    #

```scala
trait FlatHashTable[A] extends HashUtils[A]
```

An implementation class backing a `HashSet` .

This trait is used internally. It can be mixed in with various collections
relying on hash table as an implementation.

* Source
  * [FlatHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/FlatHashTable.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.FlatHashTable
--------------------------------------------------------------------------------


### `def addElem(elem: A): Boolean`                                          ###

Add elem if not yet in table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def addEntry(newEntry: AnyRef): Boolean`                                ###

Add an entry (an elem converted to an entry via elemToEntry) if not yet in
table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def calcSizeMapSize(tableLength: Int): Int`                             ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def capacity(expectedSize: Int): Int`                                   ###

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def containsElem(elem: A): Boolean`                                     ###

Checks whether an element is contained in the hash table.

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def findEntry(elem: A): Option[A]`                                      ###

Finds an entry in the hash table if such an element exists.

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `final def index(hcode: Int): Int`                                       ###

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def initWithContents(c: Contents[A]): Unit`                             ###

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapAdd(h: Int): Unit`                                         ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapRemove(h: Int): Unit`                                      ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapReset(tableLength: Int): Unit`                             ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def removeElem(elem: A): Boolean`                                       ###

Removes an elem from the hash table returning true if the element was found (and
thus removed) or false if it didn't exist.

* Attributes
  * protected

(defined at scala.collection.mutable.FlatHashTable)


### `def sizeMapInit(tableLength: Int): Unit`                                ###

* Attributes
  * protected
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


--------------------------------------------------------------------------------
      Value Members From scala.collection.mutable.FlatHashTable.HashUtils
--------------------------------------------------------------------------------


### `final def elemToEntry(elem: A): AnyRef`                                 ###

Elems have type A, but we store AnyRef in the table. Plus we need to deal with
null elems, which need to be stored as NullSentinel

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


### `final def entryToElem(entry: AnyRef): A`                                ###

Does the inverse translation of elemToEntry

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


### `final def improve(hcode: Int, seed: Int): Int`                          ###

* Attributes
  * protected
* Definition Classes
  * HashUtils
(defined at scala.collection.mutable.FlatHashTable.HashUtils)
