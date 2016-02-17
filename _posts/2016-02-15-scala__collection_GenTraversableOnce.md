
#                     scala.collection.GenTraversableOnce                     #

```scala
trait GenTraversableOnce[+A] extends Any
```

A template trait for all traversable-once objects which may be traversed in
parallel.

Methods in this trait are either abstract or can be implemented in terms of
other methods.

* Source
  * [GenTraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenTraversableOnce.scala#L1)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.GenTraversableOnce
--------------------------------------------------------------------------------


### `abstract def /:[B](z: B)(op: (B, A) ⇒ B): B`                            ###

Applies a binary operator to a start value and all elements of this collection
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
  * the result of inserting `op` between consecutive elements of this collection
    or iterator, going left to right with the start value `z` on the left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def :\[B](z: B)(op: (A, B) ⇒ B): B`                            ###

Applies a binary operator to all elements of this collection or iterator and a
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
  * the result of inserting `op` between consecutive elements of this collection
    or iterator, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def aggregate[B](z: ⇒ B)(seqop: (B, A) ⇒ B, combop: (B, B) ⇒ B): B` ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It is similar to
 `foldLeft` in that it doesn't require the result to be a supertype of the
element type. In addition, it allows parallel collections to be processed in
chunks, and then combines the intermediate results.

 `aggregate` splits the collection or iterator into partitions and processes
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

(defined at scala.collection.GenTraversableOnce)


### `abstract def count(p: (A) ⇒ Boolean): Int`                              ###

Counts the number of elements in the collection or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

(defined at scala.collection.GenTraversableOnce)


### `abstract def exists(p: (A) ⇒ Boolean): Boolean`                         ###

Tests whether a predicate holds for at least one element of this collection or
iterator.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if the given predicate `p` is satisfied by at least one element of
    this collection or iterator, otherwise `false`

(defined at scala.collection.GenTraversableOnce)


### `abstract def find(p: (A) ⇒ Boolean): Option[A]`                         ###

Finds the first element of the collection or iterator satisfying a predicate, if
any.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the collection or iterator
    that satisfies `p` , or `None` if none exists.

(defined at scala.collection.GenTraversableOnce)


### `abstract def foldLeft[B](z: B)(op: (B, A) ⇒ B): B`                      ###

Applies a binary operator to a start value and all elements of this collection
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
  * the result of inserting `op` between consecutive elements of this collection
    or iterator, going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this collection or iterator. Returns
     `z` if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def foldRight[B](z: B)(op: (A, B) ⇒ B): B`                     ###

Applies a binary operator to all elements of this collection or iterator and a
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
  * the result of inserting `op` between consecutive elements of this collection
    or iterator, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this collection or iterator. Returns
     `z` if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def fold[A1 >: A](z: A1)(op: (A1, A1) ⇒ A1): A1`               ###

Folds the elements of this collection or iterator using the specified
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
     `z` , or `z` if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def forall(p: (A) ⇒ Boolean): Boolean`                         ###

Tests whether a predicate holds for all elements of this collection or iterator.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this collection or iterator is empty or the given predicate `p`
    holds for all elements of this collection or iterator, otherwise `false` .

(defined at scala.collection.GenTraversableOnce)


### `abstract def mkString(sep: String): String`                             ###

Displays all elements of this collection or iterator in a string using a
separator string.

* sep
  * the separator string.
* returns
  * a string representation of this collection or iterator. In the resulting
    string the string representations (w.r.t. the method `toString` ) of all
    elements of this collection or iterator are separated by the string `sep` .

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(defined at scala.collection.GenTraversableOnce)


### `abstract def mkString(start: String, sep: String, end: String): String` ###

Displays all elements of this collection or iterator in a string using start,
end, and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this collection or iterator. The resulting string
    begins with the string `start` and ends with the string `end` . Inside, the
    string representations (w.r.t. the method `toString` ) of all elements of
    this collection or iterator are separated by the string `sep` .

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(defined at scala.collection.GenTraversableOnce)


### `abstract def reduceLeftOption[B >: A](op: (B, A) ⇒ B): Option[B]`       ###

Optionally applies a binary operator to all elements of this collection or
iterator, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this collection
    or iterator is nonempty, `None` otherwise.

(defined at scala.collection.GenTraversableOnce)


### `abstract def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`      ###

Reduces the elements of this collection or iterator, if any, using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * An option value containing result of applying reduce operator `op` between
    all the elements if the collection is nonempty, and `None` otherwise.

(defined at scala.collection.GenTraversableOnce)


### `abstract def reduceRightOption[B >: A](op: (A, B) ⇒ B): Option[B]`      ###

Optionally applies a binary operator to all elements of this collection or
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
    collection or iterator is nonempty, `None` otherwise.

(defined at scala.collection.GenTraversableOnce)


### `abstract def reduceRight[B >: A](op: (A, B) ⇒ B): B`                    ###

Applies a binary operator to all elements of this collection or iterator, going
right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this collection
    or iterator, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this collection or iterator.

* Exceptions thrown
  * UnsupportedOperationException if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                    ###

Reduces the elements of this collection or iterator using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    collection or iterator is nonempty.

* Exceptions thrown
  * UnsupportedOperationException if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def seq: TraversableOnce[A]`                                   ###

(defined at scala.collection.GenTraversableOnce)


### `abstract def toBuffer[A1 >: A]: Buffer[A1]`                             ###

Uses the contents of this collection or iterator to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIndexedSeq: immutable.IndexedSeq[A]`                     ###

Converts this collection or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIterable: GenIterable[A]`                                ###

Converts this collection or iterator to an iterable collection. Note that the
choice of target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toSeq: GenSeq[A]`                                          ###

Converts this collection or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toSet[A1 >: A]: GenSet[A1]`                                ###

Converts this collection or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toTraversable: GenTraversable[A]`                          ###

Converts this collection or iterator to an unspecified Traversable. Will return
the same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this collection or iterator.

(defined at scala.collection.GenTraversableOnce)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.GenTraversableOnce
--------------------------------------------------------------------------------


### `abstract def copyToArray[B >: A](xs: Array[B]): Unit`                   ###

[use case]

Copies the elements of this collection or iterator to an array. Fills the given
array `xs` with values of this collection or iterator. Copying will stop once
either the end of the current collection or iterator is reached, or the end of
the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int): Unit`       ###

[use case]

Copies the elements of this collection or iterator to an array. Fills the given
array `xs` with values of this collection or iterator, beginning at index
 `start` . Copying will stop once either the end of the current collection or
iterator is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this collection or iterator to an array. Fills the given
array `xs` with at most `len` elements of this collection or iterator, starting
at position `start` . Copying will stop once either the end of the current
collection or iterator is reached, or the end of the target array is reached, or
 `len` elements have been copied.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

(defined at scala.collection.GenTraversableOnce)


### `abstract def foreach[U](f: (A) ⇒ U): Unit`                              ###

[use case]

Applies a function `f` to all elements of this collection or iterator.

Note: this method underlies the implementation of most other bulk operations.
It's important to implement this method in an efficient way.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

(defined at scala.collection.GenTraversableOnce)


### `abstract def maxBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`        ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection or iterator with the largest value
    measured by function f.

(defined at scala.collection.GenTraversableOnce)


### `abstract def minBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`        ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection or iterator with the smallest value
    measured by function f.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toMap[K, V](implicit ev: <:<[A, (K, V)]): GenMap[K, V]`    ###

[use case]

Converts this collection or iterator to a map. This method is unavailable unless
the elements are members of Tuple2, each ((T, U)) becoming a key-value pair in
the map. Duplicate keys will be overwritten by later keys: if this is an
unordered collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this collection or iterator.
(defined at scala.collection.GenTraversableOnce)
