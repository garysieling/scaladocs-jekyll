
#                 scala.collection.IterableViewLike#EmptyView                 #

```scala
trait EmptyView extends Transformed[Nothing] with IterableViewLike.EmptyView
```

* Source
  * [IterableViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/IterableViewLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Appended[B >: A] extends IterableViewLike.Appended[B] with Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `trait DroppedWhile extends IterableViewLike.DroppedWhile with Transformed[A]` ###

* Definition Classes
  * IterableViewLike


### `trait EmptyView extends Transformed[Nothing] with IterableViewLike.EmptyView` ###

* Definition Classes
  * IterableViewLike


### `trait Filtered extends IterableViewLike.Filtered with Transformed[A]`   ###

* Definition Classes
  * IterableViewLike


### `trait FlatMapped[B] extends IterableViewLike.FlatMapped[B] with Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `trait Forced[B] extends IterableViewLike.Forced[B] with Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `trait Mapped[B] extends IterableViewLike.Mapped[B] with Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `trait Prepended[B >: A] extends IterableViewLike.Prepended[B] with Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `type Self = IterableView[Nothing, Coll]`                                ###

The type implementing this traversable

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike


### `trait Sliced extends IterableViewLike.Sliced with Transformed[A]`       ###

* Definition Classes
  * IterableViewLike


### `trait TakenWhile extends IterableViewLike.TakenWhile with Transformed[A]` ###

* Definition Classes
  * IterableViewLike


### `trait Transformed[+B] extends IterableView[B, Coll] with IterableViewLike.Transformed[B]` ###

* Definition Classes
  * IterableViewLike


### `class WithFilter extends FilterMonadic[A, Repr]`                        ###

A class supporting filtered operations. Instances of this class are returned by
method `withFilter` .

* Definition Classes
  * TraversableLike


### `trait Zipped[B] extends Transformed[(A, B)]`                            ###

* Definition Classes
  * IterableViewLike


### `trait ZippedAll[A1 >: A, B] extends Transformed[(A1, B)]`               ###

* Definition Classes
  * IterableViewLike


--------------------------------------------------------------------------------
                  Value Members From scala.collection.Iterable
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[Iterable]`                              ###

The factory companion object that builds instances of class Iterable. (or its
 `Iterable` superclass where class Iterable is not a `Seq` .)

* Definition Classes
  * Iterable → GenIterable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.Iterable)


### `def seq: Iterable[Nothing]`                                             ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Iterable → GenIterable → Traversable → GenTraversable → Parallelizable →
    TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterable)


--------------------------------------------------------------------------------
                Value Members From scala.collection.IterableLike
--------------------------------------------------------------------------------


### `def canEqual(that: Any): Boolean`                                       ###

Method called from equality methods, so that user-defined subclasses can refuse
to be equal to other collections of the same kind.

* that
  * The object with which this iterable collection should be compared
* returns
  * `true` , if this iterable collection can possibly equal `that` , `false`
    otherwise. The test takes into consideration only the run-time types of
    objects but ignores their elements.

* Definition Classes
  * IterableLike → Equals

(defined at scala.collection.IterableLike)


### `def copyToArray[B >: Nothing](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this iterable collection to an array. Fills the given
array `xs` with at most `len` elements of this iterable collection, starting at
position `start` . Copying will stop once either the end of the current iterable
collection is reached, or the end of the target array is reached, or `len`
elements have been copied.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def exists(p: (Nothing) ⇒ Boolean): Boolean`                            ###

Tests whether a predicate holds for at least one element of this iterable
collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `false` if this iterable collection is empty, otherwise `true` if the given
    predicate `p` holds for some of the elements of this iterable collection,
    otherwise `false`

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def find(p: (Nothing) ⇒ Boolean): Option[Nothing]`                      ###

Finds the first element of the iterable collection satisfying a predicate, if
any.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the iterable collection that
    satisfies `p` , or `None` if none exists.

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def foldRight[B](z: B)(op: (Nothing, B) ⇒ B): B`                        ###

Applies a binary operator to all elements of this iterable collection and a
start value, going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this iterable collection. Returns
     `z` if this iterable collection is empty.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def forall(p: (Nothing) ⇒ Boolean): Boolean`                            ###

Tests whether a predicate holds for all elements of this iterable collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this iterable collection is empty or the given predicate `p` holds
    for all elements of this iterable collection, otherwise `false` .

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def head: Nothing`                                                      ###

Selects the first element of this iterable collection.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the iterable collection is empty.

(defined at scala.collection.IterableLike)


### `def reduceRight[B >: Nothing](op: (Nothing, B) ⇒ B): B`                 ###

Applies a binary operator to all elements of this iterable collection, going
right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this iterable collection is empty.

(defined at scala.collection.IterableLike)


### `def sameElements[B >: Nothing](that: GenIterable[B]): Boolean`          ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this iterable collection.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def thisCollection: Iterable[Nothing]`                                  ###

The underlying collection seen as an instance of `Iterable` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toCollection(repr: IterableView[Nothing, Coll]): Iterable[Nothing]` ###

A conversion from collections of type `Repr` to `Iterable` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: Iterable[Nothing]`                                      ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[Nothing]`                                      ###

Returns an Iterator over the elements in this iterable collection. Produces the
same result as `iterator` .

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.IterableLike)


### `def toStream: immutable.Stream[Nothing]`                                ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def view(from: Int, until: Int): IterableView[Nothing, IterableView[Nothing, Coll]]` ###

Creates a non-strict view of a slice of this iterable collection.

Note: the difference between `view` and `slice` is that `view` produces a view
of the current iterable collection, whereas `slice` produces a new iterable
collection.

Note: `view(from, to)` is equivalent to `view.slice(from, to)`

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* from
  * the index of the first element of the view
* until
  * the index of the element following the view
* returns
  * a non-strict view of a slice of this iterable collection, starting at index
     `from` and extending up to (but not including) index `until` .

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def view: IterableView[Nothing, IterableView[Nothing, Coll]]`           ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
              Value Members From scala.collection.IterableViewLike
--------------------------------------------------------------------------------


### `def drop(n: Int): IterableView[Nothing, Coll]`                          ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this iterable collection.
* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the first `n` ones, or else the empty iterable collection, if this
    iterable collection has less than `n` elements.

* Definition Classes
  * IterableViewLike → TraversableViewLike → IterableLike → TraversableLike →
    GenTraversableLike

(defined at scala.collection.IterableViewLike)


### `def dropRight(n: Int): IterableView[Nothing, Coll]`                     ###

Selects all elements except last _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * The number of elements to take
* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the last `n` ones, or else the empty iterable collection, if this
    iterable collection has less than `n` elements.

* Definition Classes
  * IterableViewLike → IterableLike

(defined at scala.collection.IterableViewLike)


### `def grouped(size: Int): Iterator[IterableView[Nothing, Coll]]`          ###

Partitions elements in fixed size iterable collections.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    will be less than size `size` if the elements don't divide evenly.

* Definition Classes
  * IterableViewLike → IterableLike
* See also
  * scala.collection.Iterator, method `grouped`

(defined at scala.collection.IterableViewLike)


### `def newAppended[B >: Nothing](that: GenTraversable[B]): Transformed[B]` ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newDropped(n: Int): Transformed[Nothing]`                           ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newDroppedWhile(p: (Nothing) ⇒ Boolean): Transformed[Nothing]`      ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newFiltered(p: (Nothing) ⇒ Boolean): Transformed[Nothing]`          ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newFlatMapped[B](f: (Nothing) ⇒ GenTraversableOnce[B]): Transformed[B]` ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newForced[B](xs: ⇒ GenSeq[B]): Transformed[B]`                      ###

Boilerplate method, to override in each subclass This method could be eliminated
if Scala had virtual classes

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newMapped[B](f: (Nothing) ⇒ B): Transformed[B]`                     ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newPrepended[B >: Nothing](that: GenTraversable[B]): Transformed[B]` ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newSliced(_endpoints: SliceInterval): Transformed[Nothing]`         ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newTaken(n: Int): Transformed[Nothing]`                             ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newTakenWhile(p: (Nothing) ⇒ Boolean): Transformed[Nothing]`        ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike → TraversableViewLike

(defined at scala.collection.IterableViewLike)


### `def newZippedAll[A1 >: Nothing, B](that: GenIterable[B], _thisElem: A1, _thatElem: B): Transformed[(A1, B)]` ###

* Attributes
  * protected
* Definition Classes
  * IterableViewLike

(defined at scala.collection.IterableViewLike)


### `def newZipped[B](that: GenIterable[B]): Transformed[(Nothing, B)]`      ###

Boilerplate method, to override in each subclass This method could be eliminated
if Scala had virtual classes

* Attributes
  * protected
* Definition Classes
  * IterableViewLike

(defined at scala.collection.IterableViewLike)


### `def sliding(size: Int): Iterator[IterableView[Nothing, Coll]]`          ###

Groups elements in fixed size blocks by passing a "sliding window" over them (as
opposed to partitioning them, as is done in grouped.) "Sliding window" step is 1
by default.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    and the only element will be truncated if there are fewer elements than
    size.

* Definition Classes
  * IterableViewLike → IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableViewLike)


### `def sliding(size: Int, step: Int): Iterator[IterableView[Nothing, Coll]]` ###

Groups elements in fixed size blocks by passing a "sliding window" over them (as
opposed to partitioning them, as is done in grouped.)

* size
  * the number of elements per group
* step
  * the distance between the first elements of successive groups
* returns
  * An iterator producing iterable collections of size `size` , except the last
    and the only element will be truncated if there are fewer elements than
    size.

* Definition Classes
  * IterableViewLike → IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableViewLike)


### `def take(n: Int): IterableView[Nothing, Coll]`                          ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this iterable collection.
* returns
  * a iterable collection consisting only of the first `n` elements of this
    iterable collection, or else the whole iterable collection, if it has less
    than `n` elements.

* Definition Classes
  * IterableViewLike → TraversableViewLike → IterableLike → TraversableLike →
    GenTraversableLike

(defined at scala.collection.IterableViewLike)


### `def takeRight(n: Int): IterableView[Nothing, Coll]`                     ###

Selects last _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take
* returns
  * a iterable collection consisting only of the last `n` elements of this
    iterable collection, or else the whole iterable collection, if it has less
    than `n` elements.

* Definition Classes
  * IterableViewLike → IterableLike

(defined at scala.collection.IterableViewLike)


### `def zipAll[B, A1 >: Nothing, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], (A1, B), That]): That` ###

[use case]

Returns a iterable collection formed from this iterable collection and another
iterable collection by combining corresponding elements in pairs. If one of the
two collections is shorter than the other, placeholder elements are used to
extend the shorter collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this iterable collection is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    iterable collection.
* returns
  * a new iterable collection containing pairs consisting of corresponding
    elements of this iterable collection and `that` . The length of the returned
    collection is the maximum of the lengths of this iterable collection and
     `that` . If this iterable collection is shorter than `that` , `thisElem`
    values are used to pad the result. If `that` is shorter than this iterable
    collection, `thatElem` values are used to pad the result.

* Definition Classes
  * IterableViewLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableViewLike)


### `def zip[A1 >: Nothing, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], (A1, B), That]): That` ###

[use case]

Returns a iterable collection formed from this iterable collection and another
iterable collection by combining corresponding elements in pairs. If one of the
two collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new iterable collection containing pairs consisting of corresponding
    elements of this iterable collection and `that` . The length of the returned
    collection is the minimum of the lengths of this iterable collection and
     `that` .

* Definition Classes
  * IterableViewLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableViewLike)


--------------------------------------------------------------------------------
               Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParIterable[Nothing]`                                          ###

Returns a parallel implementation of this collection.

For most collection types, this method creates a new parallel collection by
copying all the elements. For these collection, `par` takes linear time. Mutable
collections in this category do not produce a mutable parallel collection that
has the same underlying dataset, so changes in one collection will not be
reflected in the other one.

Specific collections (e.g. `ParArray` or `mutable.ParHashMap` ) override this
default behaviour by creating a parallel collection which shares the same
underlying dataset. For these collections, `par` takes constant or sublinear
time.

All parallel collections return a reference to themselves.

* returns
  * a parallel implementation of this collection

* Definition Classes
  * Parallelizable

(defined at scala.collection.Parallelizable)


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def last: Nothing`                                                      ###

Selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * The last element of this traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the traversable collection is empty.

(defined at scala.collection.TraversableLike)


### `def parCombiner: Combiner[Nothing, ParIterable[Nothing]]`               ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike → Parallelizable

(defined at scala.collection.TraversableLike)


### `def repr: IterableView[Nothing, Coll]`                                  ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scan[B >: Nothing, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

Computes a prefix scan of the elements of the collection.

Note: The neutral element `z` may be applied more than once.

* B
  * element type of the resulting collection
* That
  * type of the resulting collection
* z
  * neutral element for the operator `op`
* op
  * the associative operator for the scan
* cbf
  * combiner factory which provides a combiner
* returns
  * a new traversable collection containing the prefix scan of the elements in
    this traversable collection

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def toTraversable: Traversable[Nothing]`                                ###

Converts this traversable collection to an unspecified Traversable. Will return
the same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this traversable collection.

* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.TraversableLike)


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableOnce
--------------------------------------------------------------------------------


### `def /:[B](z: B)(op: (B, Nothing) ⇒ B): B`                               ###

Applies a binary operator to a start value and all elements of this traversable
or iterator, going left to right.

Note: `/:` is alternate syntax for `foldLeft` ; `z /: xs` is the same as
 `xs foldLeft z` .

Examples:

Note that the folding function used to compute b is equivalent to that used to
compute c.

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = (5 /: a)(_+_)
b: Int = 15

scala> val c = (5 /: a)((x,y) => x + y)
c: Int = 15
```

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable or iterator, going left to right with the start value `z` on the
    left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def :\[B](z: B)(op: (Nothing, B) ⇒ B): B`                               ###

Applies a binary operator to all elements of this traversable or iterator and a
start value, going right to left.

Note: `:\` is alternate syntax for `foldRight` ; `xs :\ z` is the same as
 `xs foldRight z` .

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

Examples:

Note that the folding function used to compute b is equivalent to that used to
compute c.

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = (a :\ 5)(_+_)
b: Int = 15

scala> val c = (a :\ 5)((x,y) => x + y)
c: Int = 15
```

* B
  * the result type of the binary operator.
* z
  * the start value
* op
  * the binary operator
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable or iterator, going right to left with the start value `z` on the
    right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def addString(b: StringBuilder): StringBuilder`                         ###

Appends all elements of this traversable or iterator to a string builder. The
written text consists of the string representations (w.r.t. the method
 `toString` ) of all elements of this traversable or iterator without any
separator string.

Example:

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = new StringBuilder()
b: StringBuilder =

scala> val h = a.addString(b)
h: StringBuilder = 1234
```

* b
  * the string builder to which elements are appended.
* returns
  * the string builder `b` to which elements were appended.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def addString(b: StringBuilder, sep: String): StringBuilder`            ###

Appends all elements of this traversable or iterator to a string builder using a
separator string. The written text consists of the string representations
(w.r.t. the method `toString` ) of all elements of this traversable or iterator,
separated by the string `sep` .

Example:

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = new StringBuilder()
b: StringBuilder =

scala> a.addString(b, ", ")
res0: StringBuilder = 1, 2, 3, 4
```

* b
  * the string builder to which elements are appended.
* sep
  * the separator string.
* returns
  * the string builder `b` to which elements were appended.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def aggregate[B](z: ⇒ B)(seqop: (B, Nothing) ⇒ B, combop: (B, B) ⇒ B): B` ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It is similar to
 `foldLeft` in that it doesn't require the result to be a supertype of the
element type. In addition, it allows parallel collections to be processed in
chunks, and then combines the intermediate results.

 `aggregate` splits the traversable or iterator into partitions and processes
each partition by sequentially applying `seqop` , starting with `z` (like
 `foldLeft` ). Those intermediate results are then combined by using `combop`
(like `fold` ). The implementation of this operation may operate on an arbitrary
number of collection partitions (even 1), so `combop` may be invoked an
arbitrary number of times (even 0).

As an example, consider summing up the integer values of a list of chars. The
initial value for the sum is 0. First, `seqop` transforms each input character
to an Int and adds it to the sum (of the partition). Then, `combop` just needs
to sum up the intermediate results of the partitions:

```scala
List('a', 'b', 'c').aggregate(0)({ (sum, ch) => sum + ch.toInt }, { (p1, p2) => p1 + p2 })
```

* B
  * the type of accumulated results
* z
  * the initial value for the accumulated result of the partition - this will
    typically be the neutral element for the `seqop` operator (e.g. `Nil` for
    list concatenation or `0` for summation) and may be evaluated more than once
* seqop
  * an operator used to accumulate results within a partition
* combop
  * an associative operator used to combine results from different partitions

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def collectFirst[B](pf: PartialFunction[Nothing, B]): Option[B]`        ###

Finds the first element of the traversable or iterator for which the given
partial function is defined, and applies the partial function to it.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pf
  * the partial function
* returns
  * an option value containing pf applied to the first value for which it is
    defined, or `None` if none exists.

* Definition Classes
  * TraversableOnce

Example:

```scala
Seq("a", 1, 5L).collectFirst({ case x: Int => x*10 }) = Some(10)
```

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: Nothing](xs: Array[B]): Unit`                      ###

[use case]

Copies the elements of this iterable collection to an array. Fills the given
array `xs` with values of this iterable collection. Copying will stop once
either the end of the current iterable collection is reached, or the end of the
target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: Nothing](xs: Array[B], start: Int): Unit`          ###

[use case]

Copies the elements of this iterable collection to an array. Fills the given
array `xs` with values of this iterable collection, beginning at index `start` .
Copying will stop once either the end of the current iterable collection is
reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: Nothing](dest: Buffer[B]): Unit`                  ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: (Nothing) ⇒ Boolean): Int`                                 ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, Nothing) ⇒ B): B`                         ###

Applies a binary operator to a start value and all elements of this traversable
or iterator, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable or iterator, going left to right with the start value `z` on the
    left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.
    Returns `z` if this traversable or iterator is empty.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def fold[A1 >: Nothing](z: A1)(op: (A1, A1) ⇒ A1): A1`                  ###

Folds the elements of this traversable or iterator using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

Note: will not terminate for infinite-sized collections.

* A1
  * a type parameter for the binary operator, a supertype of `A` .
* z
  * a neutral element for the fold operation; may be added to the result an
    arbitrary number of times, and must not change the result (e.g., `Nil` for
    list concatenation, 0 for addition, or 1 for multiplication).
* op
  * a binary operator that must be associative.
* returns
  * the result of applying the fold operator `op` between all the elements and
     `z` , or `z` if this traversable or iterator is empty.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def maxBy[B](f: (Nothing) ⇒ B)(implicit cmp: Ordering[B]): Nothing`     ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this iterable collection with the largest value
    measured by function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: (Nothing) ⇒ B)(implicit cmp: Ordering[B]): Nothing`     ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this iterable collection with the smallest value
    measured by function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduceLeftOption[B >: Nothing](op: (B, Nothing) ⇒ B): Option[B]`    ###

Optionally applies a binary operator to all elements of this traversable or
iterator, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this
    traversable or iterator is nonempty, `None` otherwise.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduceLeft[B >: Nothing](op: (B, Nothing) ⇒ B): B`                  ###

Applies a binary operator to all elements of this traversable or iterator, going
left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable or iterator, going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable or iterator is empty.

(defined at scala.collection.TraversableOnce)


### `def reduceOption[A1 >: Nothing](op: (A1, A1) ⇒ A1): Option[A1]`         ###

Reduces the elements of this traversable or iterator, if any, using the
specified associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * An option value containing result of applying reduce operator `op` between
    all the elements if the collection is nonempty, and `None` otherwise.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduceRightOption[B >: Nothing](op: (Nothing, B) ⇒ B): Option[B]`   ###

Optionally applies a binary operator to all elements of this traversable or
iterator, going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this
    traversable or iterator is nonempty, `None` otherwise.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduce[A1 >: Nothing](op: (A1, A1) ⇒ A1): A1`                       ###

Reduces the elements of this traversable or iterator using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    traversable or iterator is nonempty.

* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable or iterator is empty.

(defined at scala.collection.TraversableOnce)


### `def reversed: List[Nothing]`                                            ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toBuffer[B >: Nothing]: Buffer[B]`                                  ###

Uses the contents of this traversable or iterator to create a new mutable
buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[Nothing]`                        ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: List[Nothing]`                                              ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[Nothing, (T, U)]): immutable.Map[T, U]` ###

[use case]

Converts this iterable collection to a map. This method is unavailable unless
the elements are members of Tuple2, each ((T, U)) becoming a key-value pair in
the map. Duplicate keys will be overwritten by later keys: if this is an
unordered collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this iterable collection.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSeq: Seq[Nothing]`                                                ###

Converts this traversable or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: Nothing]: immutable.Set[B]`                              ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: Vector[Nothing]`                                          ###

Converts this traversable or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
            Value Members From scala.collection.TraversableViewLike
--------------------------------------------------------------------------------


### `def ++:[B >: Nothing, That](xs: Traversable[B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

As with `++` , returns a new collection containing the elements from the left
operand followed by the elements from the right operand.

It differs from `++` in that the right operand determines the type of the
resulting collection rather than the left one. Mnemonic: the COLon is on the
side of the new COLlection type.

Example:

```scala
scala> val x = List(1)
x: List[Int] = List(1)

scala> val y = LinkedList(2)
y: scala.collection.mutable.LinkedList[Int] = LinkedList(2)

scala> val z = x ++: y
z: scala.collection.mutable.LinkedList[Int] = LinkedList(1, 2)
```

This overload exists because: for the implementation of `++:` we should reuse
that of `++` because many collections override it with more efficient versions.

Since `TraversableOnce` has no `++` method, we have to implement that directly,
but `Traversable` and down can use the overload.

* B
  * the element type of the returned collection.
* That
  * the class of the returned collection. Where possible, `That` is the same
    class as the current collection class `Repr` , but this depends on the
    element type `B` being admissible for that class, which means that an
    implicit instance of type `CanBuildFrom[Repr, B, That]` is found.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * a new collection of type `That` which contains all elements of this
    collection followed by all elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike

(defined at scala.collection.TraversableViewLike)


### `def ++:[B >: Nothing, That](xs: TraversableOnce[B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

[use case]

As with `++` , returns a new collection containing the elements from the left
operand followed by the elements from the right operand.

It differs from `++` in that the right operand determines the type of the
resulting collection rather than the left one. Mnemonic: the COLon is on the
side of the new COLlection type.

Example:

```scala
scala> val x = List(1)
x: List[Int] = List(1)

scala> val y = LinkedList(2)
y: scala.collection.mutable.LinkedList[Int] = LinkedList(2)

scala> val z = x ++: y
z: scala.collection.mutable.LinkedList[Int] = LinkedList(1, 2)
```

* B
  * the element type of the returned collection.
* that
  * the traversable to append.
* returns
  * a new iterable collection which contains all elements of this iterable
    collection followed by all elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike

(defined at scala.collection.TraversableViewLike)


### `def ++[B >: Nothing, That](xs: GenTraversableOnce[B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

[use case]

Returns a new iterable collection containing the elements from the left hand
operand followed by the elements from the right hand operand. The element type
of the iterable collection is the most specific superclass encompassing the
element types of the two operands.

Example:

```scala
scala> val a = List(1)
a: List[Int] = List(1)

scala> val b = List(2)
b: List[Int] = List(2)

scala> val c = a ++ b
c: List[Int] = List(1, 2)

scala> val d = List('a')
d: List[Char] = List(a)

scala> val e = c ++ d
e: List[AnyVal] = List(1, 2, a)
```

* B
  * the element type of the returned collection.
* that
  * the traversable to append.
* returns
  * a new iterable collection which contains all elements of this iterable
    collection followed by all elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def collect[B, That](pf: PartialFunction[Nothing, B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
iterable collection on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the iterable collection.
* returns
  * a new iterable collection resulting from applying the given partial function
     `pf` to each element on which it is defined and collecting the results. The
    order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def dropWhile(p: (Nothing) ⇒ Boolean): IterableView[Nothing, Coll]`     ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this collection whose first element does not satisfy
    the predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filter(p: (Nothing) ⇒ Boolean): IterableView[Nothing, Coll]`        ###

Selects all elements of this collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that satisfy
    the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filterNot(p: (Nothing) ⇒ Boolean): IterableView[Nothing, Coll]`     ###

Selects all elements of this collection which do not satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that do not
    satisfy the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def flatMap[B, That](f: (Nothing) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this iterable
collection and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of iterable
collection. This might cause unexpected results sometimes. For example:

```scala
// lettersOf will return a Seq[Char] of likely repeated letters, instead of a Set
def lettersOf(words: Seq[String]) = words flatMap (word => word.toSet)

// lettersOf will return a Set[Char], not a Seq
def lettersOf(words: Seq[String]) = words.toSet flatMap (word => word.toSeq)

// xs will be an Iterable[Int]
val xs = Map("a" -> List(11,111), "b" -> List(22,222)).flatMap(_._2)

// ys will be a Map[Int, Int]
val ys = Map("a" -> List(1 -> 11,1 -> 111), "b" -> List(2 -> 22,2 -> 222)).flatMap(_._2)
```

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new iterable collection resulting from applying the given
    collection-valued function `f` to each element of this iterable collection
    and concatenating the results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def force[B >: Nothing, That](implicit bf: CanBuildFrom[Coll, B, That]): That` ###

* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def groupBy[K](f: (Nothing) ⇒ K): immutable.Map[K, IterableView[Nothing, Coll]]` ###

Partitions this collection into a map of collections according to some
discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new collection.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to collections such that the following invariant holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a collection of those elements `x` for
    which `f(x)` equals `k` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def init: IterableView[Nothing, Coll]`                                  ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection consisting of all elements of this collection except the last
    one.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the collection is empty.

(defined at scala.collection.TraversableViewLike)


### `def inits: Iterator[IterableView[Nothing, Coll]]`                       ###

Iterates over the inits of this collection. The first value will be this
collection and the final one will be an empty collection, with the intervening
values the results of successive applications of `init` .

* returns
  * an iterator over all the inits of this collection

* Definition Classes
  * TraversableViewLike → TraversableLike

Example:

```scala
List(1,2,3).inits = Iterator(List(1,2,3), List(1,2), List(1), Nil)
```

(defined at scala.collection.TraversableViewLike)


### `def map[B, That](f: (Nothing) ⇒ B)(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this iterable
collection.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new iterable collection resulting from applying the given function `f` to
    each element of this iterable collection and collecting the results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def newBuilder: Builder[Nothing, IterableView[Nothing, Coll]]`          ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * TraversableViewLike → GenericTraversableTemplate → TraversableLike →
    HasNewBuilder

(defined at scala.collection.TraversableViewLike)


### `def partition(p: (Nothing) ⇒ Boolean): (IterableView[Nothing, Coll], IterableView[Nothing, Coll])` ###

Partitions this collection in two collections according to a predicate.

* p
  * the predicate on which to partition.
* returns
  * a pair of collections: the first collection consists of all elements that
    satisfy the predicate `p` and the second collection consists of all elements
    that don't. The relative order of the elements in the resulting collections
    is the same as in the original collection.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def scanLeft[B, That](z: B)(op: (B, Nothing) ⇒ B)(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the elements in the resulting collection
* That
  * the actual type of the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * collection with intermediate results

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def scanRight[B, That](z: B)(op: (Nothing, B) ⇒ B)(implicit bf: CanBuildFrom[IterableView[Nothing, Coll], B, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going right to left. The head of the collection is the last cumulative result.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Example:

```scala
List(1, 2, 3, 4).scanRight(0)(_ + _) == List(10, 9, 7, 4, 0)
```

* B
  * the type of the elements in the resulting collection
* That
  * the actual type of the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * collection with intermediate results

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(defined at scala.collection.TraversableViewLike)


### `def slice(from: Int, until: Int): IterableView[Nothing, Coll]`          ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection containing the elements greater than or equal to index `from`
    extending up to (but not including) index `until` of this collection.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def span(p: (Nothing) ⇒ Boolean): (IterableView[Nothing, Coll], IterableView[Nothing, Coll])` ###

Splits this collection into a prefix/suffix pair according to a predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a pair consisting of the longest prefix of this collection whose elements
    all satisfy `p` , and the rest of this collection.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def splitAt(n: Int): (IterableView[Nothing, Coll], IterableView[Nothing, Coll])` ###

Splits this collection into two at a given position. Note: `c splitAt n` is
equivalent to (but possibly more efficient than) `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of collections consisting of the first `n` elements of this
    collection, and the other elements.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def tail: IterableView[Nothing, Coll]`                                  ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection consisting of all elements of this collection except the first
    one.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the collection is empty.

(defined at scala.collection.TraversableViewLike)


### `def tails: Iterator[IterableView[Nothing, Coll]]`                       ###

Iterates over the tails of this collection. The first value will be this
collection and the final one will be an empty collection, with the intervening
values the results of successive applications of `tail` .

* returns
  * an iterator over all the tails of this collection

* Definition Classes
  * TraversableViewLike → TraversableLike

Example:

```scala
List(1,2,3).tails = Iterator(List(1,2,3), List(2,3), List(3), Nil)
```

(defined at scala.collection.TraversableViewLike)


### `def takeWhile(p: (Nothing) ⇒ Boolean): IterableView[Nothing, Coll]`     ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this collection whose elements all satisfy the
    predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def unzip3[A1, A2, A3](implicit asTriple: (Nothing) ⇒ (A1, A2, A3)): (EmptyView.Transformed[A1], EmptyView.Transformed[A2], EmptyView.Transformed[A3])` ###

Converts this collection of triples into three collections of the first, second,
and third element of each triple.

```scala
val xs = Traversable(
           (1, "one", '1'),
           (2, "two", '2'),
           (3, "three", '3')).unzip3
// xs == (Traversable(1, 2, 3),
//        Traversable(one, two, three),
//        Traversable(1, 2, 3))
```

* A1
  * the type of the first member of the element triples
* A2
  * the type of the second member of the element triples
* A3
  * the type of the third member of the element triples
* asTriple
  * an implicit conversion which asserts that the element type of this
    collection is a triple.
* returns
  * a triple of collections, containing the first, second, respectively third
    member of each element triple of this collection.

* Definition Classes
  * TraversableViewLike → GenericTraversableTemplate

(defined at scala.collection.TraversableViewLike)


### `def unzip[A1, A2](implicit asPair: (Nothing) ⇒ (A1, A2)): (EmptyView.Transformed[A1], EmptyView.Transformed[A2])` ###

Converts this collection of pairs into two collections of the first and second
half of each pair.

```scala
val xs = Traversable(
           (1, "one"),
           (2, "two"),
           (3, "three")).unzip
// xs == (Traversable(1, 2, 3),
//        Traversable(one, two, three))
```

* A1
  * the type of the first half of the element pairs
* A2
  * the type of the second half of the element pairs
* asPair
  * an implicit conversion which asserts that the element type of this
    collection is a pair.
* returns
  * a pair of collections, containing the first, respectively second half of
    each element pair of this collection.

* Definition Classes
  * TraversableViewLike → GenericTraversableTemplate

(defined at scala.collection.TraversableViewLike)


### `def withFilter(p: (Nothing) ⇒ Boolean): IterableView[Nothing, Coll]`    ###

Creates a non-strict filter of this collection.

Note: the difference between `c filter p` and `c withFilter p` is that the
former creates a new collection, whereas the latter only restricts the domain of
subsequent `map` , `flatMap` , `foreach` , and `withFilter` operations.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this collection which satisfy the predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


--------------------------------------------------------------------------------
       Value Members From scala.collection.TraversableViewLike.EmptyView
--------------------------------------------------------------------------------


### `final def foreach[U](f: (Nothing) ⇒ U): Unit`                           ###

[use case]

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * EmptyView → Transformed → GenericTraversableTemplate → TraversableLike →
    GenTraversableLike → TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.TraversableViewLike.EmptyView)


--------------------------------------------------------------------------------
      Value Members From scala.collection.TraversableViewLike.Transformed
--------------------------------------------------------------------------------


### `def headOption: Option[Nothing]`                                        ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this collection if it is nonempty, `None` if it is
    empty.

* Definition Classes
  * Transformed → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike.Transformed)


### `def lastOption: Option[Nothing]`                                        ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this collection$ if it is nonempty, `None` if it is
    empty.

* Definition Classes
  * Transformed → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike.Transformed)


--------------------------------------------------------------------------------
                Value Members From scala.collection.ViewMkString
--------------------------------------------------------------------------------


### `def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder` ###

* Definition Classes
  * ViewMkString

(defined at scala.collection.ViewMkString)


### `def mkString(sep: String): String`                                      ###

* Definition Classes
  * ViewMkString

(defined at scala.collection.ViewMkString)


### `def mkString(start: String, sep: String, end: String): String`          ###

* Definition Classes
  * ViewMkString

(defined at scala.collection.ViewMkString)


### `def thisSeq: Seq[Nothing]`                                              ###

* Attributes
  * protected[this]
* Definition Classes
  * ViewMkString

(defined at scala.collection.ViewMkString)


--------------------------------------------------------------------------------
     Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Builder[B, Iterable[B]]`                         ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (Nothing) ⇒ GenTraversableOnce[B]): Iterable[Iterable[B]]` ###

Transposes this collection of traversable collections into a collection of
collections.

The resulting collection's type will be guided by the static type of collection.
For example:

```scala
val xs = List(
           Set(1, 2, 3),
           Set(4, 5, 6)).transpose
// xs == List(
//         List(1, 4),
//         List(2, 5),
//         List(3, 6))

val ys = Vector(
           List(1, 2, 3),
           List(4, 5, 6)).transpose
// ys == Vector(
//         Vector(1, 4),
//         Vector(2, 5),
//         Vector(3, 6))
```

* B
  * the type of the elements of each traversable collection.
* asTraversable
  * an implicit conversion which asserts that the element type of this
    collection is a `Traversable` .
* returns
  * a two-dimensional collection of collections which has as _n_ th row the _n_
    th column of this collection.

* Definition Classes
  * GenericTraversableTemplate
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_  `transpose` throws an
     `IllegalArgumentException` if collections are not uniformly sized.
* Exceptions thrown
  * IllegalArgumentException if all collections in this collection are not of
    the same size.

(defined at scala.collection.generic.GenericTraversableTemplate)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from EmptyView to
    CollectionsHaveToParArray [EmptyView, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (EmptyView) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
