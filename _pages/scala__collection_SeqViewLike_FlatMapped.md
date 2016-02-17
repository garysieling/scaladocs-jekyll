
#                   scala.collection.SeqViewLike#FlatMapped                   #

```scala
trait FlatMapped[B] extends SeqViewLike.FlatMapped[B] with Transformed[B]
```

* Source
  * [SeqViewLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SeqViewLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait Appended[B >: A] extends SeqViewLike.Appended[B] with Transformed[B]` ###

* Definition Classes
  * SeqViewLike


### `trait DroppedWhile extends SeqViewLike.DroppedWhile with Transformed[A]` ###

* Definition Classes
  * SeqViewLike


### `trait EmptyView extends Transformed[Nothing] with SeqViewLike.EmptyView` ###

* Definition Classes
  * SeqViewLike


### `trait Filtered extends SeqViewLike.Filtered with Transformed[A]`        ###

* Definition Classes
  * SeqViewLike


### `trait FlatMapped[B] extends SeqViewLike.FlatMapped[B] with Transformed[B]` ###

* Definition Classes
  * SeqViewLike


### `trait Forced[B] extends SeqViewLike.Forced[B] with Transformed[B]`      ###

* Definition Classes
  * SeqViewLike


### `trait Mapped[B] extends SeqViewLike.Mapped[B] with Transformed[B]`      ###

* Definition Classes
  * SeqViewLike


### `trait Patched[B >: A] extends Transformed[B]`                           ###

* Definition Classes
  * SeqViewLike


### `trait Prepended[B >: A] extends SeqViewLike.Prepended[B] with Transformed[B]` ###

* Definition Classes
  * SeqViewLike


### `trait Reversed extends Transformed[A]`                                  ###

* Definition Classes
  * SeqViewLike


### `type Self = SeqView[B, Coll]`                                           ###

The type implementing this traversable

* Attributes
  * protected[this]
* Definition Classes
  * TraversableLike


### `trait Sliced extends SeqViewLike.Sliced with Transformed[A]`            ###

* Definition Classes
  * SeqViewLike


### `trait TakenWhile extends SeqViewLike.TakenWhile with Transformed[A]`    ###

* Definition Classes
  * SeqViewLike


### `trait Transformed[+B] extends SeqView[B, Coll] with SeqViewLike.Transformed[B]` ###

* Definition Classes
  * SeqViewLike


### `class WithFilter extends FilterMonadic[A, Repr]`                        ###

A class supporting filtered operations. Instances of this class are returned by
method `withFilter` .

* Definition Classes
  * TraversableLike


### `trait Zipped[B] extends SeqViewLike.Zipped[B] with Transformed[(A, B)]` ###

* Definition Classes
  * SeqViewLike


### `trait ZippedAll[A1 >: A, B] extends SeqViewLike.ZippedAll[A1, B] with Transformed[(A1, B)]` ###

* Definition Classes
  * SeqViewLike


--------------------------------------------------------------------------------
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def compose[A](g: (A) ⇒ Int): (A) ⇒ B`                                  ###

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


### `def andThen[C](k: (B) ⇒ C): PartialFunction[Int, C]`                    ###

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


### `def applyOrElse[A1 <: Int, B1 >: B](x: A1, default: (A1) ⇒ B1): B1`     ###

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


### `def lift: (Int) ⇒ Option[B]`                                            ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: Int, B1 >: B](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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


### `def runWith[U](action: (B) ⇒ U): (Int) ⇒ Boolean`                       ###

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


### `def indexOf[B >: B](elem: B): Int`                                      ###

[use case]

Finds index of first occurrence of some value in this sequence.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this sequence that is equal (as determined
    by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexOf[B >: B](elem: B, from: Int): Int`                           ###

[use case]

Finds index of first occurrence of some value in this sequence after or at some
start index.

Note: may not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this sequence that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def indexWhere(p: (B) ⇒ Boolean): Int`                                  ###

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


### `def lastIndexOf[B >: B](elem: B): Int`                                  ###

[use case]

Finds index of last occurrence of some value in this sequence.

Note: will not terminate for infinite-sized collections.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this sequence that is equal (as determined
    by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexOf[B >: B](elem: B, end: Int): Int`                        ###

[use case]

Finds index of last occurrence of some value in this sequence before or at a
given end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this sequence that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Definition Classes
  * GenSeqLike

(defined at scala.collection.GenSeqLike)


### `def lastIndexWhere(p: (B) ⇒ Boolean): Int`                              ###

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


### `def prefixLength(p: (B) ⇒ Boolean): Int`                                ###

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


### `def copyToArray[B >: B](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this sequence to an array. Fills the given array `xs`
with at most `len` elements of this sequence, starting at position `start` .
Copying will stop once either the end of the current sequence is reached, or the
end of the target array is reached, or `len` elements have been copied.

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


### `def exists(p: (B) ⇒ Boolean): Boolean`                                  ###

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


### `def find(p: (B) ⇒ Boolean): Option[B]`                                  ###

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


### `def foldRight[B](z: B)(op: (B, B) ⇒ B): B`                              ###

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


### `def forall(p: (B) ⇒ Boolean): Boolean`                                  ###

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


### `def head: B`                                                            ###

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


### `def reduceRight[B >: B](op: (B, B) ⇒ B): B`                             ###

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


### `def sameElements[B >: B](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def slice(from: Int, until: Int): SeqView[B, Coll]`                     ###

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


### `def takeWhile(p: (B) ⇒ Boolean): SeqView[B, Coll]`                      ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: Iterable[B]`                                            ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[B]`                                            ###

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


### `def toStream: immutable.Stream[B]`                                      ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.IterableViewLike
--------------------------------------------------------------------------------


### `def drop(n: Int): SeqView[B, Coll]`                                     ###

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


### `def dropRight(n: Int): SeqView[B, Coll]`                                ###

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


### `def grouped(size: Int): Iterator[SeqView[B, Coll]]`                     ###

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


### `def sliding(size: Int): Iterator[SeqView[B, Coll]]`                     ###

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


### `def sliding(size: Int, step: Int): Iterator[SeqView[B, Coll]]`          ###

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


### `def take(n: Int): SeqView[B, Coll]`                                     ###

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


### `def takeRight(n: Int): SeqView[B, Coll]`                                ###

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


### `def zipAll[B, A1 >: B, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[SeqView[B, Coll], (A1, B), That]): That` ###

[use case]

Returns a sequence formed from this sequence and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
shorter than the other, placeholder elements are used to extend the shorter
collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this sequence is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    sequence.
* returns
  * a new sequence containing pairs consisting of corresponding elements of this
    sequence and `that` . The length of the returned collection is the maximum
    of the lengths of this sequence and `that` . If this sequence is shorter
    than `that` , `thisElem` values are used to pad the result. If `that` is
    shorter than this sequence, `thatElem` values are used to pad the result.

* Definition Classes
  * IterableViewLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableViewLike)


### `def zip[A1 >: B, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], (A1, B), That]): That` ###

[use case]

Returns a sequence formed from this sequence and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
longer than the other, its remaining elements are ignored.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new sequence containing pairs consisting of corresponding elements of this
    sequence and `that` . The length of the returned collection is the minimum
    of the lengths of this sequence and `that` .

* Definition Classes
  * IterableViewLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableViewLike)


--------------------------------------------------------------------------------
   Concrete Value Members From scala.collection.IterableViewLike.Transformed
--------------------------------------------------------------------------------


### `def foreach[U](f: (B) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of this sequence.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * Transformed → Transformed → IterableLike → GenericTraversableTemplate →
    TraversableLike → GenTraversableLike → TraversableOnce → GenTraversableOnce
    → FilterMonadic

(defined at scala.collection.IterableViewLike.Transformed)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParSeq[B]`                                                     ###

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
                Concrete Value Members From scala.collection.Seq
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[Seq]`                                   ###

The factory companion object that builds instances of class `Seq` . (or its
 `Iterable` superclass where class `Seq` is not a `Seq` .)

* Definition Classes
  * Seq → GenSeq → Iterable → GenIterable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.Seq)


### `def seq: Seq[B]`                                                        ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Seq → GenSeq → GenSeqLike → Iterable → GenIterable → Traversable →
    GenTraversable → Parallelizable → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Seq)


--------------------------------------------------------------------------------
              Concrete Value Members From scala.collection.SeqLike
--------------------------------------------------------------------------------


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


### `def contains[A1 >: B](elem: A1): Boolean`                               ###

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


### `def corresponds[B](that: GenSeq[B])(p: (B, B) ⇒ Boolean): Boolean`      ###

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


### `def indexOfSlice[B >: B](that: GenSeq[B]): Int`                         ###

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


### `def indexOfSlice[B >: B](that: GenSeq[B], from: Int): Int`              ###

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


### `def indexWhere(p: (B) ⇒ Boolean, from: Int): Int`                       ###

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


### `def indices: immutable.Range`                                           ###

Produces the range of all indices of this sequence.

* returns
  * a `Range` value from `0` to one less than the length of this sequence.

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def lastIndexOfSlice[B >: B](that: GenSeq[B]): Int`                     ###

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


### `def lastIndexOfSlice[B >: B](that: GenSeq[B], end: Int): Int`           ###

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


### `def lastIndexWhere(p: (B) ⇒ Boolean, end: Int): Int`                    ###

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


### `def parCombiner: Combiner[B, ParSeq[B]]`                                ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * SeqLike → TraversableLike → Parallelizable

(defined at scala.collection.SeqLike)


### `def reverseIterator: Iterator[B]`                                       ###

An iterator yielding elements in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseIterator` is the same as `xs.reverse.iterator` but might be
more efficient.

* returns
  * an iterator yielding the elements of this sequence in reversed order

* Definition Classes
  * SeqLike

(defined at scala.collection.SeqLike)


### `def segmentLength(p: (B) ⇒ Boolean, from: Int): Int`                    ###

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


### `def thisCollection: Seq[B]`                                             ###

The underlying collection seen as an instance of `Seq` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


### `def toCollection(repr: SeqView[B, Coll]): Seq[B]`                       ###

A conversion from collections of type `Repr` to `Seq` objects. By default this
is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


### `def toSeq: Seq[B]`                                                      ###

Converts this sequence to a sequence.

Note: will not terminate for infinite-sized collections.

A new collection will not be built; in particular, lazy sequences will stay
lazy.

* returns
  * a sequence containing all elements of this sequence.

* Definition Classes
  * SeqLike → GenSeqLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.SeqLike)


### `def view(from: Int, until: Int): SeqView[B, SeqView[B, Coll]]`          ###

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


### `def view: SeqView[B, SeqView[B, Coll]]`                                 ###

Creates a non-strict view of this sequence.

* returns
  * a non-strict view of this sequence.

* Definition Classes
  * SeqLike → IterableLike → TraversableLike

(defined at scala.collection.SeqLike)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.SeqViewLike
--------------------------------------------------------------------------------


### `def +:[B >: B, That](elem: B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

A copy of the sequence with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original sequence is not modified, so you will want to capture the
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
  * a new sequence consisting of `elem` followed by all elements of this
    sequence.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def :+[B >: B, That](elem: B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

A copy of this sequence with an element appended.

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
  * a new sequence consisting of all elements of this sequence followed by
     `elem` .

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def combinations(n: Int): Iterator[SeqView[B, Coll]]`                   ###

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
  * SeqViewLike → SeqLike

Example:

```scala
"abbbc".combinations(2) = Iterator(ab, ac, bb, bc)
```

(defined at scala.collection.SeqViewLike)


### `def diff[B >: B](that: GenSeq[B]): SeqView[B, Coll]`                    ###

[use case]

Computes the multiset difference between this sequence and another sequence.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence of elements to remove
* returns
  * a new sequence which contains all elements of this sequence except some of
    occurrences of elements that also appear in `that` . If an element value
     `x` appears _n_ times in `that` , then the first _n_ occurrences of `x`
    will not form part of the result, but any following occurrences will.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def distinct: SeqView[B, Coll]`                                         ###

Builds a new sequence from this sequence without any duplicate elements.

Note: will not terminate for infinite-sized collections.

* returns
  * A new sequence which contains the first occurrence of every element of this
    sequence.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def intersect[B >: B](that: GenSeq[B]): SeqView[B, Coll]`               ###

[use case]

Computes the multiset intersection between this sequence and another sequence.

Note: may not terminate for infinite-sized collections.

* that
  * the sequence of elements to intersect with.
* returns
  * a new sequence which contains all elements of this sequence which also
    appear in `that` . If an element value `x` appears _n_ times in `that` ,
    then the first _n_ occurrences of `x` will be retained in the result, but
    any following occurrences will be omitted.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def newAppended[B >: B](that: GenTraversable[B]): Transformed[B]`       ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newDropped(n: Int): Transformed[B]`                                 ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newDroppedWhile(p: (B) ⇒ Boolean): Transformed[B]`                  ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newFiltered(p: (B) ⇒ Boolean): Transformed[B]`                      ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newFlatMapped[B](f: (B) ⇒ GenTraversableOnce[B]): Transformed[B]`   ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newForced[B](xs: ⇒ GenSeq[B]): Transformed[B]`                      ###

Boilerplate method, to override in each subclass This method could be eliminated
if Scala had virtual classes

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newMapped[B](f: (B) ⇒ B): Transformed[B]`                           ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newPatched[B >: B](_from: Int, _patch: GenSeq[B], _replaced: Int): Transformed[B]` ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike

(defined at scala.collection.SeqViewLike)


### `def newPrepended[B >: B](that: GenTraversable[B]): Transformed[B]`      ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newReversed: Transformed[B]`                                        ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike

(defined at scala.collection.SeqViewLike)


### `def newSliced(_endpoints: SliceInterval): Transformed[B]`               ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newTaken(n: Int): Transformed[B]`                                   ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newTakenWhile(p: (B) ⇒ Boolean): Transformed[B]`                    ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike → TraversableViewLike

(defined at scala.collection.SeqViewLike)


### `def newZippedAll[A1 >: B, B](that: GenIterable[B], _thisElem: A1, _thatElem: B): Transformed[(A1, B)]` ###

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike

(defined at scala.collection.SeqViewLike)


### `def newZipped[B](that: GenIterable[B]): Transformed[(B, B)]`            ###

Boilerplate method, to override in each subclass This method could be eliminated
if Scala had virtual classes

* Attributes
  * protected
* Definition Classes
  * SeqViewLike → IterableViewLike

(defined at scala.collection.SeqViewLike)


### `def padTo[B >: B, That](len: Int, elem: B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

A copy of this sequence with an element value appended until a given target
length is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new sequence consisting of all elements of this sequence followed by the
    minimal number of occurrences of `elem` so that the resulting sequence has a
    length of at least `len` .

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def patch[B >: B, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Produces a new sequence where a slice of elements in this sequence is replaced
by another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original sequence
* returns
  * a new sequence consisting of all elements of this sequence except that
     `replaced` elements starting from `from` are replaced by `patch` .

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def permutations: Iterator[SeqView[B, Coll]]`                           ###

Iterates over distinct permutations.

* returns
  * An Iterator which traverses the distinct permutations of this sequence.

* Definition Classes
  * SeqViewLike → SeqLike

Example:

```scala
"abb".permutations = Iterator(abb, bab, bba)
```

(defined at scala.collection.SeqViewLike)


### `def reverse: SeqView[B, Coll]`                                          ###

Returns new sequence with elements in reversed order.

Note: will not terminate for infinite-sized collections.

* returns
  * A new sequence with all elements of this sequence in reversed order.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def reverseMap[B, That](f: (B) ⇒ B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this sequence
and collecting the results in reversed order.

Note: will not terminate for infinite-sized collections.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new sequence resulting from applying the given function `f` to each
    element of this sequence and collecting the results in reversed order.

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def sortBy[B](f: (B) ⇒ B)(implicit ord: Ordering[B]): SeqView[B, Coll]` ###

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
  * SeqViewLike → SeqLike
* See also
  * scala.math.Ordering Note: will not terminate for infinite-sized collections.

Example:

```scala
val words = "The quick brown fox jumped over the lazy dog".split(' ')
// this works because scala.Ordering will implicitly provide an Ordering[Tuple2[Int, Char]]
words.sortBy(x => (x.length, x.head))
res0: Array[String] = Array(The, dog, fox, the, lazy, over, brown, quick, jumped)
```

(defined at scala.collection.SeqViewLike)


### `def sortWith(lt: (B, B) ⇒ Boolean): SeqView[B, Coll]`                   ###

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
  * SeqViewLike → SeqLike

Example:

```scala
List("Steve", "Tom", "John", "Bob").sortWith(_.compareTo(_) < 0) =
List("Bob", "John", "Steve", "Tom")
```

(defined at scala.collection.SeqViewLike)


### `def sorted[B >: B](implicit ord: Ordering[B]): SeqView[B, Coll]`        ###

Sorts this sequence according to an Ordering.

The sort is stable. That is, elements that are equal (as determined by `lt` )
appear in the same order in the sorted sequence as in the original.

* ord
  * the ordering to be used to compare elements.
* returns
  * a sequence consisting of the elements of this sequence sorted according to
    the ordering `ord` .

* Definition Classes
  * SeqViewLike → SeqLike
* See also
  * scala.math.Ordering

(defined at scala.collection.SeqViewLike)


### `def union[B >: B, That](that: GenSeq[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this sequence and also
all elements of a given sequence. `xs union ys` is equivalent to `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

Note: will not terminate for infinite-sized collections.

* that
  * the sequence to add.
* returns
  * a new sequence which contains all elements of this sequence followed by all
    elements of `that` .

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


### `def updated[B >: B, That](index: Int, elem: B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

A copy of this sequence with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this sequence with the element at position `index` replaced by
     `elem` .

* Definition Classes
  * SeqViewLike → SeqLike → GenSeqLike

(defined at scala.collection.SeqViewLike)


--------------------------------------------------------------------------------
      Concrete Value Members From scala.collection.SeqViewLike.FlatMapped
--------------------------------------------------------------------------------


### `def apply(idx: Int): B`                                                 ###

Selects an element by its index in the sequence.

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
  * the element of this sequence at index `idx` , where `0` indicates the first
    element.

* Definition Classes
  * FlatMapped → Transformed → SeqLike → GenSeqLike → Function1
* Exceptions thrown
  * IndexOutOfBoundsException if `idx` does not satisfy `0 <= idx < length` .

(defined at scala.collection.SeqViewLike.FlatMapped)


### `def findRow(idx: Int, lo: Int, hi: Int): Int`                           ###

* Attributes
  * protected[this]

(defined at scala.collection.SeqViewLike.FlatMapped)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


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


### `def repr: SeqView[B, Coll]`                                             ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scan[B >: B, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

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

Copies the elements of this sequence to an array. Fills the given array `xs`
with values of this sequence. Copying will stop once either the end of the
current sequence is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: B](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this sequence to an array. Fills the given array `xs`
with values of this sequence, beginning at index `start` . Copying will stop
once either the end of the current sequence is reached, or the end of the target
array is reached.

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
  * the first element of this sequence with the largest value measured by
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
  * the first element of this sequence with the smallest value measured by
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

Converts this sequence to a map. This method is unavailable unless the elements
are members of Tuple2, each ((T, U)) becoming a key-value pair in the map.
Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this sequence.

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


### `def ++:[B >: B, That](xs: Traversable[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

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


### `def ++:[B >: B, That](xs: TraversableOnce[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

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
  * a new sequence which contains all elements of this sequence followed by all
    elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike

(defined at scala.collection.TraversableViewLike)


### `def ++[B >: B, That](xs: GenTraversableOnce[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Returns a new sequence containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
sequence is the most specific superclass encompassing the element types of the
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
  * a new sequence which contains all elements of this sequence followed by all
    elements of `that` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def collect[B, That](pf: PartialFunction[B, B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
sequence on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the sequence.
* returns
  * a new sequence resulting from applying the given partial function `pf` to
    each element on which it is defined and collecting the results. The order of
    the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def dropWhile(p: (B) ⇒ Boolean): SeqView[B, Coll]`                      ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this collection whose first element does not satisfy
    the predicate `p` .

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filter(p: (B) ⇒ Boolean): SeqView[B, Coll]`                         ###

Selects all elements of this collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that satisfy
    the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def filterNot(p: (B) ⇒ Boolean): SeqView[B, Coll]`                      ###

Selects all elements of this collection which do not satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that do not
    satisfy the given predicate `p` . The order of the elements is preserved.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableViewLike)


### `def flatMap[B, That](f: (B) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this sequence
and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of sequence.
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
  * a new sequence resulting from applying the given collection-valued function
     `f` to each element of this sequence and concatenating the results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def force[B >: B, That](implicit bf: CanBuildFrom[Coll, B, That]): That` ###

* Definition Classes
  * TraversableViewLike

(defined at scala.collection.TraversableViewLike)


### `def groupBy[K](f: (B) ⇒ K): immutable.Map[K, SeqView[B, Coll]]`         ###

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


### `def init: SeqView[B, Coll]`                                             ###

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


### `def inits: Iterator[SeqView[B, Coll]]`                                  ###

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


### `def map[B, That](f: (B) ⇒ B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this sequence.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new sequence resulting from applying the given function `f` to each
    element of this sequence and collecting the results.

* Definition Classes
  * TraversableViewLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableViewLike)


### `def newBuilder: Builder[B, SeqView[B, Coll]]`                           ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * TraversableViewLike → GenericTraversableTemplate → TraversableLike →
    HasNewBuilder

(defined at scala.collection.TraversableViewLike)


### `def partition(p: (B) ⇒ Boolean): (SeqView[B, Coll], SeqView[B, Coll])`  ###

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


### `def scanLeft[B, That](z: B)(op: (B, B) ⇒ B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: (B, B) ⇒ B)(implicit bf: CanBuildFrom[SeqView[B, Coll], B, That]): That` ###

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


### `def span(p: (B) ⇒ Boolean): (SeqView[B, Coll], SeqView[B, Coll])`       ###

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


### `def splitAt(n: Int): (SeqView[B, Coll], SeqView[B, Coll])`              ###

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


### `def tail: SeqView[B, Coll]`                                             ###

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


### `def tails: Iterator[SeqView[B, Coll]]`                                  ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (B) ⇒ (A1, A2, A3)): (FlatMapped.Transformed[A1], FlatMapped.Transformed[A2], FlatMapped.Transformed[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (B) ⇒ (A1, A2)): (FlatMapped.Transformed[A1], FlatMapped.Transformed[A2])` ###

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


### `def withFilter(p: (B) ⇒ Boolean): SeqView[B, Coll]`                     ###

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
  Abstract Value Members From scala.collection.TraversableViewLike.FlatMapped
--------------------------------------------------------------------------------


### `abstract val mapping: (A) ⇒ GenTraversableOnce[B]`                      ###

* Attributes
  * protected[this]
* Definition Classes
  * FlatMapped

(defined at scala.collection.TraversableViewLike.FlatMapped)


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


### `def genericBuilder[B]: Builder[B, Seq[B]]`                              ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (B) ⇒ GenTraversableOnce[B]): Seq[Seq[B]]` ###

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
  * This member is added by an implicit conversion from FlatMapped [B] to
    CollectionsHaveToParArray [FlatMapped [B], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (FlatMapped [B]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
