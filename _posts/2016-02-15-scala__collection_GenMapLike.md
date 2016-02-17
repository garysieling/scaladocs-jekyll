
#                         scala.collection.GenMapLike                         #

```scala
trait GenMapLike[A, +B, +Repr] extends GenIterableLike[(A, B), Repr] with Equals with Parallelizable[(A, B), ParMap[A, B]]
```

A trait for all maps upon which operations may be implemented in parallel.

* Source
  * [GenMapLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/GenMapLike.scala#L1)


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
          Abstract Value Members From scala.collection.GenIterableLike
--------------------------------------------------------------------------------


### `abstract def iterator: Iterator[(A, B)]`                                ###

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.GenIterableLike
--------------------------------------------------------------------------------


### `abstract def sameElements[A1 >: (A, B)](that: GenIterable[A1]): Boolean` ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this general map.

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


### `abstract def zipAll[B, A1 >: (A, B), That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[Repr, (A1, B), That]): That` ###

[use case]

Returns a general map formed from this general map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is shorter than the other, placeholder elements are used to extend
the shorter collection to the length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this general map is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    general map.
* returns
  * a new general map containing pairs consisting of corresponding elements of
    this general map and `that` . The length of the returned collection is the
    maximum of the lengths of this general map and `that` . If this general map
    is shorter than `that` , `thisElem` values are used to pad the result. If
     `that` is shorter than this general map, `thatElem` values are used to pad
    the result.

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


### `abstract def zipWithIndex[A1 >: (A, B), That](implicit bf: CanBuildFrom[Repr, (A1, Int), That]): That` ###

[use case]

Zips this general map with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new general map containing pairs consisting of all elements of this
    general map paired with their index. Indices start at `0` .

* Definition Classes
  * GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.GenIterableLike)


### `abstract def zip[A1 >: (A, B), B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[Repr, (A1, B), That]): That` ###

[use case]

Returns a general map formed from this general map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new general map containing pairs consisting of corresponding elements of
    this general map and `that` . The length of the returned collection is the
    minimum of the lengths of this general map and `that` .

* Definition Classes
  * GenIterableLike

(defined at scala.collection.GenIterableLike)


--------------------------------------------------------------------------------
            Abstract Value Members From scala.collection.GenMapLike
--------------------------------------------------------------------------------


### `abstract def +[B1 >: B](kv: (A, B1)): GenMap[A, B1]`                    ###

(defined at scala.collection.GenMapLike)


### `abstract def -(key: A): Repr`                                           ###

(defined at scala.collection.GenMapLike)


### `abstract def apply(key: A): B`                                          ###

(defined at scala.collection.GenMapLike)


### `abstract def contains(key: A): Boolean`                                 ###

Tests whether this map contains a binding for a key.

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

(defined at scala.collection.GenMapLike)


### `abstract def default(key: A): B`                                        ###

(defined at scala.collection.GenMapLike)


### `abstract def filterKeys(p: (A) ⇒ Boolean): GenMap[A, B]`                ###

Filters this map by retaining only keys satisfying a predicate.

* p
  * the predicate used to test keys
* returns
  * an immutable map consisting only of those key value pairs of this map where
    the key satisfies the predicate `p` . The resulting map wraps the original
    map without copying any elements.

(defined at scala.collection.GenMapLike)


### `abstract def get(key: A): Option[B]`                                    ###

(defined at scala.collection.GenMapLike)


### `abstract def isDefinedAt(key: A): Boolean`                              ###

Tests whether this map contains a binding for a key. This method, which
implements an abstract method of trait `PartialFunction` , is equivalent to
 `contains` .

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

(defined at scala.collection.GenMapLike)


### `abstract def keySet: GenSet[A]`                                         ###

(defined at scala.collection.GenMapLike)


### `abstract def keys: GenIterable[A]`                                      ###

Collects all keys of this map in an iterable collection.

* returns
  * the keys of this map as an iterable.

(defined at scala.collection.GenMapLike)


### `abstract def mapValues[C](f: (B) ⇒ C): GenMap[A, C]`                    ###

Transforms this map by applying a function to every retrieved value.

* f
  * the function used to transform values of this map.
* returns
  * a map view which maps every key of this map to `f(this(key))` . The
    resulting map wraps the original map without copying any elements.

(defined at scala.collection.GenMapLike)


### `abstract def seq: Map[A, B]`                                            ###

* Definition Classes
  * GenMapLike → Parallelizable → GenTraversableOnce

(defined at scala.collection.GenMapLike)


### `abstract def values: GenIterable[B]`                                    ###

Collects all values of this map in an iterable collection.

* returns
  * the values of this map as an iterable.

(defined at scala.collection.GenMapLike)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.GenMapLike
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

Compares two maps structurally; i.e., checks if all mappings contained in this
map are also contained in the other map, and vice versa.

* that
  * the other map
* returns
  * `true` if both maps contain exactly the same mappings, `false` otherwise.

* Definition Classes
  * GenMapLike → Equals → AnyRef → Any

(defined at scala.collection.GenMapLike)


### `abstract def getOrElse[B1 >: B](key: A, default: ⇒ B1): B1`             ###

[use case]

Returns the value associated with a key, or a default value if the key is not
contained in the map.

* key
  * the key.
* default
  * a computation that yields a default value in case no binding for `key` is
    found in the map.
* returns
  * the value associated with `key` if it exists, otherwise the result of the
     `default` computation.

(defined at scala.collection.GenMapLike)


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


### `abstract def dropWhile(pred: ((A, B)) ⇒ Boolean): Repr`                 ###

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


### `abstract def filter(pred: ((A, B)) ⇒ Boolean): Repr`                    ###

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


### `abstract def filterNot(pred: ((A, B)) ⇒ Boolean): Repr`                 ###

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


### `abstract def groupBy[K](f: ((A, B)) ⇒ K): GenMap[K, Repr]`              ###

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


### `abstract def head: (A, B)`                                              ###

Selects the first element of this general collection.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this general collection.

* Definition Classes
  * GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the general collection is empty.

(defined at scala.collection.GenTraversableLike)


### `abstract def headOption: Option[(A, B)]`                                ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this general collection if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def last: (A, B)`                                              ###

Selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * The last element of this general collection.

* Definition Classes
  * GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the general collection is empty.

(defined at scala.collection.GenTraversableLike)


### `abstract def lastOption: Option[(A, B)]`                                ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this general collection$ if it is nonempty, `None` if it
    is empty.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def partition(pred: ((A, B)) ⇒ Boolean): (Repr, Repr)`         ###

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


### `abstract def scanLeft[B, That](z: B)(op: (B, (A, B)) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

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


### `abstract def scanRight[B, That](z: B)(op: ((A, B), B) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

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


### `abstract def scan[B >: (A, B), That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[Repr, B, That]): That` ###

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


### `abstract def span(pred: ((A, B)) ⇒ Boolean): (Repr, Repr)`              ###

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


### `abstract def takeWhile(pred: ((A, B)) ⇒ Boolean): Repr`                 ###

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


### `abstract def ++[B >: (A, B), That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Returns a new general map containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
general map is the most specific superclass encompassing the element types of
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
  * a new general map which contains all elements of this general map followed
    by all elements of `that` .

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def collect[B, That](pf: PartialFunction[(A, B), B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
general map on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the general map.
* returns
  * a new general map resulting from applying the given partial function `pf` to
    each element on which it is defined and collecting the results. The order of
    the elements is preserved.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def flatMap[B, That](f: ((A, B)) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this general
map and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of general
map. This might cause unexpected results sometimes. For example:

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
  * a new general map resulting from applying the given collection-valued
    function `f` to each element of this general map and concatenating the
    results.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


### `abstract def foreach[U](f: ((A, B)) ⇒ U): Unit`                         ###

[use case]

Applies a function `f` to all elements of this general map.

Note: this method underlies the implementation of most other bulk operations.
It's important to implement this method in an efficient way.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * GenTraversableLike → GenTraversableOnce

(defined at scala.collection.GenTraversableLike)


### `abstract def map[B, That](f: ((A, B)) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this general
map.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new general map resulting from applying the given function `f` to each
    element of this general map and collecting the results.

* Definition Classes
  * GenTraversableLike

(defined at scala.collection.GenTraversableLike)


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.GenTraversableOnce
--------------------------------------------------------------------------------


### `abstract def /:[B](z: B)(op: (B, (A, B)) ⇒ B): B`                       ###

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


### `abstract def :\[B](z: B)(op: ((A, B), B) ⇒ B): B`                       ###

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


### `abstract def aggregate[B](z: ⇒ B)(seqop: (B, (A, B)) ⇒ B, combop: (B, B) ⇒ B): B` ###

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


### `abstract def count(p: ((A, B)) ⇒ Boolean): Int`                         ###

Counts the number of elements in the collection or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def exists(p: ((A, B)) ⇒ Boolean): Boolean`                    ###

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


### `abstract def find(p: ((A, B)) ⇒ Boolean): Option[(A, B)]`               ###

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


### `abstract def foldLeft[B](z: B)(op: (B, (A, B)) ⇒ B): B`                 ###

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


### `abstract def foldRight[B](z: B)(op: ((A, B), B) ⇒ B): B`                ###

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


### `abstract def fold[A1 >: (A, B)](z: A1)(op: (A1, A1) ⇒ A1): A1`          ###

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


### `abstract def forall(p: ((A, B)) ⇒ Boolean): Boolean`                    ###

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


### `abstract def reduceLeftOption[B >: (A, B)](op: (B, (A, B)) ⇒ B): Option[B]` ###

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


### `abstract def reduceOption[A1 >: (A, B)](op: (A1, A1) ⇒ A1): Option[A1]` ###

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


### `abstract def reduceRightOption[B >: (A, B)](op: ((A, B), B) ⇒ B): Option[B]` ###

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


### `abstract def reduceRight[B >: (A, B)](op: ((A, B), B) ⇒ B): B`          ###

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


### `abstract def reduce[A1 >: (A, B)](op: (A1, A1) ⇒ A1): A1`               ###

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


### `abstract def toBuffer[A1 >: (A, B)]: Buffer[A1]`                        ###

Uses the contents of this collection or iterator to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIndexedSeq: immutable.IndexedSeq[(A, B)]`                ###

Converts this collection or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toIterable: GenIterable[(A, B)]`                           ###

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


### `abstract def toIterator: Iterator[(A, B)]`                              ###

Returns an Iterator over the elements in this collection or iterator. Will
return the same Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toList: List[(A, B)]`                                      ###

Converts this collection or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toSeq: GenSeq[(A, B)]`                                     ###

Converts this collection or iterator to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toSet[A1 >: (A, B)]: GenSet[A1]`                           ###

Converts this collection or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toStream: Stream[(A, B)]`                                  ###

Converts this collection or iterator to a stream.

* returns
  * a stream containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toTraversable: GenTraversable[(A, B)]`                     ###

Converts this collection or iterator to an unspecified Traversable. Will return
the same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this collection or iterator.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toVector: Vector[(A, B)]`                                  ###

Converts this collection or iterator to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this collection or iterator.

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


### `abstract def copyToArray[B >: (A, B)](xs: Array[B]): Unit`              ###

[use case]

Copies the elements of this general map to an array. Fills the given array `xs`
with values of this general map. Copying will stop once either the end of the
current general map is reached, or the end of the target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: (A, B)](xs: Array[B], start: Int): Unit`  ###

[use case]

Copies the elements of this general map to an array. Fills the given array `xs`
with values of this general map, beginning at index `start` . Copying will stop
once either the end of the current general map is reached, or the end of the
target array is reached.

Note: will not terminate for infinite-sized collections.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def copyToArray[B >: (A, B)](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this general map to an array. Fills the given array `xs`
with at most `len` elements of this general map, starting at position `start` .
Copying will stop once either the end of the current general map is reached, or
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


### `abstract def maxBy[B](f: ((A, B)) ⇒ B)(implicit cmp: Ordering[B]): (A, B)` ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this general map with the largest value measured by
    function f.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def minBy[B](f: ((A, B)) ⇒ B)(implicit cmp: Ordering[B]): (A, B)` ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this general map with the smallest value measured by
    function f.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


### `abstract def toMap[K, V](implicit ev: <:<[(A, B), (K, V)]): GenMap[K, V]` ###

[use case]

Converts this general map to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

Note: will not terminate for infinite-sized collections.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this general map.

* Definition Classes
  * GenTraversableOnce

(defined at scala.collection.GenTraversableOnce)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `abstract def parCombiner: Combiner[(A, B), ParMap[A, B]]`               ###

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


### `def par: ParMap[A, B]`                                                  ###

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
  * This member is added by an implicit conversion from GenMapLike [A, B, Repr]
    to CollectionsHaveToParArray [GenMapLike [A, B, Repr], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (GenMapLike [A,
    B, Repr]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
