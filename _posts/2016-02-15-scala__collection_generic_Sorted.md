
#                       scala.collection.generic.Sorted                       #

```scala
trait Sorted[K, +This <: Sorted[K, This]] extends AnyRef
```

Any collection (including maps) whose keys (or elements) are ordered.

* Source
  * [Sorted.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Sorted.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.generic.Sorted
--------------------------------------------------------------------------------


### `abstract def keySet: SortedSet[K]`                                      ###

return as a projection the set of keys in this collection

(defined at scala.collection.generic.Sorted)


### `abstract def keysIteratorFrom(start: K): Iterator[K]`                   ###

Creates an iterator over all the keys(or elements) contained in this collection
greater than or equal to `start` according to the ordering of this collection.
x.keysIteratorFrom(y) is equivalent to but often more efficient than
x.from(y).keysIterator.

* start
  * The lower bound (inclusive) on the keys to be returned

(defined at scala.collection.generic.Sorted)


### `abstract def rangeImpl(from: Option[K], until: Option[K]): This`        ###

Creates a ranged projection of this collection. Any mutations in the ranged
projection will update this collection and vice versa.

Note: keys are not guaranteed to be consistent between this collection and the
projection. This is the case for buffers where indexing is relative to the
projection.

* from
  * The lower-bound (inclusive) of the ranged projection. `None` if there is no
    lower bound.
* until
  * The upper-bound (exclusive) of the ranged projection. `None` if there is no
    upper bound.

(defined at scala.collection.generic.Sorted)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.generic.Sorted
--------------------------------------------------------------------------------


### `abstract def firstKey: K`                                               ###

Returns the first key of the collection.

(defined at scala.collection.generic.Sorted)


### `def compare(k0: K, k1: K): Int`                                         ###

Comparison function that orders keys.

(defined at scala.collection.generic.Sorted)


### `def from(from: K): This`                                                ###

Creates a ranged projection of this collection with no upper-bound.

* from
  * The lower-bound (inclusive) of the ranged projection.

(defined at scala.collection.generic.Sorted)


### `def hasAll(j: Iterator[K]): Boolean`                                    ###

* Attributes
  * protected

(defined at scala.collection.generic.Sorted)


### `def range(from: K, until: K): This`                                     ###

Creates a ranged projection of this collection with both a lower-bound and an
upper-bound.

* from
  * The lower-bound (inclusive) of the ranged projection.
* until
  * The upper-bound (exclusive) of the ranged projection.

(defined at scala.collection.generic.Sorted)


### `def to(to: K): This`                                                    ###

Create a range projection of this collection with no lower-bound.

* to
  * The upper-bound (inclusive) of the ranged projection.

(defined at scala.collection.generic.Sorted)


### `def until(until: K): This`                                              ###

Creates a ranged projection of this collection with no lower-bound.

* until
  * The upper-bound (exclusive) of the ranged projection.
(defined at scala.collection.generic.Sorted)
