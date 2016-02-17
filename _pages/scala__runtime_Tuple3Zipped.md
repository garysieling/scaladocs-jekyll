
#                          scala.runtime.Tuple3Zipped                          #

```scala
final class Tuple3Zipped[El1, Repr1, El2, Repr2, El3, Repr3] extends AnyVal with ZippedTraversable3[El1, El2, El3]
```

* Source
  * [Tuple3Zipped.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/runtime/Tuple3Zipped.scala#L1)


--------------------------------------------------------------------------------
                        Value Members From scala.Any###
--------------------------------------------------------------------------------


### `final def ##(): Int`                                                    ###

Equivalent to `x.hashCode` except for boxed numeric types and `null` . For
numerics, it returns a hash value which is consistent with value equality: if
two value type instances compare as true, then ## will produce the same hash
value for each of them. For `null` returns a hashcode where `null.hashCode`
throws a `NullPointerException` .

* returns
  * a hash value consistent with ==

* Definition Classes
  * Any

(defined at scala.Any###)


--------------------------------------------------------------------------------
             Instance Constructors From scala.runtime.Tuple3Zipped
--------------------------------------------------------------------------------


### `new Tuple3Zipped(colls: (TraversableLike[El1, Repr1], IterableLike[El2, Repr2], IterableLike[El3, Repr3]))` ###

(defined at scala.runtime.Tuple3Zipped)


--------------------------------------------------------------------------------
                 Value Members From scala.runtime.Tuple3Zipped
--------------------------------------------------------------------------------


### `val colls: (TraversableLike[El1, Repr1], IterableLike[El2, Repr2], IterableLike[El3, Repr3])` ###

(defined at scala.runtime.Tuple3Zipped)


### `def exists(p: (El1, El2, El3) ⇒ Boolean): Boolean`                      ###

(defined at scala.runtime.Tuple3Zipped)


### `def filter[To1, To2, To3](f: (El1, El2, El3) ⇒ Boolean)(implicit cbf1: CanBuildFrom[Repr1, El1, To1], cbf2: CanBuildFrom[Repr2, El2, To2], cbf3: CanBuildFrom[Repr3, El3, To3]): (To1, To2, To3)` ###

(defined at scala.runtime.Tuple3Zipped)


### `def flatMap[B, To](f: (El1, El2, El3) ⇒ TraversableOnce[B])(implicit cbf: CanBuildFrom[Repr1, B, To]): To` ###

(defined at scala.runtime.Tuple3Zipped)


### `def forall(p: (El1, El2, El3) ⇒ Boolean): Boolean`                      ###

(defined at scala.runtime.Tuple3Zipped)


### `def foreach[U](f: (El1, El2, El3) ⇒ U): Unit`                           ###

* Definition Classes
  * Tuple3Zipped → ZippedTraversable3

(defined at scala.runtime.Tuple3Zipped)


### `def map[B, To](f: (El1, El2, El3) ⇒ B)(implicit cbf: CanBuildFrom[Repr1, B, To]): To` ###

(defined at scala.runtime.Tuple3Zipped)


--------------------------------------------------------------------------------
Value Members From Implicit scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable
--------------------------------------------------------------------------------


### `def ++:[B >: A, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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
    collection followed by all elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def ++:[B >: A, That](that: collection.TraversableOnce[B])(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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
  * a new collection which contains all elements of this collection followed by
    all elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def /:[B](z: B)(op: (B, (El1, El2, El3)) ⇒ B): B`                       ###

Applies a binary operator to a start value and all elements of this collection,
going left to right.

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
    collection, going left to right with the start value `z` on the left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def :\[B](z: B)(op: ((El1, El2, El3), B) ⇒ B): B`                       ###

Applies a binary operator to all elements of this collection and a start value,
going right to left.

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
    collection, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def addString(b: StringBuilder): StringBuilder`                         ###

Appends all elements of this collection to a string builder. The written text
consists of the string representations (w.r.t. the method `toString` ) of all
elements of this collection without any separator string.

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def addString(b: StringBuilder, sep: String): StringBuilder`            ###

Appends all elements of this collection to a string builder using a separator
string. The written text consists of the string representations (w.r.t. the
method `toString` ) of all elements of this collection, separated by the string
 `sep` .

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder` ###

Appends all elements of this collection to a string builder using start, end,
and separator strings. The written text begins with the string `start` and ends
with the string `end` . Inside, the string representations (w.r.t. the method
 `toString` ) of all elements of this collection are separated by the string
 `sep` .

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def aggregate[B](z: ⇒ B)(seqop: (B, (El1, El2, El3)) ⇒ B, combop: (B, B) ⇒ B): B` ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It is similar to
 `foldLeft` in that it doesn't require the result to be a supertype of the
element type. In addition, it allows parallel collections to be processed in
chunks, and then combines the intermediate results.

 `aggregate` splits the collection into partitions and processes each partition
by sequentially applying `seqop` , starting with `z` (like `foldLeft` ). Those
intermediate results are then combined by using `combop` (like `fold` ). The
implementation of this operation may operate on an arbitrary number of
collection partitions (even 1), so `combop` may be invoked an arbitrary number
of times (even 0).

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def collectFirst[B](pf: PartialFunction[(El1, El2, El3), B]): Option[B]` ###

Finds the first element of the collection for which the given partial function
is defined, and applies the partial function to it.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pf
  * the partial function
* returns
  * an option value containing pf applied to the first value for which it is
    defined, or `None` if none exists.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce

Example:

```scala
Seq("a", 1, 5L).collectFirst({ case x: Int => x*10 }) = Some(10)
```

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def collect[B, That](pf: PartialFunction[(El1, El2, El3), B])(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def companion: GenericCompanion[collection.Traversable]`                ###

The factory companion object that builds instances of class Traversable. (or its
 `Iterable` superclass where class Traversable is not a `Seq` .)

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * Traversable → GenTraversable → GenericTraversableTemplate

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with values of this collection. Copying will stop once either the end of the
current collection is reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with values of this collection, beginning at index `start` . Copying will stop
once either the end of the current collection is reached, or the end of the
target array is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this collection to an array. Fills the given array `xs`
with at most `len` elements of this collection, starting at position `start` .
Copying will stop once either the end of the current collection is reached, or
the end of the target array is reached, or `len` elements have been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this collection to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def count(p: ((El1, El2, El3)) ⇒ Boolean): Int`                         ###

Counts the number of elements in the collection which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def drop(n: Int): collection.Traversable[(El1, El2, El3)]`              ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this collection.
* returns
  * a collection consisting of all elements of this collection except the first
     `n` ones, or else the empty collection, if this collection has less than
     `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def dropWhile(p: ((El1, El2, El3)) ⇒ Boolean): collection.Traversable[(El1, El2, El3)]` ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this collection whose first element does not satisfy
    the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def filterNot(p: ((El1, El2, El3)) ⇒ Boolean): collection.Traversable[(El1, El2, El3)]` ###

Selects all elements of this collection which do not satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new collection consisting of all elements of this collection that do not
    satisfy the given predicate `p` . The order of the elements is preserved.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def find(p: ((El1, El2, El3)) ⇒ Boolean): Option[(El1, El2, El3)]`      ###

Finds the first element of the collection satisfying a predicate, if any.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the collection that
    satisfies `p` , or `None` if none exists.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def flatten[B](implicit asTraversable: ((El1, El2, El3)) ⇒ GenTraversableOnce[B]): collection.Traversable[B]` ###

[use case]

Converts this collection of traversable collections into a collection formed by
the elements of these traversable collections.

The resulting collection's type will be guided by the static type of collection.
For example:

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
  * a new collection resulting from concatenating all element collections.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def foldLeft[B](z: B)(op: (B, (El1, El2, El3)) ⇒ B): B`                 ###

Applies a binary operator to a start value and all elements of this collection,
going left to right.

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
    collection, going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this collection. Returns `z` if this
    collection is empty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def foldRight[B](z: B)(op: ((El1, El2, El3), B) ⇒ B): B`                ###

Applies a binary operator to all elements of this collection and a start value,
going right to left.

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
    collection, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this collection. Returns `z` if this
    collection is empty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def fold[A1 >: A](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

Folds the elements of this collection using the specified associative binary
operator.

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
     `z` , or `z` if this collection is empty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def genericBuilder[B]: Builder[B, collection.Traversable[B]]`           ###

The generic builder that builds instances of Traversable at arbitrary element
types.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def groupBy[K](f: ((El1, El2, El3)) ⇒ K): Map[K, collection.Traversable[(El1, El2, El3)]]` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def head: (El1, El2, El3)`                                              ###

Selects the first element of this collection.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def headOption: Option[(El1, El2, El3)]`                                ###

Optionally selects the first element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the first element of this collection if it is nonempty, `None` if it is
    empty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def init: collection.Traversable[(El1, El2, El3)]`                      ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection consisting of all elements of this collection except the last
    one.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def inits: collection.Iterator[collection.Traversable[(El1, El2, El3)]]` ###

Iterates over the inits of this collection. The first value will be this
collection and the final one will be an empty collection, with the intervening
values the results of successive applications of `init` .

* returns
  * an iterator over all the inits of this collection

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).inits = Iterator(List(1,2,3), List(1,2), List(1), Nil)
```

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def last: (El1, El2, El3)`                                              ###

Selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * The last element of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def lastOption: Option[(El1, El2, El3)]`                                ###

Optionally selects the last element.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the last element of this collection$ if it is nonempty, `None` if it is
    empty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def maxBy[B](f: ((El1, El2, El3)) ⇒ B)(implicit cmp: Ordering[B]): (El1, El2, El3)` ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection with the largest value measured by
    function f.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def minBy[B](f: ((El1, El2, El3)) ⇒ B)(implicit cmp: Ordering[B]): (El1, El2, El3)` ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this collection with the smallest value measured by
    function f.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this collection in a string using a separator string.

* sep
  * the separator string.
* returns
  * a string representation of this collection. In the resulting string the
    string representations (w.r.t. the method `toString` ) of all elements of
    this collection are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this collection in a string using start, end, and
separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this collection. The resulting string begins with
    the string `start` and ends with the string `end` . Inside, the string
    representations (w.r.t. the method `toString` ) of all elements of this
    collection are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def par: ParIterable[(El1, El2, El3)]`                                  ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * Parallelizable

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def partition(p: ((El1, El2, El3)) ⇒ Boolean): (collection.Traversable[(El1, El2, El3)], collection.Traversable[(El1, El2, El3)])` ###

Partitions this collection in two collections according to a predicate.

* p
  * the predicate on which to partition.
* returns
  * a pair of collections: the first collection consists of all elements that
    satisfy the predicate `p` and the second collection consists of all elements
    that don't. The relative order of the elements in the resulting collections
    is the same as in the original collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduceLeftOption[B >: A](op: (B, (El1, El2, El3)) ⇒ B): Option[B]`  ###

Optionally applies a binary operator to all elements of this collection, going
left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this collection
    is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduceLeft[B >: A](op: (B, (El1, El2, El3)) ⇒ B): B`                ###

Applies a binary operator to all elements of this collection, going left to
right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    collection, going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`               ###

Reduces the elements of this collection, if any, using the specified associative
binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * An option value containing result of applying reduce operator `op` between
    all the elements if the collection is nonempty, and `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduceRightOption[B >: A](op: ((El1, El2, El3), B) ⇒ B): Option[B]` ###

Optionally applies a binary operator to all elements of this collection, going
right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this
    collection is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduceRight[B >: A](op: ((El1, El2, El3), B) ⇒ B): B`               ###

Applies a binary operator to all elements of this collection, going right to
left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this
    collection, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                             ###

Reduces the elements of this collection using the specified associative binary
operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    collection is nonempty.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def repr: collection.Traversable[(El1, El2, El3)]`                      ###

The collection of type collection underlying this `TraversableLike` object. By
default this is implemented as the `TraversableLike` object itself, but this can
be overridden.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def scanLeft[B, That](z: B)(op: (B, (El1, El2, El3)) ⇒ B)(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def scanRight[B, That](z: B)(op: ((El1, El2, El3), B) ⇒ B)(implicit bf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[collection.Traversable[(El1, El2, El3)], B, That]): That` ###

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
  * a new collection containing the prefix scan of the elements in this
    collection

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def seq: collection.Traversable[(El1, El2, El3)]`                       ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * Traversable → GenTraversable → Parallelizable → TraversableOnce →
    GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def slice(from: Int, until: Int): collection.Traversable[(El1, El2, El3)]` ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection containing the elements greater than or equal to index `from`
    extending up to (but not including) index `until` of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def span(p: ((El1, El2, El3)) ⇒ Boolean): (collection.Traversable[(El1, El2, El3)], collection.Traversable[(El1, El2, El3)])` ###

Splits this collection into a prefix/suffix pair according to a predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a pair consisting of the longest prefix of this collection whose elements
    all satisfy `p` , and the rest of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def splitAt(n: Int): (collection.Traversable[(El1, El2, El3)], collection.Traversable[(El1, El2, El3)])` ###

Splits this collection into two at a given position. Note: `c splitAt n` is
equivalent to (but possibly more efficient than) `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of collections consisting of the first `n` elements of this
    collection, and the other elements.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def tail: collection.Traversable[(El1, El2, El3)]`                      ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a collection consisting of all elements of this collection except the first
    one.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the collection is empty.

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def tails: collection.Iterator[collection.Traversable[(El1, El2, El3)]]` ###

Iterates over the tails of this collection. The first value will be this
collection and the final one will be an empty collection, with the intervening
values the results of successive applications of `tail` .

* returns
  * an iterator over all the tails of this collection

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).tails = Iterator(List(1,2,3), List(2,3), List(3), Nil)
```

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def take(n: Int): collection.Traversable[(El1, El2, El3)]`              ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this collection.
* returns
  * a collection consisting only of the first `n` elements of this collection,
    or else the whole collection, if it has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def takeWhile(p: ((El1, El2, El3)) ⇒ Boolean): collection.Traversable[(El1, El2, El3)]` ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this collection whose elements all satisfy the
    predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toBuffer[B >: A]: Buffer[B]`                                        ###

Uses the contents of this collection to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toIndexedSeq: collection.immutable.IndexedSeq[(El1, El2, El3)]`     ###

Converts this collection to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toIterable: collection.Iterable[(El1, El2, El3)]`                   ###

Converts this collection to an iterable collection. Note that the choice of
target `Iterable` is lazy in this default implementation as this
 `TraversableOnce` may be lazy and unevaluated (i.e. it may be an iterator which
is only traversable once).

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toIterator: collection.Iterator[(El1, El2, El3)]`                   ###

Returns an Iterator over the elements in this collection. Will return the same
Iterator if this instance is already an Iterator.

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toList: List[(El1, El2, El3)]`                                      ###

Converts this collection to a list.

Note: will not terminate for infinite-sized collections.

* returns
  * a list containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toMap[T, U](implicit ev: <:<[(El1, El2, El3), (T, U)]): Map[T, U]`  ###

[use case]

Converts this collection to a map. This method is unavailable unless the
elements are members of Tuple2, each ((T, U)) becoming a key-value pair in the
map. Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toSeq: collection.Seq[(El1, El2, El3)]`                             ###

Converts this collection to a sequence. As with `toIterable` , it's lazy in this
default implementation, as this `TraversableOnce` may be lazy and unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toSet[B >: A]: Set[B]`                                              ###

Converts this collection to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toStream: Stream[(El1, El2, El3)]`                                  ###

Converts this collection to a stream.

* returns
  * a stream containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toTraversable: collection.Traversable[(El1, El2, El3)]`             ###

Converts this collection to an unspecified Traversable. Will return the same
collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def toVector: Vector[(El1, El2, El3)]`                                  ###

Converts this collection to a Vector.

Note: will not terminate for infinite-sized collections.

* returns
  * a vector containing all elements of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def transpose[B](implicit asTraversable: ((El1, El2, El3)) ⇒ GenTraversableOnce[B]): collection.Traversable[collection.Traversable[B]]` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
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

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def unzip3[A1, A2, A3](implicit asTriple: ((El1, El2, El3)) ⇒ (A1, A2, A3)): (collection.Traversable[A1], collection.Traversable[A2], collection.Traversable[A3])` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def unzip[A1, A2](implicit asPair: ((El1, El2, El3)) ⇒ (A1, A2)): (collection.Traversable[A1], collection.Traversable[A2])` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def view(from: Int, until: Int): TraversableView[(El1, El2, El3), collection.Traversable[(El1, El2, El3)]]` ###

Creates a non-strict view of a slice of this collection.

Note: the difference between `view` and `slice` is that `view` produces a view
of the current collection, whereas `slice` produces a new collection.

Note: `view(from, to)` is equivalent to `view.slice(from, to)`

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* from
  * the index of the first element of the view
* until
  * the index of the element following the view
* returns
  * a non-strict view of a slice of this collection, starting at index `from`
    and extending up to (but not including) index `until` .

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def view: TraversableView[(El1, El2, El3), collection.Traversable[(El1, El2, El3)]]` ###

Creates a non-strict view of this collection.

* returns
  * a non-strict view of this collection.

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)


### `def withFilter(p: ((El1, El2, El3)) ⇒ Boolean): FilterMonadic[(El1, El2, El3), collection.Traversable[(El1, El2, El3)]]` ###

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

* Implicit information
  * This member is added by an implicit conversion from Tuple3Zipped [El1, Repr1,
    El2, Repr2, El3, Repr3] to Traversable [(El1, El2, El3)] performed by method
    zippedTraversable3ToTraversable in scala.runtime.ZippedTraversable3.
* Definition Classes
  * TraversableLike → FilterMonadic
(added by implicit convertion: scala.runtime.ZippedTraversable3.zippedTraversable3ToTraversable)
