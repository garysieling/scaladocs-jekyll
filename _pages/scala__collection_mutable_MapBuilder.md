
#                     scala.collection.mutable.MapBuilder                     #

```scala
class MapBuilder[A, B, Coll <: GenMap[A, B] with GenMapLike[A, B, Coll]] extends ReusableBuilder[(A, B), Coll]
```

The canonical builder for immutable maps, working with the map's `+` method to
add new elements. Collections are built from their `empty` element using this +
method.

* A
  * Type of the keys for the map this builder creates.
* B
  * Type of the values for the map this builder creates.
* Coll
  * The type of the actual collection this builder builds.

* Source
  * [MapBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/MapBuilder.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
              Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[(A, B)]): MapBuilder.this.type`             ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: (A, B), elem2: (A, B), elems: (A, B)*): MapBuilder.this.type` ###

adds two or more elements to this growable collection.

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * the growable collection itself

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (Coll) ⇒ NewTo): Builder[(A, B), NewTo]`        ###

Creates a new builder by applying a transformation function to the results of
this builder.

* NewTo
  * the type of collection returned by `f` .
* f
  * the transformation function.
* returns
  * a new builder which is the same as the current builder except that a
    transformation function is applied to this builder's result.

* Definition Classes
  * Builder
* Note
  * The original builder should no longer be used after `mapResult` is called.

(defined at scala.collection.mutable.Builder)


### `def sizeHint(size: Int): Unit`                                          ###

Gives a hint how many elements are expected to be added when the next `result`
is called. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _]): Unit`                        ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _], delta: Int): Unit`            ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.
* delta
  * a correction to add to the `coll.size` to produce the size hint.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHintBounded(size: Int, boundingColl: TraversableLike[_, _]): Unit` ###

Gives a hint how many elements are expected to be added when the next `result`
is called, together with an upper bound given by the size of some other
collection. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.
* boundingColl
  * the bounding collection. If it is an IndexedSeqLike, then sizes larger than
    collection's size are reduced.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


--------------------------------------------------------------------------------
         Instance Constructors From scala.collection.mutable.MapBuilder
--------------------------------------------------------------------------------


### `new MapBuilder(empty: Coll)`                                            ###

* empty
  * The empty element of the collection.

(defined at scala.collection.mutable.MapBuilder)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.MapBuilder
--------------------------------------------------------------------------------


### `def +=(x: (A, B)): MapBuilder.this.type`                                ###

Adds a single element to the builder.

* returns
  * the builder itself.

* Definition Classes
  * MapBuilder → Builder → Growable

(defined at scala.collection.mutable.MapBuilder)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from MapBuilder [A, B, Coll]
    to CollectionsHaveToParArray [MapBuilder [A, B, Coll], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (MapBuilder [A,
    B, Coll]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
