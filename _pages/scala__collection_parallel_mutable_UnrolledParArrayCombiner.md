
#          scala.collection.parallel.mutable.UnrolledParArrayCombiner          #

```scala
trait UnrolledParArrayCombiner[T] extends Combiner[T, ParArray[T]]
```

An array combiner that uses doubling unrolled buffers to store elements.

* Source
  * [UnrolledParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/UnrolledParArrayCombiner.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class CopyUnrolledToArray extends Task[Unit, CopyUnrolledToArray]`      ###

* Source
  * [UnrolledParArrayCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/UnrolledParArrayCombiner.scala#L1)


--------------------------------------------------------------------------------
              Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[T]): UnrolledParArrayCombiner.this.type`    ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: T, elem2: T, elems: T*): UnrolledParArrayCombiner.this.type` ###

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


### `def mapResult[NewTo](f: (ParArray[T]) ⇒ NewTo): Builder[T, NewTo]`      ###

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
             Value Members From scala.collection.parallel.Combiner
--------------------------------------------------------------------------------


### `var _combinerTaskSupport: TaskSupport`                                  ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport: TaskSupport`                                   ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport_=(cts: TaskSupport): Unit`                      ###

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


### `def resultWithTaskSupport: ParArray[T]`                                 ###

Constructs the result and sets the appropriate tasksupport object to the
resulting collection if this is applicable.

* Definition Classes
  * Combiner

(defined at scala.collection.parallel.Combiner)


--------------------------------------------------------------------------------
 Value Members From scala.collection.parallel.mutable.UnrolledParArrayCombiner
--------------------------------------------------------------------------------


### `def +=(elem: T): UnrolledParArrayCombiner.this.type`                    ###

Adds a single element to the builder.

* elem
  * the element to be added.
* returns
  * the builder itself.

* Definition Classes
  * UnrolledParArrayCombiner → Builder → Growable

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner)


### `val buff: DoublingUnrolledBuffer[Any]`                                  ###

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner)


### `def combine[N <: T, NewTo >: ParArray[T]](other: Combiner[N, NewTo]): Combiner[N, NewTo]` ###

Combines the contents of the receiver builder and the `other` builder, producing
a new builder containing both their elements.

This method may combine the two builders by copying them into a larger
collection, by producing a lazy view that gets evaluated once `result` is
invoked, or use a merge operation specific to the data structure in question.

Note that both the receiver builder and `other` builder become invalidated after
the invocation of this method, and should be cleared (see `clear` ) if they are
to be used again.

Also, combining two combiners `c1` and `c2` for which `c1 eq c2` is `true` ,
that is, they are the same objects in memory:

```scala
c1.combine(c2)
```

always does nothing and returns `c1` .

* N
  * the type of elements contained by the `other` builder
* NewTo
  * the type of collection produced by the `other` builder
* other
  * the other builder
* returns
  * the parallel builder containing both the elements of this and the `other`
    builder

* Definition Classes
  * UnrolledParArrayCombiner → Combiner

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner)


### `def result(): ParArray[T]`                                              ###

Produces a collection from the added elements. This is a terminal operation: the
builder's contents are undefined after this operation, and no further methods
should be called.

* returns
  * a collection containing the elements added to this builder.

* Definition Classes
  * UnrolledParArrayCombiner → Builder

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner)


### `def sizeHint(sz: Int): Unit`                                            ###

Gives a hint how many elements are expected to be added when the next `result`
is called. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* Definition Classes
  * UnrolledParArrayCombiner → Builder

(defined at scala.collection.parallel.mutable.UnrolledParArrayCombiner)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from UnrolledParArrayCombiner
    [T] to CollectionsHaveToParArray [UnrolledParArrayCombiner [T], T] performed
    by method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    UnrolledParArrayCombiner [T]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
