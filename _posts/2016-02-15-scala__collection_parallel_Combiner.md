
#                      scala.collection.parallel.Combiner                      #

```scala
trait Combiner[-Elem, +To] extends Builder[Elem, To] with Sizing with Parallel
```

The base trait for all combiners. A combiner incremental collection construction
just like a regular builder, but also implements an efficient merge operation of
two builders via `combine` method. Once the collection is constructed, it may be
obtained by invoking the `result` method.

The complexity of the `combine` method should be less than linear for best
performance. The `result` method doesn't have to be a constant time operation,
but may be performed in parallel.

* Elem
  * the type of the elements added to the builder
* To
  * the type of the collection the builder produces

* Source
  * [Combiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/Combiner.scala#L1)
* Since
  * 2.9


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[Elem]): Combiner.this.type`                 ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: Elem, elem2: Elem, elems: Elem*): Combiner.this.type`     ###

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
          Abstract Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `abstract def +=(elem: Elem): Combiner.this.type`                        ###

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


### `abstract def clear(): Unit`                                             ###

Clears the contents of this builder. After execution of this method the builder
will contain no elements.

* Definition Classes
  * Builder → Growable → Clearable

(defined at scala.collection.mutable.Builder)


### `def mapResult[NewTo](f: (To) ⇒ NewTo): Builder[Elem, NewTo]`            ###

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
         Abstract Value Members From scala.collection.parallel.Combiner
--------------------------------------------------------------------------------


### `abstract def combine[N <: Elem, NewTo >: To](other: Combiner[N, NewTo]): Combiner[N, NewTo]` ###

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

(defined at scala.collection.parallel.Combiner)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.parallel.Combiner
--------------------------------------------------------------------------------


### `var _combinerTaskSupport: TaskSupport`                                  ###

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport: TaskSupport`                                   ###

(defined at scala.collection.parallel.Combiner)


### `def combinerTaskSupport_=(cts: TaskSupport): Unit`                      ###

(defined at scala.collection.parallel.Combiner)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Combiner [Elem, To] to
    CollectionsHaveToParArray [Combiner [Elem, To], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Combiner [Elem, To]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
