
#                           scala.collection.GenSet                           #

```scala
trait GenSet[A] extends GenSetLike[A, GenSet[A]] with GenIterable[A] with GenericSetTemplate[A, GenSet]
```

A trait for sets which may possibly have their operations implemented in
parallel.

* Source
  * [GenSet.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenSet.scala#L1)
* Since
  * 2.9


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
                  Concrete Value Members From scala.Function1
--------------------------------------------------------------------------------


### `def andThen[A](g: (Boolean) ⇒ A): (A) ⇒ A`                              ###

Composes two instances of Function1 in a new Function1, with this function
applied first.

* A
  * the result type of function `g`
* g
  * a function R => A
* returns
  * a new function `f` such that `f(x) == g(apply(x))`

* Definition Classes
  * Function1
* Annotations
  * @ unspecialized ()

(defined at scala.Function1)


### `def compose[A](g: (A) ⇒ A): (A) ⇒ Boolean`                              ###

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
          Concrete Value Members From scala.collection.GenIterableLike
--------------------------------------------------------------------------------


### `abstract def sameElements[A1 >: A](that: GenIterable[A1]): Boolean`     ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this collection.

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


### `abstract def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[GenSet[A], (A1, B), That]): That` ###

[use case]

Returns a collection formed from this collection and another iterable collection
by combining corresponding elements in pairs. If one of the two collections is
shorter than the other, placeholder elements are used to extend the shorter
collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this collection is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    collection.
* returns
  * a new collection containing pairs consisting of corresponding elements of
    this collection and `that` . The length of the returned collection is the
    maximum of the lengths of this collection and `that` . If this collection is
    shorter than `that` , `thisElem` values are used to pad the result. If
     `that` is shorter than this collection, `thatElem` values are used to pad
    the result.

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


### `abstract def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[GenSet[A], (A1, B), That]): That` ###

[use case]

Returns a collection formed from this collection and another iterable collection
by combining corresponding elements in pairs. If one of the two collections is
longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new collection containing pairs consisting of corresponding elements of
    this collection and `that` . The length of the returned collection is the
    minimum of the lengths of this collection and `that` .

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


--------------------------------------------------------------------------------
              Abstract Value Members From scala.collection.GenSet
--------------------------------------------------------------------------------


### `abstract def seq: Set[A]`                                               ###

* Definition Classes
  * GenSet → GenIterable → GenTraversable → GenSetLike → Parallelizable →
    GenTraversableOnce

(defined at scala.collection.GenSet)


--------------------------------------------------------------------------------
              Concrete Value Members From scala.collection.GenSet
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[GenSet]`                                ###

The factory companion object that builds instances of class Traversable. (or its
 `Iterable` superclass where class Traversable is not a `Seq` .)

* Definition Classes
  * GenSet → GenIterable → GenTraversable → GenericTraversableTemplate

(defined at scala.collection.GenSet)


--------------------------------------------------------------------------------
            Abstract Value Members From scala.collection.GenSetLike
--------------------------------------------------------------------------------


### `abstract def +(elem: A): GenSet[A]`                                     ###

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `abstract def -(elem: A): GenSet[A]`                                     ###

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `abstract def contains(elem: A): Boolean`                                ###

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `abstract def diff(that: GenSet[A]): GenSet[A]`                          ###

Computes the difference of this set and another set.

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `abstract def union(that: GenSet[A]): GenSet[A]`                         ###

Computes the union between of set and another set.

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.GenSetLike
--------------------------------------------------------------------------------


### `def &(that: GenSet[A]): GenSet[A]`                                      ###

Computes the intersection between this set and another set.

 *Note:* Same as `intersect` .

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def &~(that: GenSet[A]): GenSet[A]`                                     ###

The difference of this set and another set.

 *Note:* Same as `diff` .

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def apply(elem: A): Boolean`                                            ###

Tests if some element is contained in this set.

This method is equivalent to `contains` . It allows sets to be interpreted as
predicates.

* elem
  * the element to test for membership.
* returns
  * `true` if `elem` is contained in this set, `false` otherwise.

* Definition Classes
  * GenSetLike → Function1

(defined at scala.collection.GenSetLike)


### `def equals(that: Any): Boolean`                                         ###

Compares this set with another object for equality.

 *Note:* This operation contains an unchecked cast: if `that` is a set, it will
assume with an unchecked cast that it has the same element type as this set. Any
subsequent ClassCastException is treated as a `false` result.

* that
  * the other object
* returns
  * `true` if `that` is a set which contains the same elements as this set.

* Definition Classes
  * GenSetLike → Equals → AnyRef → Any

(defined at scala.collection.GenSetLike)


### `def intersect(that: GenSet[A]): GenSet[A]`                              ###

Computes the intersection between this set and another set.

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def subsetOf(that: GenSet[A]): Boolean`                                 ###

Tests whether this set is a subset of another set.

* that
  * the set to test.
* returns
  * `true` if this set is a subset of `that` , i.e. if every element of this set
    is also an element of `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


### `def |(that: GenSet[A]): GenSet[A]`                                      ###

Computes the union between this set and another set.

 *Note:* Same as `union` .

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * GenSetLike

(defined at scala.collection.GenSetLike)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.GenTraversableLike
--------------------------------------------------------------------------------


### `abstract def drop(n: Int): GenSet[A]`                                   ###

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


### `abstract def dropWhile(pred: (A) ⇒ Boolean): GenSet[A]`                 ###

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


### `abstract def filter(pred: (A) ⇒ Boolean): GenSet[A]`                    ###

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


### `abstract def filterNot(pred: (A) ⇒ Boolean): GenSet[A]`                 ###

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


### `abstract def groupBy[K](f: (A) ⇒ K): GenMap[K, GenSet[A]]`              ###

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


### `abstract def init: GenSet[A]`                                           ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a general collection consisting of all elements of this general collection
    except the last one.

* Definition Classes
  * GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the general collection is empty.

(defined at scala.collection.GenTraversableLike)


### `abstract def partition(pred: (A) ⇒ Boolean): (GenSet[A], GenSet[A])`    ###

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


### `abstract def repr: GenSet[A]`                                           ###

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def scanLeft[B, That](z: B)(op: (B, A) ⇒ B)(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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


### `abstract def scanRight[B, That](z: B)(op: (A, B) ⇒ B)(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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


### `abstract def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[GenSet[A], B, That]): That` ###

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


### `abstract def slice(unc_from: Int, unc_until: Int): GenSet[A]`           ###

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


### `abstract def span(pred: (A) ⇒ Boolean): (GenSet[A], GenSet[A])`         ###

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


### `abstract def splitAt(n: Int): (GenSet[A], GenSet[A])`                   ###

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


### `abstract def tail: GenSet[A]`                                           ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a general collection consisting of all elements of this general collection
    except the first one.

* Definition Classes
  * GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the general collection is empty.

(defined at scala.collection.GenTraversableLike)


### `abstract def take(n: Int): GenSet[A]`                                   ###

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


### `abstract def takeWhile(pred: (A) ⇒ Boolean): GenSet[A]`                 ###

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


### `abstract def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def collect[B, That](pf: PartialFunction[A, B])(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[GenSet[A], B, That]): That` ###

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


### `abstract def toSeq: GenSeq[A]`                                          ###

Converts this collection or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this collection or iterator.

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


### `abstract def hasDefiniteSize: Boolean`                                  ###

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B]): Unit`                   ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with values of this collection. Copying will stop once either the end of the
current collection is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int): Unit`       ###

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
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit` ###

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
  * the first element of this collection with the largest value measured by
    function f.

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
  * the first element of this collection with the smallest value measured by
    function f.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toMap[K, V](implicit ev: <:<[A, (K, V)]): GenMap[K, V]`    ###

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
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `abstract def parCombiner: Combiner[A, ParSet[A]]`                       ###

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


### `def par: ParSet[A]`                                                     ###

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
    Concrete Value Members From scala.collection.generic.GenericSetTemplate
--------------------------------------------------------------------------------


### `def empty: GenSet[A]`                                                   ###

* Definition Classes
  * GenericSetTemplate

(defined at scala.collection.generic.GenericSetTemplate)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `abstract def foreach[U](f: (A) ⇒ U): Unit`                              ###

[use case]

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, GenSet[B]]`                           ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def newBuilder: Builder[A, GenSet[A]]`                                  ###

The builder that builds instances of type Traversable[A]

* Attributes
  * protected[this]
* Definition Classes
  * GenericTraversableTemplate → HasNewBuilder

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (A) ⇒ GenTraversableOnce[B]): GenSet[GenSet[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (A) ⇒ (A1, A2, A3)): (GenSet[A1], GenSet[A2], GenSet[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (A) ⇒ (A1, A2)): (GenSet[A1], GenSet[A2])` ###

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
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from GenSet [A] to
    CollectionsHaveToParArray [GenSet [A], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (GenSet [A]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
