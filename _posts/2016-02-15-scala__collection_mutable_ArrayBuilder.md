
#                    scala.collection.mutable.ArrayBuilder                    #

```scala
abstract class ArrayBuilder[T] extends ReusableBuilder[T, Array[T]] with Serializable
```

A builder class for arrays.

* T
  * the type of the elements for the builder.

* Source
  * [ArrayBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/ArrayBuilder.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[T]): ArrayBuilder.this.type`                ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: T, elem2: T, elems: T*): ArrayBuilder.this.type`          ###

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
        Instance Constructors From scala.collection.mutable.ArrayBuilder
--------------------------------------------------------------------------------


### `new ArrayBuilder()`                                                     ###

(defined at scala.collection.mutable.ArrayBuilder)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `abstract def +=(elem: T): ArrayBuilder.this.type`                       ###

Adds a single element to the builder.

* elem
  * the element to be added.
* returns
  * the builder itself.

* Definition Classes
  * Builder → Growable

(defined at scala.collection.mutable.Builder)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (Array[T]) ⇒ NewTo): Builder[T, NewTo]`         ###

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
      Abstract Value Members From scala.collection.mutable.ReusableBuilder
--------------------------------------------------------------------------------


### `abstract def result(): Array[T]`                                        ###

Produces a collection from the added elements.

After a call to `result` , the behavior of all other methods is undefined save
for `clear` . If `clear` is called, then the builder is reset and may be used to
build another instance.

* returns
  * a collection containing the elements added to this builder.

* Definition Classes
  * ReusableBuilder → Builder

(defined at scala.collection.mutable.ReusableBuilder)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.mutable.ReusableBuilder
--------------------------------------------------------------------------------


### `abstract def clear(): Unit`                                             ###

Clears the contents of this builder. After execution of this method, the builder
will contain no elements.

If executed immediately after a call to `result` , this allows a new instance of
the same type of collection to be built.

* Definition Classes
  * ReusableBuilder → Builder → Growable → Clearable
(defined at scala.collection.mutable.ReusableBuilder)
