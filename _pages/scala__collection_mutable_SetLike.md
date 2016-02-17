
#                       scala.collection.mutable.SetLike                       #

```scala
trait SetLike[A, +This <: SetLike[A, This] with Set[A]] extends collection.SetLike[A, This] with Scriptable[A] with Builder[A, This] with Growable[A] with Shrinkable[A] with Cloneable[Set[A]] with Parallelizable[A, ParSet[A]]
```

A template trait for mutable sets of type `mutable.Set[A]` .

This trait provides most of the operations of a `mutable.Set` independently of
its representation. It is typically inherited by concrete implementations of
sets.

To implement a concrete mutable set, you need to provide implementations of the
following methods:

```scala
def contains(elem: A): Boolean
def iterator: Iterator[A]
def += (elem: A): this.type
def -= (elem: A): this.type
```

If you wish that methods like `take` , `drop` , `filter` return the same kind of
set, you should also override:

```scala
def empty: This
```

It is also good idea to override methods `foreach` and `size` for efficiency.

* A
  * the type of the elements of the set
* This
  * the type of the set itself.

* Self Type
  * SetLike [A, This]
* Source
  * [SetLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/SetLike.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Self = This`                                                       ###

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
            Abstract Value Members From scala.collection.GenSetLike
--------------------------------------------------------------------------------


### `abstract def seq: collection.Set[A]`                                    ###

* Definition Classes
  * GenSetLike → Parallelizable → GenTraversableOnce

(defined at scala.collection.GenSetLike)


--------------------------------------------------------------------------------
            Concrete Value Members From scala.collection.GenSetLike
--------------------------------------------------------------------------------


### `def &(that: GenSet[A]): This`                                           ###

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


### `def &~(that: GenSet[A]): This`                                          ###

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


### `def intersect(that: GenSet[A]): This`                                   ###

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


### `def |(that: GenSet[A]): This`                                           ###

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


### `def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this mutable set to an array. Fills the given array `xs`
with at most `len` elements of this mutable set, starting at position `start` .
Copying will stop once either the end of the current mutable set is reached, or
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


### `def drop(n: Int): This`                                                 ###

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


### `def dropRight(n: Int): This`                                            ###

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


### `def exists(p: (A) ⇒ Boolean): Boolean`                                  ###

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


### `def find(p: (A) ⇒ Boolean): Option[A]`                                  ###

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


### `def foldRight[B](z: B)(op: (A, B) ⇒ B): B`                              ###

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


### `def forall(p: (A) ⇒ Boolean): Boolean`                                  ###

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


### `def foreach[U](f: (A) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of this mutable set.

Note: this method underlies the implementation of most other bulk operations.
Subclasses should re-implement this method if a more efficient implementation
exists.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike → TraversableOnce →
    GenTraversableOnce → FilterMonadic

(defined at scala.collection.IterableLike)


### `def grouped(size: Int): Iterator[This]`                                 ###

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


### `def reduceRight[B >: A](op: (A, B) ⇒ B): B`                             ###

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


### `def sameElements[B >: A](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this mutable set.

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


### `def slice(from: Int, until: Int): This`                                 ###

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


### `def sliding(size: Int): Iterator[This]`                                 ###

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


### `def sliding(size: Int, step: Int): Iterator[This]`                      ###

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


### `def take(n: Int): This`                                                 ###

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


### `def takeRight(n: Int): This`                                            ###

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


### `def takeWhile(p: (A) ⇒ Boolean): This`                                  ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(defined at scala.collection.IterableLike)


### `def thisCollection: collection.Iterable[A]`                             ###

The underlying collection seen as an instance of `Iterable` . By default this is
implemented as the current collection object itself, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toCollection(repr: This): collection.Iterable[A]`                   ###

A conversion from collections of type `Repr` to `Iterable` objects. By default
this is implemented as just a cast, but this can be overridden.

* Attributes
  * protected[this]
* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def toIterable: collection.Iterable[A]`                                 ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def toStream: immutable.Stream[A]`                                      ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(defined at scala.collection.IterableLike)


### `def view(from: Int, until: Int): IterableView[A, This]`                 ###

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


### `def view: IterableView[A, This]`                                        ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Definition Classes
  * IterableLike → TraversableLike

(defined at scala.collection.IterableLike)


### `def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[This, (A1, B), That]): That` ###

[use case]

Returns a mutable set formed from this mutable set and another iterable
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
  * the element to be used to fill up the result if this mutable set is shorter
    than `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    mutable set.
* returns
  * a new mutable set containing pairs consisting of corresponding elements of
    this mutable set and `that` . The length of the returned collection is the
    maximum of the lengths of this mutable set and `that` . If this mutable set
    is shorter than `that` , `thisElem` values are used to pad the result. If
     `that` is shorter than this mutable set, `thatElem` values are used to pad
    the result.

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


### `def zipWithIndex[A1 >: A, That](implicit bf: CanBuildFrom[This, (A1, Int), That]): That` ###

[use case]

Zips this mutable set with its indices.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * A new mutable set containing pairs consisting of all elements of this
    mutable set paired with their index. Indices start at `0` .

* Definition Classes
  * IterableLike → GenIterableLike

Example:

```scala
List("a", "b", "c").zipWithIndex = List(("a", 0), ("b", 1), ("c", 2))
```

(defined at scala.collection.IterableLike)


### `def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[This, (A1, B), That]): That` ###

[use case]

Returns a mutable set formed from this mutable set and another iterable
collection by combining corresponding elements in pairs. If one of the two
collections is longer than the other, its remaining elements are ignored.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new mutable set containing pairs consisting of corresponding elements of
    this mutable set and `that` . The length of the returned collection is the
    minimum of the lengths of this mutable set and `that` .

* Definition Classes
  * IterableLike → GenIterableLike

(defined at scala.collection.IterableLike)


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
              Abstract Value Members From scala.collection.SetLike
--------------------------------------------------------------------------------


### `abstract def contains(elem: A): Boolean`                                ###

Tests if some element is contained in this set.

* elem
  * the element to test for membership.
* returns
  * `true` if `elem` is contained in this set, `false` otherwise.

* Definition Classes
  * SetLike → GenSetLike

(defined at scala.collection.SetLike)


--------------------------------------------------------------------------------
              Concrete Value Members From scala.collection.SetLike
--------------------------------------------------------------------------------


### `abstract def empty: This`                                               ###

The empty set of the same type as this set

* returns
  * an empty set of type `This` .

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


### `def diff(that: GenSet[A]): This`                                        ###

Computes the difference of this set and another set.

* that
  * the set of elements to exclude.
* returns
  * a set containing those elements of this set that are not also contained in
    the given set `that` .

* Definition Classes
  * SetLike → GenSetLike

(defined at scala.collection.SetLike)


### `def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[This, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this mutable
set.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new mutable set resulting from applying the given function `f` to each
    element of this mutable set and collecting the results.

* Definition Classes
  * SetLike → TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.SetLike)


### `def subsets(len: Int): Iterator[This]`                                  ###

An iterator over all subsets of this set of the given size. If the requested
size is impossible, an empty iterator is returned.

* len
  * the size of the subsets.
* returns
  * the iterator.

* Definition Classes
  * SetLike

(defined at scala.collection.SetLike)


### `def toBuffer[A1 >: A]: Buffer[A1]`                                      ###

Uses the contents of this set to create a new mutable buffer.

* returns
  * a buffer containing all elements of this set.

* Definition Classes
  * SetLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.SetLike)


### `def union(that: GenSet[A]): This`                                       ###

Computes the union between of set and another set.

* that
  * the set to form the union with.
* returns
  * a new set consisting of all elements that are in this set or in the given
    set `that` .

* Definition Classes
  * SetLike → GenSetLike

(defined at scala.collection.SetLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.TraversableLike
--------------------------------------------------------------------------------


### `def ++:[B >: A, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[This, B, That]): That` ###

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


### `def ++:[B >: A, That](that: TraversableOnce[B])(implicit bf: CanBuildFrom[This, B, That]): That` ###

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
  * a new mutable set which contains all elements of this mutable set followed
    by all elements of `that` .

* Definition Classes
  * TraversableLike

(defined at scala.collection.TraversableLike)


### `def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[This, B, That]): That` ###

[use case]

Returns a new mutable set containing the elements from the left hand operand
followed by the elements from the right hand operand. The element type of the
mutable set is the most specific superclass encompassing the element types of
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
  * a new mutable set which contains all elements of this mutable set followed
    by all elements of `that` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def collect[B, That](pf: PartialFunction[A, B])(implicit bf: CanBuildFrom[This, B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
mutable set on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the mutable set.
* returns
  * a new mutable set resulting from applying the given partial function `pf` to
    each element on which it is defined and collecting the results. The order of
    the elements is preserved.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def dropWhile(p: (A) ⇒ Boolean): This`                                  ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this traversable collection whose first element does
    not satisfy the predicate `p` .

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def filter(p: (A) ⇒ Boolean): This`                                     ###

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


### `def filterNot(p: (A) ⇒ Boolean): This`                                  ###

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


### `def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[This, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this mutable
set and using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of mutable
set. This might cause unexpected results sometimes. For example:

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
  * a new mutable set resulting from applying the given collection-valued
    function `f` to each element of this mutable set and concatenating the
    results.

* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(defined at scala.collection.TraversableLike)


### `def groupBy[K](f: (A) ⇒ K): immutable.Map[K, This]`                     ###

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


### `def init: This`                                                         ###

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


### `def inits: Iterator[This]`                                              ###

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


### `def partition(p: (A) ⇒ Boolean): (This, This)`                          ###

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


### `def repr: This`                                                         ###

The collection of type traversable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Definition Classes
  * TraversableLike → GenTraversableLike

(defined at scala.collection.TraversableLike)


### `def scanLeft[B, That](z: B)(op: (B, A) ⇒ B)(implicit bf: CanBuildFrom[This, B, That]): That` ###

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


### `def scanRight[B, That](z: B)(op: (A, B) ⇒ B)(implicit bf: CanBuildFrom[This, B, That]): That` ###

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


### `def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[This, B, That]): That` ###

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


### `def span(p: (A) ⇒ Boolean): (This, This)`                               ###

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


### `def splitAt(n: Int): (This, This)`                                      ###

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


### `def tail: This`                                                         ###

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


### `def tails: Iterator[This]`                                              ###

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


### `def toTraversable: collection.Traversable[A]`                           ###

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


### `def withFilter(p: (A) ⇒ Boolean): FilterMonadic[A, This]`               ###

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


### `def /:[B](z: B)(op: (B, A) ⇒ B): B`                                     ###

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


### `def :\[B](z: B)(op: (A, B) ⇒ B): B`                                     ###

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


### `def addString(b: scala.StringBuilder, start: String, sep: String, end: String): scala.StringBuilder` ###

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


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this mutable set to an array. Fills the given array `xs`
with values of this mutable set. Copying will stop once either the end of the
current mutable set is reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this mutable set to an array. Fills the given array `xs`
with values of this mutable set, beginning at index `start` . Copying will stop
once either the end of the current mutable set is reached, or the end of the
target array is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this traversable or iterator to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Definition Classes
  * TraversableOnce

(defined at scala.collection.TraversableOnce)


### `def count(p: (A) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the traversable or iterator which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def foldLeft[B](z: B)(op: (B, A) ⇒ B): B`                               ###

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
  * the first element of this mutable set with the largest value measured by
    function f.

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
  * the first element of this mutable set with the smallest value measured by
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


### `def reduceLeftOption[B >: A](op: (B, A) ⇒ B): Option[B]`                ###

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


### `def reduceLeft[B >: A](op: (B, A) ⇒ B): B`                              ###

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


### `def reduceRightOption[B >: A](op: (A, B) ⇒ B): Option[B]`               ###

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


### `def toIndexedSeq: immutable.IndexedSeq[A]`                              ###

Converts this traversable or iterator to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toMap[T, U](implicit ev: <:<[A, (T, U)]): immutable.Map[T, U]`      ###

[use case]

Converts this mutable set to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this mutable set.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


### `def toSet[B >: A]: immutable.Set[B]`                                    ###

Converts this traversable or iterator to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this traversable or iterator.

* Definition Classes
  * TraversableOnce → GenTraversableOnce

(defined at scala.collection.TraversableOnce)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `def ++=(xs: TraversableOnce[A]): SetLike.this.type`                     ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

* Definition Classes
  * Growable

(defined at scala.collection.generic.Growable)


### `def +=(elem1: A, elem2: A, elems: A*): SetLike.this.type`               ###

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
        Concrete Value Members From scala.collection.generic.Shrinkable
--------------------------------------------------------------------------------


### `def --=(xs: TraversableOnce[A]): SetLike.this.type`                     ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

* Definition Classes
  * Shrinkable

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: A, elem2: A, elems: A*): SetLike.this.type`               ###

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
          Concrete Value Members From scala.collection.mutable.Builder
--------------------------------------------------------------------------------


### `def mapResult[NewTo](f: (This) ⇒ NewTo): Builder[A, NewTo]`             ###

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
          Abstract Value Members From scala.collection.mutable.SetLike
--------------------------------------------------------------------------------


### `abstract def +=(elem: A): SetLike.this.type`                            ###

Adds a single element to the set.

* elem
  * the element to be added.
* returns
  * the builder itself.

* Definition Classes
  * SetLike → Builder → Growable

(defined at scala.collection.mutable.SetLike)


### `abstract def -=(elem: A): SetLike.this.type`                            ###

Removes a single element from this mutable set.

* elem
  * the element to remove.
* returns
  * the mutable set itself

* Definition Classes
  * SetLike → Shrinkable

(defined at scala.collection.mutable.SetLike)


--------------------------------------------------------------------------------
          Concrete Value Members From scala.collection.mutable.SetLike
--------------------------------------------------------------------------------


### `def +(elem: A): This`                                                   ###

Creates a new set consisting of all the elements of this set and `elem` .

Note that duplicates (elements for which `equals` yields true) will be removed,
but it is not specified whether it will be an element of this set or a newly
added element.

* elem
  * the element to add.
* returns
  * a new set consisting of elements of this set and `elem` .

* Definition Classes
  * SetLike → SetLike → GenSetLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `+` creates a new set. Use `+=` to add an
    element to this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def +(elem1: A, elem2: A, elems: A*): This`                             ###

Creates a new set consisting of all the elements of this set and two or more
specified elements.

Note that duplicates (elements for which `equals` yields true) will be removed,
but it is not specified whether it will be an element of this set or a newly
added element.

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * a new set consisting of all the elements of this set, `elem1` , `elem2` and
    those in `elems` .

* Definition Classes
  * SetLike → SetLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `+` creates a new set. Use `+=` to add an
    element to this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def ++(xs: GenTraversableOnce[A]): This`                                ###

Creates a new set consisting of all the elements of this set and those provided
by the specified traversable object.

Note that duplicates (elements for which `equals` yields true) will be removed,
but it is not specified whether it will be an element of this set or a newly
added element.

* xs
  * the traversable object.
* returns
  * a new set consisting of elements of this set and those in `xs` .

* Definition Classes
  * SetLike → SetLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `++` creates a new set. Use `++=` to add
    elements to this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def -(elem: A): This`                                                   ###

Creates a new set consisting of all the elements of this set except `elem` .

* elem
  * the element to remove.
* returns
  * a new set consisting of all the elements of this set except `elem` .

* Definition Classes
  * SetLike → SetLike → Subtractable → GenSetLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `-` creates a new set. Use `-=` to remove an
    element from this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def -(elem1: A, elem2: A, elems: A*): This`                             ###

Creates a new set consisting of all the elements of this set except the two or
more specified elements.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * a new set consisting of all the elements of this set except `elem1` ,
     `elem2` and `elems` .

* Definition Classes
  * SetLike → Subtractable
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `-` creates a new set. Use `-=` to remove an
    element from this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def --(xs: GenTraversableOnce[A]): This`                                ###

Creates a new set consisting of all the elements of this set except those
provided by the specified traversable object.

* xs
  * the traversable object.
* returns
  * a new set consisting of all the elements of this set except elements from
     `xs` .

* Definition Classes
  * SetLike → Subtractable
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.8.0)_  `--` creates a new set. Use `--=` to remove
    elements from this set and return that set itself.

(defined at scala.collection.mutable.SetLike)


### `def add(elem: A): Boolean`                                              ###

Adds an element to this mutable set.

* elem
  * the element to be added
* returns
  * `true` if the element was not yet present in the set, `false` otherwise.

(defined at scala.collection.mutable.SetLike)


### `def newBuilder: Builder[A, This]`                                       ###

A common implementation of `newBuilder` for all mutable sets in terms of
 `empty` . Overrides the implementation in `collection.SetLike` for better
efficiency.

* Attributes
  * protected[this]
* Definition Classes
  * SetLike → SetLike → TraversableLike → HasNewBuilder

(defined at scala.collection.mutable.SetLike)


### `def parCombiner: Combiner[A, ParSet[A]]`                                ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * SetLike → SetLike → TraversableLike → Parallelizable

(defined at scala.collection.mutable.SetLike)


### `def remove(elem: A): Boolean`                                           ###

Removes an element from this set.

* elem
  * The element to be removed.
* returns
  * `true` if the element was previously present in the set, `false` otherwise.

(defined at scala.collection.mutable.SetLike)


### `def retain(p: (A) ⇒ Boolean): Unit`                                     ###

Removes all elements from the set for which do not satisfy a predicate.

* p
  * the predicate used to test elements. Only elements for which `p` returns
     `true` are retained in the set; all others are removed.

(defined at scala.collection.mutable.SetLike)


### `def toSeq: collection.Seq[A]`                                           ###

Converts this mutable set to a sequence.

 `Note` : assumes a fast `size` method. Subclasses should override if this is
not true.

* returns
  * a sequence containing all elements of this mutable set.

* Definition Classes
  * SetLike → SetLike → TraversableOnce → GenTraversableOnce

(defined at scala.collection.mutable.SetLike)


### `def update(elem: A, included: Boolean): Unit`                           ###

Updates the presence of a single element in this set.

This method allows one to add or remove an element `elem` from this set
depending on the value of parameter `included` . Typically, one would use the
following syntax:

```scala
set(elem) = true  // adds element
set(elem) = false // removes element
```

* elem
  * the element to be added or removed
* included
  * a flag indicating whether element should be included or excluded.

(defined at scala.collection.mutable.SetLike)


--------------------------------------------------------------------------------
         Deprecated Value Members From scala.collection.mutable.SetLike
--------------------------------------------------------------------------------


### `def <<(cmd: Message[A]): Unit`                                          ###

Send a message to this scriptable object.

* cmd
  * the message to send.

* Definition Classes
  * SetLike → Scriptable
* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Scripting is deprecated.
* Exceptions thrown
  * UnsupportedOperationException if the message was not understood.

(defined at scala.collection.mutable.SetLike)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from SetLike [A, This] to
    CollectionsHaveToParArray [SetLike [A, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (SetLike [A, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
