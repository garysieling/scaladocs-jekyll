
#                          scala.collection.SetProxy                          #

```scala
trait SetProxy[A] extends Set[A] with SetProxyLike[A, Set[A]]
```

This is a simple wrapper class for scala.collection.Set. It is most useful for
assembling customized set abstractions dynamically using object composition and
forwarding.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.3)_ Proxying is deprecated due to lack of use and
    compiler-level support.
* Source
  * [SetProxy.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/SetProxy.scala#L1)
* Version
  * 2.0, 01/01/2007


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Self = Set[A]`                                                     ###

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
                    Concrete Value Members From scala.Proxy
--------------------------------------------------------------------------------


### `def equals(that: Any): Boolean`                                         ###

Compares the receiver object ( `this` ) with the argument object ( `that` ) for
equivalence.

Any implementation of this method should be an
[equivalence relation](http://en.wikipedia.org/wiki/Equivalence_relation) :

* It is reflexive: for any instance `x` of type `Any` , `x.equals(x)` should
   return `true` .
* It is symmetric: for any instances `x` and `y` of type `Any` , `x.equals(y)`
   should return `true` if and only if `y.equals(x)` returns `true` .
* It is transitive: for any instances `x` , `y` , and `z` of type `Any` if
    `x.equals(y)` returns `true` and `y.equals(z)` returns `true` , then
    `x.equals(z)` should return `true` .

If you override this method, you should verify that your implementation remains
an equivalence relation. Additionally, when overriding this method it is usually
necessary to override `hashCode` to ensure that objects which are "equal" (
 `o1.equals(o2)` returns `true` ) hash to the same scala.Int. (
 `o1.hashCode.equals(o2.hashCode)` ).

* that
  * the object to compare against this object for equality.
* returns
  * `true` if the receiver object is equivalent to the argument; `false`
    otherwise.

* Definition Classes
  * Proxy → Any

(defined at scala.Proxy)


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


### `def toCollection(repr: Set[A]): Iterable[A]`                            ###

A conversion from collections of type `Repr` to `Iterable` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.IterableProxyLike
--------------------------------------------------------------------------------


### `def dropRight(n: Int): Set[A]`                                          ###

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
  * IterableProxyLike → IterableLike

(defined at scala.collection.IterableProxyLike)


### `def grouped(size: Int): Iterator[Set[A]]`                               ###

Partitions elements in fixed size iterable collections.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    will be less than size `size` if the elements don't divide evenly.

* Definition Classes
  * IterableProxyLike → IterableLike
* See also
  * scala.collection.Iterator, method `grouped`

(defined at scala.collection.IterableProxyLike)


### `def sameElements[B >: A](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this set.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Definition Classes
  * IterableProxyLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableProxyLike)


### `def sliding(size: Int): Iterator[Set[A]]`                               ###

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
  * IterableProxyLike → IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableProxyLike)


### `def sliding(size: Int, step: Int): Iterator[Set[A]]`                    ###

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
  * IterableProxyLike → IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(defined at scala.collection.IterableProxyLike)


### `def takeRight(n: Int): Set[A]`                                          ###

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
  * IterableProxyLike → IterableLike

(defined at scala.collection.IterableProxyLike)


### `def view(from: Int, until: Int): IterableView[A, Set[A]]`               ###

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
  * IterableProxyLike → TraversableProxyLike → IterableLike → TraversableLike

(defined at scala.collection.IterableProxyLike)


### `def view: IterableView[A, Set[A]]`                                      ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Definition Classes
  * IterableProxyLike → TraversableProxyLike → IterableLike → TraversableLike

(defined at scala.collection.IterableProxyLike)


### `def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[Set[A], (A1, B), That]): That` ###

[use case]

Returns a set formed from this set and another iterable collection by combining
corresponding elements in pairs. If one of the two collections is shorter than
the other, placeholder elements are used to extend the shorter collection to the
length of the longer.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this set is shorter than
     `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    set.
* returns
  * a new set containing pairs consisting of corresponding elements of this set
    and `that` . The length of the returned collection is the maximum of the
    lengths of this set and `that` . If this set is shorter than `that` ,
     `thisElem` values are used to pad the result. If `that` is shorter than
    this set, `thatElem` values are used to pad the result.

* Definition Classes
  * IterableProxyLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableProxyLike)


### `def zipWithIndex[A1 >: A, That](implicit bf: CanBuildFrom[Set[A], (A1, Int), That]): That` ###

[use case]

Zips this set with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new set containing pairs consisting of all elements of this set paired
    with their index. Indices start at `0` .

* Definition Classes
  * IterableProxyLike → IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IterableProxyLike)


### `def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[Set[A], (A1, B), That]): That` ###

[use case]

Returns a set formed from this set and another iterable collection by combining
corresponding elements in pairs. If one of the two collections is longer than
the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new set containing pairs consisting of corresponding elements of this set
    and `that` . The length of the returned collection is the minimum of the
    lengths of this set and `that` .

* Definition Classes
  * IterableProxyLike → IterableLike → GenIterableLike

(defined at scala.collection.IterableProxyLike)


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
                Concrete Value Members From scala.collection.Set
--------------------------------------------------------------------------------


### `def companion: GenericCompanion[Set]`                                   ###

The factory companion object that builds instances of class Set. (or its
 `Iterable` superclass where class Set is not a `Seq` .)

* Definition Classes
  * Set → GenSet → Iterable → GenIterable → Traversable → GenTraversable →
    GenericTraversableTemplate

(defined at scala.collection.Set)


### `def seq: Set[A]`                                                        ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Definition Classes
  * Set → GenSet → GenSetLike → Iterable → GenIterable → Traversable →
    GenTraversable → Parallelizable → TraversableOnce → GenTraversableOnce

(defined at scala.collection.Set)


--------------------------------------------------------------------------------
              Concrete Value Members From scala.collection.SetLike
--------------------------------------------------------------------------------


### `def +(elem1: A, elem2: A, elems: A*): Set[A]`                           ###

Creates a new set with additional elements, omitting duplicates.

This method takes two or more elements to be added. Elements that already exist
in the set will not be added. Another overloaded variant of this method handles
the case where a single element is added.

Example:

```scala
scala> val a = Set(1, 3) + 2 + 3
a: scala.collection.immutable.Set[Int] = Set(1, 3, 2)
```

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * a new set with the given elements added, omitting duplicates.

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


### `def ++(elems: GenTraversableOnce[A]): Set[A]`                           ###

Creates a new set by adding all elements contained in another collection to this
set, omitting duplicates.

This method takes a collection of elements and adds all elements, omitting
duplicates, into set.

Example:

```scala
scala> val a = Set(1, 2) ++ Set(2, "a")
a: scala.collection.immutable.Set[Any] = Set(1, 2, a)
```

* elems
  * the collection containing the elements to add.
* returns
  * a new set with the given elements added, omitting duplicates.

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


### `def newBuilder: Builder[A, Set[A]]`                                     ###

A common implementation of `newBuilder` for all sets in terms of `empty` .
Overridden for mutable sets in `mutable.SetLike`.

* Attributes
  * protected[this]
* Definition Classes
  * SetLike → TraversableLike → HasNewBuilder

(defined at scala.collection.SetLike)


### `def parCombiner: Combiner[A, ParSet[A]]`                                ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * SetLike → TraversableLike → Parallelizable

(defined at scala.collection.SetLike)


### `def subsets(): Iterator[Set[A]]`                                        ###

An iterator over all subsets of this set.

* returns
  * the iterator.

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


### `def subsets(len: Int): Iterator[Set[A]]`                                ###

An iterator over all subsets of this set of the given size. If the requested
size is impossible, an empty iterator is returned.

* len
  * the size of the subsets.
* returns
  * the iterator.

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.SetProxyLike
--------------------------------------------------------------------------------


### `def &(that: GenSet[A]): Set[A]`                                         ###

Computes the intersection between this set and another set.

 *Note:* Same as `intersect` .

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * SetProxyLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def &~(that: GenSet[A]): Set[A]`                                        ###

The difference of this set and another set.

 *Note:* Same as `diff` .

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * SetProxyLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def +(elem: A): Set[A]`                                                 ###

Creates a new set with an additional element, unless the element is already
present.

* elem
  * the element to be added
* returns
  * a new set that contains all elements of this set and that also contains
     `elem` .

* Definition Classes
  * SetProxyLike → SetLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def -(elem: A): Set[A]`                                                 ###

Creates a new set with a given element removed from this set.

* elem
  * the element to be removed
* returns
  * a new set that contains all elements of this set but that does not contain
     `elem` .

* Definition Classes
  * SetProxyLike → SetLike → Subtractable → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def apply(elem: A): Boolean`                                            ###

Tests if some element is contained in this set.

This method is equivalent to `contains` . It allows sets to be interpreted as
predicates.

* elem
  * the element to test for membership.
* returns
  * `true` if `elem` is contained in this set, `false` otherwise.

* Definition Classes
  * SetProxyLike → GenSetLike → Function1

(defined at scala.collection.SetProxyLike)


### `def contains(elem: A): Boolean`                                         ###

Tests if some element is contained in this set.

* elem
  * the element to test for membership.
* returns
  * `true` if `elem` is contained in this set, `false` otherwise.

* Definition Classes
  * SetProxyLike → SetLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def diff(that: GenSet[A]): Set[A]`                                      ###

Computes the difference of this set and another set.

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * SetProxyLike → SetLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def intersect(that: GenSet[A]): Set[A]`                                 ###

Computes the intersection between this set and another set.

* that
  * the set to intersect with.
* returns
  * a new set consisting of all elements that are both in this set and in the
    given set `that` .

* Definition Classes
  * SetProxyLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def subsetOf(that: GenSet[A]): Boolean`                                 ###

Tests whether this set is a subset of another set.

* that
  * the set to test.
* returns
  * `true` if this set is a subset of `that` , i.e. if every element of this set
    is also an element of `that` .

* Definition Classes
  * SetProxyLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def union(that: GenSet[A]): Set[A]`                                     ###

Computes the union between of set and another set.

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * SetProxyLike → SetLike → GenSetLike

(defined at scala.collection.SetProxyLike)


### `def |(that: GenSet[A]): Set[A]`                                         ###

Computes the union between this set and another set.

 *Note:* Same as `union` .

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * SetProxyLike → GenSetLike

(defined at scala.collection.SetProxyLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: A, That](that: Traversable[B])(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

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


### `def ++:[B >: A, That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

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
  * a new set which contains all elements of this set followed by all elements
    of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def inits: Iterator[Set[A]]`                                            ###

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


### `def repr: Set[A]`                                                       ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[Set[A], B, That]): That` ###

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


### `def tails: Iterator[Set[A]]`                                            ###

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


### `def withFilter(p: (A) ⇒ Boolean): FilterMonadic[A, Set[A]]`             ###

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


### `def aggregate[B](z: ⇒ B)(seqop: (B, A) ⇒ B, combop: (B, B) ⇒ B): B`     ###

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


### `def collectFirst[B](pf: PartialFunction[A, B]): Option[B]`              ###

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


### `def fold[A1 >: A](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

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


### `def maxBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this set with the largest value measured by function f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def minBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this set with the smallest value measured by function
    f.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`               ###

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


### `def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                             ###

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


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.TraversableProxyLike
--------------------------------------------------------------------------------


### `abstract def self: Set[A]`                                              ###

* Definition Classes
  * TraversableProxyLike → Proxy

(defined at scala.collection.TraversableProxyLike)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.TraversableProxyLike
--------------------------------------------------------------------------------


### `def ++[B >: A, That](xs: GenTraversableOnce[B])(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

[use case]

Returns a new set containing the elements from the left hand operand followed by
the elements from the right hand operand. The element type of the set is the
most specific superclass encompassing the element types of the two operands.

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
  * a new set which contains all elements of this set followed by all elements
    of `that` .

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def /:[B](z: B)(op: (B, A) ⇒ B): B`                                     ###

Applies a binary operator to a start value and all elements of this traversable
collection, going left to right.

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
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable collection, going left to right with the start value `z` on the
    left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def :\[B](z: B)(op: (A, B) ⇒ B): B`                                     ###

Applies a binary operator to all elements of this traversable collection and a
start value, going right to left.

Note: `:\` is alternate syntax for `foldRight` ; `xs :\ z` is the same as
 `xs foldRight z` .

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

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
    traversable collection, going right to left with the start value `z` on the
    right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def addString(b: mutable.StringBuilder): mutable.StringBuilder`         ###

Appends all elements of this traversable collection to a string builder. The
written text consists of the string representations (w.r.t. the method
 `toString` ) of all elements of this traversable collection without any
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
  * TraversableProxyLike → TraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def addString(b: mutable.StringBuilder, sep: String): mutable.StringBuilder` ###

Appends all elements of this traversable collection to a string builder using a
separator string. The written text consists of the string representations
(w.r.t. the method `toString` ) of all elements of this traversable collection,
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
  * TraversableProxyLike → TraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def addString(b: mutable.StringBuilder, start: String, sep: String, end: String): mutable.StringBuilder` ###

Appends all elements of this traversable collection to a string builder using
start, end, and separator strings. The written text begins with the string
 `start` and ends with the string `end` . Inside, the string representations
(w.r.t. the method `toString` ) of all elements of this traversable collection
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
  * TraversableProxyLike → TraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def collect[B, That](pf: PartialFunction[A, B])(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
set on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the set.
* returns
  * a new set resulting from applying the given partial function `pf` to each
    element on which it is defined and collecting the results. The order of the
    elements is preserved.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this set to an array. Fills the given array `xs` with
values of this set. Copying will stop once either the end of the current set is
reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this set to an array. Fills the given array `xs` with
values of this set, beginning at index `start` . Copying will stop once either
the end of the current set is reached, or the end of the target array is
reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this set to an array. Fills the given array `xs` with at
most `len` elements of this set, starting at position `start` . Copying will
stop once either the end of the current set is reached, or the end of the target
array is reached, or `len` elements have been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Definition Classes
  * TraversableProxyLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this traversable collection to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableProxyLike → TraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def count(p: (A) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable collection which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def drop(n: Int): Set[A]`                                               ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this traversable collection.
* returns
  * a traversable collection consisting of all elements of this traversable
    collection except the first `n` ones, or else the empty traversable
    collection, if this traversable collection has less than `n` elements.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def dropWhile(p: (A) ⇒ Boolean): Set[A]`                                ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this traversable collection whose first element does
    not satisfy the predicate `p` .

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def exists(p: (A) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for at least one element of this traversable
collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `false` if this traversable collection is empty, otherwise `true` if the
    given predicate `p` holds for some of the elements of this traversable
    collection, otherwise `false`

* Definition Classes
  * TraversableProxyLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def filter(p: (A) ⇒ Boolean): Set[A]`                                   ###

Selects all elements of this traversable collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new traversable collection consisting of all elements of this traversable
    collection that satisfy the given predicate `p` . The order of the elements
    is preserved.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def filterNot(p: (A) ⇒ Boolean): Set[A]`                                ###

Selects all elements of this traversable collection which do not satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * a new traversable collection consisting of all elements of this traversable
    collection that do not satisfy the given predicate `p` . The order of the
    elements is preserved.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def find(p: (A) ⇒ Boolean): Option[A]`                                  ###

Finds the first element of the traversable collection satisfying a predicate, if
any.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the traversable collection
    that satisfies `p` , or `None` if none exists.

* Definition Classes
  * TraversableProxyLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this set and
using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of set. This
might cause unexpected results sometimes. For example:

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
  * a new set resulting from applying the given collection-valued function `f`
    to each element of this set and concatenating the results.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableProxyLike)


### `def foldLeft[B](z: B)(op: (B, A) ⇒ B): B`                               ###

Applies a binary operator to a start value and all elements of this traversable
collection, going left to right.

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
  * the result of inserting `op` between consecutive elements of this
    traversable collection, going left to right with the start value `z` on the
    left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable collection. Returns
     `z` if this traversable collection is empty.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def foldRight[B](z: B)(op: (A, B) ⇒ B): B`                              ###

Applies a binary operator to all elements of this traversable collection and a
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
  * the result of inserting `op` between consecutive elements of this
    traversable collection, going right to left with the start value `z` on the
    right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this traversable collection. Returns
     `z` if this traversable collection is empty.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def forall(p: (A) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for all elements of this traversable collection.

Note: may not terminate for infinite-sized collections.

* p
  * the predicate used to test elements.
* returns
  * `true` if this traversable collection is empty or the given predicate `p`
    holds for all elements of this traversable collection, otherwise `false` .

* Definition Classes
  * TraversableProxyLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def foreach[U](f: (A) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of this set.

Note: this method underlies the implementation of most other bulk operations.
It's important to implement this method in an efficient way.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike →
    TraversableOnce → GenTraversableOnce → FilterMonadic

(defined at scala.collection.TraversableProxyLike)


### `def groupBy[K](f: (A) ⇒ K): immutable.Map[K, Set[A]]`                   ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def init: Set[A]`                                                       ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a traversable collection consisting of all elements of this traversable
    collection except the last one.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the traversable collection is empty.

(defined at scala.collection.TraversableProxyLike)


### `def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this set.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new set resulting from applying the given function `f` to each element of
    this set and collecting the results.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableProxyLike)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this traversable collection in a string using a
separator string.

* sep
  * the separator string.
* returns
  * a string representation of this traversable collection. In the resulting
    string the string representations (w.r.t. the method `toString` ) of all
    elements of this traversable collection are separated by the string `sep` .

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(defined at scala.collection.TraversableProxyLike)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this traversable collection in a string using start,
end, and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this traversable collection. The resulting string
    begins with the string `start` and ends with the string `end` . Inside, the
    string representations (w.r.t. the method `toString` ) of all elements of
    this traversable collection are separated by the string `sep` .

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(defined at scala.collection.TraversableProxyLike)


### `def partition(p: (A) ⇒ Boolean): (Set[A], Set[A])`                      ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def reduceLeftOption[B >: A](op: (B, A) ⇒ B): Option[B]`                ###

Optionally applies a binary operator to all elements of this traversable
collection, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this
    traversable collection is nonempty, `None` otherwise.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def reduceLeft[B >: A](op: (B, A) ⇒ B): B`                              ###

Applies a binary operator to all elements of this traversable collection, going
left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable collection, going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable collection is empty.

(defined at scala.collection.TraversableProxyLike)


### `def reduceRightOption[B >: A](op: (A, B) ⇒ B): Option[B]`               ###

Optionally applies a binary operator to all elements of this traversable
collection, going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this
    traversable collection is nonempty, `None` otherwise.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def reduceRight[B >: A](op: (A, B) ⇒ B): B`                             ###

Applies a binary operator to all elements of this traversable collection, going
right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    traversable collection, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this traversable collection is empty.

(defined at scala.collection.TraversableProxyLike)


### `def scanLeft[B, That](z: B)(op: (B, A) ⇒ B)(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def scanRight[B, That](z: B)(op: (A, B) ⇒ B)(implicit bf: CanBuildFrom[Set[A], B, That]): That` ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def slice(from: Int, until: Int): Set[A]`                               ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a traversable collection containing the elements greater than or equal to
    index `from` extending up to (but not including) index `until` of this
    traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def span(p: (A) ⇒ Boolean): (Set[A], Set[A])`                           ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def splitAt(n: Int): (Set[A], Set[A])`                                  ###

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
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def tail: Set[A]`                                                       ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a traversable collection consisting of all elements of this traversable
    collection except the first one.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the traversable collection is empty.

(defined at scala.collection.TraversableProxyLike)


### `def take(n: Int): Set[A]`                                               ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this traversable collection.
* returns
  * a traversable collection consisting only of the first `n` elements of this
    traversable collection, or else the whole traversable collection, if it has
    less than `n` elements.

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def takeWhile(p: (A) ⇒ Boolean): Set[A]`                                ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this traversable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * TraversableProxyLike → TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableProxyLike)


### `def toBuffer[B >: A]: Buffer[B]`                                        ###

Uses the contents of this traversable collection to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def toIndexedSeq: immutable.IndexedSeq[A]`                              ###

Converts this traversable collection to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def toMap[T, U](implicit ev: <:<[A, (T, U)]): immutable.Map[T, U]`      ###

[use case]

Converts this set to a map. This method is unavailable unless the elements are
members of Tuple2, each ((T, U)) becoming a key-value pair in the map. Duplicate
keys will be overwritten by later keys: if this is an unordered collection,
which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this set.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


### `def toSet[B >: A]: immutable.Set[B]`                                    ###

Converts this traversable collection to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable collection.

* Definition Classes
  * TraversableProxyLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableProxyLike)


--------------------------------------------------------------------------------
    Concrete Value Members From scala.collection.generic.GenericSetTemplate
--------------------------------------------------------------------------------


### `def empty: Set[A]`                                                      ###

* Definition Classes
  * GenericSetTemplate

(defined at scala.collection.generic.GenericSetTemplate)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.generic.GenericTraversableTemplate
--------------------------------------------------------------------------------


### `def flatten[B](implicit asTraversable: (A) ⇒ GenTraversableOnce[B]): Set[B]` ###

[use case]

Converts this set of traversable collections into a set formed by the elements
of these traversable collections.

The resulting collection's type will be guided by the static type of set. For
example:

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
  * a new set resulting from concatenating all element sets.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def genericBuilder[B]: Builder[B, Set[B]]`                              ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Definition Classes
  * GenericTraversableTemplate

(defined at scala.collection.generic.GenericTraversableTemplate)


### `def transpose[B](implicit asTraversable: (A) ⇒ GenTraversableOnce[B]): Set[Set[B]]` ###

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


### `def unzip3[A1, A2, A3](implicit asTriple: (A) ⇒ (A1, A2, A3)): (Set[A1], Set[A2], Set[A3])` ###

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


### `def unzip[A1, A2](implicit asPair: (A) ⇒ (A1, A2)): (Set[A1], Set[A2])` ###

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
       Concrete Value Members From scala.collection.generic.Subtractable
--------------------------------------------------------------------------------


### `def -(elem1: A, elem2: A, elems: A*): Set[A]`                           ###

Creates a new collection from this collection with some elements removed.

This method takes two or more elements to be removed. Another overloaded variant
of this method handles the case where a single element is removed.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * a new collection that contains all elements of the current collection except
    one less occurrence of each of the given elements.

* Definition Classes
  * Subtractable

(defined at scala.collection.generic.Subtractable)


### `def --(xs: GenTraversableOnce[A]): Set[A]`                              ###

Creates a new collection from this collection by removing all elements of
another collection.

* xs
  * the collection containing the removed elements.
* returns
  * a new collection that contains all elements of the current collection except
    one less occurrence of each of the elements of `elems` .

* Definition Classes
  * Subtractable

(defined at scala.collection.generic.Subtractable)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SetProxy [A] to
    CollectionsHaveToParArray [SetProxy [A], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (SetProxy [A]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
