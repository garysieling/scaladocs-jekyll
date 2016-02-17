
#                      scala.collection.AbstractIterator                      #

```scala
abstract class AbstractIterator[+A] extends Iterator[A]
```

Explicit instantiation of the `Iterator` trait to reduce class file size in
subclasses.

* Source
  * [Iterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterator.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class GroupedIterator[B >: A] extends AbstractIterator[Seq[B]] with Iterator[Seq[B]]` ###

A flexible iterator for transforming an `Iterator[A]` into an Iterator[Seq[A]],
with configurable sequence size, step, and strategy for dealing with elements
which don't fit evenly.

Typical uses can be achieved via methods `grouped` and `sliding` .

* Definition Classes
  * Iterator


--------------------------------------------------------------------------------
          Instance Constructors From scala.collection.AbstractIterator
--------------------------------------------------------------------------------


### `new AbstractIterator()`                                                 ###

(defined at scala.collection.AbstractIterator)


--------------------------------------------------------------------------------
             Concrete Value Members From scala.collection.Iterator
--------------------------------------------------------------------------------


### `abstract def hasNext: Boolean`                                          ###

Tests whether this iterator can provide another element.

* returns
  * `true` if a subsequent call to `next` will yield an element, `false`
    otherwise.

* Definition Classes
  * Iterator
* Note
  * Reuse: The iterator remains valid for further use whatever result is
    returned.

(defined at scala.collection.Iterator)


### `def ++[B >: A](that: ⇒ GenTraversableOnce[B]): Iterator[B]`             ###

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


### `def buffered: BufferedIterator[A]`                                      ###

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


### `def collect[B](pf: PartialFunction[A, B]): Iterator[B]`                 ###

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


### `def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit`      ###

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
  * Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def corresponds[B](that: GenTraversableOnce[B])(p: (A, B) ⇒ Boolean): Boolean` ###

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


### `def drop(n: Int): Iterator[A]`                                          ###

Advances this iterator past the first _n_ elements, or the length of the
iterator, whichever is smaller.

* n
  * the number of elements to drop
* returns
  * an iterator which produces all values of the current iterator, except it
    omits the first `n` values.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def dropWhile(p: (A) ⇒ Boolean): Iterator[A]`                           ###

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


### `def exists(p: (A) ⇒ Boolean): Boolean`                                  ###

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


### `def filter(p: (A) ⇒ Boolean): Iterator[A]`                              ###

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


### `def filterNot(p: (A) ⇒ Boolean): Iterator[A]`                           ###

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


### `def find(p: (A) ⇒ Boolean): Option[A]`                                  ###

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


### `def flatMap[B](f: (A) ⇒ GenTraversableOnce[B]): Iterator[B]`            ###

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


### `def forall(p: (A) ⇒ Boolean): Boolean`                                  ###

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


### `def foreach[U](f: (A) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all values produced by this iterator.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * Iterator → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def grouped[B >: A](size: Int): GroupedIterator[B]`                     ###

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


### `def indexOf[B >: A](elem: B): Int`                                      ###

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


### `def indexOf[B >: A](elem: B, from: Int): Int`                           ###

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


### `def indexWhere(p: (A) ⇒ Boolean): Int`                                  ###

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


### `def indexWhere(p: (A) ⇒ Boolean, from: Int): Int`                       ###

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


### `def map[B](f: (A) ⇒ B): Iterator[B]`                                    ###

Creates a new iterator that maps all produced values of this iterator to new
values using a transformation function.

* f
  * the transformation function
* returns
  * a new iterator which transforms every value produced by this iterator by
    applying the function `f` to it.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def padTo[A1 >: A](len: Int, elem: A1): Iterator[A1]`                   ###

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


### `def partition(p: (A) ⇒ Boolean): (Iterator[A], Iterator[A])`            ###

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


### `def patch[B >: A](from: Int, patchElems: Iterator[B], replaced: Int): Iterator[B]` ###

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


### `def scanLeft[B](z: B)(op: (B, A) ⇒ B): Iterator[B]`                     ###

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


### `def scanRight[B](z: B)(op: (A, B) ⇒ B): Iterator[B]`                    ###

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


### `def slice(from: Int, until: Int): Iterator[A]`                          ###

Creates an iterator returning an interval of the values produced by this
iterator.

* from
  * the index of the first element in this iterator which forms part of the
    slice. If negative, the slice starts at zero.
* until
  * the index of the first element following the slice. If negative, the slice
    is empty.
* returns
  * an iterator which advances this iterator past the first `from` elements
    using `drop` , and then takes `until - from` elements, using `take` .

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def sliceIterator(from: Int, until: Int): Iterator[A]`                  ###

Creates an optionally bounded slice, unbounded if `until` is negative.

* Attributes
  * protected
* Definition Classes
  * Iterator

(defined at scala.collection.Iterator)


### `def sliding[B >: A](size: Int, step: Int = 1): GroupedIterator[B]`      ###

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


### `def span(p: (A) ⇒ Boolean): (Iterator[A], Iterator[A])`                 ###

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


### `def take(n: Int): Iterator[A]`                                          ###

Selects first _n_ values of this iterator.

* n
  * the number of values to take
* returns
  * an iterator producing only the first `n` values of this iterator, or else
    the whole iterator, if it produces fewer than `n` values.

* Definition Classes
  * Iterator
* Note
  * Reuse: After calling this method, one should discard the iterator it was
    called on, and use only the iterator that was returned. Using the old
    iterator is undefined, subject to change, and may result in changes to the
    new iterator as well.

(defined at scala.collection.Iterator)


### `def takeWhile(p: (A) ⇒ Boolean): Iterator[A]`                           ###

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


### `def toStream: immutable.Stream[A]`                                      ###

Converts this traversable or iterator to a stream.

* returns
  * a stream containing all elements of this traversable or iterator.

* Definition Classes
  * Iterator → GenTraversableOnce

(defined at scala.collection.Iterator)


### `def withFilter(p: (A) ⇒ Boolean): Iterator[A]`                          ###

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


### `def zipAll[B, A1 >: A, B1 >: B](that: Iterator[B], thisElem: A1, thatElem: B1): Iterator[(A1, B1)]` ###

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


### `def zip[B](that: Iterator[B]): Iterator[(A, B)]`                        ###

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


### `def /:[B](z: B)(op: (B, A) ⇒ B): B`                                     ###

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


### `def :\[B](z: B)(op: (A, B) ⇒ B): B`                                     ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, A) ⇒ B, combop: (B, B) ⇒ B): B`     ###

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


### `def collectFirst[B](pf: PartialFunction[A, B]): Option[B]`              ###

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


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

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


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

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


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: (A) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, A) ⇒ B): B`                               ###

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


### `def foldRight[B](z: B)(op: (A, B) ⇒ B): B`                              ###

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


### `def fold[A1 >: A](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

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


### `def maxBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

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


### `def minBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

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


### `def reduceLeftOption[B >: A](op: (B, A) ⇒ B): Option[B]`                ###

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


### `def reduceLeft[B >: A](op: (B, A) ⇒ B): B`                              ###

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


### `def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`               ###

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


### `def reduceRightOption[B >: A](op: (A, B) ⇒ B): Option[B]`               ###

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


### `def reduceRight[B >: A](op: (A, B) ⇒ B): B`                             ###

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


### `def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                             ###

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


### `def toBuffer[B >: A]: Buffer[B]`                                        ###

Uses the contents of this traversable or iterator to create a new mutable
buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[A]`                              ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[A, (T, U)]): immutable.Map[T, U]`      ###

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


### `def toSet[B >: A]: immutable.Set[B]`                                    ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce
(defined at scala.collection.TraversableOnce)
