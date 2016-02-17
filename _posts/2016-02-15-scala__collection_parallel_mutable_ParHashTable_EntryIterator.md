
#         scala.collection.parallel.mutable.ParHashTable#EntryIterator         #

```scala
abstract class EntryIterator[T, +IterRepr <: IterableSplitter[T]] extends IterableSplitter[T] with SizeMapUtils
```

A parallel iterator returning all the entries.

* Source
  * [ParHashTable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParHashTable.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Appended[U >: T, PI <: IterableSplitter[U]] extends IterableSplitter[U]` ###

* Definition Classes
  * IterableSplitter


### `class GroupedIterator[B >: A] extends AbstractIterator[Seq[B]] with Iterator[Seq[B]]` ###

A flexible iterator for transforming an `Iterator[A]` into an Iterator[Seq[A]],
with configurable sequence size, step, and strategy for dealing with elements
which don't fit evenly.

Typical uses can be achieved via methods `grouped` and `sliding` .

* Definition Classes
  * Iterator


### `class Mapped[S] extends IterableSplitter[S]`                            ###

* Definition Classes
  * IterableSplitter


### `class Taken extends IterableSplitter[T]`                                ###

* Definition Classes
  * IterableSplitter


### `class Zipped[S] extends IterableSplitter[(T, S)]`                       ###

* Definition Classes
  * IterableSplitter


### `class ZippedAll[U >: T, S] extends IterableSplitter[(U, S)]`            ###

* Definition Classes
  * IterableSplitter


--------------------------------------------------------------------------------
             Concrete Value Members From scala.collection.Iterator
--------------------------------------------------------------------------------


### `def ++[B >: T](that: ⇒ GenTraversableOnce[B]): Iterator[B]`             ###

[use case]

Concatenates this iterator with another.

* that
  * the other iterator
* returns
  * a new iterator that first yields the values produced by this iterator
    followed by the values produced by iterator `that` .

* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def buffered: BufferedIterator[T]`                                      ###

Creates a buffered iterator from this iterator.

* returns
  * a buffered iterator producing the same values as this iterator.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.
* See also
  * scala.collection.BufferedIterator

(defined at scala.collection.Iterator)


### `def collect[B](pf: PartialFunction[T, B]): Iterator[B]`                 ###

Creates an iterator by transforming values produced by this iterator with a
partial function, dropping those values for which the partial function is not
defined.

* pf
  * the partial function which filters and maps the iterator.
* returns
  * a new iterator which yields each value `x` produced by this iterator for
    which `pf` is defined the image `pf(x)` .

* Definition Classes
  * Iterator
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `collect` has changed. The previous behavior
    can be reproduced with `toSeq` .
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def contains(elem: Any): Boolean`                                       ###

Tests whether this iterator contains a given value as an element.

Note: may not terminate for infinite iterators.

* elem
  * the element to test.
* returns
  * `true` if this iterator produces some value that is is equal (as determined
    by `==` ) to `elem` , `false` otherwise.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def corresponds[B](that: GenTraversableOnce[B])(p: (T, B) ⇒ Boolean): Boolean` ###

Tests whether every element of this iterator relates to the corresponding
element of another collection by satisfying a test predicate.

* B
  * the type of the elements of `that`
* that
  * the other collection
* p
  * the test predicate, which relates elements from both collections
* returns
  * `true` if both collections have the same length and `p(x, y)` is `true` for
    all corresponding elements `x` of this iterator and `y` of `that` ,
    otherwise `false`

* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def dropWhile(p: (T) ⇒ Boolean): Iterator[T]`                           ###

Skips longest sequence of elements of this iterator which satisfy given
predicate `p` , and returns an iterator of the remaining elements.

* p
  * the predicate used to skip elements.
* returns
  * an iterator consisting of the remaining elements

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def duplicate: (Iterator[T], Iterator[T])`                              ###

Creates two new iterators that both iterate over the same elements as this
iterator (in the same order). The duplicate iterators are considered equal if
they are positioned at the same element.

Given that most methods on iterators will make the original iterator unfit for
further use, this methods provides a reliable way of calling multiple such
methods on an iterator.

* returns
  * a pair of iterators

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterators that were returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterators as well., The implementation may allocate temporary storage
    for elements iterated by one iterator but not yet by the other.

(defined at scala.collection.Iterator)


### `def exists(p: (T) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for some of the values produced by this
iterator.

Note: may not terminate for infinite iterators.

* p
  * the predicate used to test elements.
* returns
  * `true` if the given predicate `p` holds for some of the values produced by
    this iterator, otherwise `false` .

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def filter(p: (T) ⇒ Boolean): Iterator[T]`                              ###

Returns an iterator over all the elements of this iterator that satisfy the
predicate `p` . The order of the elements is preserved.

* p
  * the predicate used to test values.
* returns
  * an iterator which produces those values of this iterator which satisfy the
    predicate `p` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def filterNot(p: (T) ⇒ Boolean): Iterator[T]`                           ###

Creates an iterator over all the elements of this iterator which do not satisfy
a predicate p.

* p
  * the predicate used to test values.
* returns
  * an iterator which produces those values of this iterator which do not
    satisfy the predicate `p` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def find(p: (T) ⇒ Boolean): Option[T]`                                  ###

Finds the first value produced by the iterator satisfying a predicate, if any.

Note: may not terminate for infinite iterators.

* p
  * the predicate used to test values.
* returns
  * an option value containing the first value produced by the iterator that
    satisfies predicate `p` , or `None` if none exists.

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def flatMap[B](f: (T) ⇒ GenTraversableOnce[B]): Iterator[B]`            ###

Creates a new iterator by applying a function to all values produced by this
iterator and concatenating the results.

* f
  * the function to apply on each element.
* returns
  * the iterator resulting from applying the given iterator-valued function `f`
    to each value produced by this iterator and concatenating the results.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def forall(p: (T) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for all values produced by this iterator.

Note: may not terminate for infinite iterators.

* p
  * the predicate used to test elements.
* returns
  * `true` if the given predicate `p` holds for all values produced by this
    iterator, otherwise `false` .

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all values produced by this iterator.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def grouped[B >: T](size: Int): GroupedIterator[B]`                     ###

Returns an iterator which groups this iterator into fixed size blocks. Example
usages:

```scala
// Returns List(List(1, 2, 3), List(4, 5, 6), List(7)))
(1 to 7).iterator grouped 3 toList
// Returns List(List(1, 2, 3), List(4, 5, 6))
(1 to 7).iterator grouped 3 withPartial false toList
// Returns List(List(1, 2, 3), List(4, 5, 6), List(7, 20, 25)
// Illustrating that withPadding's argument is by-name.
val it2 = Iterator.iterate(20)(_ + 5)
(1 to 7).iterator grouped 3 withPadding it2.next toList
```

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def indexOf[B >: T](elem: B): Int`                                      ###

Returns the index of the first occurrence of the specified object in this
iterable object.

Note: may not terminate for infinite iterators.

* elem
  * element to search for.
* returns
  * the index of the first occurrence of `elem` in the values produced by this
    iterator, or -1 if such an element does not exist until the end of the
    iterator is reached.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def indexOf[B >: T](elem: B, from: Int): Int`                           ###

Returns the index of the first occurrence of the specified object in this
iterable object after or at some start index.

Note: may not terminate for infinite iterators.

* elem
  * element to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first occurrence of `elem` in the values produced
    by this iterator, or -1 if such an element does not exist until the end of
    the iterator is reached.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def indexWhere(p: (T) ⇒ Boolean): Int`                                  ###

Returns the index of the first produced value satisfying a predicate, or -1.

Note: may not terminate for infinite iterators.

* p
  * the predicate to test values
* returns
  * the index of the first produced value satisfying `p` , or -1 if such an
    element does not exist until the end of the iterator is reached.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def indexWhere(p: (T) ⇒ Boolean, from: Int): Int`                       ###

Returns the index of the first produced value satisfying a predicate, or -1,
after or at some start index.

Note: may not terminate for infinite iterators.

* p
  * the predicate to test values
* from
  * the start index
* returns
  * the index `>= from` of the first produced value satisfying `p` , or -1 if
    such an element does not exist until the end of the iterator is reached.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on. Using it is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def padTo[A1 >: T](len: Int, elem: A1): Iterator[A1]`                   ###

[use case]

Appends an element value to this iterator until a given target length is
reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new iterator consisting of producing all values of this iterator, followed
    by the minimal number of occurrences of `elem` so that the number of
    produced values is at least `len` .

* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def partition(p: (T) ⇒ Boolean): (Iterator[T], Iterator[T])`            ###

Partitions this iterator in two iterators according to a predicate.

* p
  * the predicate on which to partition
* returns
  * a pair of iterators: the iterator that satisfies the predicate `p` and the
    iterator that does not. The relative order of the elements in the resulting
    iterators is the same as in the original iterator.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterators that were returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterators as well.

(defined at scala.collection.Iterator)


### `def patch[B >: T](from: Int, patchElems: Iterator[B], replaced: Int): Iterator[B]` ###

Returns this iterator with patched values. Patching at negative indices is the
same as patching starting at 0. Patching at indices at or larger than the length
of the original iterator appends the patch to the end. If more values are
replaced than actually exist, the excess is ignored.

* from
  * The start index from which to patch
* patchElems
  * The iterator of patch values
* replaced
  * The number of values in the original iterator that are replaced by the
    patch.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, as well as the one passed as a parameter, and use only the
    iterator that was returned. Using the old iterators is undefined, subject to
    change, and may result in changes to the new iterator as well.

(defined at scala.collection.Iterator)


### `def sameElements(that: Iterator[_]): Boolean`                           ###

Tests if another iterator produces the same values as this one.

Note: will not terminate for infinite iterators.

* that
  * the other iterator
* returns
  * `true` , if both iterators produce the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, as well as the one passed as parameter. Using the old iterators
    is undefined and subject to change.

(defined at scala.collection.Iterator)


### `def scanLeft[B](z: B)(op: (B, T) ⇒ B): Iterator[B]`                     ###

Produces a collection containing cumulative results of applying the operator
going left to right.

Note: will not terminate for infinite iterators.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the elements in the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* returns
  * iterator with intermediate results

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def scanRight[B](z: B)(op: (T, B) ⇒ B): Iterator[B]`                    ###

Produces a collection containing cumulative results of applying the operator
going right to left. The head of the collection is the last cumulative result.

Note: will not terminate for infinite iterators.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the elements in the resulting collection
* z
  * the initial value
* op
  * the binary operator applied to the intermediate result and the element
* returns
  * iterator with intermediate results

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

Example:

```scala
Iterator(1, 2, 3, 4).scanRight(0)(_ + _).toList == List(10, 9, 7, 4, 0)
```

(defined at scala.collection.Iterator)


### `def seq: Iterator[T]`                                                   ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def sliceIterator(from: Int, until: Int): Iterator[T]`                  ###

Creates an optionally bounded slice, unbounded if `until` is negative.

* Attributes
  * protected
* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def sliding[B >: T](size: Int, step: Int = 1): GroupedIterator[B]`      ###

Returns an iterator which presents a "sliding window" view of another iterator.
The first argument is the window size, and the second is how far to advance the
window on each iteration; defaults to `1` . Example usages:

```scala
// Returns List(List(1, 2, 3), List(2, 3, 4), List(3, 4, 5))
(1 to 5).iterator.sliding(3).toList
// Returns List(List(1, 2, 3, 4), List(4, 5))
(1 to 5).iterator.sliding(4, 3).toList
// Returns List(List(1, 2, 3, 4))
(1 to 5).iterator.sliding(4, 3).withPartial(false).toList
// Returns List(List(1, 2, 3, 4), List(4, 5, 20, 25))
// Illustrating that withPadding's argument is by-name.
val it2 = Iterator.iterate(20)(_ + 5)
(1 to 5).iterator.sliding(4, 3).withPadding(it2.next).toList
```

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def span(p: (T) ⇒ Boolean): (Iterator[T], Iterator[T])`                 ###

Splits this Iterator into a prefix/suffix pair according to a predicate.

* p
  * the test predicate
* returns
  * a pair of Iterators consisting of the longest prefix of this whose elements
    all satisfy `p` , and the rest of the Iterator.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterators that were returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterators as well.

(defined at scala.collection.Iterator)


### `def takeWhile(p: (T) ⇒ Boolean): Iterator[T]`                           ###

Takes longest prefix of values produced by this iterator that satisfy a
predicate.

* p
  * The predicate used to test elements.
* returns
  * An iterator returning the values produced by this iterator, until this
    iterator produces a value that does not satisfy the predicate `p` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def toIterator: Iterator[T]`                                            ###

Returns an Iterator over the elements in this traversable or iterator. Will
return the same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite iterators.

* returns
  * an Iterator containing all elements of this traversable or iterator.

* Definition Classes
  * Iterator → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def toStream: immutable.Stream[T]`                                      ###

Converts this traversable or iterator to a stream.

* returns
  * a stream containing all elements of this traversable or iterator.

* Definition Classes
  * Iterator → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def toTraversable: Traversable[T]`                                      ###

Converts this traversable or iterator to an unspecified Traversable. Will return
the same collection if this instance is already Traversable.

Note: will not terminate for infinite iterators.

* returns
  * a Traversable containing all elements of this traversable or iterator.

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def withFilter(p: (T) ⇒ Boolean): Iterator[T]`                          ###

Creates an iterator over all the elements of this iterator that satisfy the
predicate `p` . The order of the elements is preserved.

 *Note:*  `withFilter` is the same as `filter` on iterators. It exists so that
for-expressions with filters work over iterators.

* p
  * the predicate used to test values.
* returns
  * an iterator which produces those values of this iterator which satisfy the
    predicate `p` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def zipAll[B, A1 >: T, B1 >: B](that: Iterator[B], thisElem: A1, thatElem: B1): Iterator[(A1, B1)]` ###

[use case]

Creates an iterator formed from this iterator and another iterator by combining
corresponding elements in pairs. If one of the two iterators is shorter than the
other, placeholder elements are used to extend the shorter iterator to the
length of the longer.

* that
  * iterator `that` may have a different length as the self iterator.
* thisElem
  * element `thisElem` is used to fill up the resulting iterator if the self
    iterator is shorter than `that`
* thatElem
  * element `thatElem` is used to fill up the resulting iterator if `that` is
    shorter than the self iterator
* returns
  * a new iterator containing pairs consisting of corresponding values of this
    iterator and `that` . The length of the returned iterator is the maximum of
    the lengths of this iterator and `that` . If this iterator is shorter than
     `that` , `thisElem` values are used to pad the result. If `that` is shorter
    than this iterator, `thatElem` values are used to pad the result.

* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def zipWithIndex: Iterator[(T, Int)]`                                   ###

Creates an iterator that pairs each element produced by this iterator with its
index, counting from 0.

* returns
  * a new iterator containing pairs consisting of corresponding elements of this
    iterator and their indices.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def zip[B](that: Iterator[B]): Iterator[(T, B)]`                        ###

Creates an iterator formed from this iterator and another iterator by combining
corresponding values in pairs. If one of the two iterators is longer than the
other, its remaining elements are ignored.

* that
  * The iterator providing the second half of each result pair
* returns
  * a new iterator containing pairs consisting of corresponding elements of this
    iterator and `that` . The number of elements returned by the new iterator is
    the minimum of the number of elements returned by this iterator and `that` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, as well as the one passed as a parameter, and use only the
    iterator that was returned. Using the old iterators is undefined, subject to
    change, and may result in changes to the new iterator as well.

(defined at scala.collection.Iterator)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableOnce
--------------------------------------------------------------------------------


### `def /:[B](z: B)(op: (B, T) ⇒ B): B`                                     ###

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


### `def :\[B](z: B)(op: (T, B) ⇒ B): B`                                     ###

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


### `def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder` ###

Appends all elements of this traversable or iterator to a string builder using
start, end, and separator strings. The written text begins with the string
 `start` and ends with the string `end` . Inside, the string representations
(w.r.t. the method `toString` ) of all elements of this traversable or iterator
are separated by the string `sep` .

Example:

```scala
scala> val a = List(1,2,3,4)
a: List[Int] = List(1, 2, 3, 4)

scala> val b = new StringBuilder()
b: StringBuilder =

scala> a.addString(b , "List(" , ", " , ")")
res5: StringBuilder = List(1, 2, 3, 4)
```

* b
  * the string builder to which elements are appended.
* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * the string builder `b` to which elements were appended.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def aggregate[B](z: ⇒ B)(seqop: (B, T) ⇒ B, combop: (B, B) ⇒ B): B`     ###

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


### `def collectFirst[B](pf: PartialFunction[T, B]): Option[B]`              ###

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


### `def copyToArray[B >: T](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this traversable or iterator to an array. Fills the given
array `xs` with values of this traversable or iterator. Copying will stop once
either the end of the current traversable or iterator is reached, or the end of
the target array is reached.

Note: will not terminate for infinite iterators.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: T](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this traversable or iterator to an array. Fills the given
array `xs` with values of this traversable or iterator, beginning at index
 `start` . Copying will stop once either the end of the current traversable or
iterator is reached, or the end of the target array is reached.

Note: will not terminate for infinite iterators.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: T](dest: Buffer[B]): Unit`                        ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, T) ⇒ B): B`                               ###

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


### `def foldRight[B](z: B)(op: (T, B) ⇒ B): B`                              ###

Applies a binary operator to all elements of this traversable or iterator and a
start value, going right to left.

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
    traversable or iterator, going right to left with the start value `z` on the
    right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.
    Returns `z` if this traversable or iterator is empty.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def maxBy[B](f: (T) ⇒ B)(implicit cmp: Ordering[B]): T`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this traversable or iterator with the largest value
    measured by function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: (T) ⇒ B)(implicit cmp: Ordering[B]): T`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this traversable or iterator with the smallest value
    measured by function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this traversable or iterator in a string using a
separator string.

* sep
  * the separator string.
* returns
  * a string representation of this traversable or iterator. In the resulting
    string the string representations (w.r.t. the method `toString` ) of all
    elements of this traversable or iterator are separated by the string `sep` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(defined at scala.collection.TraversableOnce)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this traversable or iterator in a string using start,
end, and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this traversable or iterator. The resulting
    string begins with the string `start` and ends with the string `end` .
    Inside, the string representations (w.r.t. the method `toString` ) of all
    elements of this traversable or iterator are separated by the string `sep` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(defined at scala.collection.TraversableOnce)


### `def reduceLeftOption[B >: T](op: (B, T) ⇒ B): Option[B]`                ###

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


### `def reduceLeft[B >: T](op: (B, T) ⇒ B): B`                              ###

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


### `def reduceOption[A1 >: T](op: (A1, A1) ⇒ A1): Option[A1]`               ###

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


### `def reduceRightOption[B >: T](op: (T, B) ⇒ B): Option[B]`               ###

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


### `def reduceRight[B >: T](op: (T, B) ⇒ B): B`                             ###

Applies a binary operator to all elements of this traversable or iterator, going
right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable or iterator, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable or iterator is empty.

(defined at scala.collection.TraversableOnce)


### `def reversed: List[T]`                                                  ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toBuffer[B >: T]: Buffer[B]`                                        ###

Uses the contents of this traversable or iterator to create a new mutable
buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[T]`                              ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIterable: Iterable[T]`                                            ###

Converts this traversable or iterator to an iterable collection. Note that the
choice of target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: List[T]`                                                    ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[T, (T, U)]): immutable.Map[T, U]`      ###

[use case]

Converts this traversable or iterator to a map. This method is unavailable
unless the elements are members of Tuple2, each ((T, U)) becoming a key-value
pair in the map. Duplicate keys will be overwritten by later keys: if this is an
unordered collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite iterators.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSeq: Seq[T]`                                                      ###

Converts this traversable or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: T]: immutable.Set[B]`                                    ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: Vector[T]`                                                ###

Converts this traversable or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.generic.DelegatedSignalling
--------------------------------------------------------------------------------


### `def setIndexFlag(f: Int): Unit`                                         ###

Sets the value of the index flag.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set.

* Definition Classes
  * DelegatedSignalling → Signalling

(defined at scala.collection.generic.DelegatedSignalling)


### `def setIndexFlagIfGreater(f: Int): Unit`                                ###

Sets the value of the index flag if argument is greater than current value. This
method does this atomically.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set

* Definition Classes
  * DelegatedSignalling → Signalling

(defined at scala.collection.generic.DelegatedSignalling)


### `def setIndexFlagIfLesser(f: Int): Unit`                                 ###

Sets the value of the index flag if argument is lesser than current value. This
method does this atomically.

The index flag holds an integer which carries some operation-specific meaning.
For instance, `takeWhile` operation sets the index flag to the position of the
element where the predicate fails. Other workers may check this index against
the indices they are working on and return if this index is smaller than their
index. Examples of operations using this are `takeWhile` , `dropWhile` , `span`
and `indexOf` .

* f
  * the value to which the index flag is set

* Definition Classes
  * DelegatedSignalling → Signalling

(defined at scala.collection.generic.DelegatedSignalling)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.AugmentedIterableIterator
--------------------------------------------------------------------------------


### `def collect2combiner[S, That](pf: PartialFunction[T, S], cb: Combiner[S, That]): Combiner[S, That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def copy2builder[U >: T, Coll, Bld <: Builder[U, Coll]](b: Bld): Bld`   ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def copyToArray[U >: T](array: Array[U], from: Int, len: Int): Unit`    ###

[use case]

Copies selected values produced by this iterator to an array. Fills the given
array `xs` starting at index `start` with at most `len` values produced by this
iterator. Copying will stop once either the end of the current iterator is
reached, or the end of the array is reached, or `len` elements have been copied.

Note: will not terminate for infinite iterators.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * AugmentedIterableIterator → Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def count(p: (T) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * AugmentedIterableIterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def drop2combiner[U >: T, This](n: Int, cb: Combiner[U, This]): Combiner[U, This]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def filter2combiner[U >: T, This](pred: (T) ⇒ Boolean, cb: Combiner[U, This]): Combiner[U, This]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def filterNot2combiner[U >: T, This](pred: (T) ⇒ Boolean, cb: Combiner[U, This]): Combiner[U, This]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def flatmap2combiner[S, That](f: (T) ⇒ GenTraversableOnce[S], cb: Combiner[S, That]): Combiner[S, That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def fold[U >: T](z: U)(op: (U, U) ⇒ U): U`                              ###

Folds the elements of this traversable or iterator using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

Note: will not terminate for infinite iterators.

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
  * AugmentedIterableIterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def map2combiner[S, That](f: (T) ⇒ S, cb: Combiner[S, That]): Combiner[S, That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def partition2combiners[U >: T, This](pred: (T) ⇒ Boolean, btrue: Combiner[U, This], bfalse: Combiner[U, This]): (Combiner[U, This], Combiner[U, This])` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def reduceLeft[U >: T](howmany: Int, op: (U, U) ⇒ U): U`                ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def reduce[U >: T](op: (U, U) ⇒ U): U`                                  ###

Reduces the elements of this traversable or iterator using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    traversable or iterator is nonempty.

* Definition Classes
  * AugmentedIterableIterator → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable or iterator is empty.

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def scanToArray[U >: T, A >: U](z: U, op: (U, U) ⇒ U, array: Array[A], from: Int): Unit` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def scanToCombiner[U >: T, That](howmany: Int, startValue: U, op: (U, U) ⇒ U, cb: Combiner[U, That]): Combiner[U, That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def scanToCombiner[U >: T, That](startValue: U, op: (U, U) ⇒ U, cb: Combiner[U, That]): Combiner[U, That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def slice2combiner[U >: T, This](from: Int, until: Int, cb: Combiner[U, This]): Combiner[U, This]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def span2combiners[U >: T, This](p: (T) ⇒ Boolean, before: Combiner[U, This], after: Combiner[U, This]): (Combiner[U, This], Combiner[U, This])` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def splitAt2combiners[U >: T, This](at: Int, before: Combiner[U, This], after: Combiner[U, This]): (Combiner[U, This], Combiner[U, This])` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def take2combiner[U >: T, This](n: Int, cb: Combiner[U, This]): Combiner[U, This]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def takeWhile2combiner[U >: T, This](p: (T) ⇒ Boolean, cb: Combiner[U, This]): (Combiner[U, This], Boolean)` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def zip2combiner[U >: T, S, That](otherpit: RemainsIterator[S], cb: Combiner[(U, S), That]): Combiner[(U, S), That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


### `def zipAll2combiner[U >: T, S, That](that: RemainsIterator[S], thiselem: U, thatelem: S, cb: Combiner[(U, S), That]): Combiner[(U, S), That]` ###

* Definition Classes
  * AugmentedIterableIterator

(defined at scala.collection.parallel.AugmentedIterableIterator)


--------------------------------------------------------------------------------
     Concrete Value Members From scala.collection.parallel.IterableSplitter
--------------------------------------------------------------------------------


### `def appendParIterable[U >: T, PI <: IterableSplitter[U]](that: PI): Appended[U, PI]` ###

* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


### `def buildString(closure: ((String) ⇒ Unit) ⇒ Unit): String`             ###

* Attributes
  * protected
* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


### `def drop(n: Int): IterableSplitter[T]`                                  ###

Drop implemented as simple eager consumption.

* n
  * the number of elements to drop
* returns
  * an iterator which produces all values of the current iterator, except it
    omits the first `n` values.

* Definition Classes
  * IterableSplitter → Iterator

(defined at scala.collection.parallel.IterableSplitter)


### `def map[S](f: (T) ⇒ S): Mapped[S]`                                      ###

Creates a new iterator that maps all produced values of this iterator to new
values using a transformation function.

* f
  * the transformation function
* returns
  * a new iterator which transforms every value produced by this iterator by
    applying the function `f` to it.

* Definition Classes
  * IterableSplitter → Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.parallel.IterableSplitter)


### `def shouldSplitFurther[S](coll: parallel.ParIterable[S], parallelismLevel: Int): Boolean` ###

* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


### `var signalDelegate: Signalling`                                         ###

A delegate that method calls are redirected to.

* Definition Classes
  * IterableSplitter → DelegatedSignalling

(defined at scala.collection.parallel.IterableSplitter)


### `def slice(from1: Int, until1: Int): IterableSplitter[T]`                ###

Creates an iterator returning an interval of the values produced by this
iterator.

* returns
  * an iterator which advances this iterator past the first `from` elements
    using `drop` , and then takes `until - from` elements, using `take` .

* Definition Classes
  * IterableSplitter → Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.parallel.IterableSplitter)


### `def splitWithSignalling: scala.Seq[IterableSplitter[T]]`                ###

* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


### `def take(n: Int): IterableSplitter[T]`                                  ###

Selects first _n_ values of this iterator.

* n
  * the number of values to take
* returns
  * an iterator producing only the first `n` values of this iterator, or else
    the whole iterator, if it produces fewer than `n` values.

* Definition Classes
  * IterableSplitter → Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.parallel.IterableSplitter)


### `def zipAllParSeq[S, U >: T, R >: S](that: SeqSplitter[S], thisElem: U, thatElem: R): ZippedAll[U, R]` ###

* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


### `def zipParSeq[S](that: SeqSplitter[S]): Zipped[S]`                      ###

* Definition Classes
  * IterableSplitter

(defined at scala.collection.parallel.IterableSplitter)


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.mutable.ParHashTable.EntryIterator
--------------------------------------------------------------------------------


### `abstract def entry2item(e: Entry): T`                                   ###

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


### `abstract def newIterator(idxFrom: Int, idxUntil: Int, totalSize: Int, es: Entry): IterRepr` ###

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.mutable.ParHashTable.EntryIterator
--------------------------------------------------------------------------------


### `def countBucketSizes(fromBucket: Int, untilBucket: Int): Int`           ###

* Attributes
  * protected
* Definition Classes
  * EntryIterator → SizeMapUtils

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


### `def countElems(from: Int, until: Int): Int`                             ###

* Attributes
  * protected
* Definition Classes
  * EntryIterator → SizeMapUtils

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


### `def split: Seq[IterableSplitter[T]]`                                    ###

Splits the iterator into a sequence of disjunct views.

Returns a sequence of split iterators, each iterating over some subset of the
elements in the collection. These subsets are disjoint and should be
approximately equal in size. These subsets are not empty, unless the iterator is
empty in which case this method returns a sequence with a single empty iterator.
If the splitter has more than two elements, this method will return two or more
splitters.

Implementors are advised to keep this partition relatively small - two splitters
are already enough when partitioning the collection, although there may be a few
more.

 *Note:* this method actually invalidates the current splitter.

* returns
  * a sequence of disjunct iterators of the collection

* Definition Classes
  * EntryIterator → IterableSplitter → Splitter

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.mutable.ParHashTable.EntryIterator
--------------------------------------------------------------------------------


### `new EntryIterator(idx: Int, until: Int, totalsize: Int, es: Entry)`     ###

(defined at scala.collection.parallel.mutable.ParHashTable.EntryIterator)


--------------------------------------------------------------------------------
   Concrete Value Members From scala.collection.parallel.mutable.SizeMapUtils
--------------------------------------------------------------------------------


### `def calcNumElems(from: Int, until: Int, tableLength: Int, sizeMapBucketSize: Int): Int` ###

* Attributes
  * protected
* Definition Classes
  * SizeMapUtils

(defined at scala.collection.parallel.mutable.SizeMapUtils)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from EntryIterator [T,
    IterRepr] to CollectionsHaveToParArray [EntryIterator [T, IterRepr], T]
    performed by method CollectionsHaveToParArray in scala.collection.parallel.
    This conversion will take place only if an implicit value of type (
    EntryIterator [T, IterRepr]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
