
#                     scala.collection.mutable.OpenHashMap                     #

```scala
class OpenHashMap[Key, Value] extends AbstractMap[Key, Value] with Map[Key, Value] with MapLike[Key, Value, OpenHashMap[Key, Value]]
```

A mutable hash map based on an open hashing scheme. The precise scheme is
undefined, but it should make a reasonable effort to ensure that an insert with
consecutive hash codes is not unnecessarily penalised. In particular, mappings
of consecutive integer keys should work without significant performance loss.

* Key
  * type of the keys in this map.
* Value
  * type of the values in this map.

* Source
  * [OpenHashMap.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/OpenHashMap.scala#L1)
* Since
  * 2.7


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


### `type Self = OpenHashMap[Key, Value]`                                    ###

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


### `def compose[A](g: (A) ⇒ Key): (A) ⇒ Value`                              ###

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


### `def andThen[C](k: (Value) ⇒ C): PartialFunction[Key, C]`                ###

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


### `def applyOrElse[A1 <: Key, B1 >: Value](x: A1, default: (A1) ⇒ B1): B1` ###

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


### `def lift: (Key) ⇒ Option[Value]`                                        ###

Turns this partial function into a plain function returning an `Option` result.

* returns
  * a function that takes an argument `x` to `Some(this(x))` if `this` is
    defined for `x` , and to `None` otherwise.

* Definition Classes
  * PartialFunction
* See also
  * Function.unlift

(defined at scala.PartialFunction)


### `def orElse[A1 <: Key, B1 >: Value](that: PartialFunction[A1, B1]): PartialFunction[A1, B1]` ###

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


### `def runWith[U](action: (Value) ⇒ U): (Key) ⇒ Boolean`                   ###

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


### `def copyToArray[B >: (Key, Value)](xs: Array[B], start: Int, len: Int): Unit` ###

[use case]

Copies the elements of this open hash map to an array. Fills the given array
 `xs` with at most `len` elements of this open hash map, starting at position
 `start` . Copying will stop once either the end of the current open hash map is
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


### `def drop(n: Int): OpenHashMap[Key, Value]`                              ###

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


### `def dropRight(n: Int): OpenHashMap[Key, Value]`                         ###

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


### `def exists(p: ((Key, Value)) ⇒ Boolean): Boolean`                       ###

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


### `def find(p: ((Key, Value)) ⇒ Boolean): Option[(Key, Value)]`            ###

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


### `def foldRight[B](z: B)(op: ((Key, Value), B) ⇒ B): B`                   ###

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


### `def forall(p: ((Key, Value)) ⇒ Boolean): Boolean`                       ###

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


### `def grouped(size: Int): Iterator[OpenHashMap[Key, Value]]`              ###

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


### `def head: (Key, Value)`                                                 ###

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


### `def reduceRight[B >: (Key, Value)](op: ((Key, Value), B) ⇒ B): B`       ###

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


### `def sameElements[B >: (Key, Value)](that: GenIterable[B]): Boolean`     ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this open hash map.

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


### `def slice(from: Int, until: Int): OpenHashMap[Key, Value]`              ###

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


### `def sliding(size: Int): Iterator[OpenHashMap[Key, Value]]`              ###

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


### `def sliding(size: Int, step: Int): Iterator[OpenHashMap[Key, Value]]`   ###

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


### `def take(n: Int): OpenHashMap[Key, Value]`                              ###

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


### `def takeRight(n: Int): OpenHashMap[Key, Value]`                         ###

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


### `def takeWhile(p: ((Key, Value)) ⇒ Boolean): OpenHashMap[Key, Value]`    ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def thisCollection: collection.Iterable[(Key, Value)]`                  ###

The underlying collection seen as an instance of `Iterable` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toCollection(repr: OpenHashMap[Key, Value]): collection.Iterable[(Key, Value)]` ###

A conversion from collections of type `Repr` to `Iterable` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: collection.Iterable[(Key, Value)]`                      ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toIterator: Iterator[(Key, Value)]`                                 ###

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


### `def toStream: immutable.Stream[(Key, Value)]`                           ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def view(from: Int, until: Int): IterableView[(Key, Value), OpenHashMap[Key, Value]]` ###

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


### `def view: IterableView[(Key, Value), OpenHashMap[Key, Value]]`          ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def zipAll[B, A1 >: (Key, Value), That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], (A1, B), That]): That` ###

[use case]

Returns a open hash map formed from this open hash map and another iterable
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
  * the element to be used to fill up the result if this open hash map is
    shorter than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    open hash map.
* returns
  * a new open hash map containing pairs consisting of corresponding elements of
    this open hash map and `that` . The length of the returned collection is the
    maximum of the lengths of this open hash map and `that` . If this open hash
    map is shorter than `that` , `thisElem` values are used to pad the result.
    If `that` is shorter than this open hash map, `thatElem` values are used to
    pad the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def zipWithIndex[A1 >: (Key, Value), That](implicit bf: CanBuildFrom[OpenHashMap[Key, Value], (A1, Int), That]): That` ###

[use case]

Zips this open hash map with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new open hash map containing pairs consisting of all elements of this open
    hash map paired with their index. Indices start at `0` .

* Definition Classes
  * IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IterableLike)


### `def zip[A1 >: (Key, Value), B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], (A1, B), That]): That` ###

[use case]

Returns a open hash map formed from this open hash map and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new open hash map containing pairs consisting of corresponding elements of
    this open hash map and `that` . The length of the returned collection is the
    minimum of the lengths of this open hash map and `that` .

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


### `def apply(key: Key): Value`                                             ###

Retrieves the value which is associated with the given key. This method invokes
the `default` method of the map if there is no mapping from the given key to a
value. Unless overridden, the `default` method throws a
 `NoSuchElementException` .

* key
  * the key
* returns
  * the value associated with the given key, or the result of the map's
     `default` method, if none exists.

* Definition Classes
  * MapLike → GenMapLike → Function1

(defined at scala.collection.MapLike)


### `def contains(key: Key): Boolean`                                        ###

Tests whether this map contains a binding for a key.

* key
  * the key
* returns
  * `true` if there is a binding for `key` in this map, `false` otherwise.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def default(key: Key): Value`                                           ###

Defines the default value computation for the map, returned when a key is not
found The method implemented here throws an exception, but it might be
overridden in subclasses.

* key
  * the given key value for which a binding is missing.

* Definition Classes
  * MapLike → GenMapLike
* Exceptions thrown
  *

(defined at scala.collection.MapLike)


### `def filterKeys(p: (Key) ⇒ Boolean): collection.Map[Key, Value]`         ###

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


### `def filterNot(p: ((Key, Value)) ⇒ Boolean): OpenHashMap[Key, Value]`    ###

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


### `def getOrElse[B1 >: Value](key: Key, default: ⇒ B1): B1`                ###

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
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def isDefinedAt(key: Key): Boolean`                                     ###

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


### `def keySet: collection.Set[Key]`                                        ###

Collects all keys of this map in a set.

* returns
  * a set containing all keys of this map.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def keys: collection.Iterable[Key]`                                     ###

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


### `def keysIterator: Iterator[Key]`                                        ###

Creates an iterator for all keys.

* returns
  * an iterator over all keys.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def mapValues[C](f: (Value) ⇒ C): collection.Map[Key, C]`               ###

Transforms this map by applying a function to every retrieved value.

* f
  * the function used to transform values of this map.
* returns
  * a map view which maps every key of this map to `f(this(key))` . The
    resulting map wraps the original map without copying any elements.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


### `def toBuffer[C >: (Key, Value)]: Buffer[C]`                             ###

Uses the contents of this map to create a new mutable buffer.

* returns
  * a buffer containing all elements of this map.

* Definition Classes
  * MapLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.MapLike)


### `def values: collection.Iterable[Value]`                                 ###

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


### `def valuesIterator: Iterator[Value]`                                    ###

Creates an iterator for all values in this map.

* returns
  * an iterator over all values that are associated with some key in this map.

* Definition Classes
  * MapLike → GenMapLike

(defined at scala.collection.MapLike)


--------------------------------------------------------------------------------
               Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `def par: ParMap[Key, Value]`                                            ###

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


### `def ++:[B >: (Key, Value), That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

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


### `def ++:[B >: (Key, Value), That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

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
  * a new open hash map which contains all elements of this open hash map
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++[B >: (Key, Value), That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

[use case]

Returns a new open hash map containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
open hash map is the most specific superclass encompassing the element types of
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
  * a new open hash map which contains all elements of this open hash map
    followed by all elements of `that` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def collect[B, That](pf: PartialFunction[(Key, Value), B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
open hash map on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the open hash map.
* returns
  * a new open hash map resulting from applying the given partial function `pf`
    to each element on which it is defined and collecting the results. The order
    of the elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def dropWhile(p: ((Key, Value)) ⇒ Boolean): OpenHashMap[Key, Value]`    ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this traversable collection whose first element does
    not satisfy the predicate `p` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: ((Key, Value)) ⇒ Boolean): OpenHashMap[Key, Value]`       ###

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


### `def flatMap[B, That](f: ((Key, Value)) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this open hash
map and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of open hash
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
  * a new open hash map resulting from applying the given collection-valued
    function `f` to each element of this open hash map and concatenating the
    results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def groupBy[K](f: ((Key, Value)) ⇒ K): immutable.Map[K, OpenHashMap[Key, Value]]` ###

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


### `def headOption: Option[(Key, Value)]`                                   ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this traversable collection if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def init: OpenHashMap[Key, Value]`                                      ###

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


### `def inits: Iterator[OpenHashMap[Key, Value]]`                           ###

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


### `def last: (Key, Value)`                                                 ###

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


### `def lastOption: Option[(Key, Value)]`                                   ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this traversable collection$ if it is nonempty, `None`
    if it is empty.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def map[B, That](f: ((Key, Value)) ⇒ B)(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this open hash
map.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new open hash map resulting from applying the given function `f` to each
    element of this open hash map and collecting the results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def partition(p: ((Key, Value)) ⇒ Boolean): (OpenHashMap[Key, Value], OpenHashMap[Key, Value])` ###

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


### `def repr: OpenHashMap[Key, Value]`                                      ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanLeft[B, That](z: B)(op: (B, (Key, Value)) ⇒ B)(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: ((Key, Value), B) ⇒ B)(implicit bf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

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


### `def scan[B >: (Key, Value), That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[OpenHashMap[Key, Value], B, That]): That` ###

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


### `def span(p: ((Key, Value)) ⇒ Boolean): (OpenHashMap[Key, Value], OpenHashMap[Key, Value])` ###

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


### `def splitAt(n: Int): (OpenHashMap[Key, Value], OpenHashMap[Key, Value])` ###

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


### `def tail: OpenHashMap[Key, Value]`                                      ###

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


### `def tails: Iterator[OpenHashMap[Key, Value]]`                           ###

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


### `def toTraversable: collection.Traversable[(Key, Value)]`                ###

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


### `def withFilter(p: ((Key, Value)) ⇒ Boolean): FilterMonadic[(Key, Value), OpenHashMap[Key, Value]]` ###

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


### `def /:[B](z: B)(op: (B, (Key, Value)) ⇒ B): B`                          ###

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


### `def :\[B](z: B)(op: ((Key, Value), B) ⇒ B): B`                          ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, (Key, Value)) ⇒ B, combop: (B, B) ⇒ B): B` ###

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


### `def collectFirst[B](pf: PartialFunction[(Key, Value), B]): Option[B]`   ###

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


### `def copyToArray[B >: (Key, Value)](xs: Array[B]): Unit`                 ###

[use case]

Copies the elements of this open hash map to an array. Fills the given array
 `xs` with values of this open hash map. Copying will stop once either the end
of the current open hash map is reached, or the end of the target array is
reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: (Key, Value)](xs: Array[B], start: Int): Unit`     ###

[use case]

Copies the elements of this open hash map to an array. Fills the given array
 `xs` with values of this open hash map, beginning at index `start` . Copying
will stop once either the end of the current open hash map is reached, or the
end of the target array is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: (Key, Value)](dest: Buffer[B]): Unit`             ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: ((Key, Value)) ⇒ Boolean): Int`                            ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, (Key, Value)) ⇒ B): B`                    ###

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


### `def fold[A1 >: (Key, Value)](z: A1)(op: (A1, A1) ⇒ A1): A1`             ###

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


### `def maxBy[B](f: ((Key, Value)) ⇒ B)(implicit cmp: Ordering[B]): (Key, Value)` ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this open hash map with the largest value measured by
    function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: ((Key, Value)) ⇒ B)(implicit cmp: Ordering[B]): (Key, Value)` ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this open hash map with the smallest value measured by
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


### `def reduceLeftOption[B >: (Key, Value)](op: (B, (Key, Value)) ⇒ B): Option[B]` ###

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


### `def reduceLeft[B >: (Key, Value)](op: (B, (Key, Value)) ⇒ B): B`        ###

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


### `def reduceOption[A1 >: (Key, Value)](op: (A1, A1) ⇒ A1): Option[A1]`    ###

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


### `def reduceRightOption[B >: (Key, Value)](op: ((Key, Value), B) ⇒ B): Option[B]` ###

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


### `def reduce[A1 >: (Key, Value)](op: (A1, A1) ⇒ A1): A1`                  ###

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


### `def reversed: List[(Key, Value)]`                                       ###

* Attributes
  * protected[this]
* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toIndexedSeq: immutable.IndexedSeq[(Key, Value)]`                   ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toList: List[(Key, Value)]`                                         ###

Converts this traversable or iterator to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[(Key, Value), (T, U)]): immutable.Map[T, U]` ###

[use case]

Converts this open hash map to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this open hash map.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: (Key, Value)]: immutable.Set[B]`                         ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toVector: Vector[(Key, Value)]`                                     ###

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


### `def flatten[B](implicit asTraversable: ((Key, Value)) ⇒ GenTraversableOnce[B]): Iterable[B]` ###

[use case]

Converts this open hash map of traversable collections into a open hash map
formed by the elements of these traversable collections.

The resulting collection's type will be guided by the static type of open hash
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
  * a new open hash map resulting from concatenating all element open hash maps.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, Iterable[B]]`                         ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: ((Key, Value)) ⇒ GenTraversableOnce[B]): Iterable[Iterable[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: ((Key, Value)) ⇒ (A1, A2, A3)): (Iterable[A1], Iterable[A2], Iterable[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: ((Key, Value)) ⇒ (A1, A2)): (Iterable[A1], Iterable[A2])` ###

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


### `def ++=(xs: TraversableOnce[(Key, Value)]): OpenHashMap.this.type`      ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: (Key, Value), elem2: (Key, Value), elems: (Key, Value)*): OpenHashMap.this.type` ###

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


### `def --=(xs: TraversableOnce[Key]): OpenHashMap.this.type`               ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: Key, elem2: Key, elems: Key*): OpenHashMap.this.type`     ###

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
              Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (OpenHashMap[Key, Value]) ⇒ NewTo): Builder[(Key, Value), NewTo]` ###

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


### `def seq: Map[Key, Value]`                                               ###

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


### `def withDefault(d: (Key) ⇒ Value): Map[Key, Value]`                     ###

The same map with a given default function.

Invoking transformer methods (e.g. `map` ) will not preserve the default value.

* d
  * the function mapping keys to values, used for non-present keys
* returns
  * a wrapper of the map with a default value

* Definition Classes
  * Map

(defined at scala.collection.mutable.Map)


### `def withDefaultValue(d: Value): Map[Key, Value]`                        ###

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


### `def ++[B1 >: Value](xs: GenTraversableOnce[(Key, B1)]): Map[Key, B1]`   ###

Creates a new map containing the key/value mappings provided by the specified
traversable object and all the key/value mappings of this map.

Note that existing mappings from this map with the same key as those in `xs`
will be overridden.

* B1
  * the type of the added values
* xs
  * the traversable object.
* returns
  * a new map containing mappings of this map and those provided by `xs` .

* Definition Classes
  * MapLike → MapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `++` creates a new map. Use `++=` to add an
    element to this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def +[B1 >: Value](kv: (Key, B1)): Map[Key, B1]`                        ###

Creates a new map containing a new key/value mapping and all the key/value
mappings of this map.

Mapping `kv` will override existing mappings from this map with the same key.

* B1
  * the type of the value in the key/value pair.
* kv
  * the key/value mapping to be added
* returns
  * a new map containing mappings of this map and the mapping `kv` .

* Definition Classes
  * MapLike → MapLike → GenMapLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `+` creates a new map. Use `+=` to add an
    element to this map and return that map itself.

(defined at scala.collection.mutable.MapLike)


### `def +[B1 >: Value](elem1: (Key, B1), elem2: (Key, B1), elems: (Key, B1)*): Map[Key, B1]` ###

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


### `def -(key: Key): OpenHashMap[Key, Value]`                               ###

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


### `def -(elem1: Key, elem2: Key, elems: Key*): OpenHashMap[Key, Value]`    ###

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


### `def --(xs: GenTraversableOnce[Key]): OpenHashMap[Key, Value]`           ###

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


### `def getOrElseUpdate(key: Key, op: ⇒ Value): Value`                      ###

If given key is already in this map, returns associated value.

Otherwise, computes value from given expression `op` , stores with key in map
and returns that value.

Concurrent map implementations may evaluate the expression `op` multiple times,
or may evaluate `op` without inserting the result.

* key
  * the key to test
* op
  * the computation yielding the value to associate with `key` , if `key` is
    previously unbound.
* returns
  * the value associated with key (either previously or as a result of executing
    the method).

* Definition Classes
  * MapLike

(defined at scala.collection.mutable.MapLike)


### `def newBuilder: Builder[(Key, Value), OpenHashMap[Key, Value]]`         ###

A common implementation of `newBuilder` for all mutable maps in terms of
 `empty` .

Overrides `MapLike` implementation for better efficiency.

* Attributes
  * protected[this]
* Definition Classes
  * MapLike → MapLike → TraversableLike → HasNewBuilder

(defined at scala.collection.mutable.MapLike)


### `def parCombiner: Combiner[(Key, Value), ParMap[Key, Value]]`            ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * MapLike → MapLike → TraversableLike → Parallelizable

(defined at scala.collection.mutable.MapLike)


### `def result(): OpenHashMap[Key, Value]`                                  ###

The result when this map is used as a builder

* returns
  * the map representation itself.

* Definition Classes
  * MapLike → Builder

(defined at scala.collection.mutable.MapLike)


### `def toSeq: collection.Seq[(Key, Value)]`                                ###

Converts this mutable map to a sequence.

 `Note` : assumes a fast `size` method. Subclasses should override if this is
not true.

* returns
  * a sequence containing all elements of this mutable map.

* Definition Classes
  * MapLike → MapLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.mutable.MapLike)


### `def updated[B1 >: Value](key: Key, value: B1): Map[Key, B1]`            ###

Creates a new map consisting of all key/value pairs of the current map plus a
new pair of a given key and value.

* B1
  * the type of the added value
* key
  * The key to add
* value
  * The new value
* returns
  * A fresh immutable map with the binding from `key` to `value` added to this
    map.

* Definition Classes
  * MapLike → MapLike

(defined at scala.collection.mutable.MapLike)


--------------------------------------------------------------------------------
        Instance Constructors From scala.collection.mutable.OpenHashMap
--------------------------------------------------------------------------------


### `new OpenHashMap()`                                                      ###

A default constructor creates a hashmap with initial size `8` .

(defined at scala.collection.mutable.OpenHashMap)


--------------------------------------------------------------------------------
            Value Members From scala.collection.mutable.OpenHashMap
--------------------------------------------------------------------------------


### `def +=(kv: (Key, Value)): OpenHashMap.this.type`                        ###

Adds a new key/value pair to this map. If the map already contains a mapping for
the key, it will be overridden by the new value.

* kv
  * the key/value pair.
* returns
  * the map itself

* Definition Classes
  * OpenHashMap → MapLike → Builder → Growable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.OpenHashMap)


### `def -=(key: Key): OpenHashMap.this.type`                                ###

Removes a key from this map.

* key
  * the key to be removed
* returns
  * the map itself.

* Definition Classes
  * OpenHashMap → MapLike → Shrinkable
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(defined at scala.collection.mutable.OpenHashMap)


### `def clone(): OpenHashMap[Key, Value]`                                   ###

Create a copy of the receiver object.

The default implementation of the `clone` method is platform dependent.

* returns
  * a copy of the receiver object.

* Definition Classes
  * OpenHashMap → MapLike → Cloneable → AnyRef
* Note
  * not specified by SLS as a member of AnyRef

(defined at scala.collection.mutable.OpenHashMap)


### `def empty: OpenHashMap[Key, Value]`                                     ###

The empty map of the same type as this map

* returns
  * an empty map of type `This` .

* Definition Classes
  * OpenHashMap → Map → Map → MapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def foreach[U](f: ((Key, Value)) ⇒ U): Unit`                            ###

Loop over the key, value mappings of this map.

The behaviour of modifying the map during an iteration is as follows:

* Deleting a mapping is always permitted.
* Changing the value of mapping which is already present is permitted.
* Anything else is not permitted. It will usually, but not always, throw an
   exception.

* U
  * The return type of the specified function `f` , return result of which is
    ignored.
* f
  * The function to apply to each key, value mapping.

* Definition Classes
  * OpenHashMap → IterableLike → GenericTraversableTemplate → TraversableLike →
    GenTraversableLike → TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.mutable.OpenHashMap)


### `def get(key: Key): Option[Value]`                                       ###

Optionally returns the value associated with a key.

* key
  * the key value
* returns
  * an option value containing the value associated with `key` in this map, or
     `None` if none exists.

* Definition Classes
  * OpenHashMap → MapLike → GenMapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def hashOf(key: Key): Int`                                              ###

Returns a mangled hash code of the provided key.

* Attributes
  * protected

(defined at scala.collection.mutable.OpenHashMap)


### `def put(key: Key, value: Value): Option[Value]`                         ###

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
  * OpenHashMap → MapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def remove(key: Key): Option[Value]`                                    ###

Removes a key from this map, returning the value associated previously with that
key as an option.

* key
  * the key to be removed
* returns
  * an option value containing the value associated previously with `key` , or
     `None` if `key` was not defined in the map before.

* Definition Classes
  * OpenHashMap → MapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def retain(f: (Key, Value) ⇒ Boolean): OpenHashMap.this.type`           ###

Retains only those mappings for which the predicate `p` returns `true` .

* Definition Classes
  * OpenHashMap → MapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def transform(f: (Key, Value) ⇒ Value): OpenHashMap.this.type`          ###

Applies a transformation function to all values contained in this map. The
transformation function produces new values from existing keys associated
values.

* f
  * the transformation to apply
* returns
  * the map itself.

* Definition Classes
  * OpenHashMap → MapLike

(defined at scala.collection.mutable.OpenHashMap)


### `def update(key: Key, value: Value): Unit`                               ###

Adds a new key/value pair to this map. If the map already contains a mapping for
the key, it will be overridden by the new value.

* key
  * The key to update
* value
  * The new value

* Definition Classes
  * OpenHashMap → MapLike

(defined at scala.collection.mutable.OpenHashMap)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from OpenHashMap [Key, Value]
    to CollectionsHaveToParArray [OpenHashMap [Key, Value], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (OpenHashMap [
    Key, Value]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
