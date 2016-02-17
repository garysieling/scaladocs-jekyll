
#              scala.collection.parallel.mutable.ParFlatHashTable              #

```scala
trait ParFlatHashTable[T] extends FlatHashTable[T]
```

Parallel flat hash table.

* T
  * type of the elements in the table.

* Source
  * [ParFlatHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParFlatHashTable.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract class ParFlatHashTableIterator extends IterableSplitter[T] with SizeMapUtils` ###

* Source
  * [ParFlatHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParFlatHashTable.scala#L1)


--------------------------------------------------------------------------------
           Value Members From scala.collection.mutable.FlatHashTable
--------------------------------------------------------------------------------


### `def addElem(elem: T): Boolean`                                          ###

Add elem if not yet in table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def addEntry(newEntry: AnyRef): Boolean`                                ###

Add an entry (an elem converted to an entry via elemToEntry) if not yet in
table.

* returns
  * Returns `true` if a new elem was added, `false` otherwise.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def calcSizeMapSize(tableLength: Int): Int`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def capacity(expectedSize: Int): Int`                                   ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def containsElem(elem: T): Boolean`                                     ###

Checks whether an element is contained in the hash table.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def findEntry(elem: T): Option[T]`                                      ###

Finds an entry in the hash table if such an element exists.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `final def index(hcode: Int): Int`                                       ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def initWithContents(c: Contents[T]): Unit`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def iterator: Iterator[T]`                                              ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapAdd(h: Int): Unit`                                         ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapRemove(h: Int): Unit`                                      ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def nnSizeMapReset(tableLength: Int): Unit`                             ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


### `def removeElem(elem: T): Boolean`                                       ###

Removes an elem from the hash table returning true if the element was found (and
thus removed) or false if it didn't exist.

* Attributes
  * protected
* Definition Classes
  * FlatHashTable

(defined at scala.collection.mutable.FlatHashTable)


### `def sizeMapInit(tableLength: Int): Unit`                                ###

* Attributes
  * protected
* Definition Classes
  * FlatHashTable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.FlatHashTable)


--------------------------------------------------------------------------------
      Value Members From scala.collection.mutable.FlatHashTable.HashUtils
--------------------------------------------------------------------------------


### `final def elemToEntry(elem: T): AnyRef`                                 ###

Elems have type A, but we store AnyRef in the table. Plus we need to deal with
null elems, which need to be stored as NullSentinel

* Attributes
  * protected
* Definition Classes
  * HashUtils

(defined at scala.collection.mutable.FlatHashTable.HashUtils)


### `final def entryToElem(entry: AnyRef): T`                                ###

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


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ParFlatHashTable [T] to
    CollectionsHaveToParArray [ParFlatHashTable [T], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ParFlatHashTable [T]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
