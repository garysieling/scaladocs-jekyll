
#                   scala.collection.immutable.NumericRange                   #

```scala
abstract class NumericRange[T] extends AbstractSeq[T] with IndexedSeq[T] with Serializable
```

 `NumericRange` is a more generic version of the `Range` class which works with
arbitrary types. It must be supplied with an `Integral` implementation of the
range type.

Factories for likely types include `Range.BigInt` , `Range.Long` , and
 `Range.BigDecimal` . `Range.Int` exists for completeness, but the `Int` -based
 `scala.Range` should be more performant.

```scala
val r1 = new Range(0, 100, 1)
val veryBig = Int.MaxValue.toLong + 1
val r2 = Range.Long(veryBig, veryBig + 100, 1)
assert(r1 sameElements r2.map(_ - veryBig))
```

* Source
  * [NumericRange.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/NumericRange.scala#L1)
* Version
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class Elements extends AbstractIterator[A] with BufferedIterator[A] with Serializable` ###

The class of the iterator returned by the `iterator` method. multiple `take` ,
 `drop` , and `slice` operations on this iterator are bunched together for
better efficiency.

* Attributes
  * protected
* Definition Classes
  * IndexedSeqLike
* Annotations
  * @ SerialVersionUID ()


### `type Self = IndexedSeq[T]`                                              ###

The type implementing this traversable

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike


### `class WithFilter extends FilterMonadic[A, Repr]`                        ###

A class supporting filtered operations. Instances of this class are returned by
method `withFilter` .

* Definition Classes
  * TraversableLike


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def compose[A](g: (A) ⇒ Int): (A) ⇒ T`                                  ###

Composes two instances of Function1 in a new Function1, with this function
applied last.

* A
  * the type to which function `g` can be applied
* g
  * a function A => T1
* returns
  * a new function `f` such that `f(x) == apply(g(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


--------------------------------------------------------------------------------
               Concrete Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `def andThen[C](k: (T) ⇒ C): PartialFunction[Int, C]`                    ###

Composes this partial function with a transformation function that gets applied
to results of this partial function.

* C
  * the result type of the transformation function.
* k
  * the transformation function
* returns
  * a partial function with the same domain as this partial function, which maps
    arguments `x` to `k(this(x))` .

* Definition Classes
  * PartialFunction → Function1

(defined at scala.PartialFunction)


### `def applyOrElse[A1 <: Int, B1 >: T](x: A1, default: (A1) ⇒ B1): B1`     ###

Applies this partial function to the given argument when it is contained in the
function domain. Applies fallback function where this partial function is not
defined.

Note that expression `pf.applyOrElse(x, default)` is equivalent to

```scala
if(pf isDefinedAt x) pf(x) else default(x)
```

except that `applyOrElse` method can be implemented more efficiently. For all
partial function literals the compiler generates an `applyOrElse` implementation
which avoids double evaluation of pattern matchers and guards. This makes
 `applyOrElse` the basis for the efficient implementation for many operations
and scenarios, such as:

* combining partial functions into `orElse` / `andThen` chains does not lead to
   excessive `apply` / `isDefinedAt` evaluation
*  `lift` and `unlift` do not evaluate source functions twice on each invocation
*  `runWith` allows efficient imperative-style combining of partial functions
   with conditionally applied actions

For non-literal partial function classes with nontrivial `isDefinedAt` method it
is recommended to override `applyOrElse` with custom implementation that avoids
double `isDefinedAt` evaluation. This may result in better performance and more
predictable behavior w.r.t. side effects.

* x
  * the function argument
* default
  * the fallback function
* returns
  * the result of this function or fallback function application.

* Definition Classes
  * PartialFunction
* Since
  * 2.10

(defined at scala.PartialFunction)


### `def lift: (Int) ⇒ Option[T]`                                            ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: Int, B1 >: T](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

Composes this partial function with a fallback partial function which gets
applied where this partial function is not defined.

* A1
  * the argument type of the fallback function
* B1
  * the result type of the fallback function
* that
  * the fallback function
* returns
  * a partial function which has as domain the union of the domains of this
    partial function and `that` . The resulting partial function takes `x` to
     `this(x)` where `this` is defined, and to `that(x)` where it is not.

* Definition Classes
  * PartialFunction

(defined at scala.PartialFunction)


### `def runWith[U](action: (T) ⇒ U): (Int) ⇒ Boolean`                       ###

Composes this partial function with an action function which gets applied to
results of this partial function. The action function is invoked only for its
side effects; its result is ignored.

Note that expression `pf.runWith(action)(x)` is equivalent to

```scala
if(pf isDefinedAt x) { action(pf(x)); true } else false
```

except that `runWith` is implemented via `applyOrElse` and thus potentially more
efficient. Using `runWith` avoids double evaluation of pattern matchers and
guards for partial function literals.

* action
  * the action function
* returns
  * a function which maps arguments `x` to `isDefinedAt(x)` . The resulting
    function runs `action(this(x))` where `this` is defined.

* Definition Classes
  * PartialFunction
* Since
  * 2.10
* See also
  * `applyOrElse` .

(defined at scala.PartialFunction)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.GenSeqLike
--------------------------------------------------------------------------------


### `def indexOf[B >: T](elem: B): Int`                                      ###

[use case]

Finds index of first occurrence of some value in this numeric range.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this numeric range that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: T](elem: B, from: Int): Int`                           ###

[use case]

Finds index of first occurrence of some value in this numeric range after or at
some start index.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this numeric range that is equal
    (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (T) ⇒ Boolean): Int`                                  ###

Finds index of first element satisfying some predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the first element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def isDefinedAt(idx: Int): Boolean`                                     ###

Tests whether this general sequence contains given index.

The implementations of methods `apply` and `isDefinedAt` turn a `Seq[A]` into a
 `PartialFunction[Int, A]` .

* idx
  * the index to test
* returns
  * `true` if this general sequence contains an element at position `idx` ,
     `false` otherwise.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: T](elem: B): Int`                                  ###

[use case]

Finds index of last occurrence of some value in this numeric range.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this numeric range that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: T](elem: B, end: Int): Int`                        ###

[use case]

Finds index of last occurrence of some value in this numeric range before or at
a given end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this numeric range that is equal
    (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (T) ⇒ Boolean): Int`                              ###

Finds index of last element satisfying some predicate.

Note: will not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the last element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def prefixLength(p: (T) ⇒ Boolean): Int`                                ###

Returns the length of the longest prefix whose elements all satisfy some
predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the length of the longest prefix of this general sequence such that every
    element of the segment satisfies the predicate `p` .

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def startsWith[B](that: GenSeq[B]): Boolean`                            ###

Tests whether this general sequence starts with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this collection has `that` as a prefix, `false` otherwise.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.IndexedSeqLike
--------------------------------------------------------------------------------


### `def iterator: Iterator[T]`                                              ###

Creates a new iterator over all elements contained in this iterable object.

* returns
  * the new iterator

* Definition Classes
  * IndexedSeqLike → IterableLike → GenIterableLike

(defined at scala.collection.IndexedSeqLike)


### `def thisCollection: collection.IndexedSeq[T]`                           ###

The underlying collection seen as an instance of `IndexedSeq` . By default this
is implemented as the current collection object itself, but this can be
overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IndexedSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.IndexedSeqLike)


### `def toBuffer[A1 >: T]: Buffer[A1]`                                      ###

Uses the contents of this sequence to create a new mutable buffer.

* returns
  * a buffer containing all elements of this sequence.

* Definition Classes
  * IndexedSeqLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IndexedSeqLike)


### `def toCollection(repr: IndexedSeq[T]): collection.IndexedSeq[T]`        ###

A conversion from collections of type `Repr` to `IndexedSeq` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IndexedSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.IndexedSeqLike)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.IterableLike
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


### `def copyToArray[B >: T](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this numeric range to an array. Fills the given array
 `xs` with at most `len` elements of this numeric range, starting at position
 `start` . Copying will stop once either the end of the current numeric range is
reached, or the end of the target array is reached, or `len` elements have been
copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def dropRight(n: Int): IndexedSeq[T]`                                   ###

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
  * IterableLike

(defined at scala.collection.IterableLike)


### `def exists(p: (T) ⇒ Boolean): Boolean`                                  ###

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


### `def find(p: (T) ⇒ Boolean): Option[T]`                                  ###

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


### `def foldRight[B](z: B)(op: (T, B) ⇒ B): B`                              ###

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


### `def forall(p: (T) ⇒ Boolean): Boolean`                                  ###

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


### `def grouped(size: Int): Iterator[IndexedSeq[T]]`                        ###

Partitions elements in fixed size iterable collections.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    will be less than size `size` if the elements don't divide evenly.

* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `grouped`

(defined at scala.collection.IterableLike)


### `def head: T`                                                            ###

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


### `def reduceRight[B >: T](op: (T, B) ⇒ B): B`                             ###

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


### `def sameElements[B >: T](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this numeric range.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def slice(from: Int, until: Int): IndexedSeq[T]`                        ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a iterable collection containing the elements greater than or equal to index
     `from` extending up to (but not including) index `until` of this iterable
    collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def sliding(size: Int): Iterator[IndexedSeq[T]]`                        ###

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
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableLike)


### `def sliding(size: Int, step: Int): Iterator[IndexedSeq[T]]`             ###

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
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableLike)


### `def takeRight(n: Int): IndexedSeq[T]`                                   ###

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
  * IterableLike

(defined at scala.collection.IterableLike)


### `def takeWhile(p: (T) ⇒ Boolean): IndexedSeq[T]`                         ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: collection.Iterable[T]`                                 ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[T]`                                            ###

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


### `def toStream: Stream[T]`                                                ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def zipAll[B, A1 >: T, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[IndexedSeq[T], (A1, B), That]): That` ###

[use case]

Returns a numeric range formed from this numeric range and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is shorter than the other, placeholder elements are used to extend
the shorter collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this numeric range is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    numeric range.
* returns
  * a new numeric range containing pairs consisting of corresponding elements of
    this numeric range and `that` . The length of the returned collection is the
    maximum of the lengths of this numeric range and `that` . If this numeric
    range is shorter than `that` , `thisElem` values are used to pad the result.
    If `that` is shorter than this numeric range, `thatElem` values are used to
    pad the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def zipWithIndex[A1 >: T, That](implicit bf: CanBuildFrom[IndexedSeq[T], (A1, Int), That]): That` ###

[use case]

Zips this numeric range with its indices.

* returns
  * A new numeric range containing pairs consisting of all elements of this
    numeric range paired with their index. Indices start at `0` .

* Definition Classes
  * IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IterableLike)


### `def zip[A1 >: T, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[IndexedSeq[T], (A1, B), That]): That` ###

[use case]

Returns a numeric range formed from this numeric range and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new numeric range containing pairs consisting of corresponding elements of
    this numeric range and `that` . The length of the returned collection is the
    minimum of the lengths of this numeric range and `that` .

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParSeq[T]`                                                     ###

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
              Concrete Value Members From scala.collection.SeqLike
--------------------------------------------------------------------------------


### `def +:[B >: T, That](elem: B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

A copy of the numeric range with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original numeric range is not modified, so you will want to capture
the result.

Example:

```scala
scala> val x = List(1)
x: List[Int] = List(1)

scala> val y = 2 +: x
y: List[Int] = List(2, 1)

scala> println(x)
List(1)
```

* elem
  * the prepended element
* returns
  * a new numeric range consisting of `elem` followed by all elements of this
    numeric range.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def :+[B >: T, That](elem: B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

A copy of this numeric range with an element appended.

A mnemonic for `+:` vs. `:+` is: the COLon goes on the COLlection side.

Example:

```scala
scala> val a = List(1)
a: List[Int] = List(1)

scala> val b = a :+ 2
b: List[Int] = List(1, 2)

scala> println(a)
List(1)
```

* elem
  * the appended element
* returns
  * a new numeric range consisting of all elements of this numeric range
    followed by `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def combinations(n: Int): Iterator[IndexedSeq[T]]`                      ###

Iterates over combinations. A _combination_ of length `n` is a subsequence of
the original sequence, with the elements taken in order. Thus, `"xy"` and
 `"yy"` are both length-2 combinations of `"xyy"` , but `"yx"` is not. If there
is more than one way to generate the same subsequence, only one will be
returned.

For example, `"xyyy"` has three different ways to generate `"xy"` depending on
whether the first, second, or third `"y"` is selected. However, since all are
identical, only one will be chosen. Which of the three will be taken is an
implementation detail that is not defined.

* returns
  * An Iterator which traverses the possible n-element combinations of this
    sequence.

* Definition Classes
  * SeqLike

Example:

```scala
"abbbc".combinations(2) = Iterator(ab, ac, bb, bc)
```

(defined at scala.collection.SeqLike)


### `def containsSlice[B](that: GenSeq[B]): Boolean`                         ###

Tests whether this sequence contains a given sequence as a slice.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence to test
* returns
  * `true` if this sequence contains a slice with the same elements as `that` ,
    otherwise `false` .

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def corresponds[B](that: GenSeq[B])(p: (T, B) ⇒ Boolean): Boolean`      ###

Tests whether every element of this sequence relates to the corresponding
element of another sequence by satisfying a test predicate.

* B
  * the type of the elements of `that`
* that
  * the other sequence
* p
  * the test predicate, which relates elements from both sequences
* returns
  * `true` if both sequences have the same length and `p(x, y)` is `true` for
    all corresponding elements `x` of this sequence and `y` of `that` ,
    otherwise `false` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def diff[B >: T](that: GenSeq[B]): IndexedSeq[T]`                       ###

[use case]

Computes the multiset difference between this numeric range and another
sequence.

* that
  * the sequence of elements to remove
* returns
  * a new numeric range which contains all elements of this numeric range except
    some of occurrences of elements that also appear in `that` . If an element
    value `x` appears _n_ times in `that` , then the first _n_ occurrences of
     `x` will not form part of the result, but any following occurrences will.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def distinct: IndexedSeq[T]`                                            ###

Builds a new sequence from this sequence without any duplicate elements.

Note: will not terminate for infinite-sized collections.

* returns
  * A new sequence which contains the first occurrence of every element of this
    sequence.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def endsWith[B](that: GenSeq[B]): Boolean`                              ###

Tests whether this sequence ends with the given sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to test
* returns
  * `true` if this sequence has `that` as a suffix, `false` otherwise.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def indexOfSlice[B >: T](that: GenSeq[B]): Int`                         ###

Finds first index where this sequence contains a given sequence as a slice.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence to test
* returns
  * the first index such that the elements of this sequence starting at this
    index match the elements of sequence `that` , or `-1` of no such subsequence
    exists.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def indexOfSlice[B >: T](that: GenSeq[B], from: Int): Int`              ###

Finds first index after or at a start index where this sequence contains a given
sequence as a slice.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence to test
* from
  * the start index
* returns
  * the first index `>= from` such that the elements of this sequence starting
    at this index match the elements of sequence `that` , or `-1` of no such
    subsequence exists.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def indexWhere(p: (T) ⇒ Boolean, from: Int): Int`                       ###

Finds index of the first element satisfying some predicate after or at some
start index.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def indices: Range`                                                     ###

Produces the range of all indices of this sequence.

* returns
  * a `Range` value from `0` to one less than the length of this sequence.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def intersect[B >: T](that: GenSeq[B]): IndexedSeq[T]`                  ###

[use case]

Computes the multiset intersection between this numeric range and another
sequence.

* that
  * the sequence of elements to intersect with.
* returns
  * a new numeric range which contains all elements of this numeric range which
    also appear in `that` . If an element value `x` appears _n_ times in `that` ,
    then the first _n_ occurrences of `x` will be retained in the result, but
    any following occurrences will be omitted.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexOfSlice[B >: T](that: GenSeq[B]): Int`                     ###

Finds last index where this sequence contains a given sequence as a slice.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to test
* returns
  * the last index such that the elements of this sequence starting a this index
    match the elements of sequence `that` , or `-1` of no such subsequence
    exists.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexOfSlice[B >: T](that: GenSeq[B], end: Int): Int`           ###

Finds last index before or at a given end index where this sequence contains a
given sequence as a slice.

* that
  * the sequence to test
* end
  * the end index
* returns
  * the last index `<= end` such that the elements of this sequence starting at
    this index match the elements of sequence `that` , or `-1` of no such
    subsequence exists.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexWhere(p: (T) ⇒ Boolean, end: Int): Int`                    ###

Finds index of last element satisfying some predicate before or at given end
index.

* p
  * the predicate used to test elements.
* returns
  * the index `<= end` of the last element of this sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def lengthCompare(len: Int): Int`                                       ###

Compares the length of this sequence to a test value.

* len
  * the test value that gets compared with the length.
* returns
  * A value `x` where

    ```scala
    x <  0       if this.length <  len
    x == 0       if this.length == len
    x >  0       if this.length >  len
    ```

    The method as implemented here does not call `length` directly; its running
    time is `O(length min len)` instead of `O(length)` . The method should be
    overwritten if computing `length` is cheap.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def padTo[B >: T, That](len: Int, elem: B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

A copy of this numeric range with an element value appended until a given target
length is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new numeric range consisting of all elements of this numeric range
    followed by the minimal number of occurrences of `elem` so that the
    resulting numeric range has a length of at least `len` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def patch[B >: T, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Produces a new numeric range where a slice of elements in this numeric range is
replaced by another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original numeric range
* returns
  * a new numeric range consisting of all elements of this numeric range except
    that `replaced` elements starting from `from` are replaced by `patch` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def permutations: Iterator[IndexedSeq[T]]`                              ###

Iterates over distinct permutations.

* returns
  * An Iterator which traverses the distinct permutations of this sequence.

* Definition Classes
  * SeqLike

Example:

```scala
"abb".permutations = Iterator(abb, bab, bba)
```

(defined at scala.collection.SeqLike)


### `def reverse: IndexedSeq[T]`                                             ###

Returns new sequence with elements in reversed order.

Note: will not terminate for infinite-sized collections.

* returns
  * A new sequence with all elements of this sequence in reversed order.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def reverseIterator: Iterator[T]`                                       ###

An iterator yielding elements in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseIterator` is the same as `xs.reverse.iterator` but might be
more efficient.

* returns
  * an iterator yielding the elements of this sequence in reversed order

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def reverseMap[B, That](f: (T) ⇒ B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this numeric
range and collecting the results in reversed order.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new numeric range resulting from applying the given function `f` to each
    element of this numeric range and collecting the results in reversed order.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def segmentLength(p: (T) ⇒ Boolean, from: Int): Int`                    ###

Computes length of longest segment whose elements all satisfy some predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* from
  * the index where the search starts.
* returns
  * the length of the longest segment of this sequence starting from index
     `from` such that every element of the segment satisfies the predicate `p` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def sortBy[B](f: (T) ⇒ B)(implicit ord: math.Ordering[B]): IndexedSeq[T]` ###

Sorts this `Seq` according to the Ordering which results from transforming an
implicitly given Ordering with a transformation function.

* B
  * the target type of the transformation `f` , and the type where the ordering
     `ord` is defined.
* f
  * the transformation function mapping elements to some other domain `B` .
* ord
  * the ordering assumed on domain `B` .
* returns
  * a sequence consisting of the elements of this sequence sorted according to
    the ordering where `x < y` if `ord.lt(f(x), f(y))` .

* Definition Classes
  * SeqLike
* See also
  * scala.math.Ordering Note: will not terminate for infinite-sized collections.

Example:

```scala
val words = "The quick brown fox jumped over the lazy dog".split(' ')
// this works because scala.Ordering will implicitly provide an Ordering[Tuple2[Int, Char]]
words.sortBy(x => (x.length, x.head))
res0: Array[String] = Array(The, dog, fox, the, lazy, over, brown, quick, jumped)
```

(defined at scala.collection.SeqLike)


### `def sortWith(lt: (T, T) ⇒ Boolean): IndexedSeq[T]`                      ###

Sorts this sequence according to a comparison function.

Note: will not terminate for infinite-sized collections.

The sort is stable. That is, elements that are equal (as determined by `lt` )
appear in the same order in the sorted sequence as in the original.

* lt
  * the comparison function which tests whether its first argument precedes its
    second argument in the desired ordering.
* returns
  * a sequence consisting of the elements of this sequence sorted according to
    the comparison function `lt` .

* Definition Classes
  * SeqLike

Example:

```scala
List("Steve", "Tom", "John", "Bob").sortWith(_.compareTo(_) < 0) =
List("Bob", "John", "Steve", "Tom")
```

(defined at scala.collection.SeqLike)


### `def sorted[B >: T](implicit ord: math.Ordering[B]): IndexedSeq[T]`      ###

Sorts this sequence according to an Ordering.

The sort is stable. That is, elements that are equal (as determined by `lt` )
appear in the same order in the sorted sequence as in the original.

* ord
  * the ordering to be used to compare elements.
* returns
  * a sequence consisting of the elements of this sequence sorted according to
    the ordering `ord` .

* Definition Classes
  * SeqLike
* See also
  * scala.math.Ordering

(defined at scala.collection.SeqLike)


### `def startsWith[B](that: GenSeq[B], offset: Int): Boolean`               ###

Tests whether this sequence contains the given sequence at a given index.

 *Note* : If the both the receiver object `this` and the argument `that` are
infinite sequences this method may not terminate.

* that
  * the sequence to test
* offset
  * the index where the sequence is searched.
* returns
  * `true` if the sequence `that` is contained in this sequence at index
     `offset` , otherwise `false` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def union[B >: T, That](that: GenSeq[B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this numeric range and
also all elements of a given sequence. `xs union ys` is equivalent to
 `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

* that
  * the sequence to add.
* returns
  * a new numeric range which contains all elements of this numeric range
    followed by all elements of `that` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def updated[B >: T, That](index: Int, elem: B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

A copy of this numeric range with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this numeric range with the element at position `index` replaced
    by `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def view(from: Int, until: Int): SeqView[T, IndexedSeq[T]]`             ###

Creates a non-strict view of a slice of this sequence.

Note: the difference between `view` and `slice` is that `view` produces a view
of the current sequence, whereas `slice` produces a new sequence.

Note: `view(from, to)` is equivalent to `view.slice(from, to)`

* from
  * the index of the first element of the view
* until
  * the index of the element following the view
* returns
  * a non-strict view of a slice of this sequence, starting at index `from` and
    extending up to (but not including) index `until` .

* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


### `def view: SeqView[T, IndexedSeq[T]]`                                    ###

Creates a non-strict view of this sequence.

* returns
  * a non-strict view of this sequence.

* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: T, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

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
* that
  * the traversable to append.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and and the new element
    type `B` .
* returns
  * a new collection of type `That` which contains all elements of this
    traversable collection followed by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++:[B >: T, That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

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
  * a new numeric range which contains all elements of this numeric range
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++[B >: T, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Returns a new numeric range containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
numeric range is the most specific superclass encompassing the element types of
the two operands.

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
  * a new numeric range which contains all elements of this numeric range
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def collect[B, That](pf: PartialFunction[T, B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
numeric range on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the numeric range.
* returns
  * a new numeric range resulting from applying the given partial function `pf`
    to each element on which it is defined and collecting the results. The order
    of the elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def dropWhile(p: (T) ⇒ Boolean): IndexedSeq[T]`                         ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this traversable collection whose first element does
    not satisfy the predicate `p` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: (T) ⇒ Boolean): IndexedSeq[T]`                            ###

Selects all elements of this traversable collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new traversable collection consisting of all elements of this traversable
    collection that satisfy the given predicate `p` . The order of the elements
    is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filterNot(p: (T) ⇒ Boolean): IndexedSeq[T]`                         ###

Selects all elements of this traversable collection which do not satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * a new traversable collection consisting of all elements of this traversable
    collection that do not satisfy the given predicate `p` . The order of the
    elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def flatMap[B, That](f: (T) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this numeric
range and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of numeric
range. This might cause unexpected results sometimes. For example:

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
  * a new numeric range resulting from applying the given collection-valued
    function `f` to each element of this numeric range and concatenating the
    results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def groupBy[K](f: (T) ⇒ K): Map[K, IndexedSeq[T]]`                      ###

Partitions this traversable collection into a map of traversable collections
according to some discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new traversable collection.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to traversable collections such that the following invariant
    holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a traversable collection of those
    elements `x` for which `f(x)` equals `k` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def headOption: Option[T]`                                              ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def init: IndexedSeq[T]`                                                ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a traversable collection consisting of all elements of this traversable
    collection except the last one.

* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the traversable collection is empty.

(defined at scala.collection.TraversableLike)


### `def inits: Iterator[IndexedSeq[T]]`                                     ###

Iterates over the inits of this traversable collection. The first value will be
this traversable collection and the final one will be an empty traversable
collection, with the intervening values the results of successive applications
of `init` .

* returns
  * an iterator over all the inits of this traversable collection

* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).inits = Iterator(List(1,2,3), List(1,2), List(1), Nil)
```

(defined at scala.collection.TraversableLike)


### `def lastOption: Option[T]`                                              ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this traversable collection$ if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def map[B, That](f: (T) ⇒ B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this numeric
range.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new numeric range resulting from applying the given function `f` to each
    element of this numeric range and collecting the results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def partition(p: (T) ⇒ Boolean): (IndexedSeq[T], IndexedSeq[T])`        ###

Partitions this traversable collection in two traversable collections according
to a predicate.

* p
  * the predicate on which to partition.
* returns
  * a pair of traversable collections: the first traversable collection consists
    of all elements that satisfy the predicate `p` and the second traversable
    collection consists of all elements that don't. The relative order of the
    elements in the resulting traversable collections is the same as in the
    original traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def repr: IndexedSeq[T]`                                                ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanLeft[B, That](z: B)(op: (B, T) ⇒ B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

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
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanRight[B, That](z: B)(op: (T, B) ⇒ B)(implicit bf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

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
  * TraversableLike → GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(defined at scala.collection.TraversableLike)


### `def scan[B >: T, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[IndexedSeq[T], B, That]): That` ###

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


### `def span(p: (T) ⇒ Boolean): (IndexedSeq[T], IndexedSeq[T])`             ###

Splits this traversable collection into a prefix/suffix pair according to a
predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a pair consisting of the longest prefix of this traversable collection whose
    elements all satisfy `p` , and the rest of this traversable collection.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def splitAt(n: Int): (IndexedSeq[T], IndexedSeq[T])`                    ###

Splits this traversable collection into two at a given position. Note:
 `c splitAt n` is equivalent to (but possibly more efficient than)
 `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of traversable collections consisting of the first `n` elements of
    this traversable collection, and the other elements.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def tail: IndexedSeq[T]`                                                ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a traversable collection consisting of all elements of this traversable
    collection except the first one.

* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the traversable collection is empty.

(defined at scala.collection.TraversableLike)


### `def tails: Iterator[IndexedSeq[T]]`                                     ###

Iterates over the tails of this traversable collection. The first value will be
this traversable collection and the final one will be an empty traversable
collection, with the intervening values the results of successive applications
of `tail` .

* returns
  * an iterator over all the tails of this traversable collection

* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).tails = Iterator(List(1,2,3), List(2,3), List(3), Nil)
```

(defined at scala.collection.TraversableLike)


### `def toTraversable: collection.Traversable[T]`                           ###

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


### `def withFilter(p: (T) ⇒ Boolean): FilterMonadic[T, IndexedSeq[T]]`      ###

Creates a non-strict filter of this traversable collection.

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
    those elements of this traversable collection which satisfy the predicate
     `p` .

* Definition Classes
  * TraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


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

Copies the elements of this numeric range to an array. Fills the given array
 `xs` with values of this numeric range. Copying will stop once either the end
of the current numeric range is reached, or the end of the target array is
reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: T](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this numeric range to an array. Fills the given array
 `xs` with values of this numeric range, beginning at index `start` . Copying
will stop once either the end of the current numeric range is reached, or the
end of the target array is reached.

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


### `def count(p: (T) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

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


### `def fold[A1 >: T](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

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


### `def maxBy[B](f: (T) ⇒ B)(implicit cmp: Ordering[B]): T`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this numeric range with the largest value measured by
    function f.

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
  * the first element of this numeric range with the smallest value measured by
    function f.

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


### `def reduce[A1 >: T](op: (A1, A1) ⇒ A1): A1`                             ###

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


### `def reversed: scala.List[T]`                                            ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: scala.List[T]`                                              ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[T, (T, U)]): Map[T, U]`                ###

[use case]

Converts this numeric range to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this numeric range.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: T]: Set[B]`                                              ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: scala.Vector[T]`                                          ###

Converts this traversable or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def flatten[B](implicit asTraversable: (T) ⇒ GenTraversableOnce[B]): IndexedSeq[B]` ###

[use case]

Converts this numeric range of traversable collections into a numeric range
formed by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of numeric
range. For example:

```scala
val xs = List(
           Set(1, 2, 3),
           Set(1, 2, 3)
         ).flatten
// xs == List(1, 2, 3, 1, 2, 3)

val ys = Set(
           List(1, 2, 3),
           List(3, 2, 1)
         ).flatten
// ys == Set(1, 2, 3)
```

* B
  * the type of the elements of each traversable collection.
* returns
  * a new numeric range resulting from concatenating all element numeric ranges.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, IndexedSeq[B]]`                       ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def newBuilder: Builder[T, IndexedSeq[T]]`                              ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (T) ⇒ GenTraversableOnce[B]): IndexedSeq[IndexedSeq[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (T) ⇒ (A1, A2, A3)): (IndexedSeq[A1], IndexedSeq[A2], IndexedSeq[A3])` ###

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
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def unzip[A1, A2](implicit asPair: (T) ⇒ (A1, A2)): (IndexedSeq[A1], IndexedSeq[A2])` ###

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
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.immutable.IndexedSeq
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[IndexedSeq]`                            ###

The factory companion object that builds instances of class IndexedSeq. (or its
 `Iterable` superclass where class IndexedSeq is not a `Seq` .)

* Definition Classes
  * IndexedSeq → IndexedSeq → Seq → Seq → GenSeq → Iterable → Iterable →
    GenIterable → Traversable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.immutable.IndexedSeq)


### `def seq: IndexedSeq[T]`                                                 ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * IndexedSeq → IndexedSeq → IndexedSeqLike → Seq → Seq → GenSeq → GenSeqLike →
    Iterable → Iterable → GenIterable → Traversable → Traversable →
    GenTraversable → Parallelizable → TraversableOnce → GenTraversableOnce

(defined at scala.collection.immutable.IndexedSeq)


### `def toIndexedSeq: IndexedSeq[T]`                                        ###

Returns this immutable sequence as an indexed sequence.

A new indexed sequence will not be built; lazy collections will stay lazy.

* returns
  * an indexed sequence containing all elements of this immutable sequence.

* Definition Classes
  * IndexedSeq → TraversableOnce → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.immutable.IndexedSeq)


--------------------------------------------------------------------------------
      Abstract Value Members From scala.collection.immutable.NumericRange
--------------------------------------------------------------------------------


### `abstract def copy(start: T, end: T, step: T): NumericRange[T]`          ###

Create a copy of this range.

(defined at scala.collection.immutable.NumericRange)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.immutable.NumericRange
--------------------------------------------------------------------------------


### `def apply(idx: Int): T`                                                 ###

Selects an element by its index in the numeric range.

Example:

```scala
scala> val x = List(1, 2, 3, 4, 5)
x: List[Int] = List(1, 2, 3, 4, 5)

scala> x(3)
res1: Int = 4
```

* idx
  * The index to select.
* returns
  * the element of this numeric range at index `idx` , where `0` indicates the
    first element.

* Definition Classes
  * NumericRange → SeqLike → GenSeqLike → Function1
* Exceptions thrown
  * IndexOutOfBoundsException if `idx` does not satisfy `0 <= idx < length` .

(defined at scala.collection.immutable.NumericRange)


### `def by(newStep: T): NumericRange[T]`                                    ###

Create a new range with the start and end values of this range and a new `step` .

(defined at scala.collection.immutable.NumericRange)


### `def containsTyped(x: T): Boolean`                                       ###

(defined at scala.collection.immutable.NumericRange)


### `def contains[A1 >: T](x: A1): Boolean`                                  ###

Tests whether this numeric range contains a given value as an element.

* returns
  * `true` if this numeric range has an element that is equal (as determined by
     `==` ) to `elem` , `false` otherwise.

* Definition Classes
  * NumericRange → SeqLike

(defined at scala.collection.immutable.NumericRange)


### `final def drop(n: Int): NumericRange[T]`                                ###

Selects all elements except first _n_ ones.

* n
  * the number of elements to drop from this numeric range.
* returns
  * a numeric range consisting of all elements of this numeric range except the
    first `n` ones, or else the empty numeric range, if this numeric range has
    less than `n` elements.

* Definition Classes
  * NumericRange → IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.immutable.NumericRange)


### `def equals(other: Any): Boolean`                                        ###

The equals method for arbitrary sequences. Compares this sequence to some other
object.

* returns
  * `true` if `that` is a sequence that has the same elements as this sequence
    in the same order, `false` otherwise

* Definition Classes
  * NumericRange → GenSeqLike → Equals → AnyRef → Any

(defined at scala.collection.immutable.NumericRange)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of this numeric range.

Note: this method underlies the implementation of most other bulk operations.
Subclasses should re-implement this method if a more efficient implementation
exists.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * NumericRange → IterableLike → GenericTraversableTemplate → TraversableLike →
    GenTraversableLike → TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.immutable.NumericRange)


### `final def take(n: Int): NumericRange[T]`                                ###

Selects first _n_ elements.

* n
  * the number of elements to take from this numeric range.
* returns
  * a numeric range consisting only of the first `n` elements of this numeric
    range, or else the whole numeric range, if it has less than `n` elements.

* Definition Classes
  * NumericRange → IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.immutable.NumericRange)


--------------------------------------------------------------------------------
       Instance Constructors From scala.collection.immutable.NumericRange
--------------------------------------------------------------------------------


### `new NumericRange(start: T, end: T, step: T, isInclusive: Boolean)(implicit num: Integral[T])` ###

(defined at scala.collection.immutable.NumericRange)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.immutable.Seq
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[T, ParSeq[T]]`                                ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * Seq → SeqLike → Iterable → TraversableLike → Parallelizable

(defined at scala.collection.immutable.Seq)


### `def toSeq: Seq[T]`                                                      ###

Converts this immutable sequence to a sequence.

Note: will not terminate for infinite-sized collections.

A new collection will not be built; in particular, lazy sequences will stay
lazy.

* returns
  * a sequence containing all elements of this immutable sequence.

* Definition Classes
  * Seq → SeqLike → GenSeqLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.immutable.Seq)


--------------------------------------------------------------------------------
       Concrete Value Members From Implicit scala.Predef.SeqCharSequence
--------------------------------------------------------------------------------


### `def charAt(index: Int): Char`                                           ###

* Implicit information
  * This member is added by an implicit conversion from NumericRange [T] to
    SeqCharSequence performed by method SeqCharSequence in scala.Predef. This
    conversion will take place only if T is a subclass of Char (T <: Char).
* Definition Classes
  * SeqCharSequence → CharSequence

(added by implicit convertion: scala.Predef.SeqCharSequence)


### `def chars(): IntStream`                                                 ###

* Implicit information
  * This member is added by an implicit conversion from NumericRange [T] to
    SeqCharSequence performed by method SeqCharSequence in scala.Predef. This
    conversion will take place only if T is a subclass of Char (T <: Char).
* Definition Classes
  * CharSequence

(added by implicit convertion: scala.Predef.SeqCharSequence)


### `def codePoints(): IntStream`                                            ###

* Implicit information
  * This member is added by an implicit conversion from NumericRange [T] to
    SeqCharSequence performed by method SeqCharSequence in scala.Predef. This
    conversion will take place only if T is a subclass of Char (T <: Char).
* Definition Classes
  * CharSequence

(added by implicit convertion: scala.Predef.SeqCharSequence)


### `def subSequence(start: Int, end: Int): CharSequence`                    ###

* Implicit information
  * This member is added by an implicit conversion from NumericRange [T] to
    SeqCharSequence performed by method SeqCharSequence in scala.Predef. This
    conversion will take place only if T is a subclass of Char (T <: Char).
* Definition Classes
  * SeqCharSequence → CharSequence

(added by implicit convertion: scala.Predef.SeqCharSequence)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from NumericRange [T] to
    CollectionsHaveToParArray [NumericRange [T], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (NumericRange [T]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
