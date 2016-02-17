
#                   scala.collection.immutable.Stream.Empty                   #

```scala
object Empty extends Stream[Nothing]
```

* Source
  * [Stream.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stream.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Self = Stream[Nothing]`                                            ###

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
                       Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def compose[A](g: (A) ⇒ Int): (A) ⇒ Nothing`                            ###

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
                    Value Members From scala.PartialFunction
--------------------------------------------------------------------------------


### `def andThen[C](k: (Nothing) ⇒ C): PartialFunction[Int, C]`              ###

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


### `def applyOrElse[A1 <: Int, B1 >: Nothing](x: A1, default: (A1) ⇒ B1): B1` ###

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


### `def lift: (Int) ⇒ Option[Nothing]`                                      ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: Int, B1 >: Nothing](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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


### `def runWith[U](action: (Nothing) ⇒ U): (Int) ⇒ Boolean`                 ###

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
                 Value Members From scala.collection.GenSeqLike
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

The equals method for arbitrary sequences. Compares this sequence to some other
object.

* that
  * The object to compare the sequence to
* returns
  * `true` if `that` is a sequence that has the same elements as this sequence
    in the same order, `false` otherwise

* Definition Classes
  * GenSeqLike → Equals → Any

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: Nothing](elem: B): Int`                                ###

[use case]

Finds index of first occurrence of some value in this stream.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this stream that is equal (as determined
    by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: Nothing](elem: B, from: Int): Int`                     ###

[use case]

Finds index of first occurrence of some value in this stream after or at some
start index.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this stream that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (Nothing) ⇒ Boolean): Int`                            ###

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


### `def lastIndexOf[B >: Nothing](elem: B): Int`                            ###

[use case]

Finds index of last occurrence of some value in this stream.

Note: will not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this stream that is equal (as determined by
     `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: Nothing](elem: B, end: Int): Int`                  ###

[use case]

Finds index of last occurrence of some value in this stream before or at a given
end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this stream that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (Nothing) ⇒ Boolean): Int`                        ###

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


### `def prefixLength(p: (Nothing) ⇒ Boolean): Int`                          ###

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

Copies the elements of this stream to an array. Fills the given array `xs` with
at most `len` elements of this stream, starting at position `start` . Copying
will stop once either the end of the current stream is reached, or the end of
the target array is reached, or `len` elements have been copied.

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


### `def grouped(size: Int): Iterator[Stream[Nothing]]`                      ###

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


### `def sliding(size: Int): Iterator[Stream[Nothing]]`                      ###

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


### `def sliding(size: Int, step: Int): Iterator[Stream[Nothing]]`           ###

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


### `def toIterable: collection.Iterable[Nothing]`                           ###

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


### `def zipAll[B, A1 >: Nothing, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[Stream[Nothing], (A1, B), That]): That` ###

[use case]

Returns a stream formed from this stream and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
shorter than the other, placeholder elements are used to extend the shorter
collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this stream is shorter than
     `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    stream.
* returns
  * a new stream containing pairs consisting of corresponding elements of this
    stream and `that` . The length of the returned collection is the maximum of
    the lengths of this stream and `that` . If this stream is shorter than
     `that` , `thisElem` values are used to pad the result. If `that` is shorter
    than this stream, `thatElem` values are used to pad the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
               Value Members From scala.collection.LinearSeqLike
--------------------------------------------------------------------------------


### `final def corresponds[B](that: GenSeq[B])(p: (Nothing, B) ⇒ Boolean): Boolean` ###

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
  * LinearSeqLike → SeqLike → GenSeqLike
* Annotations
  * @ tailrec ()

(defined at scala.collection.LinearSeqLike)


### `def thisCollection: collection.LinearSeq[Nothing]`                      ###

The underlying collection seen as an instance of `Seq` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * LinearSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.LinearSeqLike)


### `def toCollection(repr: Stream[Nothing]): collection.LinearSeq[Nothing]` ###

A conversion from collections of type `Repr` to `Seq` objects. By default this
is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * LinearSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.LinearSeqLike)


--------------------------------------------------------------------------------
             Value Members From scala.collection.LinearSeqOptimized
--------------------------------------------------------------------------------


### `def apply(n: Int): Nothing`                                             ###

Selects an element by its index in the sequence. Note: the execution of `apply`
may take time proportional to the index value.

* returns
  * the element of this sequence at index `idx` , where `0` indicates the first
    element.

* Definition Classes
  * LinearSeqOptimized → SeqLike → GenSeqLike
* Exceptions thrown
  * IndexOutOfBoundsException if `idx` does not satisfy `0 <= idx < length` .

(defined at scala.collection.LinearSeqOptimized)


### `def contains[A1 >: Nothing](elem: A1): Boolean`                         ###

Tests whether this sequence contains a given value as an element.

Note: may not terminate for infinite-sized collections.

* elem
  * the element to test.
* returns
  * `true` if this sequence has an element that is equal (as determined by `==` )
    to `elem` , `false` otherwise.

* Definition Classes
  * LinearSeqOptimized → SeqLike

(defined at scala.collection.LinearSeqOptimized)


### `def exists(p: (Nothing) ⇒ Boolean): Boolean`                            ###

Tests whether a predicate holds for at least one element of this sequence.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `false` if this sequence is empty, otherwise `true` if the given predicate
     `p` holds for some of the elements of this sequence, otherwise `false`

* Definition Classes
  * LinearSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.LinearSeqOptimized)


### `def find(p: (Nothing) ⇒ Boolean): Option[Nothing]`                      ###

Finds the first element of the sequence satisfying a predicate, if any.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the sequence that satisfies
     `p` , or `None` if none exists.

* Definition Classes
  * LinearSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.LinearSeqOptimized)


### `def foldRight[B](z: B)(op: (Nothing, B) ⇒ B): B`                        ###

Applies a binary operator to all elements of this sequence and a start value,
going right to left.

Note: will not terminate for infinite-sized collections.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this sequence,
    going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this sequence. Returns `z` if this
    sequence is empty.

* Definition Classes
  * LinearSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.LinearSeqOptimized)


### `def forall(p: (Nothing) ⇒ Boolean): Boolean`                            ###

Tests whether a predicate holds for all elements of this sequence.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this sequence is empty or the given predicate `p` holds for all
    elements of this sequence, otherwise `false` .

* Definition Classes
  * LinearSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.LinearSeqOptimized)


### `def indexWhere(p: (Nothing) ⇒ Boolean, from: Int): Int`                 ###

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
  * LinearSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.LinearSeqOptimized)


### `def isDefinedAt(x: Int): Boolean`                                       ###

Tests whether this sequence contains given index.

The implementations of methods `apply` and `isDefinedAt` turn a `Seq[A]` into a
 `PartialFunction[Int, A]` .

* returns
  * `true` if this sequence contains an element at position `idx` , `false`
    otherwise.

* Definition Classes
  * LinearSeqOptimized → GenSeqLike

(defined at scala.collection.LinearSeqOptimized)


### `def last: Nothing`                                                      ###

Selects the last element.

* returns
  * The last element of this sequence.

* Definition Classes
  * LinearSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the sequence is empty.

(defined at scala.collection.LinearSeqOptimized)


### `def lastIndexWhere(p: (Nothing) ⇒ Boolean, end: Int): Int`              ###

Finds index of last element satisfying some predicate before or at given end
index.

* p
  * the predicate used to test elements.
* returns
  * the index `<= end` of the last element of this sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * LinearSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.LinearSeqOptimized)


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
  * LinearSeqOptimized → SeqLike

(defined at scala.collection.LinearSeqOptimized)


### `def reduceRight[B >: Nothing](op: (Nothing, B) ⇒ B): B`                 ###

Applies a binary operator to all elements of this sequence, going right to left.

Note: will not terminate for infinite-sized collections.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this sequence,
    going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this sequence.

* Definition Classes
  * LinearSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this sequence is empty.

(defined at scala.collection.LinearSeqOptimized)


### `def sameElements[B >: Nothing](that: GenIterable[B]): Boolean`          ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this stream.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * LinearSeqOptimized → IterableLike → GenIterableLike

(defined at scala.collection.LinearSeqOptimized)


### `def segmentLength(p: (Nothing) ⇒ Boolean, from: Int): Int`              ###

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
  * LinearSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.LinearSeqOptimized)


### `def span(p: (Nothing) ⇒ Boolean): (Stream[Nothing], Stream[Nothing])`   ###

Splits this sequence into a prefix/suffix pair according to a predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

* returns
  * a pair consisting of the longest prefix of this sequence whose elements all
    satisfy `p` , and the rest of this sequence.

* Definition Classes
  * LinearSeqOptimized → TraversableLike → GenTraversableLike

(defined at scala.collection.LinearSeqOptimized)


--------------------------------------------------------------------------------
               Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParSeq[Nothing]`                                               ###

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
                  Value Members From scala.collection.SeqLike
--------------------------------------------------------------------------------


### `def :+[B >: Nothing, That](elem: B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

A copy of this stream with an element appended.

A mnemonic for `+:` vs. `:+` is: the COLon goes on the COLlection side.

Note: will not terminate for infinite-sized collections.

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
  * a new stream consisting of all elements of this stream followed by `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def combinations(n: Int): Iterator[Stream[Nothing]]`                    ###

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


### `def diff[B >: Nothing](that: GenSeq[B]): Stream[Nothing]`               ###

[use case]

Computes the multiset difference between this stream and another sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence of elements to remove
* returns
  * a new stream which contains all elements of this stream except some of
    occurrences of elements that also appear in `that` . If an element value
     `x` appears _n_ times in `that` , then the first _n_ occurrences of `x`
    will not form part of the result, but any following occurrences will.

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


### `def indexOfSlice[B >: Nothing](that: GenSeq[B]): Int`                   ###

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


### `def indexOfSlice[B >: Nothing](that: GenSeq[B], from: Int): Int`        ###

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


### `def indices: Range`                                                     ###

Produces the range of all indices of this sequence.

* returns
  * a `Range` value from `0` to one less than the length of this sequence.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def intersect[B >: Nothing](that: GenSeq[B]): Stream[Nothing]`          ###

[use case]

Computes the multiset intersection between this stream and another sequence.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence of elements to intersect with.
* returns
  * a new stream which contains all elements of this stream which also appear in
     `that` . If an element value `x` appears _n_ times in `that` , then the
    first _n_ occurrences of `x` will be retained in the result, but any
    following occurrences will be omitted.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexOfSlice[B >: Nothing](that: GenSeq[B]): Int`               ###

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


### `def lastIndexOfSlice[B >: Nothing](that: GenSeq[B], end: Int): Int`     ###

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


### `def patch[B >: Nothing, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

Produces a new stream where a slice of elements in this stream is replaced by
another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original stream
* returns
  * a new stream consisting of all elements of this stream except that
     `replaced` elements starting from `from` are replaced by `patch` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def permutations: Iterator[Stream[Nothing]]`                            ###

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


### `def reverseIterator: Iterator[Nothing]`                                 ###

An iterator yielding elements in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseIterator` is the same as `xs.reverse.iterator` but might be
more efficient.

* returns
  * an iterator yielding the elements of this sequence in reversed order

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def reverseMap[B, That](f: (Nothing) ⇒ B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this stream
and collecting the results in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new stream resulting from applying the given function `f` to each element
    of this stream and collecting the results in reversed order.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def sortBy[B](f: (Nothing) ⇒ B)(implicit ord: math.Ordering[B]): Stream[Nothing]` ###

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


### `def sortWith(lt: (Nothing, Nothing) ⇒ Boolean): Stream[Nothing]`        ###

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


### `def sorted[B >: Nothing](implicit ord: math.Ordering[B]): Stream[Nothing]` ###

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


### `def union[B >: Nothing, That](that: GenSeq[B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this stream and also all
elements of a given sequence. `xs union ys` is equivalent to `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to add.
* returns
  * a new stream which contains all elements of this stream followed by all
    elements of `that` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def updated[B >: Nothing, That](index: Int, elem: B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

A copy of this stream with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this stream with the element at position `index` replaced by
     `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def view(from: Int, until: Int): SeqView[Nothing, Stream[Nothing]]`     ###

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


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: Nothing, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

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


### `def ++:[B >: Nothing, That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

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
  * a new stream which contains all elements of this stream followed by all
    elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: (Nothing) ⇒ Boolean): Stream[Nothing]`                    ###

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


### `def filterNot(p: (Nothing) ⇒ Boolean): Stream[Nothing]`                 ###

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


### `def groupBy[K](f: (Nothing) ⇒ K): Map[K, Stream[Nothing]]`              ###

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


### `def headOption: Option[Nothing]`                                        ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def inits: Iterator[Stream[Nothing]]`                                   ###

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


### `def lastOption: Option[Nothing]`                                        ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this traversable collection$ if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def repr: Stream[Nothing]`                                              ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanRight[B, That](z: B)(op: (Nothing, B) ⇒ B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

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


### `def scan[B >: Nothing, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

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


### `def tails: Iterator[Stream[Nothing]]`                                   ###

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


### `def toTraversable: collection.Traversable[Nothing]`                     ###

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

Copies the elements of this stream to an array. Fills the given array `xs` with
values of this stream. Copying will stop once either the end of the current
stream is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: Nothing](xs: Array[B], start: Int): Unit`          ###

[use case]

Copies the elements of this stream to an array. Fills the given array `xs` with
values of this stream, beginning at index `start` . Copying will stop once
either the end of the current stream is reached, or the end of the target array
is reached.

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
  * the first element of this stream with the largest value measured by function
    f.

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
  * the first element of this stream with the smallest value measured by
    function f.

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


### `def reversed: scala.List[Nothing]`                                      ###

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


### `def toIndexedSeq: IndexedSeq[Nothing]`                                  ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: scala.List[Nothing]`                                        ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[Nothing, (T, U)]): Map[T, U]`          ###

[use case]

Converts this stream to a map. This method is unavailable unless the elements
are members of Tuple2, each ((T, U)) becoming a key-value pair in the map.
Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this stream.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: Nothing]: Set[B]`                                        ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: scala.Vector[Nothing]`                                    ###

Converts this traversable or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
     Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def genericBuilder[B]: Builder[B, Stream[B]]`                           ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def newBuilder: Builder[Nothing, Stream[Nothing]]`                      ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (Nothing) ⇒ GenTraversableOnce[B]): Stream[Stream[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (Nothing) ⇒ (A1, A2, A3)): (Stream[A1], Stream[A2], Stream[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (Nothing) ⇒ (A1, A2)): (Stream[A1], Stream[A2])` ###

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
            Value Members From scala.collection.immutable.LinearSeq
--------------------------------------------------------------------------------


### `def seq: LinearSeq[Nothing]`                                            ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * LinearSeq → LinearSeq → LinearSeqLike → Seq → Seq → GenSeq → GenSeqLike →
    Iterable → Iterable → GenIterable → Traversable → Traversable →
    GenTraversable → Parallelizable → TraversableOnce → GenTraversableOnce

(defined at scala.collection.immutable.LinearSeq)


--------------------------------------------------------------------------------
               Value Members From scala.collection.immutable.Seq
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[Nothing, ParSeq[Nothing]]`                    ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * Seq → SeqLike → Iterable → TraversableLike → Parallelizable

(defined at scala.collection.immutable.Seq)


### `def toSeq: Seq[Nothing]`                                                ###

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
              Value Members From scala.collection.immutable.Stream
--------------------------------------------------------------------------------


### `def ++[B >: Nothing, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

Create a new stream which contains all elements of this stream followed by all
elements of Traversable `that` .

* B
  * The element type of the returned collection. *That*
* That
  * the class of the returned collection. Where possible, `That` is the same
    class as the current collection class `Repr` , but this depends on the
    element type `B` being admissible for that class, which means that an
    implicit instance of type `CanBuildFrom[Repr, B, That]` is found.
* that
  * The scala.collection.GenTraversableOnce the be concatenated to this
     `Stream` .
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * A new collection containing the result of concatenating `this` with `that` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike
* Note
  * This method doesn't cause the `Stream` to be fully realized but it should be
    noted that using the `++` operator from another collection type could cause
    infinite realization of a `Stream` . For example, referring to the
    definition of `fibs` in the preamble, the following would never return:
     `List(BigInt(12)) ++ fibs` ., It's subtle why this works. We know that if
    the target type of the scala.collection.mutable.Builder `That` is either a
     `Stream` , or one of its supertypes, or undefined, then `StreamBuilder`
    will be chosen for the implicit. We recognize that fact and optimize to get
    more laziness.

(defined at scala.collection.immutable.Stream)


### `def +:[B >: Nothing, That](elem: B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

A copy of the stream with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original stream is not modified, so you will want to capture the
result.

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
  * a new stream consisting of `elem` followed by all elements of this stream.

* Definition Classes
  * Stream → SeqLike → GenSeqLike

(defined at scala.collection.immutable.Stream)


### `def addString(b: mutable.StringBuilder, start: String, sep: String, end: String): mutable.StringBuilder` ###

Write all defined elements of this iterable into given string builder. The
written text begins with the string `start` and is finished by the string `end` .
Inside, the string representations of defined elements (w.r.t. the method
 `toString()` ) are separated by the string `sep` . The method will not force
evaluation of undefined elements. A tail of such elements will be represented by
a `"?"` instead. A cyclic stream is represented by a `"..."` at the point where
the cycle repeats.

* b
  * The collection.mutable.StringBuilder factory to which we need to add the
    string elements.
* start
  * The prefix of the resulting string (e.g. "Stream(")
* sep
  * The separator between elements of the resulting string (e.g. ",")
* end
  * The end of the resulting string (e.g. ")")
* returns
  * The original collection.mutable.StringBuilder containing the resulting
    string.

* Definition Classes
  * Stream → TraversableOnce

(defined at scala.collection.immutable.Stream)


### `def append[B >: Nothing](rest: ⇒ TraversableOnce[B]): Stream[B]`        ###

The stream resulting from the concatenation of this stream with the argument
stream.

* rest
  * The stream that gets appended to this stream
* returns
  * The stream containing elements of this stream and the traversable object.

* Definition Classes
  * Stream

(defined at scala.collection.immutable.Stream)


### `final def collect[B, That](pf: PartialFunction[Nothing, B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
stream on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the stream.
* returns
  * a new stream resulting from applying the given partial function `pf` to each
    element on which it is defined and collecting the results. The order of the
    elements is preserved.

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike

(defined at scala.collection.immutable.Stream)


### `def companion: GenericCompanion[Stream]`                                ###

The factory companion object that builds instances of class `Stream` . (or its
 `Iterable` superclass where class `Stream` is not a `Seq` .)

* Definition Classes
  * Stream → LinearSeq → LinearSeq → Seq → Iterable → Traversable → Seq → GenSeq
    → Iterable → GenIterable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.immutable.Stream)


### `def distinct: Stream[Nothing]`                                          ###

Builds a new stream from this stream in which any duplicates (as determined by
 `==` ) have been removed. Among duplicate elements, only the first one is
retained in the resulting `Stream` .

* returns
  * A new `Stream` representing the result of applying distinctness to the
    original `Stream` .

* Definition Classes
  * Stream → SeqLike → GenSeqLike

Example:

```scala
// Creates a Stream where every element is duplicated
def naturalsFrom(i: Int): Stream[Int] = i #:: { i #:: naturalsFrom(i + 1) }
naturalsFrom(1) take 6 mkString ", "
// produces: "1, 1, 2, 2, 3, 3"
(naturalsFrom(1) distinct) take 6 mkString ", "
// produces: "1, 2, 3, 4, 5, 6"
```

(defined at scala.collection.immutable.Stream)


### `final def drop(n: Int): Stream[Nothing]`                                ###

Selects all elements except first _n_ ones.

* n
  * the number of elements to drop from this stream.
* returns
  * a stream consisting of all elements of this stream except the first `n`
    ones, or else the empty stream, if this stream has less than `n` elements.

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike → TraversableLike →
    GenTraversableLike
* Annotations
  * @ tailrec ()

(defined at scala.collection.immutable.Stream)


### `def dropRight(n: Int): Stream[Nothing]`                                 ###

Selects all elements except last _n_ ones.

Note: lazily evaluated; will terminate for infinite-sized collections.

* n
  * The number of elements to take
* returns
  * a stream consisting of all elements of this stream except the last `n` ones,
    or else the empty stream, if this stream has less than `n` elements.

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike

(defined at scala.collection.immutable.Stream)


### `def dropWhile(p: (Nothing) ⇒ Boolean): Stream[Nothing]`                 ###

Returns the a `Stream` representing the longest suffix of this iterable whose
first element does not satisfy the predicate `p` .

* p
  * the test predicate.
* returns
  * A new `Stream` representing the results of applying `p` to the original
     `Stream` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike
* Note
  * This method realizes the entire `Stream` beyond the truth value of the
    predicate `p` .

Example:

```scala
// Assume we have a Stream that takes the first 20 natural numbers
def naturalsLt50(i: Int): Stream[Int] = i #:: { if (i < 20) naturalsLt50(i * + 1) else Stream.Empty }
naturalsLt50(0) dropWhile { _ < 10 }
// produces: "10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20"
```

(defined at scala.collection.immutable.Stream)


### `final def flatMap[B, That](f: (Nothing) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

Applies the given function `f` to each element of this stream, then concatenates
the results. As with `map` this function does not need to realize the entire
 `Stream` but continues to keep it as a lazy `Stream` .

* B
  * The element type of the returned collection *That* .
* That
  * the class of the returned collection. Where possible, `That` is the same
    class as the current collection class `Repr` , but this depends on the
    element type `B` being admissible for that class, which means that an
    implicit instance of type `CanBuildFrom[Repr, B, That]` is found.
* f
  * the function to apply on each element.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * `f(a0) ::: ... ::: f(an)` if this stream is `[a0, ..., an]` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike → FilterMonadic

Example:

```scala
flatMap
```

(defined at scala.collection.immutable.Stream)


### `def flatten[B](implicit asTraversable: (Nothing) ⇒ GenTraversableOnce[B]): Stream[B]` ###

Evaluates and concatenates all elements within the `Stream` into a new flattened
 `Stream` .

* B
  * The type of the elements of the resulting `Stream` .
* asTraversable
  * an implicit conversion which asserts that the element type of this stream is
    a `GenTraversable` .
* returns
  * A new `Stream` of type `B` of the flattened elements of `this`  `Stream` .

* Definition Classes
  * Stream → GenericTraversableTemplate

Example:

```scala
val sov: Stream[Vector[Int]] = Vector(0) #:: Vector(0, 0) #:: sov.zip(sov.tail).map { n => n._1 ++ n._2 }
sov.flatten take 10 mkString ", "
// produces: "0, 0, 0, 0, 0, 0, 0, 0, 0, 0"
```

(defined at scala.collection.immutable.Stream)


### `final def foldLeft[B](z: B)(op: (B, Nothing) ⇒ B): B`                   ###

Stream specialization of foldLeft which allows GC to collect along the way.

* B
  * The type of value being accumulated.
* z
  * The initial value seeded into the function `op` .
* op
  * The operation to perform on successive elements of the `Stream` .
* returns
  * The accumulated value from successive applications of `op` .

* Definition Classes
  * Stream → LinearSeqOptimized → TraversableOnce → GenTraversableOnce
* Annotations
  * @ tailrec ()

(defined at scala.collection.immutable.Stream)


### `def force: Stream[Nothing]`                                             ###

Forces evaluation of the whole stream and returns it.

* returns
  * The fully realized `Stream` .

* Definition Classes
  * Stream
* Note
  * Often we use `Stream` s to represent an infinite set or series. If that's
    the case for your particular `Stream` then this function will never return
    and will probably crash the VM with an `OutOfMemory` exception. This
    function will not hang on a finite cycle, however.

(defined at scala.collection.immutable.Stream)


### `final def foreach[U](f: (Nothing) ⇒ U): Unit`                           ###

Apply the given function `f` to each element of this linear sequence (while
respecting the order of the elements).

* U
  * the type parameter describing the result of function `f` . This result will
    always be ignored. Typically `U` is `Unit` , but this is not necessary.
* f
  * The treatment to apply to each element.

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike → GenericTraversableTemplate →
    TraversableLike → GenTraversableLike → TraversableOnce → GenTraversableOnce
    → FilterMonadic
* Annotations
  * @ tailrec ()
* Note
  * This function will force the realization of the entire stream unless the
     `f` throws an exception., Overridden here as final to trigger tail-call
    optimization, which replaces 'this' with 'tail' at each iteration. This is
    absolutely necessary for allowing the GC to collect the underlying stream as
    elements are consumed.

(defined at scala.collection.immutable.Stream)


### `def init: Stream[Nothing]`                                              ###

The stream without its last element.

* returns
  * A new `Stream` containing everything but the last element. If your `Stream`
    represents an infinite series, this method will not return.

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the stream is empty.

(defined at scala.collection.immutable.Stream)


### `def iterator: Iterator[Nothing]`                                        ###

A lazier Iterator than LinearSeqLike's.

* returns
  * the new iterator

* Definition Classes
  * Stream → LinearSeqLike → IterableLike → GenIterableLike

(defined at scala.collection.immutable.Stream)


### `final def map[B, That](f: (Nothing) ⇒ B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

Returns the stream resulting from applying the given function `f` to each
element of this stream. This returns a lazy `Stream` such that it does not need
to be fully realized.

* B
  * The element type of the returned collection *That* .
* That
  * the class of the returned collection. Where possible, `That` is the same
    class as the current collection class `Repr` , but this depends on the
    element type `B` being admissible for that class, which means that an
    implicit instance of type `CanBuildFrom[Repr, B, That]` is found.
* f
  * function to apply to each element.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * `f(a0), ..., f(an)` if this sequence is `a0, ..., an` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike → FilterMonadic

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: naturalsFrom(i + 1)
naturalsFrom(1).map(_ + 10) take 5 mkString(", ")
// produces: "11, 12, 13, 14, 15"
```

(defined at scala.collection.immutable.Stream)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this stream in a string using a separator string.

* sep
  * the separator string.
* returns
  * a string representation of this stream. In the resulting string the string
    representations (w.r.t. the method `toString` ) of all elements of this
    stream are separated by the string `sep` .

* Definition Classes
  * Stream → TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(defined at scala.collection.immutable.Stream)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this stream in a string using start, end, and separator
strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this stream. The resulting string begins with the
    string `start` and ends with the string `end` . Inside, the string
    representations (w.r.t. the method `toString` ) of all elements of this
    stream are separated by the string `sep` .

* Definition Classes
  * Stream → TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(defined at scala.collection.immutable.Stream)


### `def padTo[B >: Nothing, That](len: Int, elem: B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

Returns a new sequence of given length containing the elements of this sequence
followed by zero or more occurrences of given elements.

* B
  * The type of the value to pad with.
* That
  * The type contained within the resulting `Stream` .
* len
  * The number of elements to pad into the `Stream` .
* elem
  * The value of the type `B` to use for padding.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * A new `Stream` representing the collection with values padding off to the
    end. If your `Stream` represents an infinite series, this method will not
    return.

* Definition Classes
  * Stream → SeqLike → GenSeqLike

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: { if (i < 5) naturalsFrom(i + 1) else Stream.Empty }
naturalsFrom(1) padTo(10, 0) foreach println
// prints
// 1
// 2
// 3
// 4
// 5
// 0
// 0
// 0
// 0
// 0
```

(defined at scala.collection.immutable.Stream)


### `def partition(p: (Nothing) ⇒ Boolean): (Stream[Nothing], Stream[Nothing])` ###

Returns all the elements of this stream that satisfy the predicate `p` returning
of scala.Tuple2 of `Stream` s obeying the partition predicate `p` . The order of
the elements is preserved.

* p
  * the predicate used to filter the stream.
* returns
  * the elements of this stream satisfying `p` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: naturalsFrom(i + 1)
val parts = naturalsFrom(1) partition { _ % 2 == 0 }
parts._1 take 10 mkString ", "
// produces: "2, 4, 6, 8, 10, 12, 14, 16, 18, 20"
parts._2 take 10 mkString ", "
// produces: "1, 3, 5, 7, 9, 11, 13, 15, 17, 19"
```

(defined at scala.collection.immutable.Stream)


### `def print(sep: String): Unit`                                           ###

Prints elements of this stream one by one, separated by `sep` .

* sep
  * The separator string printed between consecutive elements.

* Definition Classes
  * Stream

(defined at scala.collection.immutable.Stream)


### `final def reduceLeft[B >: Nothing](f: (B, Nothing) ⇒ B): B`             ###

Stream specialization of reduceLeft which allows GC to collect along the way.

* B
  * The type of value being accumulated.
* f
  * The operation to perform on successive elements of the `Stream` .
* returns
  * The accumulated value from successive applications of `f` .

* Definition Classes
  * Stream → LinearSeqOptimized → TraversableOnce

(defined at scala.collection.immutable.Stream)


### `def reverse: Stream[Nothing]`                                           ###

A list consisting of all elements of this list in reverse order.

* returns
  * A new `Stream` containing the representing of the original `Stream` in
    reverse order.

* Definition Classes
  * Stream → SeqLike → GenSeqLike
* Note
  * This function must realize the entire `Stream` in order to perform this
    operation so if your `Stream` represents an infinite sequence then this
    function will never return.

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: { if (i < 5) naturalsFrom(i + 1) else Stream.Empty }
(naturalsFrom(1) reverse) foreach println
// prints
// 5
// 4
// 3
// 2
// 1
```

(defined at scala.collection.immutable.Stream)


### `final def scanLeft[B, That](z: B)(op: (B, Nothing) ⇒ B)(implicit bf: CanBuildFrom[Stream[Nothing], B, That]): That` ###

Create a new stream which contains all intermediate results of applying the
operator to subsequent elements left to right. `scanLeft` is analogous to
 `foldLeft` .

* B
  * the type of the elements in the resulting collection
* That
  * the actual type of the resulting collection
* z
  * The initial value for the scan.
* op
  * A function that will apply operations to successive values in the `Stream`
    against previous accumulated results.
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * A new collection containing the modifications from the application of `op` .

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike
* Note
  * This works because the target type of the scala.collection.mutable.Builder
     `That` is a `Stream` .

(defined at scala.collection.immutable.Stream)


### `def slice(from: Int, until: Int): Stream[Nothing]`                      ###

A substream starting at index `from` and extending up to (but not including)
index `until` . This returns a `Stream` that is lazily evaluated.

* from
  * The index of the first element of the returned subsequence
* until
  * The index of the element following the returned subsequence
* returns
  * A new string containing the elements requested from `start` until `end` .

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike → TraversableLike →
    GenTraversableLike

Example:

```scala
naturalsFrom(0) slice(50, 60) mkString ", "
// produces: "50, 51, 52, 53, 54, 55, 56, 57, 58, 59"
```

(defined at scala.collection.immutable.Stream)


### `def splitAt(n: Int): (Stream[Nothing], Stream[Nothing])`                ###

Splits this stream into two at a given position. Note: `c splitAt n` is
equivalent to (but possibly more efficient than) `(c take n, c drop n)` .

* n
  * the position at which to split.
* returns
  * a pair of streams consisting of the first `n` elements of this stream, and
    the other elements.

* Definition Classes
  * Stream → TraversableLike → GenTraversableLike

(defined at scala.collection.immutable.Stream)


### `def take(n: Int): Stream[Nothing]`                                      ###

Returns the `n` first elements of this `Stream` as another `Stream` , or else
the whole `Stream` , if it has less than `n` elements.

The result of `take` is, again, a `Stream` meaning that it also does not make
any needless evaluations of the `Stream` itself, delaying that until the usage
of the resulting `Stream` .

* n
  * the number of elements to take.
* returns
  * the `n` first elements of this stream.

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike → TraversableLike →
    GenTraversableLike

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: naturalsFrom(i + 1)
scala> naturalsFrom(5) take 5
res1: scala.collection.immutable.Stream[Int] = Stream(5, ?)
scala> naturalsFrom(5) take 5 mkString ", "
// produces: "5, 6, 7, 8, 9"
```

(defined at scala.collection.immutable.Stream)


### `def takeRight(n: Int): Stream[Nothing]`                                 ###

Returns the rightmost `n` elements from this iterable.

* n
  * the number of elements to take
* returns
  * The last `n` elements from this `Stream` .

* Definition Classes
  * Stream → IterableLike
* Note
  * Take serious caution here. If the `Stream` represents an infinite series
    then this function _will not return_ . The right most elements of an
    infinite series takes an infinite amount of time to produce.

(defined at scala.collection.immutable.Stream)


### `def takeWhile(p: (Nothing) ⇒ Boolean): Stream[Nothing]`                 ###

Returns the longest prefix of this `Stream` whose elements satisfy the predicate
 `p` .

* p
  * the test predicate.
* returns
  * A new `Stream` representing the values that satisfy the predicate `p` .

* Definition Classes
  * Stream → LinearSeqOptimized → IterableLike → TraversableLike →
    GenTraversableLike

Example:

```scala
+ naturalsFrom(0) takeWhile { _ < 5 } mkString ", "
produces: "0, 1, 2, 3, 4"
```

(defined at scala.collection.immutable.Stream)


### `def toStream: Stream[Nothing]`                                          ###

Converts this stream to a stream.

* returns
  * a stream containing all elements of this stream.

* Definition Classes
  * Stream → IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.immutable.Stream)


### `def view: StreamView[Nothing, Stream[Nothing]]`                         ###

Creates a non-strict view of this stream.

* returns
  * a non-strict view of this stream.

* Definition Classes
  * Stream → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.immutable.Stream)


### `final def withFilter(p: (Nothing) ⇒ Boolean): FilterMonadic[Nothing, Stream[Nothing]]` ###

A FilterMonadic which allows GC of the head of stream during processing

* p
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this stream which satisfy the predicate `p` .

* Definition Classes
  * Stream → TraversableLike → FilterMonadic
* Annotations
  * @ noinline ()

(defined at scala.collection.immutable.Stream)


### `def zipWithIndex[A1 >: Nothing, That](implicit bf: CanBuildFrom[Stream[Nothing], (A1, Int), That]): That` ###

Zips this iterable with its indices. `s.zipWithIndex` is equivalent to
 `s zip s.indices` .

This method is much like `zip` in that it returns a single lazy `Stream` of
scala.Tuple2.

* A1
  * The type of the first element of the scala.Tuple2 in the resulting stream.
* That
  * The type of the resulting `Stream` .
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `(A1, Int)` .
* returns
  * `Stream({a0,0}, ..., {an,n)}`

* Definition Classes
  * Stream → IterableLike → GenIterableLike

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: naturalsFrom(i + 1)
(naturalsFrom(1) zipWithIndex) take 5 foreach println
// prints
// (1,0)
// (2,1)
// (3,2)
// (4,3)
// (5,4)
```

(defined at scala.collection.immutable.Stream)


### `final def zip[A1 >: Nothing, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[Stream[Nothing], (A1, B), That]): That` ###

Returns a stream formed from this stream and the specified stream `that` by
associating each element of the former with the element at the same position in
the latter.

If one of the two streams is longer than the other, its remaining elements are
ignored.

The return type of this function may not be obvious. The lazy aspect of the
returned value is different than that of `partition` . In `partition` we get
back a scala.Tuple2 of two lazy `Stream` s whereas here we get back a single
lazy `Stream` of scala.Tuple2 s where the scala.Tuple2 's type signature is
 `(A1, B)` .

* A1
  * The type of the first parameter of the zipped tuple
* B
  * The type of the second parameter of the zipped tuple
* That
  * The type of the returned `Stream` .
* that
  * The iterable providing the second half of each result pair
* bf
  * an implicit value of class `CanBuildFrom` which determines the result class
     `That` from the current representation type `Repr` and the new element type
     `(A1, B)` .
* returns
  * `Stream({a0,b0}, ..., {amin(m,n),bmin(m,n))}` when
     `Stream(a0, ..., am) zip Stream(b0, ..., bn)` is invoked.

* Definition Classes
  * Stream → IterableLike → GenIterableLike

Example:

```scala
def naturalsFrom(i: Int): Stream[Int] = i #:: naturalsFrom(i + 1)
naturalsFrom(1) zip naturalsFrom(2) take 5 foreach println
// prints
// (1,2)
// (2,3)
// (3,4)
// (4,5)
// (5,6)
```
(defined at scala.collection.immutable.Stream)
