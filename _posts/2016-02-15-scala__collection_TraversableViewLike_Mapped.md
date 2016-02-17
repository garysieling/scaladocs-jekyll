
#                 scala.collection.TraversableViewLike#Mapped                 #

```scala
trait Mapped[B] extends Transformed[B]
```

* Source
  * [TraversableViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableViewLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Appended[B >: A] extends Transformed[B]`                          ###

* Definition Classes
  * TraversableViewLike


### `trait DroppedWhile extends Transformed[A]`                              ###

* Definition Classes
  * TraversableViewLike


### `trait EmptyView extends Transformed[Nothing]`                           ###

* Definition Classes
  * TraversableViewLike


### `trait Filtered extends Transformed[A]`                                  ###

* Definition Classes
  * TraversableViewLike


### `trait FlatMapped[B] extends Transformed[B]`                             ###

* Definition Classes
  * TraversableViewLike


### `trait Forced[B] extends Transformed[B]`                                 ###

A fall back which forces everything into a vector and then applies an operation
on it. Used for those operations which do not naturally lend themselves to a
view

* Definition Classes
  * TraversableViewLike


### `trait Mapped[B] extends Transformed[B]`                                 ###

* Definition Classes
  * TraversableViewLike


### `trait Prepended[B >: A] extends Transformed[B]`                         ###

* Definition Classes
  * TraversableViewLike


### `type Self = TraversableView[B, Coll]`                                   ###

The type implementing this traversable

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike


### `trait Sliced extends Transformed[A]`                                    ###

* Definition Classes
  * TraversableViewLike


### `trait TakenWhile extends Transformed[A]`                                ###

* Definition Classes
  * TraversableViewLike


### `trait Transformed[+B] extends TraversableView[B, Coll]`                 ###

The implementation base trait of this view. This trait and all its subtraits has
to be re-implemented for each ViewLike class.

* Definition Classes
  * TraversableViewLike


### `class WithFilter extends FilterMonadic[A, Repr]`                        ###

A class supporting filtered operations. Instances of this class are returned by
method `withFilter` .

* Definition Classes
  * TraversableLike


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParIterable[B]`                                                ###

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
            Concrete Value Members From scala.collection.Traversable
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[Traversable]`                           ###

The factory companion object that builds instances of class Traversable. (or its
 `Iterable` superclass where class Traversable is not a `Seq` .)

* Definition Classes
  * Traversable → GenTraversable → GenericTraversableTemplate

(defined at scala.collection.Traversable)


### `def seq: Traversable[B]`                                                ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Traversable → GenTraversable → Parallelizable → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.Traversable)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def copyToArray[B >: B](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with at most `len` elements of this collection, starting at position `start` .
Copying will stop once either the end of the current collection is reached, or
the end of the target array is reached, or `len` elements have been copied.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def exists(p: (B) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for at least one element of this traversable
collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `false` if this traversable collection is empty, otherwise `true` if the
    given predicate `p` holds for some of the elements of this traversable
    collection, otherwise `false`

* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def find(p: (B) ⇒ Boolean): Option[B]`                                  ###

Finds the first element of the traversable collection satisfying a predicate, if
any.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the traversable collection
    that satisfies `p` , or `None` if none exists.

* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def forall(p: (B) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for all elements of this traversable collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this traversable collection is empty or the given predicate `p`
    holds for all elements of this traversable collection, otherwise `false` .

* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def head: B`                                                            ###

Selects the first element of this traversable collection.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the traversable collection is empty.

(defined at scala.collection.TraversableLike)


### `def last: B`                                                            ###

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


### `def parCombiner: Combiner[B, ParIterable[B]]`                           ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike → Parallelizable

(defined at scala.collection.TraversableLike)


### `def repr: TraversableView[B, Coll]`                                     ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scan[B >: B, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

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


### `def thisCollection: Traversable[B]`                                     ###

The underlying collection seen as an instance of `Traversable` . By default this
is implemented as the current collection object itself, but this can be
overridden.

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def toCollection(repr: TraversableView[B, Coll]): Traversable[B]`       ###

A conversion from collections of type `Repr` to `Traversable` objects. By
default this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def toIterator: Iterator[B]`                                            ###

Returns an Iterator over the elements in this traversable collection. Will
return the same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def toStream: Stream[B]`                                                ###

Converts this traversable collection to a stream.

* returns
  * a stream containing all elements of this traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableOnce

(defined at scala.collection.TraversableLike)


### `def toTraversable: Traversable[B]`                                      ###

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


### `def view(from: Int, until: Int): TraversableView[B, TraversableView[B, Coll]]` ###

Creates a non-strict view of a slice of this traversable collection.

Note: the difference between `view` and `slice` is that `view` produces a view
of the current traversable collection, whereas `slice` produces a new
traversable collection.

Note: `view(from, to)` is equivalent to `view.slice(from, to)`

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* from
  * the index of the first element of the view
* until
  * the index of the element following the view
* returns
  * a non-strict view of a slice of this traversable collection, starting at
    index `from` and extending up to (but not including) index `until` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def view: TraversableView[B, TraversableView[B, Coll]]`                 ###

Creates a non-strict view of this traversable collection.

* returns
  * a non-strict view of this traversable collection.

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableOnce
--------------------------------------------------------------------------------


### `def /:[B](z: B)(op: (B, B) ⇒ B): B`                                     ###

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


### `def :\[B](z: B)(op: (B, B) ⇒ B): B`                                     ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, B) ⇒ B, combop: (B, B) ⇒ B): B`     ###

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


### `def collectFirst[B](pf: PartialFunction[B, B]): Option[B]`              ###

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


### `def copyToArray[B >: B](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with values of this collection. Copying will stop once either the end of the
current collection is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: B](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with values of this collection, beginning at index `start` . Copying will stop
once either the end of the current collection is reached, or the end of the
target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: B](dest: Buffer[B]): Unit`                        ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: (B) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, B) ⇒ B): B`                               ###

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


### `def foldRight[B](z: B)(op: (B, B) ⇒ B): B`                              ###

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


### `def fold[A1 >: B](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

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


### `def maxBy[B](f: (B) ⇒ B)(implicit cmp: Ordering[B]): B`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection with the largest value measured by
    function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: (B) ⇒ B)(implicit cmp: Ordering[B]): B`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection with the smallest value measured by
    function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduceLeftOption[B >: B](op: (B, B) ⇒ B): Option[B]`                ###

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


### `def reduceLeft[B >: B](op: (B, B) ⇒ B): B`                              ###

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


### `def reduceOption[A1 >: B](op: (A1, A1) ⇒ A1): Option[A1]`               ###

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


### `def reduceRightOption[B >: B](op: (B, B) ⇒ B): Option[B]`               ###

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


### `def reduceRight[B >: B](op: (B, B) ⇒ B): B`                             ###

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


### `def reduce[A1 >: B](op: (A1, A1) ⇒ A1): A1`                             ###

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


### `def reversed: List[B]`                                                  ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toBuffer[B >: B]: Buffer[B]`                                        ###

Uses the contents of this traversable or iterator to create a new mutable
buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[B]`                              ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIterable: Iterable[B]`                                            ###

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


### `def toList: List[B]`                                                    ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[B, (T, U)]): immutable.Map[T, U]`      ###

[use case]

Converts this collection to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this collection.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSeq: Seq[B]`                                                      ###

Converts this traversable or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: B]: immutable.Set[B]`                                    ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: Vector[B]`                                                ###

Converts this traversable or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.TraversableViewLike
--------------------------------------------------------------------------------


### `def ++:[B >: B, That](xs: Traversable[B])(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

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


### `def ++:[B >: B, That](xs: TraversableOnce[B])(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

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
  * a new collection which contains all elements of this collection followed by
    all elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike

(defined at scala.collection.TraversableViewLike)


### `def ++[B >: B, That](xs: GenTraversableOnce[B])(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

[use case]

Returns a new collection containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
collection is the most specific superclass encompassing the element types of the
two operands.

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
  * a new collection which contains all elements of this collection followed by
    all elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def collect[B, That](pf: PartialFunction[B, B])(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
collection on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the collection.
* returns
  * a new collection resulting from applying the given partial function `pf` to
    each element on which it is defined and collecting the results. The order of
    the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def drop(n: Int): TraversableView[B, Coll]`                             ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this collection.
* returns
  * a collection consisting of all elements of this collection except the first
     `n` ones, or else the empty collection, if this collection has less than
     `n` elements.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def dropWhile(p: (B) ⇒ Boolean): TraversableView[B, Coll]`              ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this collection whose first element does not satisfy
    the predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filter(p: (B) ⇒ Boolean): TraversableView[B, Coll]`                 ###

Selects all elements of this collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that satisfy
    the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filterNot(p: (B) ⇒ Boolean): TraversableView[B, Coll]`              ###

Selects all elements of this collection which do not satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that do not
    satisfy the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def flatMap[B, That](f: (B) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this
collection and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of collection.
This might cause unexpected results sometimes. For example:

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
  * a new collection resulting from applying the given collection-valued
    function `f` to each element of this collection and concatenating the
    results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def force[B >: B, That](implicit bf: CanBuildFrom[Coll, B, That]): That` ###

* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def groupBy[K](f: (B) ⇒ K): immutable.Map[K, TraversableView[B, Coll]]` ###

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


### `def init: TraversableView[B, Coll]`                                     ###

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


### `def inits: Iterator[TraversableView[B, Coll]]`                          ###

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


### `def map[B, That](f: (B) ⇒ B)(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this
collection.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new collection resulting from applying the given function `f` to each
    element of this collection and collecting the results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def newAppended[B >: B](that: GenTraversable[B]): Transformed[B]`       ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newBuilder: Builder[B, TraversableView[B, Coll]]`                   ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * TraversableViewLike → GenericTraversableTemplate → TraversableLike →
    HasNewBuilder

(defined at scala.collection.TraversableViewLike)


### `def newDropped(n: Int): Transformed[B]`                                 ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newDroppedWhile(p: (B) ⇒ Boolean): Transformed[B]`                  ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newFiltered(p: (B) ⇒ Boolean): Transformed[B]`                      ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newFlatMapped[B](f: (B) ⇒ GenTraversableOnce[B]): Transformed[B]`   ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newForced[B](xs: ⇒ GenSeq[B]): Transformed[B]`                      ###

Boilerplate method, to override in each subclass This method could be eliminated
if Scala had virtual classes

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newMapped[B](f: (B) ⇒ B): Transformed[B]`                           ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newPrepended[B >: B](that: GenTraversable[B]): Transformed[B]`      ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newSliced(_endpoints: SliceInterval): Transformed[B]`               ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newTaken(n: Int): Transformed[B]`                                   ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def newTakenWhile(p: (B) ⇒ Boolean): Transformed[B]`                    ###

* Attributes
  * protected
* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def partition(p: (B) ⇒ Boolean): (TraversableView[B, Coll], TraversableView[B, Coll])` ###

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


### `def scanLeft[B, That](z: B)(op: (B, B) ⇒ B)(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: (B, B) ⇒ B)(implicit bf: CanBuildFrom[TraversableView[B, Coll], B, That]): That` ###

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


### `def slice(from: Int, until: Int): TraversableView[B, Coll]`             ###

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


### `def span(p: (B) ⇒ Boolean): (TraversableView[B, Coll], TraversableView[B, Coll])` ###

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


### `def splitAt(n: Int): (TraversableView[B, Coll], TraversableView[B, Coll])` ###

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


### `def tail: TraversableView[B, Coll]`                                     ###

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


### `def tails: Iterator[TraversableView[B, Coll]]`                          ###

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


### `def take(n: Int): TraversableView[B, Coll]`                             ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this collection.
* returns
  * a collection consisting only of the first `n` elements of this collection,
    or else the whole collection, if it has less than `n` elements.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def takeWhile(p: (B) ⇒ Boolean): TraversableView[B, Coll]`              ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this collection whose elements all satisfy the
    predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def unzip3[A1, A2, A3](implicit asTriple: (B) ⇒ (A1, A2, A3)): (Transformed[A1], Transformed[A2], Transformed[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (B) ⇒ (A1, A2)): (Transformed[A1], Transformed[A2])` ###

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


### `def withFilter(p: (B) ⇒ Boolean): TraversableView[B, Coll]`             ###

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
    Abstract Value Members From scala.collection.TraversableViewLike.Mapped
--------------------------------------------------------------------------------


### `abstract val mapping: (A) ⇒ B`                                          ###

* Attributes
  * protected[this]

(defined at scala.collection.TraversableViewLike.Mapped)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.TraversableViewLike.Mapped
--------------------------------------------------------------------------------


### `def foreach[U](f: (B) ⇒ U): Unit`                                       ###

[use case]

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * Mapped → Transformed → GenericTraversableTemplate → TraversableLike →
    GenTraversableLike → TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.TraversableViewLike.Mapped)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.ViewMkString
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


### `def thisSeq: Seq[B]`                                                    ###

* Attributes
  * protected[this]
* Definition Classes
  * ViewMkString

(defined at scala.collection.ViewMkString)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Builder[B, Traversable[B]]`                      ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (B) ⇒ GenTraversableOnce[B]): Traversable[Traversable[B]]` ###

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
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Mapped [B] to
    CollectionsHaveToParArray [Mapped [B], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Mapped [B]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
