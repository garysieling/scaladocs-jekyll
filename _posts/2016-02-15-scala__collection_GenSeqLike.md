
#                         scala.collection.GenSeqLike                         #

```scala
trait GenSeqLike[+A, +Repr] extends GenIterableLike[A, Repr] with Equals with Parallelizable[A, ParSeq[A]]
```

A template trait for all sequences which may be traversed in parallel.

* Source
  * [GenSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSeqLike.scala#L1)


--------------------------------------------------------------------------------
                    Abstract Value Members From scala.Equals
--------------------------------------------------------------------------------


### `abstract def canEqual(that: Any): Boolean`                              ###

A method that should be called from every well-designed equals method that is
open to be overridden in a subclass. See
[Programming in Scala, Chapter 28](http://www.artima.com/pins1ed/object-equality.html)
for discussion and design.

* that
  * the value being probed for possible equality
* returns
  * true if this instance can possibly equal `that` , otherwise false

* Definition Classes
  * Equals

(defined at scala.Equals)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.GenIterableLike
--------------------------------------------------------------------------------


### `abstract def sameElements[A1 >: A](that: GenIterable[A1]): Boolean`     ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this general sequence.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


### `abstract def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[Repr, (A1, B), That]): That` ###

[use case]

Returns a general sequence formed from this general sequence and another
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
  * the element to be used to fill up the result if this general sequence is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    general sequence.
* returns
  * a new general sequence containing pairs consisting of corresponding elements
    of this general sequence and `that` . The length of the returned collection
    is the maximum of the lengths of this general sequence and `that` . If this
    general sequence is shorter than `that` , `thisElem` values are used to pad
    the result. If `that` is shorter than this general sequence, `thatElem`
    values are used to pad the result.

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


### `abstract def zipWithIndex[A1 >: A, That](implicit bf: CanBuildFrom[Repr, (A1, Int), That]): That` ###

[use case]

Zips this general sequence with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new general sequence containing pairs consisting of all elements of this
    general sequence paired with their index. Indices start at `0` .

* Definition Classes
  * GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.GenIterableLike)


### `abstract def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[Repr, (A1, B), That]): That` ###

[use case]

Returns a general sequence formed from this general sequence and another
iterable collection by combining corresponding elements in pairs. If one of the
two collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new general sequence containing pairs consisting of corresponding elements
    of this general sequence and `that` . The length of the returned collection
    is the minimum of the lengths of this general sequence and `that` .

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


--------------------------------------------------------------------------------
            Abstract Value Members From scala.collection.GenSeqLike
--------------------------------------------------------------------------------


### `abstract def apply(idx: Int): A`                                        ###

Selects an element by its index in the general sequence.

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
  * the element of this general sequence at index `idx` , where `0` indicates
    the first element.

* Exceptions thrown
  * IndexOutOfBoundsException if `idx` does not satisfy `0 <= idx < length` .

(defined at scala.collection.GenSeqLike)


### `abstract def corresponds[B](that: GenSeq[B])(p: (A, B) ⇒ Boolean): Boolean` ###

Tests whether every element of this general sequence relates to the
corresponding element of another sequence by satisfying a test predicate.

* B
  * the type of the elements of `that`
* that
  * the other sequence
* p
  * the test predicate, which relates elements from both sequences
* returns
  * `true` if both sequences have the same length and `p(x, y)` is `true` for
    all corresponding elements `x` of this general sequence and `y` of `that` ,
    otherwise `false` .

(defined at scala.collection.GenSeqLike)


### `abstract def endsWith[B](that: GenSeq[B]): Boolean`                     ###

Tests whether this general sequence ends with the given sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to test
* returns
  * `true` if this general sequence has `that` as a suffix, `false` otherwise.

(defined at scala.collection.GenSeqLike)


### `abstract def indexWhere(p: (A) ⇒ Boolean, from: Int): Int`              ###

Finds index of the first element satisfying some predicate after or at some
start index.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this general sequence that
    satisfies the predicate `p` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `abstract def lastIndexWhere(p: (A) ⇒ Boolean, end: Int): Int`           ###

Finds index of last element satisfying some predicate before or at given end
index.

* p
  * the predicate used to test elements.
* returns
  * the index `<= end` of the last element of this general sequence that
    satisfies the predicate `p` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `abstract def segmentLength(p: (A) ⇒ Boolean, from: Int): Int`           ###

Computes length of longest segment whose elements all satisfy some predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* from
  * the index where the search starts.
* returns
  * the length of the longest segment of this general sequence starting from
    index `from` such that every element of the segment satisfies the predicate
     `p` .

(defined at scala.collection.GenSeqLike)


### `abstract def startsWith[B](that: GenSeq[B], offset: Int): Boolean`      ###

Tests whether this general sequence contains the given sequence at a given
index.

 *Note* : If the both the receiver object `this` and the argument `that` are
infinite sequences this method may not terminate.

* that
  * the sequence to test
* offset
  * the index where the sequence is searched.
* returns
  * `true` if the sequence `that` is contained in this general sequence at index
     `offset` , otherwise `false` .

(defined at scala.collection.GenSeqLike)


### `abstract def toSeq: GenSeq[A]`                                          ###

Converts this general sequence to a sequence. As with `toIterable` , it's lazy
in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this general sequence.

* Definition Classes
  * GenSeqLike → GenTraversableOnce

(defined at scala.collection.GenSeqLike)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.GenSeqLike
--------------------------------------------------------------------------------


### `abstract def distinct: Repr`                                            ###

Builds a new general sequence from this general sequence without any duplicate
elements.

Note: will not terminate for infinite-sized collections.

* returns
  * A new general sequence which contains the first occurrence of every element
    of this general sequence.

(defined at scala.collection.GenSeqLike)


### `abstract def +:[B >: A, That](elem: B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

A copy of the general sequence with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original general sequence is not modified, so you will want to capture
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
  * a new general sequence consisting of `elem` followed by all elements of this
    general sequence.

(defined at scala.collection.GenSeqLike)


### `abstract def :+[B >: A, That](elem: B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

A copy of this general sequence with an element appended.

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
  * a new general sequence consisting of all elements of this general sequence
    followed by `elem` .

(defined at scala.collection.GenSeqLike)


### `abstract def diff[B >: A](that: GenSeq[B]): Repr`                       ###

[use case]

Computes the multiset difference between this general sequence and another
sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence of elements to remove
* returns
  * a new general sequence which contains all elements of this general sequence
    except some of occurrences of elements that also appear in `that` . If an
    element value `x` appears _n_ times in `that` , then the first _n_
    occurrences of `x` will not form part of the result, but any following
    occurrences will.

(defined at scala.collection.GenSeqLike)


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


### `def indexOf[B >: A](elem: B): Int`                                      ###

[use case]

Finds index of first occurrence of some value in this general sequence.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this general sequence that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: A](elem: B, from: Int): Int`                           ###

[use case]

Finds index of first occurrence of some value in this general sequence after or
at some start index.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this general sequence that is
    equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (A) ⇒ Boolean): Int`                                  ###

Finds index of first element satisfying some predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the first element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `abstract def intersect[B >: A](that: GenSeq[B]): Repr`                  ###

[use case]

Computes the multiset intersection between this general sequence and another
sequence.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence of elements to intersect with.
* returns
  * a new general sequence which contains all elements of this general sequence
    which also appear in `that` . If an element value `x` appears _n_ times in
     `that` , then the first _n_ occurrences of `x` will be retained in the
    result, but any following occurrences will be omitted.

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

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: A](elem: B): Int`                                  ###

[use case]

Finds index of last occurrence of some value in this general sequence.

Note: will not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this general sequence that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: A](elem: B, end: Int): Int`                        ###

[use case]

Finds index of last occurrence of some value in this general sequence before or
at a given end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this general sequence that is
    equal (as determined by `==` ) to `elem` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (A) ⇒ Boolean): Int`                              ###

Finds index of last element satisfying some predicate.

Note: will not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the index of the last element of this general sequence that satisfies the
    predicate `p` , or `-1` , if none exists.

(defined at scala.collection.GenSeqLike)


### `abstract def padTo[B >: A, That](len: Int, elem: B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

A copy of this general sequence with an element value appended until a given
target length is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new general sequence consisting of all elements of this general sequence
    followed by the minimal number of occurrences of `elem` so that the
    resulting general sequence has a length of at least `len` .

(defined at scala.collection.GenSeqLike)


### `abstract def patch[B >: A, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Produces a new general sequence where a slice of elements in this general
sequence is replaced by another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original general sequence
* returns
  * a new general sequence consisting of all elements of this general sequence
    except that `replaced` elements starting from `from` are replaced by
     `patch` .

(defined at scala.collection.GenSeqLike)


### `def prefixLength(p: (A) ⇒ Boolean): Int`                                ###

Returns the length of the longest prefix whose elements all satisfy some
predicate.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * the length of the longest prefix of this general sequence such that every
    element of the segment satisfies the predicate `p` .

(defined at scala.collection.GenSeqLike)


### `abstract def reverseMap[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this general
sequence and collecting the results in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new general sequence resulting from applying the given function `f` to
    each element of this general sequence and collecting the results in reversed
    order.

(defined at scala.collection.GenSeqLike)


### `def startsWith[B](that: GenSeq[B]): Boolean`                            ###

Tests whether this general sequence starts with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this collection has `that` as a prefix, `false` otherwise.

(defined at scala.collection.GenSeqLike)


### `def union[B >: A, That](that: GenSeq[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this general sequence and
also all elements of a given sequence. `xs union ys` is equivalent to
 `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to add.
* returns
  * a new general sequence which contains all elements of this general sequence
    followed by all elements of `that` .

(defined at scala.collection.GenSeqLike)


### `abstract def updated[B >: A, That](index: Int, elem: B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

A copy of this general sequence with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this general sequence with the element at position `index`
    replaced by `elem` .

(defined at scala.collection.GenSeqLike)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.GenTraversableLike
--------------------------------------------------------------------------------


### `abstract def drop(n: Int): Repr`                                        ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this general collection.
* returns
  * a general collection consisting of all elements of this general collection
    except the first `n` ones, or else the empty general collection, if this
    general collection has less than `n` elements.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def dropWhile(pred: (A) ⇒ Boolean): Repr`                      ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pred
  * The predicate used to test elements.
* returns
  * the longest suffix of this general collection whose first element does not
    satisfy the predicate `p` .

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def filter(pred: (A) ⇒ Boolean): Repr`                         ###

Selects all elements of this general collection which satisfy a predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new general collection consisting of all elements of this general
    collection that satisfy the given predicate `p` . Their order may not be
    preserved.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def filterNot(pred: (A) ⇒ Boolean): Repr`                      ###

Selects all elements of this general collection which do not satisfy a
predicate.

* pred
  * the predicate used to test elements.
* returns
  * a new general collection consisting of all elements of this general
    collection that do not satisfy the given predicate `p` . Their order may not
    be preserved.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def groupBy[K](f: (A) ⇒ K): GenMap[K, Repr]`                   ###

Partitions this general collection into a map of general collections according
to some discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new general collection.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to general collections such that the following invariant
    holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a general collection of those elements
     `x` for which `f(x)` equals `k` .

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def partition(pred: (A) ⇒ Boolean): (Repr, Repr)`              ###

Partitions this general collection in two general collections according to a
predicate.

* pred
  * the predicate on which to partition.
* returns
  * a pair of general collections: the first general collection consists of all
    elements that satisfy the predicate `p` and the second general collection
    consists of all elements that don't. The relative order of the elements in
    the resulting general collections may not be preserved.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def scanLeft[B, That](z: B)(op: (B, A) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

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
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def scanRight[B, That](z: B)(op: (A, B) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

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
  * GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(defined at scala.collection.GenTraversableLike)


### `abstract def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[Repr, B, That]): That` ###

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
  * a new general collection containing the prefix scan of the elements in this
    general collection

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def slice(unc_from: Int, unc_until: Int): Repr`                ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* unc_from
  * the lowest index to include from this general collection.
* unc_until
  * the lowest index to EXCLUDE from this general collection.
* returns
  * a general collection containing the elements greater than or equal to index
     `from` extending up to (but not including) index `until` of this general
    collection.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def span(pred: (A) ⇒ Boolean): (Repr, Repr)`                   ###

Splits this general collection into a prefix/suffix pair according to a
predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pred
  * the test predicate
* returns
  * a pair consisting of the longest prefix of this general collection whose
    elements all satisfy `p` , and the rest of this general collection.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def splitAt(n: Int): (Repr, Repr)`                             ###

Splits this general collection into two at a given position. Note:
 `c splitAt n` is equivalent to (but possibly more efficient than)
 `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of general collections consisting of the first `n` elements of this
    general collection, and the other elements.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def take(n: Int): Repr`                                        ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this general collection.
* returns
  * a general collection consisting only of the first `n` elements of this
    general collection, or else the whole general collection, if it has less
    than `n` elements.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def takeWhile(pred: (A) ⇒ Boolean): Repr`                      ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pred
  * The predicate used to test elements.
* returns
  * the longest prefix of this general collection whose elements all satisfy the
    predicate `p` .

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.GenTraversableLike
--------------------------------------------------------------------------------


### `abstract def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Returns a new general sequence containing the elements from the left hand
operand followed by the elements from the right hand operand. The element type
of the general sequence is the most specific superclass encompassing the element
types of the two operands.

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
  * a new general sequence which contains all elements of this general sequence
    followed by all elements of `that` .

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def collect[B, That](pf: PartialFunction[A, B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
general sequence on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the general sequence.
* returns
  * a new general sequence resulting from applying the given partial function
     `pf` to each element on which it is defined and collecting the results. The
    order of the elements is preserved.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this general
sequence and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of general
sequence. This might cause unexpected results sometimes. For example:

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
  * a new general sequence resulting from applying the given collection-valued
    function `f` to each element of this general sequence and concatenating the
    results.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def foreach[U](f: (A) ⇒ U): Unit`                              ###

[use case]

Applies a function `f` to all elements of this general sequence.

Note: this method underlies the implementation of most other bulk operations.
It's important to implement this method in an efficient way.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * GenTraversableLike → GenTraversableOnce

(defined at scala.collection.GenTraversableLike)


### `abstract def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this general
sequence.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new general sequence resulting from applying the given function `f` to
    each element of this general sequence and collecting the results.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def count(p: (A) ⇒ Boolean): Int`                              ###

Counts the number of elements in the collection or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def forall(p: (A) ⇒ Boolean): Boolean`                         ###

Tests whether a predicate holds for all elements of this collection or iterator.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this collection or iterator is empty or the given predicate `p`
    holds for all elements of this collection or iterator, otherwise `false` .

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce

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

* Definition Classes
  * GenTraversableOnce
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

* Definition Classes
  * GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this collection or iterator is empty.

(defined at scala.collection.GenTraversableOnce)


### `abstract def toBuffer[A1 >: A]: Buffer[A1]`                             ###

Uses the contents of this collection or iterator to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIndexedSeq: immutable.IndexedSeq[A]`                     ###

Converts this collection or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIterable: GenIterable[A]`                                ###

Converts this collection or iterator to an iterable collection. Note that the
choice of target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toSet[A1 >: A]: GenSet[A1]`                                ###

Converts this collection or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toTraversable: GenTraversable[A]`                          ###

Converts this collection or iterator to an unspecified Traversable. Will return
the same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.GenTraversableOnce
--------------------------------------------------------------------------------


### `abstract def copyToArray[B >: A](xs: Array[B]): Unit`                   ###

[use case]

Copies the elements of this general sequence to an array. Fills the given array
 `xs` with values of this general sequence. Copying will stop once either the
end of the current general sequence is reached, or the end of the target array
is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int): Unit`       ###

[use case]

Copies the elements of this general sequence to an array. Fills the given array
 `xs` with values of this general sequence, beginning at index `start` . Copying
will stop once either the end of the current general sequence is reached, or the
end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this general sequence to an array. Fills the given array
 `xs` with at most `len` elements of this general sequence, starting at position
 `start` . Copying will stop once either the end of the current general sequence
is reached, or the end of the target array is reached, or `len` elements have
been copied.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def maxBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`        ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this general sequence with the largest value measured
    by function f.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def minBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`        ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this general sequence with the smallest value measured
    by function f.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toMap[K, V](implicit ev: <:<[A, (K, V)]): GenMap[K, V]`    ###

[use case]

Converts this general sequence to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this general sequence.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `abstract def parCombiner: Combiner[A, ParSeq[A]]`                       ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * Parallelizable

(defined at scala.collection.Parallelizable)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParSeq[A]`                                                     ###

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
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenSeqLike [A, Repr] to
    CollectionsHaveToParArray [GenSeqLike [A, Repr], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (GenSeqLike [A, Repr]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
