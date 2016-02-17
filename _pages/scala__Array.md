
#                                 scala.Array                                 #

```scala
final class Array[T] extends java.io.Serializable with java.lang.Cloneable
```

Arrays are mutable, indexed collections of values. `Array[T]` is Scala's
representation for Java's `T[]` .

```scala
val numbers = Array(1, 2, 3, 4)
val first = numbers(0) // read the first element
numbers(3) = 100 // replace the 4th array element with 100
val biggerNumbers = numbers.map(_ * 2) // multiply all numbers by two
```

Arrays make use of two common pieces of Scala syntactic sugar, shown on lines 2
and 3 of the above example code. Line 2 is translated into a call to
 `apply(Int)` , while line 3 is translated into a call to `update(Int, T)` .

Two implicit conversions exist in scala.Predef that are frequently applied to
arrays: a conversion to scala.collection.mutable.ArrayOps (shown on line 4 of
the example above) and a conversion to scala.collection.mutable.WrappedArray (a
subtype of scala.collection.Seq). Both types make available many of the standard
operations found in the Scala collections API. The conversion to `ArrayOps` is
temporary, as all operations defined on `ArrayOps` return an `Array` , while the
conversion to `WrappedArray` is permanent as all operations return a
 `WrappedArray` .

The conversion to `ArrayOps` takes priority over the conversion to
 `WrappedArray` . For instance, consider the following code:

```scala
val arr = Array(1, 2, 3)
val arrReversed = arr.reverse
val seqReversed : Seq[Int] = arr.reverse
```

Value `arrReversed` will be of type `Array[Int]` , with an implicit conversion
to `ArrayOps` occurring to perform the `reverse` operation. The value of
 `seqReversed` , on the other hand, will be computed by converting to
 `WrappedArray` first and invoking the variant of `reverse` that returns another
 `WrappedArray` .

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)
* Version
  * 1.0
* See also
  * ["The Scala 2.8 Collections' API"](http://docs.scala-lang.org/overviews/collections/arrays.html)
    section on `Array` by Martin Odersky for more information.
    ["Scala 2.8 Arrays"](http://docs.scala-lang.org/sips/completed/scala-2-8-arrays.html)
    the Scala Improvement Document detailing arrays since Scala 2.8.
    [Scala Language Specification](http://www.scala-lang.org/files/archive/spec/2.11/),
    for in-depth information on the transformations the Scala compiler makes on
    Arrays (Sections 6.6 and 6.15 respectively.)


--------------------------------------------------------------------------------
                     Instance Constructors From scala.Array
--------------------------------------------------------------------------------


### `new Array(_length: Int)`                                                ###

(defined at scala.Array)


--------------------------------------------------------------------------------
                         Value Members From scala.Array
--------------------------------------------------------------------------------


### `def apply(i: Int): T`                                                   ###

The element at given index.

Indices start at `0` ; `xs.apply(0)` is the first element of array `xs` . Note
the indexing syntax `xs(i)` is a shorthand for `xs.apply(i)` .

* i
  * the index
* returns
  * the element at the given index

* Exceptions thrown
  * ArrayIndexOutOfBoundsException if `i < 0` or `length <= i`

(defined at scala.Array)


### `def update(i: Int, x: T): Unit`                                         ###

Update the element at given index.

Indices start at `0` ; `xs.update(i, x)` replaces the i <sup>th</sup> element in
the array. Note the syntax `xs(i) = x` is a shorthand for `xs.update(i, x)` .

* i
  * the index
* x
  * the value to be written at index `i`

* Exceptions thrown
  * ArrayIndexOutOfBoundsException if `i < 0` or `length <= i`

(defined at scala.Array)


--------------------------------------------------------------------------------
           Value Members From Implicit scala.Predef.ArrayCharSequence
--------------------------------------------------------------------------------


### `def charAt(index: Int): Char`                                           ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to
    ArrayCharSequence performed by method ArrayCharSequence in scala.Predef.
    This conversion will take place only if T is Char (T =:= Char).
* Definition Classes
  * ArrayCharSequence → CharSequence

(added by implicit convertion: scala.Predef.ArrayCharSequence)


### `def chars(): IntStream`                                                 ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to
    ArrayCharSequence performed by method ArrayCharSequence in scala.Predef.
    This conversion will take place only if T is Char (T =:= Char).
* Definition Classes
  * CharSequence

(added by implicit convertion: scala.Predef.ArrayCharSequence)


### `def codePoints(): IntStream`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to
    ArrayCharSequence performed by method ArrayCharSequence in scala.Predef.
    This conversion will take place only if T is Char (T =:= Char).
* Definition Classes
  * CharSequence

(added by implicit convertion: scala.Predef.ArrayCharSequence)


### `def subSequence(start: Int, end: Int): CharSequence`                    ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to
    ArrayCharSequence performed by method ArrayCharSequence in scala.Predef.
    This conversion will take place only if T is Char (T =:= Char).
* Definition Classes
  * ArrayCharSequence → CharSequence

(added by implicit convertion: scala.Predef.ArrayCharSequence)


--------------------------------------------------------------------------------
            Value Members From Implicit scala.Predef.genericArrayOps
--------------------------------------------------------------------------------


### `def ++:[B >: A, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

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
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * a new collection of type `That` which contains all elements of this mutable
    indexed sequence followed by all elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def ++:[B >: A, That](that: collection.TraversableOnce[B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

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
  * a new array which contains all elements of this array followed by all
    elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Returns a new array containing the elements from the left hand operand followed
by the elements from the right hand operand. The element type of the array is
the most specific superclass encompassing the element types of the two operands.

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
  * a new array which contains all elements of this array followed by all
    elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def +:[B >: A, That](elem: B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

A copy of the array with an element prepended.

Note that :-ending operators are right associative (see example). A mnemonic for
 `+:` vs. `:+` is: the COLon goes on the COLlection side.

Also, the original array is not modified, so you will want to capture the
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
  * a new array consisting of `elem` followed by all elements of this array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def +:[B >: T](elem: B)(implicit arg0: ClassTag[B]): Array[B]`          ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def /:[B](z: B)(op: (B, T) ⇒ B): B`                                     ###

Applies a binary operator to a start value and all elements of this mutable
indexed sequence, going left to right.

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

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going left to right with the start value `z` on the left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def :+[B >: A, That](elem: B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

A copy of this array with an element appended.

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
  * a new array consisting of all elements of this array followed by `elem` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def :+[B >: T](elem: B)(implicit arg0: ClassTag[B]): Array[B]`          ###

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def :\[B](z: B)(op: (T, B) ⇒ B): B`                                     ###

Applies a binary operator to all elements of this mutable indexed sequence and a
start value, going right to left.

Note: `:\` is alternate syntax for `foldRight` ; `xs :\ z` is the same as
 `xs foldRight z` .

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
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def addString(b: StringBuilder): StringBuilder`                         ###

Appends all elements of this mutable indexed sequence to a string builder. The
written text consists of the string representations (w.r.t. the method
 `toString` ) of all elements of this mutable indexed sequence without any
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

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def addString(b: StringBuilder, sep: String): StringBuilder`            ###

Appends all elements of this mutable indexed sequence to a string builder using
a separator string. The written text consists of the string representations
(w.r.t. the method `toString` ) of all elements of this mutable indexed
sequence, separated by the string `sep` .

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
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder` ###

Appends all elements of this mutable indexed sequence to a string builder using
start, end, and separator strings. The written text begins with the string
 `start` and ends with the string `end` . Inside, the string representations
(w.r.t. the method `toString` ) of all elements of this mutable indexed sequence
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

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def aggregate[B](z: ⇒ B)(seqop: (B, T) ⇒ B, combop: (B, B) ⇒ B): B`     ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It is similar to
 `foldLeft` in that it doesn't require the result to be a supertype of the
element type. In addition, it allows parallel collections to be processed in
chunks, and then combines the intermediate results.

 `aggregate` splits the mutable indexed sequence into partitions and processes
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

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def canEqual(that: Any): Boolean`                                       ###

Method called from equality methods, so that user-defined subclasses can refuse
to be equal to other collections of the same kind.

* that
  * The object with which this mutable indexed sequence should be compared
* returns
  * `true` , if this mutable indexed sequence can possibly equal `that` ,
     `false` otherwise. The test takes into consideration only the run-time
    types of objects but ignores their elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike → Equals

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def collectFirst[B](pf: PartialFunction[T, B]): Option[B]`              ###

Finds the first element of the mutable indexed sequence for which the given
partial function is defined, and applies the partial function to it.

* pf
  * the partial function
* returns
  * an option value containing pf applied to the first value for which it is
    defined, or `None` if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce

Example:

```scala
Seq("a", 1, 5L).collectFirst({ case x: Int => x*10 }) = Some(10)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def collect[B, That](pf: PartialFunction[T, B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Builds a new collection by applying a partial function to all elements of this
array on which the function is defined.

* B
  * the element type of the returned collection.
* pf
  * the partial function which filters and maps the array.
* returns
  * a new array resulting from applying the given partial function `pf` to each
    element on which it is defined and collecting the results. The order of the
    elements is preserved.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def combinations(n: Int): collection.Iterator[Array[T]]`                ###

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
    mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

Example:

```scala
"abbbc".combinations(2) = Iterator(ab, ac, bb, bc)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def containsSlice[B](that: GenSeq[B]): Boolean`                         ###

Tests whether this mutable indexed sequence contains a given sequence as a
slice.

* that
  * the sequence to test
* returns
  * `true` if this mutable indexed sequence contains a slice with the same
    elements as `that` , otherwise `false` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def contains[A1 >: A](elem: A1): Boolean`                               ###

Tests whether this mutable indexed sequence contains a given value as an
element.

* elem
  * the element to test.
* returns
  * `true` if this mutable indexed sequence has an element that is equal (as
    determined by `==` ) to `elem` , `false` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this array to an array. Fills the given array `xs` with
values of this array. Copying will stop once either the end of the current array
is reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this array to an array. Fills the given array `xs` with
values of this array, beginning at index `start` . Copying will stop once either
the end of the current array is reached, or the end of the target array is
reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def copyToArray[U >: T](xs: Array[U], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this array to an array. Fills the given array `xs` with
at most `len` elements of this array, starting at position `start` . Copying
will stop once either the end of the current array is reached, or the end of the
target array is reached, or `len` elements have been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps → IndexedSeqOptimized → IterableLike → TraversableLike →
    TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this mutable indexed sequence to a buffer.

* dest
  * The buffer to which elements are copied.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def corresponds[B](that: GenSeq[B])(p: (T, B) ⇒ Boolean): Boolean`      ###

Tests whether every element of this mutable indexed sequence relates to the
corresponding element of another sequence by satisfying a test predicate.

* B
  * the type of the elements of `that`
* that
  * the other sequence
* p
  * the test predicate, which relates elements from both sequences
* returns
  * `true` if both sequences have the same length and `p(x, y)` is `true` for
    all corresponding elements `x` of this mutable indexed sequence and `y` of
     `that` , otherwise `false` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def count(p: (T) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the mutable indexed sequence which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def deep: collection.IndexedSeq[Any]`                                   ###

Creates a possible nested `IndexedSeq` which consists of all the elements of
this array. If the elements are arrays themselves, the `deep` transformation is
applied recursively to them. The `stringPrefix` of the `IndexedSeq` is "Array",
hence the `IndexedSeq` prints like an array with all its elements shown, and the
same recursively for any subarrays.

Example:

```scala
Array(Array(1, 2), Array(3, 4)).deep.toString
```

prints: `Array(Array(1, 2), Array(3, 4))`

* returns
  * An possibly nested indexed sequence of consisting of all the elements of the
    array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def diff[B >: A](that: GenSeq[B]): Array[T]`                            ###

[use case]

Computes the multiset difference between this array and another sequence.

* that
  * the sequence of elements to remove
* returns
  * a new array which contains all elements of this array except some of
    occurrences of elements that also appear in `that` . If an element value
     `x` appears _n_ times in `that` , then the first _n_ occurrences of `x`
    will not form part of the result, but any following occurrences will.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def distinct: Array[T]`                                                 ###

Builds a new mutable indexed sequence from this mutable indexed sequence without
any duplicate elements.

* returns
  * A new mutable indexed sequence which contains the first occurrence of every
    element of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def drop(n: Int): Array[T]`                                             ###

Selects all elements except first _n_ ones.

* n
  * the number of elements to drop from this mutable indexed sequence.
* returns
  * a mutable indexed sequence consisting of all elements of this mutable
    indexed sequence except the first `n` ones, or else the empty mutable
    indexed sequence, if this mutable indexed sequence has less than `n`
    elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def dropRight(n: Int): Array[T]`                                        ###

Selects all elements except last _n_ ones.

* n
  * The number of elements to take
* returns
  * a mutable indexed sequence consisting of all elements of this mutable
    indexed sequence except the last `n` ones, or else the empty mutable indexed
    sequence, if this mutable indexed sequence has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def dropWhile(p: (T) ⇒ Boolean): Array[T]`                              ###

Drops longest prefix of elements that satisfy a predicate.

* returns
  * the longest suffix of this mutable indexed sequence whose first element does
    not satisfy the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def endsWith[B](that: GenSeq[B]): Boolean`                              ###

Tests whether this mutable indexed sequence ends with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this mutable indexed sequence has `that` as a suffix, `false`
    otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def exists(p: (T) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for at least one element of this mutable indexed
sequence.

* p
  * the predicate used to test elements.
* returns
  * `false` if this mutable indexed sequence is empty, otherwise `true` if the
    given predicate `p` holds for some of the elements of this mutable indexed
    sequence, otherwise `false`

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def filter(p: (T) ⇒ Boolean): Array[T]`                                 ###

Selects all elements of this mutable indexed sequence which satisfy a predicate.

* p
  * the predicate used to test elements.
* returns
  * a new mutable indexed sequence consisting of all elements of this mutable
    indexed sequence that satisfy the given predicate `p` . The order of the
    elements is preserved.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def filterNot(p: (T) ⇒ Boolean): Array[T]`                              ###

Selects all elements of this mutable indexed sequence which do not satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * a new mutable indexed sequence consisting of all elements of this mutable
    indexed sequence that do not satisfy the given predicate `p` . The order of
    the elements is preserved.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def find(p: (T) ⇒ Boolean): Option[T]`                                  ###

Finds the first element of the mutable indexed sequence satisfying a predicate,
if any.

* p
  * the predicate used to test elements.
* returns
  * an option value containing the first element in the mutable indexed sequence
    that satisfies `p` , or `None` if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def flatMap[B, That](f: (T) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this array and
using the elements of the resulting collections.

For example:

```scala
def getWords(lines: Seq[String]): Seq[String] = lines flatMap (line => line split "\\W+")
```

The type of the resulting collection is guided by the static type of array. This
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
  * a new array resulting from applying the given collection-valued function
     `f` to each element of this array and concatenating the results.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def flatten[U](implicit asTrav: (T) ⇒ collection.Traversable[U], m: ClassTag[U]): Array[U]` ###

Flattens a two-dimensional array by concatenating all its rows into a single
array.

* U
  * Type of row elements.
* asTrav
  * A function that converts elements of this array to rows - arrays of type
     `U` .
* returns
  * An array obtained by concatenating rows of this array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def foldLeft[B](z: B)(op: (B, T) ⇒ B): B`                               ###

Applies a binary operator to a start value and all elements of this mutable
indexed sequence, going left to right.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.
    Returns `z` if this mutable indexed sequence is empty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def foldRight[B](z: B)(op: (T, B) ⇒ B): B`                              ###

Applies a binary operator to all elements of this mutable indexed sequence and a
start value, going right to left.

* B
  * the result type of the binary operator.
* z
  * the start value.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.
    Returns `z` if this mutable indexed sequence is empty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def fold[A1 >: A](z: A1)(op: (A1, A1) ⇒ A1): A1`                        ###

Folds the elements of this mutable indexed sequence using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

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
     `z` , or `z` if this mutable indexed sequence is empty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def forall(p: (T) ⇒ Boolean): Boolean`                                  ###

Tests whether a predicate holds for all elements of this mutable indexed
sequence.

* p
  * the predicate used to test elements.
* returns
  * `true` if this mutable indexed sequence is empty or the given predicate `p`
    holds for all elements of this mutable indexed sequence, otherwise `false` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → TraversableOnce →
    GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of this array.

Note: this method underlies the implementation of most other bulk operations.
Subclasses should re-implement this method if a more efficient implementation
exists.

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike →
    TraversableOnce → GenTraversableOnce → FilterMonadic

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def groupBy[K](f: (T) ⇒ K): Map[K, Array[T]]`                           ###

Partitions this mutable indexed sequence into a map of mutable indexed sequences
according to some discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new mutable indexed sequence.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to mutable indexed sequences such that the following
    invariant holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a mutable indexed sequence of those
    elements `x` for which `f(x)` equals `k` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def grouped(size: Int): collection.Iterator[Array[T]]`                  ###

Partitions elements in fixed size mutable indexed sequences.

* size
  * the number of elements per group
* returns
  * An iterator producing mutable indexed sequences of size `size` , except the
    last will be less than size `size` if the elements don't divide evenly.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `grouped`

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def head: T`                                                            ###

Selects the first element of this mutable indexed sequence.

* returns
  * the first element of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException if the mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def headOption: Option[T]`                                              ###

Optionally selects the first element.

* returns
  * the first element of this mutable indexed sequence if it is nonempty,
     `None` if it is empty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexOf[B >: A](elem: B): Int`                                      ###

[use case]

Finds index of first occurrence of some value in this array.

* elem
  * the element value to search for.
* returns
  * the index of the first element of this array that is equal (as determined by
     `==` ) to `elem` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexOf[B >: A](elem: B, from: Int): Int`                           ###

[use case]

Finds index of first occurrence of some value in this array after or at some
start index.

* elem
  * the element value to search for.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this array that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexOfSlice[B >: A](that: GenSeq[B]): Int`                         ###

Finds first index where this mutable indexed sequence contains a given sequence
as a slice.

* that
  * the sequence to test
* returns
  * the first index such that the elements of this mutable indexed sequence
    starting at this index match the elements of sequence `that` , or `-1` of no
    such subsequence exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexOfSlice[B >: A](that: GenSeq[B], from: Int): Int`              ###

Finds first index after or at a start index where this mutable indexed sequence
contains a given sequence as a slice.

* that
  * the sequence to test
* from
  * the start index
* returns
  * the first index `>= from` such that the elements of this mutable indexed
    sequence starting at this index match the elements of sequence `that` , or
     `-1` of no such subsequence exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexWhere(p: (T) ⇒ Boolean): Int`                                  ###

Finds index of first element satisfying some predicate.

* p
  * the predicate used to test elements.
* returns
  * the index of the first element of this mutable indexed sequence that
    satisfies the predicate `p` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indexWhere(p: (T) ⇒ Boolean, from: Int): Int`                       ###

Finds index of the first element satisfying some predicate after or at some
start index.

* p
  * the predicate used to test elements.
* from
  * the start index
* returns
  * the index `>= from` of the first element of this mutable indexed sequence
    that satisfies the predicate `p` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def indices: collection.immutable.Range`                                ###

Produces the range of all indices of this sequence.

* returns
  * a `Range` value from `0` to one less than the length of this mutable indexed
    sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def init: Array[T]`                                                     ###

Selects all elements except the last.

* returns
  * a mutable indexed sequence consisting of all elements of this mutable
    indexed sequence except the last one.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def inits: collection.Iterator[Array[T]]`                               ###

Iterates over the inits of this mutable indexed sequence. The first value will
be this mutable indexed sequence and the final one will be an empty mutable
indexed sequence, with the intervening values the results of successive
applications of `init` .

* returns
  * an iterator over all the inits of this mutable indexed sequence

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).inits = Iterator(List(1,2,3), List(1,2), List(1), Nil)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def intersect[B >: A](that: GenSeq[B]): Array[T]`                       ###

[use case]

Computes the multiset intersection between this array and another sequence.

* that
  * the sequence of elements to intersect with.
* returns
  * a new array which contains all elements of this array which also appear in
     `that` . If an element value `x` appears _n_ times in `that` , then the
    first _n_ occurrences of `x` will be retained in the result, but any
    following occurrences will be omitted.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def isDefinedAt(idx: Int): Boolean`                                     ###

Tests whether this mutable indexed sequence contains given index.

The implementations of methods `apply` and `isDefinedAt` turn a `Seq[A]` into a
 `PartialFunction[Int, A]` .

* idx
  * the index to test
* returns
  * `true` if this mutable indexed sequence contains an element at position
     `idx` , `false` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def iterator: collection.Iterator[T]`                                   ###

Creates a new iterator over all elements contained in this iterable object.

* returns
  * the new iterator

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqLike → IterableLike → GenIterableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def last: T`                                                            ###

Selects the last element.

* returns
  * The last element of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * NoSuchElementException If the mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexOf[B >: A](elem: B): Int`                                  ###

[use case]

Finds index of last occurrence of some value in this array.

* elem
  * the element value to search for.
* returns
  * the index of the last element of this array that is equal (as determined by
     `==` ) to `elem` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexOf[B >: A](elem: B, end: Int): Int`                        ###

[use case]

Finds index of last occurrence of some value in this array before or at a given
end index.

* elem
  * the element value to search for.
* end
  * the end index.
* returns
  * the index `<= end` of the last element of this array that is equal (as
    determined by `==` ) to `elem` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexOfSlice[B >: A](that: GenSeq[B]): Int`                     ###

Finds last index where this mutable indexed sequence contains a given sequence
as a slice.

* that
  * the sequence to test
* returns
  * the last index such that the elements of this mutable indexed sequence
    starting a this index match the elements of sequence `that` , or `-1` of no
    such subsequence exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexOfSlice[B >: A](that: GenSeq[B], end: Int): Int`           ###

Finds last index before or at a given end index where this mutable indexed
sequence contains a given sequence as a slice.

* that
  * the sequence to test
* end
  * the end index
* returns
  * the last index `<= end` such that the elements of this mutable indexed
    sequence starting at this index match the elements of sequence `that` , or
     `-1` of no such subsequence exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexWhere(p: (T) ⇒ Boolean): Int`                              ###

Finds index of last element satisfying some predicate.

* p
  * the predicate used to test elements.
* returns
  * the index of the last element of this mutable indexed sequence that
    satisfies the predicate `p` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastIndexWhere(p: (T) ⇒ Boolean, end: Int): Int`                    ###

Finds index of last element satisfying some predicate before or at given end
index.

* p
  * the predicate used to test elements.
* returns
  * the index `<= end` of the last element of this mutable indexed sequence that
    satisfies the predicate `p` , or `-1` , if none exists.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lastOption: Option[T]`                                              ###

Optionally selects the last element.

* returns
  * the last element of this mutable indexed sequence$ if it is nonempty,
     `None` if it is empty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def lengthCompare(len: Int): Int`                                       ###

Compares the length of this mutable indexed sequence to a test value.

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

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def map[B, That](f: (T) ⇒ B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this array.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new array resulting from applying the given function `f` to each element
    of this array and collecting the results.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike → FilterMonadic

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def maxBy[B](f: (T) ⇒ B)(implicit cmp: Ordering[B]): T`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this array with the largest value measured by function
    f.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def minBy[B](f: (T) ⇒ B)(implicit cmp: Ordering[B]): T`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this array with the smallest value measured by function
    f.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this mutable indexed sequence in a string using a
separator string.

* sep
  * the separator string.
* returns
  * a string representation of this mutable indexed sequence. In the resulting
    string the string representations (w.r.t. the method `toString` ) of all
    elements of this mutable indexed sequence are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this mutable indexed sequence in a string using start,
end, and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this mutable indexed sequence. The resulting
    string begins with the string `start` and ends with the string `end` .
    Inside, the string representations (w.r.t. the method `toString` ) of all
    elements of this mutable indexed sequence are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def padTo[B >: A, That](len: Int, elem: B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

A copy of this array with an element value appended until a given target length
is reached.

* len
  * the target length
* elem
  * the padding value
* returns
  * a new array consisting of all elements of this array followed by the minimal
    number of occurrences of `elem` so that the resulting array has a length of
    at least `len` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def par: ParArray[T]`                                                   ###

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
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps → CustomParallelizable → Parallelizable

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def partition(p: (T) ⇒ Boolean): (Array[T], Array[T])`                  ###

Partitions this mutable indexed sequence in two mutable indexed sequences
according to a predicate.

* p
  * the predicate on which to partition.
* returns
  * a pair of mutable indexed sequences: the first mutable indexed sequence
    consists of all elements that satisfy the predicate `p` and the second
    mutable indexed sequence consists of all elements that don't. The relative
    order of the elements in the resulting mutable indexed sequences is the same
    as in the original mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def patch[B >: A, That](from: Int, patch: GenSeq[B], replaced: Int)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Produces a new array where a slice of elements in this array is replaced by
another sequence.

* from
  * the index of the first replaced element
* replaced
  * the number of elements to drop in the original array
* returns
  * a new array consisting of all elements of this array except that `replaced`
    elements starting from `from` are replaced by `patch` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def permutations: collection.Iterator[Array[T]]`                        ###

Iterates over distinct permutations.

* returns
  * An Iterator which traverses the distinct permutations of this mutable
    indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

Example:

```scala
"abb".permutations = Iterator(abb, bab, bba)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def prefixLength(p: (T) ⇒ Boolean): Int`                                ###

Returns the length of the longest prefix whose elements all satisfy some
predicate.

* p
  * the predicate used to test elements.
* returns
  * the length of the longest prefix of this mutable indexed sequence such that
    every element of the segment satisfies the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduceLeftOption[B >: A](op: (B, T) ⇒ B): Option[B]`                ###

Optionally applies a binary operator to all elements of this mutable indexed
sequence, going left to right.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this mutable
    indexed sequence is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduceLeft[B >: A](op: (B, T) ⇒ B): B`                              ###

Applies a binary operator to all elements of this mutable indexed sequence,
going left to right.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`               ###

Reduces the elements of this mutable indexed sequence, if any, using the
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

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduceRightOption[B >: A](op: (T, B) ⇒ B): Option[B]`               ###

Optionally applies a binary operator to all elements of this mutable indexed
sequence, going right to left.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this mutable
    indexed sequence is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduceRight[B >: A](op: (T, B) ⇒ B): B`                             ###

Applies a binary operator to all elements of this mutable indexed sequence,
going right to left.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this mutable
    indexed sequence, going right to left:

    ```scala
    op(x_1, op(x_2, ..., op(x_{n-1}, x_n)...))
    ```

    where `x1, ..., xn` are the elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                             ###

Reduces the elements of this mutable indexed sequence using the specified
associative binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    mutable indexed sequence is nonempty.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def repr: Array[T]`                                                     ###

The collection of type mutable indexed sequence underlying this
 `TraversableLike` object. By default this is implemented as the
 `TraversableLike` object itself, but this can be overridden.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reverse: Array[T]`                                                  ###

Returns new mutable indexed sequence with elements in reversed order.

* returns
  * A new mutable indexed sequence with all elements of this mutable indexed
    sequence in reversed order.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reverseIterator: collection.Iterator[T]`                            ###

An iterator yielding elements in reversed order.

Note: `xs.reverseIterator` is the same as `xs.reverse.iterator` but might be
more efficient.

* returns
  * an iterator yielding the elements of this mutable indexed sequence in
    reversed order

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def reverseMap[B, That](f: (T) ⇒ B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of this array and
collecting the results in reversed order.

Note: `xs.reverseMap(f)` is the same as `xs.reverse.map(f)` but might be more
efficient.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new array resulting from applying the given function `f` to each element
    of this array and collecting the results in reversed order.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sameElements[B >: A](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this array.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → GenIterableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def scanLeft[B, That](z: B)(op: (B, T) ⇒ B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going left to right.

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
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * collection with intermediate results

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def scanRight[B, That](z: B)(op: (T, B) ⇒ B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

Produces a collection containing cumulative results of applying the operator
going right to left. The head of the collection is the last cumulative result.

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
     `That` from the current representation type `Repr` and the new element type
     `B` .
* returns
  * collection with intermediate results

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[Array[T], B, That]): That` ###

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
  * a new mutable indexed sequence containing the prefix scan of the elements in
    this mutable indexed sequence

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def segmentLength(p: (T) ⇒ Boolean, from: Int): Int`                    ###

Computes length of longest segment whose elements all satisfy some predicate.

* p
  * the predicate used to test elements.
* from
  * the index where the search starts.
* returns
  * the length of the longest segment of this mutable indexed sequence starting
    from index `from` such that every element of the segment satisfies the
    predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def seq: collection.mutable.IndexedSeq[T]`                              ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps → IndexedSeqLike → GenSeqLike → Parallelizable → TraversableOnce →
    GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def slice(from: Int, until: Int): Array[T]`                             ###

Selects an interval of elements. The returned collection is made up of all
elements `x` which satisfy the invariant:

```scala
from <= indexOf(x) < until
```

* returns
  * a mutable indexed sequence containing the elements greater than or equal to
    index `from` extending up to (but not including) index `until` of this
    mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sliding(size: Int): collection.Iterator[Array[T]]`                  ###

Groups elements in fixed size blocks by passing a "sliding window" over them (as
opposed to partitioning them, as is done in grouped.) "Sliding window" step is 1
by default.

* size
  * the number of elements per group
* returns
  * An iterator producing mutable indexed sequences of size `size` , except the
    last and the only element will be truncated if there are fewer elements than
    size.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sliding(size: Int, step: Int): collection.Iterator[Array[T]]`       ###

Groups elements in fixed size blocks by passing a "sliding window" over them (as
opposed to partitioning them, as is done in grouped.)

* size
  * the number of elements per group
* step
  * the distance between the first elements of successive groups
* returns
  * An iterator producing mutable indexed sequences of size `size` , except the
    last and the only element will be truncated if there are fewer elements than
    size.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sortBy[B](f: (T) ⇒ B)(implicit ord: math.Ordering[B]): Array[T]`    ###

Sorts this `Array` according to the Ordering which results from transforming an
implicitly given Ordering with a transformation function.

* B
  * the target type of the transformation `f` , and the type where the ordering
     `ord` is defined.
* f
  * the transformation function mapping elements to some other domain `B` .
* ord
  * the ordering assumed on domain `B` .
* returns
  * a mutable indexed sequence consisting of the elements of this mutable
    indexed sequence sorted according to the ordering where `x < y` if
     `ord.lt(f(x), f(y))` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike
* See also
  * scala.math.Ordering

Example:

```scala
val words = "The quick brown fox jumped over the lazy dog".split(' ')
// this works because scala.Ordering will implicitly provide an Ordering[Tuple2[Int, Char]]
words.sortBy(x => (x.length, x.head))
res0: Array[String] = Array(The, dog, fox, the, lazy, over, brown, quick, jumped)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sortWith(lt: (T, T) ⇒ Boolean): Array[T]`                           ###

Sorts this mutable indexed sequence according to a comparison function.

The sort is stable. That is, elements that are equal (as determined by `lt` )
appear in the same order in the sorted sequence as in the original.

* lt
  * the comparison function which tests whether its first argument precedes its
    second argument in the desired ordering.
* returns
  * a mutable indexed sequence consisting of the elements of this mutable
    indexed sequence sorted according to the comparison function `lt` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike

Example:

```scala
List("Steve", "Tom", "John", "Bob").sortWith(_.compareTo(_) < 0) =
List("Bob", "John", "Steve", "Tom")
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def sorted[B >: A](implicit ord: math.Ordering[B]): Array[T]`           ###

Sorts this mutable indexed sequence according to an Ordering.

The sort is stable. That is, elements that are equal (as determined by `lt` )
appear in the same order in the sorted sequence as in the original.

* ord
  * the ordering to be used to compare elements.
* returns
  * a mutable indexed sequence consisting of the elements of this mutable
    indexed sequence sorted according to the ordering `ord` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike
* See also
  * scala.math.Ordering

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def span(p: (T) ⇒ Boolean): (Array[T], Array[T])`                       ###

Splits this mutable indexed sequence into a prefix/suffix pair according to a
predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

* returns
  * a pair consisting of the longest prefix of this mutable indexed sequence
    whose elements all satisfy `p` , and the rest of this mutable indexed
    sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def splitAt(n: Int): (Array[T], Array[T])`                              ###

Splits this mutable indexed sequence into two at a given position. Note:
 `c splitAt n` is equivalent to (but possibly more efficient than)
 `(c take n, c drop n)` .

* n
  * the position at which to split.
* returns
  * a pair of mutable indexed sequences consisting of the first `n` elements of
    this mutable indexed sequence, and the other elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def startsWith[B](that: GenSeq[B]): Boolean`                            ###

Tests whether this mutable indexed sequence starts with the given sequence.

* that
  * the sequence to test
* returns
  * `true` if this collection has `that` as a prefix, `false` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def startsWith[B](that: GenSeq[B], offset: Int): Boolean`               ###

Tests whether this mutable indexed sequence contains the given sequence at a
given index.

 *Note* : If the both the receiver object `this` and the argument `that` are
infinite sequences this method may not terminate.

* that
  * the sequence to test
* offset
  * the index where the sequence is searched.
* returns
  * `true` if the sequence `that` is contained in this mutable indexed sequence
    at index `offset` , otherwise `false` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def tail: Array[T]`                                                     ###

Selects all elements except the first.

* returns
  * a mutable indexed sequence consisting of all elements of this mutable
    indexed sequence except the first one.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the mutable indexed sequence is empty.

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def tails: collection.Iterator[Array[T]]`                               ###

Iterates over the tails of this mutable indexed sequence. The first value will
be this mutable indexed sequence and the final one will be an empty mutable
indexed sequence, with the intervening values the results of successive
applications of `tail` .

* returns
  * an iterator over all the tails of this mutable indexed sequence

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).tails = Iterator(List(1,2,3), List(2,3), List(3), Nil)
```

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def take(n: Int): Array[T]`                                             ###

Selects first _n_ elements.

* n
  * the number of elements to take from this mutable indexed sequence.
* returns
  * a mutable indexed sequence consisting only of the first `n` elements of this
    mutable indexed sequence, or else the whole mutable indexed sequence, if it
    has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def takeRight(n: Int): Array[T]`                                        ###

Selects last _n_ elements.

* n
  * the number of elements to take
* returns
  * a mutable indexed sequence consisting only of the last `n` elements of this
    mutable indexed sequence, or else the whole mutable indexed sequence, if it
    has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def takeWhile(p: (T) ⇒ Boolean): Array[T]`                              ###

Takes longest prefix of elements that satisfy a predicate.

* returns
  * the longest prefix of this mutable indexed sequence whose elements all
    satisfy the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toBuffer[A1 >: A]: Buffer[A1]`                                      ###

Uses the contents of this mutable indexed sequence to create a new mutable
buffer.

* returns
  * a buffer containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toIndexedSeq: collection.immutable.IndexedSeq[T]`                   ###

Converts this mutable indexed sequence to an indexed sequence.

* returns
  * an indexed sequence containing all elements of this mutable indexed
    sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toIterable: collection.Iterable[T]`                                 ###

Returns this mutable indexed sequence as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

* returns
  * an `Iterable` containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toIterator: collection.Iterator[T]`                                 ###

Returns an Iterator over the elements in this mutable indexed sequence. Produces
the same result as `iterator` .

* returns
  * an Iterator containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toList: List[T]`                                                    ###

Converts this mutable indexed sequence to a list.

* returns
  * a list containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toMap[T, U](implicit ev: <:<[T, (T, U)]): Map[T, U]`                ###

[use case]

Converts this array to a map. This method is unavailable unless the elements are
members of Tuple2, each ((T, U)) becoming a key-value pair in the map. Duplicate
keys will be overwritten by later keys: if this is an unordered collection,
which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toSeq: collection.Seq[T]`                                           ###

Converts this mutable indexed sequence to a sequence.

A new collection will not be built; in particular, lazy sequences will stay
lazy.

* returns
  * a sequence containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toSet[B >: A]: Set[B]`                                              ###

Converts this mutable indexed sequence to a set.

* returns
  * a set containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toStream: collection.immutable.Stream[T]`                           ###

Converts this mutable indexed sequence to a stream.

* returns
  * a stream containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toTraversable: collection.Traversable[T]`                           ###

Converts this mutable indexed sequence to an unspecified Traversable. Will
return the same collection if this instance is already Traversable.

* returns
  * a Traversable containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def toVector: Vector[T]`                                                ###

Converts this mutable indexed sequence to a Vector.

* returns
  * a vector containing all elements of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def transpose[U](implicit asArray: (T) ⇒ Array[U]): Array[Array[U]]`    ###

Transposes a two dimensional array.

* U
  * Type of row elements.
* asArray
  * A function that converts elements of this array to rows - arrays of type
     `U` .
* returns
  * An array obtained by replacing elements of this arrays with rows the
    represent.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def union[B >: A, That](that: GenSeq[B])(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

Produces a new sequence which contains all elements of this array and also all
elements of a given sequence. `xs union ys` is equivalent to `xs ++ ys` .

Another way to express this is that `xs union ys` computes the order-preserving
multi-set union of `xs` and `ys` . `union` is hence a counter-part of `diff` and
 `intersect` which also work on multi-sets.

* that
  * the sequence to add.
* returns
  * a new array which contains all elements of this array followed by all
    elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def unzip3[T1, T2, T3](implicit asTriple: (T) ⇒ (T1, T2, T3), ct1: ClassTag[T1], ct2: ClassTag[T2], ct3: ClassTag[T3]): (Array[T1], Array[T2], Array[T3])` ###

Converts an array of triples into three arrays, one containing the elements from
each position of the triple.

* T1
  * the type of the first of three elements in the triple
* T2
  * the type of the second of three elements in the triple
* T3
  * the type of the third of three elements in the triple
* asTriple
  * an implicit conversion which asserts that the element type of this Array is
    a triple.
* ct1
  * a class tag for T1 type parameter that is required to create an instance of
    Array[T1]
* ct2
  * a class tag for T2 type parameter that is required to create an instance of
    Array[T2]
* ct3
  * a class tag for T3 type parameter that is required to create an instance of
    Array[T3]
* returns
  * a triple of Arrays, containing, respectively, the first, second, and third
    elements from each element triple of this Array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def unzip[T1, T2](implicit asPair: (T) ⇒ (T1, T2), ct1: ClassTag[T1], ct2: ClassTag[T2]): (Array[T1], Array[T2])` ###

Converts an array of pairs into an array of first elements and an array of
second elements.

* T1
  * the type of the first half of the element pairs
* T2
  * the type of the second half of the element pairs
* asPair
  * an implicit conversion which asserts that the element type of this Array is
    a pair.
* ct1
  * a class tag for T1 type parameter that is required to create an instance of
    Array[T1]
* ct2
  * a class tag for T2 type parameter that is required to create an instance of
    Array[T2]
* returns
  * a pair of Arrays, containing, respectively, the first and second half of
    each element pair of this Array.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * ArrayOps

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def updated[B >: A, That](index: Int, elem: B)(implicit bf: CanBuildFrom[Array[T], B, That]): That` ###

[use case]

A copy of this array with one single replaced element.

* index
  * the position of the replacement
* elem
  * the replacing element
* returns
  * a copy of this array with the element at position `index` replaced by
     `elem` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * SeqLike → GenSeqLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def view(from: Int, until: Int): IndexedSeqView[T, Array[T]]`           ###

A sub-sequence view starting at index `from` and extending up to (but not
including) index `until` .

* from
  * The index of the first element of the slice
* until
  * The index of the element following the slice
* returns
  * a non-strict view of a slice of this mutable indexed sequence, starting at
    index `from` and extending up to (but not including) index `until` .@note
    The difference between `view` and `slice` is that `view` produces a view of
    the current sequence, whereas `slice` produces a new sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqLike → SeqLike → IterableLike → TraversableLike
* Note
  * view(from, to) is equivalent to view.slice(from, to)

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def view: IndexedSeqView[T, Array[T]]`                                  ###

Creates a view of this iterable @see Iterable.View

* returns
  * a non-strict view of this mutable indexed sequence.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqLike → SeqLike → IterableLike → TraversableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def withFilter(p: (T) ⇒ Boolean): FilterMonadic[T, Array[T]]`           ###

Creates a non-strict filter of this mutable indexed sequence.

Note: the difference between `c filter p` and `c withFilter p` is that the
former creates a new collection, whereas the latter only restricts the domain of
subsequent `map` , `flatMap` , `foreach` , and `withFilter` operations.

* p
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this mutable indexed sequence which satisfy the predicate
     `p` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * TraversableLike → FilterMonadic

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[Array[T], (A1, B), That]): That` ###

[use case]

Returns a array formed from this array and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
shorter than the other, placeholder elements are used to extend the shorter
collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this array is shorter than
     `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    array.
* returns
  * a new array containing pairs consisting of corresponding elements of this
    array and `that` . The length of the returned collection is the maximum of
    the lengths of this array and `that` . If this array is shorter than `that` ,
     `thisElem` values are used to pad the result. If `that` is shorter than
    this array, `thatElem` values are used to pad the result.

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IterableLike → GenIterableLike

(added by implicit convertion: scala.Predef.genericArrayOps)


### `def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[Array[T], (A1, B), That]): That` ###

[use case]

Returns a array formed from this array and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
longer than the other, its remaining elements are ignored.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new array containing pairs consisting of corresponding elements of this
    array and `that` . The length of the returned collection is the minimum of
    the lengths of this array and `that` .

* Implicit information
  * This member is added by an implicit conversion from Array [T] to ArrayOps [T]
    performed by method genericArrayOps in scala.Predef.
* Definition Classes
  * IndexedSeqOptimized → IterableLike → GenIterableLike
(added by implicit convertion: scala.Predef.genericArrayOps)
