
#                      scala.collection.mutable.AnyRefMap                      #

```scala
final class AnyRefMap[K <: AnyRef, V] extends AbstractMap[K, V] with Map[K, V] with MapLike[K, V, AnyRefMap[K, V]] with Serializable
```

This class implements mutable maps with `AnyRef` keys based on a hash table with
open addressing.

Basic map operations on single entries, including `contains` and `get` , are
typically significantly faster with `AnyRefMap` than HashMap. Note that numbers
and characters are not handled specially in AnyRefMap; only plain `equals` and
 `hashCode` are used in comparisons.

Methods that traverse or regenerate the map, including `foreach` and `map` , are
not in general faster than with `HashMap` . The methods `foreachKey` ,
 `foreachValue` , `mapValuesNow` , and `transformValues` are, however, faster
than alternative ways to achieve the same functionality.

Maps with open addressing may become less efficient at lookup after repeated
addition/removal of elements. Although `AnyRefMap` makes a decent attempt to
remain efficient regardless, calling `repack` on a map that will no longer have
elements removed but will be used heavily may save both time and storage space.

This map is not intended to contain more than 2 <sup>29</sup> entries
(approximately 500 million). The maximum capacity is 2 <sup>30</sup>, but
performance will degrade rapidly as 2 <sup>30</sup> is approached.

* Annotations
  * @ SerialVersionUID ()
* Source
  * [AnyRefMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/AnyRefMap.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class DefaultKeySet extends AbstractSet[A] with Set[A] with Serializable` ###

The implementation class of the set returned by `keySet` .

* Attributes
  * protected
* Definition Classes
  * MapLike


### `class DefaultValuesIterable extends AbstractIterable[B] with Iterable[B] with Serializable` ###

The implementation class of the iterable returned by `values` .

* Attributes
  * protected
* Definition Classes
  * MapLike


### `class FilteredKeys extends AbstractMap[A, B] with DefaultMap[A, B]`     ###

* Attributes
  * protected
* Definition Classes
  * MapLike


### `class MappedValues[C] extends AbstractMap[A, C] with DefaultMap[A, C]`  ###

* Attributes
  * protected
* Definition Classes
  * MapLike


### `type Self = AnyRefMap[K, V]`                                            ###

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


### `def compose[A](g: (A) ⇒ K): (A) ⇒ V`                                    ###

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


### `def andThen[C](k: (V) ⇒ C): PartialFunction[K, C]`                      ###

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


### `def applyOrElse[A1 <: K, B1 >: V](x: A1, default: (A1) ⇒ B1): B1`       ###

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


### `def lift: (K) ⇒ Option[V]`                                              ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: K, B1 >: V](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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


### `def runWith[U](action: (V) ⇒ U): (K) ⇒ Boolean`                         ###

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
                 Value Members From scala.collection.GenMapLike
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


### `def copyToArray[B >: (K, V)](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this mutable map to an array. Fills the given array `xs`
with at most `len` elements of this mutable map, starting at position `start` .
Copying will stop once either the end of the current mutable map is reached, or
the end of the target array is reached, or `len` elements have been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def drop(n: Int): AnyRefMap[K, V]`                                      ###

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
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def dropRight(n: Int): AnyRefMap[K, V]`                                 ###

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


### `def exists(p: ((K, V)) ⇒ Boolean): Boolean`                             ###

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


### `def find(p: ((K, V)) ⇒ Boolean): Option[(K, V)]`                        ###

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


### `def foldRight[B](z: B)(op: ((K, V), B) ⇒ B): B`                         ###

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


### `def forall(p: ((K, V)) ⇒ Boolean): Boolean`                             ###

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


### `def grouped(size: Int): Iterator[AnyRefMap[K, V]]`                      ###

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


### `def head: (K, V)`                                                       ###

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


### `def reduceRight[B >: (K, V)](op: ((K, V), B) ⇒ B): B`                   ###

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


### `def sameElements[B >: (K, V)](that: GenIterable[B]): Boolean`           ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this mutable map.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def slice(from: Int, until: Int): AnyRefMap[K, V]`                      ###

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


### `def sliding(size: Int): Iterator[AnyRefMap[K, V]]`                      ###

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


### `def sliding(size: Int, step: Int): Iterator[AnyRefMap[K, V]]`           ###

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


### `def take(n: Int): AnyRefMap[K, V]`                                      ###

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
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def takeRight(n: Int): AnyRefMap[K, V]`                                 ###

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


### `def takeWhile(p: ((K, V)) ⇒ Boolean): AnyRefMap[K, V]`                  ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def thisCollection: collection.Iterable[(K, V)]`                        ###

The underlying collection seen as an instance of `Iterable` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toCollection(repr: AnyRefMap[K, V]): collection.Iterable[(K, V)]`   ###

A conversion from collections of type `Repr` to `Iterable` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: collection.Iterable[(K, V)]`                            ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[(K, V)]`                                       ###

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


### `def toStream: immutable.Stream[(K, V)]`                                 ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def view(from: Int, until: Int): IterableView[(K, V), AnyRefMap[K, V]]` ###

Creates a non-strict view of a slice of this iterable collection.

Note: the difference between `view` and `slice` is that `view` produces a view
of the current iterable collection, whereas `slice` produces a new iterable
collection.

Note: `view(from, to)` is equivalent to `view.slice(from, to)`

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* from
  * the index of the first element of the view
* until
  * the index of the element following the view
* returns
  * a non-strict view of a slice of this iterable collection, starting at index
     `from` and extending up to (but not including) index `until` .

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def view: IterableView[(K, V), AnyRefMap[K, V]]`                        ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def zipAll[B, A1 >: (K, V), That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[AnyRefMap[K, V], (A1, B), That]): That` ###

[use case]

Returns a mutable map formed from this mutable map and another iterable
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
  * the element to be used to fill up the result if this mutable map is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    mutable map.
* returns
  * a new mutable map containing pairs consisting of corresponding elements of
    this mutable map and `that` . The length of the returned collection is the
    maximum of the lengths of this mutable map and `that` . If this mutable map
    is shorter than `that` , `thisElem` values are used to pad the result. If
     `that` is shorter than this mutable map, `thatElem` values are used to pad
    the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def zipWithIndex[A1 >: (K, V), That](implicit bf: CanBuildFrom[AnyRefMap[K, V], (A1, Int), That]): That` ###

[use case]

Zips this mutable map with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new mutable map containing pairs consisting of all elements of this
    mutable map paired with their index. Indices start at `0` .

* Definition Classes
  * IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IterableLike)


### `def zip[A1 >: (K, V), B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], (A1, B), That]): That` ###

[use case]

Returns a mutable map formed from this mutable map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new mutable map containing pairs consisting of corresponding elements of
    this mutable map and `that` . The length of the returned collection is the
    minimum of the lengths of this mutable map and `that` .

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
                  Value Members From scala.collection.MapLike
--------------------------------------------------------------------------------


### `def addString(b: scala.StringBuilder, start: String, sep: String, end: String): scala.StringBuilder` ###

Appends all bindings of this map to a string builder using start, end, and
separator strings. The written text begins with the string `start` and ends with
the string `end` . Inside, the string representations of all bindings of this
map in the form of `key -> value` are separated by the string `sep` .

* b
  * the builder to which strings are appended.
* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * the string builder `b` to which elements were appended.

* Definition Classes
  * MapLike → TraversableOnce

(defined at scala.collection.MapLike)


### `def filterKeys(p: (K) ⇒ Boolean): collection.Map[K, V]`                 ###

Filters this map by retaining only keys satisfying a predicate.

 *Note* : the predicate must accept any key of type `A` , not just those already
present in the map, as the predicate is tested before the underlying map is
queried.

* p
  * the predicate used to test keys
* returns
  * an immutable map consisting only of those key value pairs of this map where
    the key satisfies the predicate `p` . The resulting map wraps the original
    map without copying any elements.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def filterNot(p: ((K, V)) ⇒ Boolean): AnyRefMap[K, V]`                  ###

Returns a new map obtained by removing all key/value pairs for which the
predicate `p` returns `true` .

 *Note:* This method works by successively removing elements for which the
predicate is true from this set. If removal is slow, or you expect that most
elements of the set will be removed, you might consider using `filter` with a
negated predicate instead.

* p
  * A predicate over key-value pairs
* returns
  * A new map containing elements not satisfying the predicate.

* Definition Classes
  * MapLike → TraversableLike → GenTraversableLike

(defined at scala.collection.MapLike)


### `def isDefinedAt(key: K): Boolean`                                       ###

Tests whether this map contains a binding for a key. This method, which
implements an abstract method of trait `PartialFunction` , is equivalent to
 `contains` .

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

* Definition Classes
  * MapLike → GenMapLike → PartialFunction

(defined at scala.collection.MapLike)


### `def keySet: collection.Set[K]`                                          ###

Collects all keys of this map in a set.

* returns
  * a set containing all keys of this map.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def keys: collection.Iterable[K]`                                       ###

Collects all keys of this map in an iterable collection.

* returns
  * the keys of this map as an iterable.

* Definition Classes
  * MapLike → GenMapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `keys` returns `Iterable[A]` rather than
     `Iterator[A]` .

(defined at scala.collection.MapLike)


### `def keysIterator: Iterator[K]`                                          ###

Creates an iterator for all keys.

* returns
  * an iterator over all keys.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def mapValues[C](f: (V) ⇒ C): collection.Map[K, C]`                     ###

Transforms this map by applying a function to every retrieved value.

* f
  * the function used to transform values of this map.
* returns
  * a map view which maps every key of this map to `f(this(key))` . The
    resulting map wraps the original map without copying any elements.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def toBuffer[C >: (K, V)]: Buffer[C]`                                   ###

Uses the contents of this map to create a new mutable buffer.

* returns
  * a buffer containing all elements of this map.

* Definition Classes
  * MapLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.MapLike)


### `def values: collection.Iterable[V]`                                     ###

Collects all values of this map in an iterable collection.

* returns
  * the values of this map as an iterable.

* Definition Classes
  * MapLike → GenMapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `values` returns `Iterable[B]` rather than
     `Iterator[B]` .

(defined at scala.collection.MapLike)


### `def valuesIterator: Iterator[V]`                                        ###

Creates an iterator for all values in this map.

* returns
  * an iterator over all values that are associated with some key in this map.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


--------------------------------------------------------------------------------
               Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParMap[K, V]`                                                  ###

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
              Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: (K, V), That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

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


### `def ++:[B >: (K, V), That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

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
  * a new mutable map which contains all elements of this mutable map followed
    by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++[B >: (K, V), That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

[use case]

Returns a new mutable map containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
mutable map is the most specific superclass encompassing the element types of
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
  * a new mutable map which contains all elements of this mutable map followed
    by all elements of `that` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def collect[B, That](pf: PartialFunction[(K, V), B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
mutable map on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the mutable map.
* returns
  * a new mutable map resulting from applying the given partial function `pf` to
    each element on which it is defined and collecting the results. The order of
    the elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def dropWhile(p: ((K, V)) ⇒ Boolean): AnyRefMap[K, V]`                  ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this traversable collection whose first element does
    not satisfy the predicate `p` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: ((K, V)) ⇒ Boolean): AnyRefMap[K, V]`                     ###

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


### `def flatMap[B, That](f: ((K, V)) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this mutable
map and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of mutable
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
  * a new mutable map resulting from applying the given collection-valued
    function `f` to each element of this mutable map and concatenating the
    results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def groupBy[K](f: ((K, V)) ⇒ K): immutable.Map[K, AnyRefMap[K, V]]`     ###

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


### `def headOption: Option[(K, V)]`                                         ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def init: AnyRefMap[K, V]`                                              ###

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


### `def inits: Iterator[AnyRefMap[K, V]]`                                   ###

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


### `def last: (K, V)`                                                       ###

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


### `def lastOption: Option[(K, V)]`                                         ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this traversable collection$ if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def map[B, That](f: ((K, V)) ⇒ B)(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this mutable
map.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new mutable map resulting from applying the given function `f` to each
    element of this mutable map and collecting the results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def partition(p: ((K, V)) ⇒ Boolean): (AnyRefMap[K, V], AnyRefMap[K, V])` ###

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


### `def repr: AnyRefMap[K, V]`                                              ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanLeft[B, That](z: B)(op: (B, (K, V)) ⇒ B)(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: ((K, V), B) ⇒ B)(implicit bf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

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


### `def scan[B >: (K, V), That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[AnyRefMap[K, V], B, That]): That` ###

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


### `def span(p: ((K, V)) ⇒ Boolean): (AnyRefMap[K, V], AnyRefMap[K, V])`    ###

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


### `def splitAt(n: Int): (AnyRefMap[K, V], AnyRefMap[K, V])`                ###

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


### `def tail: AnyRefMap[K, V]`                                              ###

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


### `def tails: Iterator[AnyRefMap[K, V]]`                                   ###

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


### `def toTraversable: collection.Traversable[(K, V)]`                      ###

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


### `def withFilter(p: ((K, V)) ⇒ Boolean): FilterMonadic[(K, V), AnyRefMap[K, V]]` ###

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


### `def /:[B](z: B)(op: (B, (K, V)) ⇒ B): B`                                ###

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


### `def :\[B](z: B)(op: ((K, V), B) ⇒ B): B`                                ###

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


### `def addString(b: scala.StringBuilder): scala.StringBuilder`             ###

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


### `def addString(b: scala.StringBuilder, sep: String): scala.StringBuilder` ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, (K, V)) ⇒ B, combop: (B, B) ⇒ B): B` ###

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


### `def collectFirst[B](pf: PartialFunction[(K, V), B]): Option[B]`         ###

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


### `def copyToArray[B >: (K, V)](xs: Array[B]): Unit`                       ###

[use case]

Copies the elements of this mutable map to an array. Fills the given array `xs`
with values of this mutable map. Copying will stop once either the end of the
current mutable map is reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: (K, V)](xs: Array[B], start: Int): Unit`           ###

[use case]

Copies the elements of this mutable map to an array. Fills the given array `xs`
with values of this mutable map, beginning at index `start` . Copying will stop
once either the end of the current mutable map is reached, or the end of the
target array is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: (K, V)](dest: Buffer[B]): Unit`                   ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: ((K, V)) ⇒ Boolean): Int`                                  ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, (K, V)) ⇒ B): B`                          ###

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


### `def fold[A1 >: (K, V)](z: A1)(op: (A1, A1) ⇒ A1): A1`                   ###

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


### `def maxBy[B](f: ((K, V)) ⇒ B)(implicit cmp: Ordering[B]): (K, V)`       ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this mutable map with the largest value measured by
    function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: ((K, V)) ⇒ B)(implicit cmp: Ordering[B]): (K, V)`       ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this mutable map with the smallest value measured by
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


### `def reduceLeftOption[B >: (K, V)](op: (B, (K, V)) ⇒ B): Option[B]`      ###

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


### `def reduceLeft[B >: (K, V)](op: (B, (K, V)) ⇒ B): B`                    ###

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


### `def reduceOption[A1 >: (K, V)](op: (A1, A1) ⇒ A1): Option[A1]`          ###

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


### `def reduceRightOption[B >: (K, V)](op: ((K, V), B) ⇒ B): Option[B]`     ###

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


### `def reduce[A1 >: (K, V)](op: (A1, A1) ⇒ A1): A1`                        ###

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


### `def reversed: List[(K, V)]`                                             ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[(K, V)]`                         ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: List[(K, V)]`                                               ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[(K, V), (T, U)]): immutable.Map[T, U]` ###

[use case]

Converts this mutable map to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this mutable map.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: (K, V)]: immutable.Set[B]`                               ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: Vector[(K, V)]`                                           ###

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


### `def flatten[B](implicit asTraversable: ((K, V)) ⇒ GenTraversableOnce[B]): Iterable[B]` ###

[use case]

Converts this mutable map of traversable collections into a mutable map formed
by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of mutable
map. For example:

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
  * a new mutable map resulting from concatenating all element mutable maps.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, Iterable[B]]`                         ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: ((K, V)) ⇒ GenTraversableOnce[B]): Iterable[Iterable[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: ((K, V)) ⇒ (A1, A2, A3)): (Iterable[A1], Iterable[A2], Iterable[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: ((K, V)) ⇒ (A1, A2)): (Iterable[A1], Iterable[A2])` ###

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
              Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[(K, V)]): AnyRefMap.this.type`              ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: (K, V), elem2: (K, V), elems: (K, V)*): AnyRefMap.this.type` ###

adds two or more elements to this growable collection.

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * the growable collection itself

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


--------------------------------------------------------------------------------
             Value Members From scala.collection.generic.Shrinkable
--------------------------------------------------------------------------------


### `def --=(xs: TraversableOnce[K]): AnyRefMap.this.type`                   ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: K, elem2: K, elems: K*): AnyRefMap.this.type`             ###

Removes two or more elements from this shrinkable collection.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


--------------------------------------------------------------------------------
         Instance Constructors From scala.collection.mutable.AnyRefMap
--------------------------------------------------------------------------------


### `new AnyRefMap(defaultEntry: (K) ⇒ V, initialBufferSize: Int)`           ###

Creates a new `AnyRefMap` with specified default values and initial buffer size.

(defined at scala.collection.mutable.AnyRefMap)


--------------------------------------------------------------------------------
             Value Members From scala.collection.mutable.AnyRefMap
--------------------------------------------------------------------------------


### `def ++[V1 >: V](xs: GenTraversableOnce[(K, V1)]): AnyRefMap[K, V1]`     ###

Creates a new map containing the key/value mappings provided by the specified
traversable object and all the key/value mappings of this map.

Note that existing mappings from this map with the same key as those in `xs`
will be overridden.

* xs
  * the traversable object.
* returns
  * a new map containing mappings of this map and those provided by `xs` .

* Definition Classes
  * AnyRefMap → MapLike → MapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def +=(kv: (K, V)): AnyRefMap.this.type`                                ###

Adds a new key/value pair to this map. If the map already contains a mapping for
the key, it will be overridden by the new value.

* kv
  * the key/value pair.
* returns
  * the map itself

* Definition Classes
  * AnyRefMap → MapLike → Builder → Growable

(defined at scala.collection.mutable.AnyRefMap)


### `def +=(key: K, value: V): AnyRefMap.this.type`                          ###

Adds a new key/value pair to this map and returns the map.

(defined at scala.collection.mutable.AnyRefMap)


### `def +[V1 >: V](kv: (K, V1)): AnyRefMap[K, V1]`                          ###

Creates a new map containing a new key/value mapping and all the key/value
mappings of this map.

Mapping `kv` will override existing mappings from this map with the same key.

* kv
  * the key/value mapping to be added
* returns
  * a new map containing mappings of this map and the mapping `kv` .

* Definition Classes
  * AnyRefMap → MapLike → MapLike → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def -=(key: K): AnyRefMap.this.type`                                    ###

Removes a key from this map.

* key
  * the key to be removed
* returns
  * the map itself.

* Definition Classes
  * AnyRefMap → MapLike → Shrinkable

(defined at scala.collection.mutable.AnyRefMap)


### `def apply(key: K): V`                                                   ###

Retrieves the value associated with a key. If the key does not exist in the map,
the `defaultEntry` for that key will be returned instead; an exception will be
thrown if no `defaultEntry` was supplied.

* key
  * the key
* returns
  * the value associated with the given key, or the result of the map's
     `default` method, if none exists.

* Definition Classes
  * AnyRefMap → MapLike → Function1 → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def clone(): AnyRefMap[K, V]`                                           ###

Create a copy of the receiver object.

The default implementation of the `clone` method is platform dependent.

* returns
  * a copy of the receiver object.

* Definition Classes
  * AnyRefMap → MapLike → Cloneable → AnyRef
* Note
  * not specified by SLS as a member of AnyRef

(defined at scala.collection.mutable.AnyRefMap)


### `def contains(key: K): Boolean`                                          ###

Tests whether this map contains a binding for a key.

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

* Definition Classes
  * AnyRefMap → MapLike → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def default(key: K): V`                                                 ###

Defers to defaultEntry to find a default value for the key. Throws an exception
if no other default behavior was specified.

* key
  * the given key value for which a binding is missing.

* Definition Classes
  * AnyRefMap → MapLike → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def empty: AnyRefMap[K, V]`                                             ###

The empty map of the same type as this map

* returns
  * an empty map of type `This` .

* Definition Classes
  * AnyRefMap → Map → Map → MapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def foreach[U](f: ((K, V)) ⇒ U): Unit`                                  ###

[use case]

Applies a function `f` to all elements of this mutable map.

Note: this method underlies the implementation of most other bulk operations.
Subclasses should re-implement this method if a more efficient implementation
exists.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * AnyRefMap → IterableLike → GenericTraversableTemplate → TraversableLike →
    GenTraversableLike → TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.mutable.AnyRefMap)


### `def foreachKey[A](f: (K) ⇒ A): Unit`                                    ###

Applies a function to all keys of this map.

(defined at scala.collection.mutable.AnyRefMap)


### `def foreachValue[A](f: (V) ⇒ A): Unit`                                  ###

Applies a function to all values of this map.

(defined at scala.collection.mutable.AnyRefMap)


### `def get(key: K): Option[V]`                                             ###

Optionally returns the value associated with a key.

* key
  * the key value
* returns
  * an option value containing the value associated with `key` in this map, or
     `None` if none exists.

* Definition Classes
  * AnyRefMap → MapLike → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def getOrElse[V1 >: V](key: K, default: ⇒ V1): V1`                      ###

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

* Definition Classes
  * AnyRefMap → MapLike → GenMapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def getOrElseUpdate(key: K, defaultValue: ⇒ V): V`                      ###

If given key is already in this map, returns associated value.

Otherwise, computes value from given expression `op` , stores with key in map
and returns that value.

Concurrent map implementations may evaluate the expression `op` multiple times,
or may evaluate `op` without inserting the result.

* key
  * the key to test
* returns
  * the value associated with key (either previously or as a result of executing
    the method).

* Definition Classes
  * AnyRefMap → MapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def getOrNull(key: K): V`                                               ###

Retrieves the value associated with a key, or the default for that type if none
exists (null for AnyRef, 0 for floats and integers).

Note: this is the fastest way to retrieve a value that may or may not exist, if
the default null/zero is acceptable. For key/value pairs that do exist, `apply`
(i.e. `map(key)` ) is equally fast.

(defined at scala.collection.mutable.AnyRefMap)


### `def mapValuesNow[V1](f: (V) ⇒ V1): AnyRefMap[K, V1]`                    ###

Creates a new `AnyRefMap` with different values. Unlike `mapValues` , this
method generates a new collection immediately.

(defined at scala.collection.mutable.AnyRefMap)


### `def put(key: K, value: V): Option[V]`                                   ###

Adds a new key/value pair to this map and optionally returns previously bound
value. If the map already contains a mapping for the key, it will be overridden
by the new value.

* key
  * the key to update
* value
  * the new value
* returns
  * an option value containing the value associated with the key before the
     `put` operation was executed, or `None` if `key` was not defined in the map
    before.

* Definition Classes
  * AnyRefMap → MapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def transformValues(f: (V) ⇒ V): AnyRefMap.this.type`                   ###

Applies a transformation function to all values stored in this map. Note: the
default, if any, is not transformed.

(defined at scala.collection.mutable.AnyRefMap)


### `def update(key: K, value: V): Unit`                                     ###

Updates the map to include a new key-value pair.

This is the fastest way to add an entry to an `AnyRefMap` .

* key
  * The key to update
* value
  * The new value

* Definition Classes
  * AnyRefMap → MapLike

(defined at scala.collection.mutable.AnyRefMap)


### `def updated[V1 >: V](key: K, value: V1): AnyRefMap[K, V1]`              ###

Creates a new map consisting of all key/value pairs of the current map plus a
new pair of a given key and value.

* key
  * The key to add
* value
  * The new value
* returns
  * A fresh immutable map with the binding from `key` to `value` added to this
    map.

* Definition Classes
  * AnyRefMap → MapLike → MapLike → GenMap

(defined at scala.collection.mutable.AnyRefMap)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (AnyRefMap[K, V]) ⇒ NewTo): Builder[(K, V), NewTo]` ###

Creates a new builder by applying a transformation function to the results of
this builder.

* NewTo
  * the type of collection returned by `f` .
* f
  * the transformation function.
* returns
  * a new builder which is the same as the current builder except that a
    transformation function is applied to this builder's result.

* Definition Classes
  * Builder
* Note
  * The original builder should no longer be used after `mapResult` is called.

(defined at scala.collection.mutable.Builder)


### `def sizeHint(size: Int): Unit`                                          ###

Gives a hint how many elements are expected to be added when the next `result`
is called. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _]): Unit`                        ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHint(coll: TraversableLike[_, _], delta: Int): Unit`            ###

Gives a hint that one expects the `result` of this builder to have the same size
as the given collection, plus some delta. This will provide a hint only if the
collection is known to have a cheap `size` method. Currently this is assumed to
be the case if and only if the collection is of type `IndexedSeqLike` . Some
builder classes will optimize their representation based on the hint. However,
builder implementations are still required to work correctly even if the hint is
wrong, i.e. a different number of elements is added.

* coll
  * the collection which serves as a hint for the result's size.
* delta
  * a correction to add to the `coll.size` to produce the size hint.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


### `def sizeHintBounded(size: Int, boundingColl: TraversableLike[_, _]): Unit` ###

Gives a hint how many elements are expected to be added when the next `result`
is called, together with an upper bound given by the size of some other
collection. Some builder classes will optimize their representation based on the
hint. However, builder implementations are still required to work correctly even
if the hint is wrong, i.e. a different number of elements is added.

* size
  * the hint how many elements will be added.
* boundingColl
  * the bounding collection. If it is an IndexedSeqLike, then sizes larger than
    collection's size are reduced.

* Definition Classes
  * Builder

(defined at scala.collection.mutable.Builder)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.Iterable
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[Iterable]`                              ###

The factory companion object that builds instances of class Iterable. (or its
 `Iterable` superclass where class Iterable is not a `Seq` .)

* Definition Classes
  * Iterable → Iterable → GenIterable → Traversable → Traversable →
    GenTraversable → GenericTraversableTemplate

(defined at scala.collection.mutable.Iterable)


--------------------------------------------------------------------------------
                Value Members From scala.collection.mutable.Map
--------------------------------------------------------------------------------


### `def seq: Map[K, V]`                                                     ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Map → Map → GenMap → GenMapLike → Iterable → Iterable → GenIterable →
    Traversable → Traversable → GenTraversable → Parallelizable →
    TraversableOnce → GenTraversableOnce

(defined at scala.collection.mutable.Map)


### `def withDefault(d: (K) ⇒ V): Map[K, V]`                                 ###

The same map with a given default function.

Invoking transformer methods (e.g. `map` ) will not preserve the default value.

* d
  * the function mapping keys to values, used for non-present keys
* returns
  * a wrapper of the map with a default value

* Definition Classes
  * Map

(defined at scala.collection.mutable.Map)


### `def withDefaultValue(d: V): Map[K, V]`                                  ###

The same map with a given default value.

Invoking transformer methods (e.g. `map` ) will not preserve the default value.

* d
  * default value used for non-present keys
* returns
  * a wrapper of the map with a default value

* Definition Classes
  * Map

(defined at scala.collection.mutable.Map)


--------------------------------------------------------------------------------
              Value Members From scala.collection.mutable.MapLike
--------------------------------------------------------------------------------


### `def +[B1 >: V](elem1: (K, B1), elem2: (K, B1), elems: (K, B1)*): Map[K, B1]` ###

Creates a new map containing two or more key/value mappings and all the
key/value mappings of this map.

Specified mappings will override existing mappings from this map with the same
keys.

* B1
  * the type of the added values
* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * a new map containing mappings of this map and two or more specified
    mappings.

* Definition Classes
  * MapLike → MapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `+` creates a new map. Use `+=` to add an
    element to this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def -(key: K): AnyRefMap[K, V]`                                         ###

Creates a new map with all the key/value mappings of this map except the
key/value mapping with the specified key.

* key
  * the key to be removed
* returns
  * a new map with all the mappings of this map except that with a key `key` .

* Definition Classes
  * MapLike → MapLike → Subtractable → GenMapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `-` creates a new map. Use `-=` to remove an
    element from this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def -(elem1: K, elem2: K, elems: K*): AnyRefMap[K, V]`                  ###

Creates a new map with all the key/value mappings of this map except mappings
with keys equal to any of the two or more specified keys.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * a new map containing all the mappings of this map except mappings with a key
    equal to `elem1` , `elem2` or any of `elems` .

* Definition Classes
  * MapLike → Subtractable
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `-` creates a new map. Use `-=` to remove an
    element from this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def --(xs: GenTraversableOnce[K]): AnyRefMap[K, V]`                     ###

Creates a new map with all the key/value mappings of this map except mappings
with keys equal to any of those provided by the specified traversable object.

* xs
  * the traversable object.
* returns
  * a new map with all the key/value mappings of this map except mappings with a
    key equal to a key from `xs` .

* Definition Classes
  * MapLike → Subtractable
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `--` creates a new map. Use `--=` to remove an
    element from this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def newBuilder: Builder[(K, V), AnyRefMap[K, V]]`                       ###

A common implementation of `newBuilder` for all mutable maps in terms of
 `empty` .

Overrides `MapLike` implementation for better efficiency.

* Attributes
  * protected[this]
* Definition Classes
  * MapLike → MapLike → TraversableLike → HasNewBuilder

(defined at scala.collection.mutable.MapLike)


### `def parCombiner: Combiner[(K, V), ParMap[K, V]]`                        ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * MapLike → MapLike → TraversableLike → Parallelizable

(defined at scala.collection.mutable.MapLike)


### `def remove(key: K): Option[V]`                                          ###

Removes a key from this map, returning the value associated previously with that
key as an option.

* key
  * the key to be removed
* returns
  * an option value containing the value associated previously with `key` , or
     `None` if `key` was not defined in the map before.

* Definition Classes
  * MapLike

(defined at scala.collection.mutable.MapLike)


### `def result(): AnyRefMap[K, V]`                                          ###

The result when this map is used as a builder

* returns
  * the map representation itself.

* Definition Classes
  * MapLike → Builder

(defined at scala.collection.mutable.MapLike)


### `def retain(p: (K, V) ⇒ Boolean): AnyRefMap.this.type`                   ###

Retains only those mappings for which the predicate `p` returns `true` .

* p
  * The test predicate

* Definition Classes
  * MapLike

(defined at scala.collection.mutable.MapLike)


### `def toSeq: collection.Seq[(K, V)]`                                      ###

Converts this mutable map to a sequence.

 `Note` : assumes a fast `size` method. Subclasses should override if this is
not true.

* returns
  * a sequence containing all elements of this mutable map.

* Definition Classes
  * MapLike → MapLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.mutable.MapLike)


### `def transform(f: (K, V) ⇒ V): AnyRefMap.this.type`                      ###

Applies a transformation function to all values contained in this map. The
transformation function produces new values from existing keys associated
values.

* f
  * the transformation to apply
* returns
  * the map itself.

* Definition Classes
  * MapLike

(defined at scala.collection.mutable.MapLike)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from AnyRefMap [K, V] to
    CollectionsHaveToParArray [AnyRefMap [K, V], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (AnyRefMap [K, V]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)