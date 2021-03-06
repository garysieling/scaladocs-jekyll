
#                 scala.collection.mutable.WrappedArrayBuilder                 #

```scala
class WrappedArrayBuilder[A] extends ReusableBuilder[A, WrappedArray[A]]
```

A builder class for arrays.

This builder can be reused.

* A
  * type of elements that can be added to this builder.

* Source
  * [WrappedArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/WrappedArrayBuilder.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
              Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[A]): WrappedArrayBuilder.this.type`         ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: A, elem2: A, elems: A*): WrappedArrayBuilder.this.type`   ###

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


### `def mapResult[NewTo](f: (WrappedArray[A]) ⇒ NewTo): Builder[A, NewTo]`  ###

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
   Deprecated Value Members From scala.collection.mutable.WrappedArrayBuilder
--------------------------------------------------------------------------------


### `val manifest: ClassTag[A]`                                              ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use tag instead

(defined at scala.collection.mutable.WrappedArrayBuilder)


--------------------------------------------------------------------------------
    Instance Constructors From scala.collection.mutable.WrappedArrayBuilder
--------------------------------------------------------------------------------


### `new WrappedArrayBuilder(tag: ClassTag[A])`                              ###

* tag
  * class tag for objects of type `A` .

(defined at scala.collection.mutable.WrappedArrayBuilder)


--------------------------------------------------------------------------------
        Value Members From scala.collection.mutable.WrappedArrayBuilder
--------------------------------------------------------------------------------


### `def +=(elem: A): WrappedArrayBuilder.this.type`                         ###

Adds a single element to the builder.

* elem
  * the element to be added.
* returns
  * the builder itself.

* Definition Classes
  * WrappedArrayBuilder → Builder → Growable

(defined at scala.collection.mutable.WrappedArrayBuilder)


### `def result(): WrappedArray[A]`                                          ###

Produces a collection from the added elements.

After a call to `result` , the behavior of all other methods is undefined save
for `clear` . If `clear` is called, then the builder is reset and may be used to
build another instance.

* returns
  * a collection containing the elements added to this builder.

* Definition Classes
  * WrappedArrayBuilder → ReusableBuilder → Builder

(defined at scala.collection.mutable.WrappedArrayBuilder)


### `def sizeHint(size: Int): Unit`                                          ###

Gives a hint how many elements are expected to be added when the next `result`
is called. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.

* Definition Classes
  * WrappedArrayBuilder → Builder

(defined at scala.collection.mutable.WrappedArrayBuilder)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedArrayBuilder [A]
    to CollectionsHaveToParArray [WrappedArrayBuilder [A], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    WrappedArrayBuilder [A]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
