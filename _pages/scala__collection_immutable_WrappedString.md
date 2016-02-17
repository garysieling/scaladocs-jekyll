
#                   scala.collection.immutable.WrappedString                   #

```scala
class WrappedString extends AbstractSeq[Char] with IndexedSeq[Char] with StringLike[WrappedString]
```

This class serves as a wrapper augmenting `String` s with all the operations
found in indexed sequences.

The difference between this class and `StringOps` is that calling transformer
methods such as `filter` and `map` will yield an object of type `WrappedString`
rather than a `String` .

* Annotations
  * @ deprecatedInheritance (message =..., since = "2.11.0")
* Source
  * [WrappedString.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/WrappedString.scala#L1)
* Since
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


### `type Self = WrappedString`                                              ###

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


### `def compose[A](g: (A) ⇒ Int): (A) ⇒ Char`                               ###

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


### `def andThen[C](k: (Char) ⇒ C): PartialFunction[Int, C]`                 ###

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


### `def applyOrElse[A1 <: Int, B1 >: Char](x: A1, default: (A1) ⇒ B1): B1`  ###

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


### `def lift: (Int) ⇒ Option[Char]`                                         ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: Int, B1 >: Char](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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


### `def runWith[U](action: (Char) ⇒ U): (Int) ⇒ Boolean`                    ###

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


### `def indexOf[B >: Char](elem: B): Int`                                   ###

[use case]

Finds index of first occurrence of some value in this wrapped string.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this wrapped string that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: Char](elem: B, from: Int): Int`                        ###

[use case]

Finds index of first occurrence of some value in this wrapped string after or at
some start index.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this wrapped string that is
    equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (Char) ⇒ Boolean): Int`                               ###

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


### `def lastIndexOf[B >: Char](elem: B): Int`                               ###

[use case]

Finds index of last occurrence of some value in this wrapped string.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this wrapped string that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: Char](elem: B, end: Int): Int`                     ###

[use case]

Finds index of last occurrence of some value in this wrapped string before or at
a given end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this wrapped string that is equal
    (as determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (Char) ⇒ Boolean): Int`                           ###

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


### `def prefixLength(p: (Char) ⇒ Boolean): Int`                             ###

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
               Value Members From scala.collection.IndexedSeqLike
--------------------------------------------------------------------------------


### `def iterator: Iterator[Char]`                                           ###

Creates a new iterator over all elements contained in this iterable object.

* returns
  * the new iterator

* Definition Classes
  * IndexedSeqLike → IterableLike → GenIterableLike

(defined at scala.collection.IndexedSeqLike)


### `def toBuffer[A1 >: Char]: Buffer[A1]`                                   ###

Uses the contents of this sequence to create a new mutable buffer.

* returns
  * a buffer containing all elements of this sequence.

* Definition Classes
  * IndexedSeqLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IndexedSeqLike)


--------------------------------------------------------------------------------
            Value Members From scala.collection.IndexedSeqOptimized
--------------------------------------------------------------------------------


### `def copyToArray[B >: Char](xs: Array[B], start: Int, len: Int): Unit`   ###

[use case]

Copies the elements of this wrapped string to an array. Fills the given array
 `xs` with at most `len` elements of this wrapped string, starting at position
 `start` . Copying will stop once either the end of the current wrapped string
is reached, or the end of the target array is reached, or `len` elements have
been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def drop(n: Int): WrappedString`                                        ###

Selects all elements except first _n_ ones.

* n
  * the number of elements to drop from this sequence.
* returns
  * a sequence consisting of all elements of this sequence except the first `n`
    ones, or else the empty sequence, if this sequence has less than `n`
    elements.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def dropRight(n: Int): WrappedString`                                   ###

Selects all elements except last _n_ ones.

* n
  * The number of elements to take
* returns
  * a sequence consisting of all elements of this sequence except the last `n`
    ones, or else the empty sequence, if this sequence has less than `n`
    elements.

* Definition Classes
  * IndexedSeqOptimized → IterableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def dropWhile(p: (Char) ⇒ Boolean): WrappedString`                      ###

Drops longest prefix of elements that satisfy a predicate.

* returns
  * the longest suffix of this sequence whose first element does not satisfy the
    predicate `p` .

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def endsWith[B](that: GenSeq[B]): Boolean`                              ###

Tests whether this sequence ends with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this sequence has `that` as a suffix, `false` otherwise.

* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def exists(p: (Char) ⇒ Boolean): Boolean`                               ###

Tests whether a predicate holds for at least one element of this sequence.

* p
  * the predicate used to test elements.
* returns
  * `false` if this sequence is empty, otherwise `true` if the given predicate
     `p` holds for some of the elements of this sequence, otherwise `false`

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def find(p: (Char) ⇒ Boolean): Option[Char]`                            ###

Finds the first element of the sequence satisfying a predicate, if any.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the sequence that satisfies
     `p` , or `None` if none exists.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def foldLeft[B](z: B)(op: (B, Char) ⇒ B): B`                            ###

Applies a binary operator to a start value and all elements of this sequence,
going left to right.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this sequence,
    going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this sequence. Returns `z` if this
    sequence is empty.

* Definition Classes
  * IndexedSeqOptimized → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def foldRight[B](z: B)(op: (Char, B) ⇒ B): B`                           ###

Applies a binary operator to all elements of this sequence and a start value,
going right to left.

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
  * IndexedSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def forall(p: (Char) ⇒ Boolean): Boolean`                               ###

Tests whether a predicate holds for all elements of this sequence.

* p
  * the predicate used to test elements.
* returns
  * `true` if this sequence is empty or the given predicate `p` holds for all
    elements of this sequence, otherwise `false` .

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.IndexedSeqOptimized)


### `def foreach[U](f: (Char) ⇒ U): Unit`                                    ###

[use case]

Applies a function `f` to all elements of this wrapped string.

Note: this method underlies the implementation of most other bulk operations.
Subclasses should re-implement this method if a more efficient implementation
exists.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike →
    TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.IndexedSeqOptimized)


### `def head: Char`                                                         ###

Selects the first element of this sequence.

* returns
  * the first element of this sequence.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def indexWhere(p: (Char) ⇒ Boolean, from: Int): Int`                    ###

Finds index of the first element satisfying some predicate after or at some
start index.

* p
  * the predicate used to test elements.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def init: WrappedString`                                                ###

Selects all elements except the last.

* returns
  * a sequence consisting of all elements of this sequence except the last one.

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def last: Char`                                                         ###

Selects the last element.

* returns
  * The last element of this sequence.

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def lastIndexWhere(p: (Char) ⇒ Boolean, end: Int): Int`                 ###

Finds index of last element satisfying some predicate before or at given end
index.

* p
  * the predicate used to test elements.
* returns
  * the index `<= end` of the last element of this sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


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
  * IndexedSeqOptimized → SeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def reduceLeft[B >: Char](op: (B, Char) ⇒ B): B`                        ###

Applies a binary operator to all elements of this sequence, going left to right.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this sequence,
    going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this sequence.

* Definition Classes
  * IndexedSeqOptimized → TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def reduceRight[B >: Char](op: (Char, B) ⇒ B): B`                       ###

Applies a binary operator to all elements of this sequence, going right to left.

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
  * IndexedSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def reverse: WrappedString`                                             ###

Returns new sequence with elements in reversed order.

* returns
  * A new sequence with all elements of this sequence in reversed order.

* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def reverseIterator: Iterator[Char]`                                    ###

An iterator yielding elements in reversed order.

Note: `xs.reverseIterator` is the same as `xs.reverse.iterator` but might be
more efficient.

* returns
  * an iterator yielding the elements of this sequence in reversed order

* Definition Classes
  * IndexedSeqOptimized → SeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def sameElements[B >: Char](that: GenIterable[B]): Boolean`             ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this wrapped string.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → GenIterableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def segmentLength(p: (Char) ⇒ Boolean, from: Int): Int`                 ###

Computes length of longest segment whose elements all satisfy some predicate.

* p
  * the predicate used to test elements.
* from
  * the index where the search starts.
* returns
  * the length of the longest segment of this sequence starting from index
     `from` such that every element of the segment satisfies the predicate `p` .

* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def span(p: (Char) ⇒ Boolean): (WrappedString, WrappedString)`          ###

Splits this sequence into a prefix/suffix pair according to a predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

* returns
  * a pair consisting of the longest prefix of this sequence whose elements all
    satisfy `p` , and the rest of this sequence.

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def splitAt(n: Int): (WrappedString, WrappedString)`                    ###

Splits this sequence into two at a given position. Note: `c splitAt n` is
equivalent to (but possibly more efficient than) `(c take n, c drop n)` .

* n
  * the position at which to split.
* returns
  * a pair of sequences consisting of the first `n` elements of this sequence,
    and the other elements.

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


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
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(defined at scala.collection.IndexedSeqOptimized)


### `def tail: WrappedString`                                                ###

Selects all elements except the first.

* returns
  * a sequence consisting of all elements of this sequence except the first one.

* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the sequence is empty.

(defined at scala.collection.IndexedSeqOptimized)


### `def take(n: Int): WrappedString`                                        ###

Selects first _n_ elements.

* n
  * the number of elements to take from this sequence.
* returns
  * a sequence consisting only of the first `n` elements of this sequence, or
    else the whole sequence, if it has less than `n` elements.

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def takeRight(n: Int): WrappedString`                                   ###

Selects last _n_ elements.

* n
  * the number of elements to take
* returns
  * a sequence consisting only of the last `n` elements of this sequence, or
    else the whole sequence, if it has less than `n` elements.

* Definition Classes
  * IndexedSeqOptimized → IterableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def takeWhile(p: (Char) ⇒ Boolean): WrappedString`                      ###

Takes longest prefix of elements that satisfy a predicate.

* returns
  * the longest prefix of this sequence whose elements all satisfy the predicate
     `p` .

* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IndexedSeqOptimized)


### `def zipWithIndex[A1 >: Char, That](implicit bf: CanBuildFrom[WrappedString, (A1, Int), That]): That` ###

[use case]

Zips this wrapped string with its indices.

* returns
  * A new wrapped string containing pairs consisting of all elements of this
    wrapped string paired with their index. Indices start at `0` .

* Definition Classes
  * IndexedSeqOptimized → IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IndexedSeqOptimized)


### `def zip[A1 >: Char, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[WrappedString, (A1, B), That]): That` ###

[use case]

Returns a wrapped string formed from this wrapped string and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new wrapped string containing pairs consisting of corresponding elements
    of this wrapped string and `that` . The length of the returned collection is
    the minimum of the lengths of this wrapped string and `that` .

* Definition Classes
  * IndexedSeqOptimized → IterableLike → GenIterableLike

(defined at scala.collection.IndexedSeqOptimized)


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


### `def grouped(size: Int): Iterator[WrappedString]`                        ###

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


### `def sliding(size: Int): Iterator[WrappedString]`                        ###

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


### `def sliding(size: Int, step: Int): Iterator[WrappedString]`             ###

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


### `def toIterable: collection.Iterable[Char]`                              ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[Char]`                                         ###

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


### `def toStream: Stream[Char]`                                             ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def zipAll[B, A1 >: Char, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[WrappedString, (A1, B), That]): That` ###

[use case]

Returns a wrapped string formed from this wrapped string and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is shorter than the other, placeholder elements are used to extend
the shorter collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this wrapped string is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    wrapped string.
* returns
  * a new wrapped string containing pairs consisting of corresponding elements
    of this wrapped string and `that` . The length of the returned collection is
    the maximum of the lengths of this wrapped string and `that` . If this
    wrapped string is shorter than `that` , `thisElem` values are used to pad
    the result. If `that` is shorter than this wrapped string, `thatElem` values
    are used to pad the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
               Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParSeq[Char]`                                                  ###

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


### `def +:[B >: Char, That](elem: B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

A copy of the wrapped string with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original wrapped string is not modified, so you will want to capture
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
  * a new wrapped string consisting of `elem` followed by all elements of this
    wrapped string.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def :+[B >: Char, That](elem: B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

A copy of this wrapped string with an element appended.

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
  * a new wrapped string consisting of all elements of this wrapped string
    followed by `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def combinations(n: Int): Iterator[WrappedString]`                      ###

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


### `def contains[A1 >: Char](elem: A1): Boolean`                            ###

Tests whether this sequence contains a given value as an element.

Note: may not terminate for infinite-sized collections.

* elem
  * the element to test.
* returns
  * `true` if this sequence has an element that is equal (as determined by `==` )
    to `elem` , `false` otherwise.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def corresponds[B](that: GenSeq[B])(p: (Char, B) ⇒ Boolean): Boolean`   ###

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


### `def diff[B >: Char](that: GenSeq[B]): WrappedString`                    ###

[use case]

Computes the multiset difference between this wrapped string and another
sequence.

* that
  * the sequence of elements to remove
* returns
  * a new wrapped string which contains all elements of this wrapped string
    except some of occurrences of elements that also appear in `that` . If an
    element value `x` appears _n_ times in `that` , then the first _n_
    occurrences of `x` will not form part of the result, but any following
    occurrences will.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def distinct: WrappedString`                                            ###

Builds a new sequence from this sequence without any duplicate elements.

Note: will not terminate for infinite-sized collections.

* returns
  * A new sequence which contains the first occurrence of every element of this
    sequence.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def indexOfSlice[B >: Char](that: GenSeq[B]): Int`                      ###

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


### `def indexOfSlice[B >: Char](that: GenSeq[B], from: Int): Int`           ###

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


### `def intersect[B >: Char](that: GenSeq[B]): WrappedString`               ###

[use case]

Computes the multiset intersection between this wrapped string and another
sequence.

* that
  * the sequence of elements to intersect with.
* returns
  * a new wrapped string which contains all elements of this wrapped string
    which also appear in `that` . If an element value `x` appears _n_ times in
     `that` , then the first _n_ occurrences of `x` will be retained in the
    result, but any following occurrences will be omitted.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexOfSlice[B >: Char](that: GenSeq[B]): Int`                  ###

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


### `def lastIndexOfSlice[B >: Char](that: GenSeq[B], end: Int): Int`        ###

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


### `def padTo[B >: Char, That](len: Int, elem: B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

A copy of this wrapped string with an element value appended until a given
target length is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new wrapped string consisting of all elements of this wrapped string
    followed by the minimal number of occurrences of `elem` so that the
    resulting wrapped string has a length of at least `len` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def patch[B >: Char, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Produces a new wrapped string where a slice of elements in this wrapped string
is replaced by another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original wrapped string
* returns
  * a new wrapped string consisting of all elements of this wrapped string
    except that `replaced` elements starting from `from` are replaced by
     `patch` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def permutations: Iterator[WrappedString]`                              ###

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


### `def reverseMap[B, That](f: (Char) ⇒ B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this wrapped
string and collecting the results in reversed order.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new wrapped string resulting from applying the given function `f` to each
    element of this wrapped string and collecting the results in reversed order.

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def sortBy[B](f: (Char) ⇒ B)(implicit ord: math.Ordering[B]): WrappedString` ###

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


### `def sortWith(lt: (Char, Char) ⇒ Boolean): WrappedString`                ###

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


### `def sorted[B >: Char](implicit ord: math.Ordering[B]): WrappedString`   ###

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


### `def union[B >: Char, That](that: GenSeq[B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this wrapped string and
also all elements of a given sequence. `xs union ys` is equivalent to
 `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

* that
  * the sequence to add.
* returns
  * a new wrapped string which contains all elements of this wrapped string
    followed by all elements of `that` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def updated[B >: Char, That](index: Int, elem: B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

A copy of this wrapped string with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this wrapped string with the element at position `index` replaced
    by `elem` .

* Definition Classes
  * SeqLike → GenSeqLike

(defined at scala.collection.SeqLike)


### `def view(from: Int, until: Int): SeqView[Char, WrappedString]`          ###

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


### `def view: SeqView[Char, WrappedString]`                                 ###

Creates a non-strict view of this sequence.

* returns
  * a non-strict view of this sequence.

* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


--------------------------------------------------------------------------------
              Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: Char, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

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


### `def ++:[B >: Char, That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

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
  * a new wrapped string which contains all elements of this wrapped string
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++[B >: Char, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Returns a new wrapped string containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
wrapped string is the most specific superclass encompassing the element types of
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
  * a new wrapped string which contains all elements of this wrapped string
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def collect[B, That](pf: PartialFunction[Char, B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
wrapped string on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the wrapped string.
* returns
  * a new wrapped string resulting from applying the given partial function
     `pf` to each element on which it is defined and collecting the results. The
    order of the elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: (Char) ⇒ Boolean): WrappedString`                         ###

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


### `def filterNot(p: (Char) ⇒ Boolean): WrappedString`                      ###

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


### `def flatMap[B, That](f: (Char) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this wrapped
string and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of wrapped
string. This might cause unexpected results sometimes. For example:

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
  * a new wrapped string resulting from applying the given collection-valued
    function `f` to each element of this wrapped string and concatenating the
    results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def groupBy[K](f: (Char) ⇒ K): Map[K, WrappedString]`                   ###

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


### `def headOption: Option[Char]`                                           ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def inits: Iterator[WrappedString]`                                     ###

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


### `def lastOption: Option[Char]`                                           ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this traversable collection$ if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def map[B, That](f: (Char) ⇒ B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this wrapped
string.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new wrapped string resulting from applying the given function `f` to each
    element of this wrapped string and collecting the results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def partition(p: (Char) ⇒ Boolean): (WrappedString, WrappedString)`     ###

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


### `def repr: WrappedString`                                                ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanLeft[B, That](z: B)(op: (B, Char) ⇒ B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: (Char, B) ⇒ B)(implicit bf: CanBuildFrom[WrappedString, B, That]): That` ###

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


### `def scan[B >: Char, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[WrappedString, B, That]): That` ###

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


### `def tails: Iterator[WrappedString]`                                     ###

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


### `def toTraversable: collection.Traversable[Char]`                        ###

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


### `def withFilter(p: (Char) ⇒ Boolean): FilterMonadic[Char, WrappedString]` ###

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
              Value Members From scala.collection.TraversableOnce
--------------------------------------------------------------------------------


### `def /:[B](z: B)(op: (B, Char) ⇒ B): B`                                  ###

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


### `def :\[B](z: B)(op: (Char, B) ⇒ B): B`                                  ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, Char) ⇒ B, combop: (B, B) ⇒ B): B`  ###

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


### `def collectFirst[B](pf: PartialFunction[Char, B]): Option[B]`           ###

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


### `def copyToArray[B >: Char](xs: Array[B]): Unit`                         ###

[use case]

Copies the elements of this wrapped string to an array. Fills the given array
 `xs` with values of this wrapped string. Copying will stop once either the end
of the current wrapped string is reached, or the end of the target array is
reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: Char](xs: Array[B], start: Int): Unit`             ###

[use case]

Copies the elements of this wrapped string to an array. Fills the given array
 `xs` with values of this wrapped string, beginning at index `start` . Copying
will stop once either the end of the current wrapped string is reached, or the
end of the target array is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: Char](dest: Buffer[B]): Unit`                     ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: (Char) ⇒ Boolean): Int`                                    ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def fold[A1 >: Char](z: A1)(op: (A1, A1) ⇒ A1): A1`                     ###

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


### `def maxBy[B](f: (Char) ⇒ B)(implicit cmp: Ordering[B]): Char`           ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this wrapped string with the largest value measured by
    function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: (Char) ⇒ B)(implicit cmp: Ordering[B]): Char`           ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this wrapped string with the smallest value measured by
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


### `def reduceLeftOption[B >: Char](op: (B, Char) ⇒ B): Option[B]`          ###

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


### `def reduceOption[A1 >: Char](op: (A1, A1) ⇒ A1): Option[A1]`            ###

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


### `def reduceRightOption[B >: Char](op: (Char, B) ⇒ B): Option[B]`         ###

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


### `def reduce[A1 >: Char](op: (A1, A1) ⇒ A1): A1`                          ###

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


### `def reversed: scala.List[Char]`                                         ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: scala.List[Char]`                                           ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[Char, (T, U)]): Map[T, U]`             ###

[use case]

Converts this wrapped string to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this wrapped string.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: Char]: Set[B]`                                           ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: scala.Vector[Char]`                                       ###

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


### `def flatten[B](implicit asTraversable: (Char) ⇒ GenTraversableOnce[B]): IndexedSeq[B]` ###

[use case]

Converts this wrapped string of traversable collections into a wrapped string
formed by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of wrapped
string. For example:

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
  * a new wrapped string resulting from concatenating all element wrapped
    strings.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, IndexedSeq[B]]`                       ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (Char) ⇒ GenTraversableOnce[B]): IndexedSeq[IndexedSeq[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (Char) ⇒ (A1, A2, A3)): (IndexedSeq[A1], IndexedSeq[A2], IndexedSeq[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (Char) ⇒ (A1, A2)): (IndexedSeq[A1], IndexedSeq[A2])` ###

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
            Value Members From scala.collection.immutable.IndexedSeq
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[IndexedSeq]`                            ###

The factory companion object that builds instances of class IndexedSeq. (or its
 `Iterable` superclass where class IndexedSeq is not a `Seq` .)

* Definition Classes
  * IndexedSeq → IndexedSeq → Seq → Seq → GenSeq → Iterable → Iterable →
    GenIterable → Traversable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.immutable.IndexedSeq)


### `def seq: IndexedSeq[Char]`                                              ###

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


### `def toIndexedSeq: IndexedSeq[Char]`                                     ###

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
               Value Members From scala.collection.immutable.Seq
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[Char, ParSeq[Char]]`                          ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * Seq → SeqLike → Iterable → TraversableLike → Parallelizable

(defined at scala.collection.immutable.Seq)


### `def toSeq: Seq[Char]`                                                   ###

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
            Value Members From scala.collection.immutable.StringLike
--------------------------------------------------------------------------------


### `def *(n: Int): String`                                                  ###

Return the current string concatenated `n` times.

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def apply(n: Int): Char`                                                ###

Return element at index `n`

* returns
  * the element of this string at index `idx` , where `0` indicates the first
    element.

* Definition Classes
  * StringLike → SeqLike → GenSeqLike
* Exceptions thrown
  * IndexOutOfBoundsException if the index is not valid

(defined at scala.collection.immutable.StringLike)


### `def compare(other: String): Int`                                        ###

Result of comparing `this` with operand `that` .

Implement this method to determine how instances of A will be sorted.

Returns `x` where:

*  `x < 0` when `this < that`
*  `x == 0` when `this == that`
*  `x > 0` when `this > that`

* Definition Classes
  * StringLike → Ordered

(defined at scala.collection.immutable.StringLike)


### `def format(args: Any*): String`                                         ###

Uses the underlying string as a pattern (in a fashion similar to printf in C),
and uses the supplied arguments to fill in the holes.

The interpretation of the formatting patterns is described in
`java.util.Formatter`, with the addition that classes deriving from
 `ScalaNumber` (such as scala.BigInt and scala.BigDecimal) are unwrapped to pass
a type which `Formatter` understands.

* args
  * the arguments used to instantiating the pattern.

* Definition Classes
  * StringLike
* Exceptions thrown
  *

(defined at scala.collection.immutable.StringLike)


### `def formatLocal(l: Locale, args: Any*): String`                         ###

Like `format(args*)` but takes an initial `Locale` parameter which influences
formatting as in `java.lang.String` 's format.

The interpretation of the formatting patterns is described in
`java.util.Formatter`, with the addition that classes deriving from
 `ScalaNumber` (such as `scala.BigInt` and `scala.BigDecimal` ) are unwrapped to
pass a type which `Formatter` understands.

* l
  * an instance of `java.util.Locale`
* args
  * the arguments used to instantiating the pattern.

* Definition Classes
  * StringLike
* Exceptions thrown
  *

(defined at scala.collection.immutable.StringLike)


### `def r(groupNames: String*): Regex`                                      ###

You can follow a string with `.r(g1, ... , gn)` , turning it into a `Regex` ,
with group names g1 through gn.

 `"""(\d\d)-(\d\d)-(\d\d\d\d)""".r("month", "day", "year")` matches dates and
provides its subcomponents through groups named "month", "day" and "year".

* groupNames
  * The names of the groups in the pattern, in the order they appear.

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def r: Regex`                                                           ###

You can follow a string with `.r` , turning it into a `Regex` . E.g.

 `"""A\w*""".r` is the regular expression for identifiers starting with `A` .

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def replaceAllLiterally(literal: String, replacement: String): String`  ###

Replace all literal occurrences of `literal` with the string `replacement` .
This is equivalent to java.lang.String#replaceAll except that both arguments are
appropriately quoted to avoid being interpreted as metacharacters.

* literal
  * the string which should be replaced everywhere it occurs
* replacement
  * the replacement string
* returns
  * the resulting string

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def split(separators: Array[Char]): Array[String]`                      ###

* Definition Classes
  * StringLike
* Annotations
  * @ throws (clazz =...)

(defined at scala.collection.immutable.StringLike)


### `def split(separator: Char): Array[String]`                              ###

Split this string around the separator character

If this string is the empty string, returns an array of strings that contains a
single empty string.

If this string is not the empty string, returns an array containing the
substrings terminated by the start of the string, the end of the string or the
separator character, excluding empty trailing substrings

If the separator character is a surrogate character, only split on matching
surrogate characters if they are not part of a surrogate pair

The behaviour follows, and is implemented in terms of
[String.split(re: String)](http://docs.oracle.com/javase/7/docs/api/java/lang/String.html#split%28java.lang.String%29)

* separator
  * the character used as a delimiter

* Definition Classes
  * StringLike

Example:

```scala
"a.b".split('.') //returns Array("a", "b")
//splitting the empty string always returns the array with a single
//empty string
"".split('.') //returns Array("")
//only trailing empty substrings are removed
"a.".split('.') //returns Array("a")
".a.".split('.') //returns Array("", "a")
"..a..".split('.') //returns Array("", "", "a")
//all parts are empty and trailing
".".split('.') //returns Array()
"..".split('.') //returns Array()
//surrogate pairs
val high = 0xD852.toChar
val low = 0xDF62.toChar
val highstring = high.toString
val lowstring = low.toString
//well-formed surrogate pairs are not split
val highlow = highstring + lowstring
highlow.split(high) //returns Array(highlow)
//bare surrogate characters are split
val bare = "_" + highstring + "_"
bare.split(high) //returns Array("_", "_")
```

(defined at scala.collection.immutable.StringLike)


### `def stripMargin(marginChar: Char): String`                              ###

For every line in this string:

Strip a leading prefix consisting of blanks or control characters followed by
 `marginChar` from the line.

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def stripPrefix(prefix: String): String`                                ###

Returns this string with the given `prefix` stripped. If this string does not
start with `prefix` , it is returned unchanged.

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


### `def stripSuffix(suffix: String): String`                                ###

Returns this string with the given `suffix` stripped. If this string does not
end with `suffix` , it is returned unchanged.

* Definition Classes
  * StringLike

(defined at scala.collection.immutable.StringLike)


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.immutable.WrappedString
--------------------------------------------------------------------------------


### `new WrappedString(self: String)`                                        ###

* self
  * a string contained within this wrapped string

(defined at scala.collection.immutable.WrappedString)


--------------------------------------------------------------------------------
          Value Members From scala.collection.immutable.WrappedString
--------------------------------------------------------------------------------


### `def newBuilder: Builder[Char, WrappedString]`                           ###

Creates a string builder buffer as builder for this class

* Attributes
  * protected[this]
* Definition Classes
  * WrappedString → StringLike → GenericTraversableTemplate → TraversableLike →
    HasNewBuilder

(defined at scala.collection.immutable.WrappedString)


### `def slice(from: Int, until: Int): WrappedString`                        ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

* returns
  * a wrapped string containing the elements greater than or equal to index
     `from` extending up to (but not including) index `until` of this wrapped
    string.

* Definition Classes
  * WrappedString → StringLike → IndexedSeqOptimized → IterableLike →
    TraversableLike → GenTraversableLike

(defined at scala.collection.immutable.WrappedString)


### `def thisCollection: WrappedString`                                      ###

The underlying collection seen as an instance of `WrappedString` . By default
this is implemented as the current collection object itself, but this can be
overridden.

* Attributes
  * protected[this]
* Definition Classes
  * WrappedString → IndexedSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.immutable.WrappedString)


### `def toCollection(repr: WrappedString): WrappedString`                   ###

A conversion from collections of type `Repr` to `WrappedString` objects. By
default this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * WrappedString → IndexedSeqLike → SeqLike → IterableLike → TraversableLike

(defined at scala.collection.immutable.WrappedString)


--------------------------------------------------------------------------------
                     Value Members From scala.math.Ordered
--------------------------------------------------------------------------------


### `def <(that: String): Boolean`                                           ###

Returns true if `this` is less than `that`

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def <=(that: String): Boolean`                                          ###

Returns true if `this` is less than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >(that: String): Boolean`                                           ###

Returns true if `this` is greater than `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def >=(that: String): Boolean`                                          ###

Returns true if `this` is greater than or equal to `that` .

* Definition Classes
  * Ordered

(defined at scala.math.Ordered)


### `def compareTo(that: String): Int`                                       ###

Result of comparing `this` with operand `that` .

* Definition Classes
  * Ordered → Comparable

(defined at scala.math.Ordered)


--------------------------------------------------------------------------------
 Deprecated Value Members From Implicit scala.LowPriorityImplicits.unwrapString
--------------------------------------------------------------------------------


### `def getBytes(arg0: Int, arg1: Int, arg2: Array[Byte], arg3: Int): Unit` ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String
* Annotations
  * @Deprecated @ deprecated
* Deprecated
  * _(Since version)_ see corresponding Javadoc for more information.

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


--------------------------------------------------------------------------------
      Value Members From Implicit scala.LowPriorityImplicits.unwrapString
--------------------------------------------------------------------------------


### `def codePointAt(arg0: Int): Int`                                        ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def codePointBefore(arg0: Int): Int`                                    ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def codePointCount(arg0: Int, arg1: Int): Int`                          ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def compareToIgnoreCase(arg0: String): Int`                             ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def concat(arg0: String): String`                                       ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def contentEquals(arg0: CharSequence): Boolean`                         ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def contentEquals(arg0: StringBuffer): Boolean`                         ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def equalsIgnoreCase(arg0: String): Boolean`                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def getBytes(arg0: Charset): Array[Byte]`                               ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def getBytes(arg0: String): Array[Byte]`                                ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String
* Annotations
  * @ throws (...)

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def getChars(arg0: Int, arg1: Int, arg2: Array[Char], arg3: Int): Unit` ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def matches(arg0: String): Boolean`                                     ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def offsetByCodePoints(arg0: Int, arg1: Int): Int`                      ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def regionMatches(arg0: Boolean, arg1: Int, arg2: String, arg3: Int, arg4: Int): Boolean` ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def regionMatches(arg0: Int, arg1: String, arg2: Int, arg3: Int): Boolean` ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def replace(arg0: Char, arg1: Char): String`                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def replace(arg0: CharSequence, arg1: CharSequence): String`            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def replaceAll(arg0: String, arg1: String): String`                     ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def replaceFirst(arg0: String, arg1: String): String`                   ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def substring(arg0: Int): String`                                       ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def substring(arg0: Int, arg1: Int): String`                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def toLowerCase(arg0: Locale): String`                                  ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


### `def toUpperCase(arg0: Locale): String`                                  ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to String
    performed by method unwrapString in scala.LowPriorityImplicits.
* Definition Classes
  * String

(added by implicit convertion: scala.LowPriorityImplicits.unwrapString)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from WrappedString to
    CollectionsHaveToParArray [WrappedString, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (WrappedString) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
