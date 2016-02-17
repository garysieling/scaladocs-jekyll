
#                                  scala.Some                                  #

```scala
final case class Some[+A](x: A) extends Option[A] with Product with Serializable
```

Class `Some[A]` represents existing values of type `A` .

* Annotations
  * @ SerialVersionUID ()
* Source
  * [Option.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Option.scala#L1)
* Version
  * 1.0, 16/07/2003


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `class WithFilter extends AnyRef`                                        ###

We need a whole WithFilter class to honor the "doesn't create a new collection"
contract even though it seems unlikely to matter much in a collection with max
size 1.

* Definition Classes
  * Option


--------------------------------------------------------------------------------
                        Value Members From scala.Option
--------------------------------------------------------------------------------


### `final def collect[B](pf: PartialFunction[A, B]): Option[B]`             ###

Returns a scala.Some containing the result of applying `pf` to this scala.Option
's contained value, *if* this option is nonempty *and*  `pf` is defined for that
value. Returns `None` otherwise.

* pf
  * the partial function.
* returns
  * the result of applying `pf` to this scala.Option 's value (if possible), or
     `None` .

* Definition Classes
  * Option
* Annotations
  * @ inline ()

Example:

```scala
// Returns Some(HTTP) because the partial function covers the case.
Some("http") collect {case "http" => "HTTP"}
// Returns None because the partial function doesn't cover the case.
Some("ftp") collect {case "http" => "HTTP"}
// Returns None because the option is empty. There is no value to pass to the partial function.
None collect {case value => value}
```

(defined at scala.Option)


### `final def contains[A1 >: A](elem: A1): Boolean`                         ###

Tests whether the option contains a given value as an element.

* elem
  * the element to test.
* returns
  * `true` if the option has an element that is equal (as determined by `==` )
    to `elem` , `false` otherwise.

* Definition Classes
  * Option

Example:

```scala
// Returns true because Some instance contains string "something" which equals "something".
Some("something") contains "something"
// Returns false because "something" != "anything".
Some("something") contains "anything"
// Returns false when method called on None.
None contains "anything"
```

(defined at scala.Option)


### `final def exists(p: (A) ⇒ Boolean): Boolean`                            ###

Returns true if this option is nonempty *and* the predicate `p` returns true
when applied to this scala.Option 's value. Otherwise, returns false.

* p
  * the predicate to test

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def filter(p: (A) ⇒ Boolean): Option[A]`                          ###

Returns this scala.Option if it is nonempty *and* applying the predicate `p` to
this scala.Option 's value returns true. Otherwise, return `None` .

* p
  * the predicate used for testing.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def filterNot(p: (A) ⇒ Boolean): Option[A]`                       ###

Returns this scala.Option if it is nonempty *and* applying the predicate `p` to
this scala.Option 's value returns false. Otherwise, return `None` .

* p
  * the predicate used for testing.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def flatMap[B](f: (A) ⇒ Option[B]): Option[B]`                    ###

Returns the result of applying `f` to this scala.Option 's value if this
scala.Option is nonempty. Returns `None` if this scala.Option is empty. Slightly
different from `map` in that `f` is expected to return an scala.Option (which
could be `None` ).

* f
  * the function to apply

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * foreach map

(defined at scala.Option)


### `def flatten[B](implicit ev: <:<[A, Option[B]]): Option[B]`              ###

* Definition Classes
  * Option

(defined at scala.Option)


### `final def fold[B](ifEmpty: ⇒ B)(f: (A) ⇒ B): B`                         ###

Returns the result of applying `f` to this scala.Option 's value if the
scala.Option is nonempty. Otherwise, evaluates expression `ifEmpty` .

* ifEmpty
  * the expression to evaluate if empty.
* f
  * the function to apply if nonempty.

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* Note
  * This is equivalent to `scala.Option map f getOrElse ifEmpty` .

(defined at scala.Option)


### `final def forall(p: (A) ⇒ Boolean): Boolean`                            ###

Returns true if this option is empty *or* the predicate `p` returns true when
applied to this scala.Option 's value.

* p
  * the predicate to test

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def foreach[U](f: (A) ⇒ U): Unit`                                 ###

Apply the given procedure `f` to the option's value, if it is nonempty.
Otherwise, do nothing.

* f
  * the procedure to apply.

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * flatMap map

(defined at scala.Option)


### `final def getOrElse[B >: A](default: ⇒ B): B`                           ###

Returns the option's value if the option is nonempty, otherwise return the
result of evaluating `default` .

* default
  * the default expression.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def map[B](f: (A) ⇒ B): Option[B]`                                ###

Returns a scala.Some containing the result of applying `f` to this scala.Option
's value if this scala.Option is nonempty. Otherwise return `None` .

* f
  * the function to apply

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* Note
  * This is similar to `flatMap` except here, `f` does not need to wrap its
    result in an scala.Option.
* See also
  * foreach flatMap

(defined at scala.Option)


### `final def orElse[B >: A](alternative: ⇒ Option[B]): Option[B]`          ###

Returns this scala.Option if it is nonempty, otherwise return the result of
evaluating `alternative` .

* alternative
  * the alternative expression.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


### `final def orNull[A1 >: A](implicit ev: <:<[Null, A1]): A1`              ###

Returns the option's value if it is nonempty, or `null` if it is empty. Although
the use of null is discouraged, code written to use scala.Option must often
interface with code that expects and returns nulls.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

Example:

```scala
val initialText: Option[String] = getInitialText
val textField = new JComponent(initialText.orNull,20)
```

(defined at scala.Option)


### `final def toLeft[X](right: ⇒ X): util.Either[A, X]`                     ###

Returns a scala.util.Right containing the given argument `right` if this is
empty, or a scala.util.Left containing this scala.Option 's value if this
scala.Option is nonempty.

* right
  * the expression to evaluate and return if this is empty

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * toRight

(defined at scala.Option)


### `final def toRight[X](left: ⇒ X): util.Either[X, A]`                     ###

Returns a scala.util.Left containing the given argument `left` if this
scala.Option is empty, or a scala.util.Right containing this scala.Option 's
value if this is nonempty.

* left
  * the expression to evaluate and return if this is empty

* Definition Classes
  * Option
* Annotations
  * @ inline ()
* See also
  * toLeft

(defined at scala.Option)


### `final def withFilter(p: (A) ⇒ Boolean): WithFilter`                     ###

Necessary to keep scala.Option from being implicitly converted to
scala.collection.Iterable in `for` comprehensions.

* Definition Classes
  * Option
* Annotations
  * @ inline ()

(defined at scala.Option)


--------------------------------------------------------------------------------
                     Instance Constructors From scala.Some
--------------------------------------------------------------------------------


### `new Some(x: A)`                                                         ###

(defined at scala.Some)


--------------------------------------------------------------------------------
            Value Members From Implicit scala.Option.option2Iterable
--------------------------------------------------------------------------------


### `def ++:[B >: A, That](that: collection.Traversable[B])(implicit bf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

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
  * a new collection of type `That` which contains all elements of this iterable
    collection followed by all elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def ++:[B >: A, That](that: collection.TraversableOnce[B])(implicit bf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

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
  * a new option which contains all elements of this option followed by all
    elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def ++[B >: A, That](that: GenTraversableOnce[B])(implicit bf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

[use case]

Returns a new option containing the elements from the left hand operand followed
by the elements from the right hand operand. The element type of the option is
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
  * a new option which contains all elements of this option followed by all
    elements of `that` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def /:[B](z: B)(op: (B, A) ⇒ B): B`                                     ###

Applies a binary operator to a start value and all elements of this iterable
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
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going left to right with the start value `z` on the left:

    ```scala
    op(...op(op(z, x_1), x_2), ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def :\[B](z: B)(op: (A, B) ⇒ B): B`                                     ###

Applies a binary operator to all elements of this iterable collection and a
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
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going right to left with the start value `z` on the right:

    ```scala
    op(x_1, op(x_2, ... op(x_n, z)...))
    ```

    where `x1, ..., xn` are the elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def addString(b: StringBuilder): StringBuilder`                         ###

Appends all elements of this iterable collection to a string builder. The
written text consists of the string representations (w.r.t. the method
 `toString` ) of all elements of this iterable collection without any separator
string.

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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def addString(b: StringBuilder, sep: String): StringBuilder`            ###

Appends all elements of this iterable collection to a string builder using a
separator string. The written text consists of the string representations
(w.r.t. the method `toString` ) of all elements of this iterable collection,
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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder` ###

Appends all elements of this iterable collection to a string builder using
start, end, and separator strings. The written text begins with the string
 `start` and ends with the string `end` . Inside, the string representations
(w.r.t. the method `toString` ) of all elements of this iterable collection are
separated by the string `sep` .

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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def aggregate[B](z: ⇒ B)(seqop: (B, A) ⇒ B, combop: (B, B) ⇒ B): B`     ###

Aggregates the results of applying an operator to subsequent elements.

This is a more general form of `fold` and `reduce` . It is similar to
 `foldLeft` in that it doesn't require the result to be a supertype of the
element type. In addition, it allows parallel collections to be processed in
chunks, and then combines the intermediate results.

 `aggregate` splits the iterable collection into partitions and processes each
partition by sequentially applying `seqop` , starting with `z` (like `foldLeft` ).
Those intermediate results are then combined by using `combop` (like `fold` ).
The implementation of this operation may operate on an arbitrary number of
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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def canEqual(that: Any): Boolean`                                       ###

Method called from equality methods, so that user-defined subclasses can refuse
to be equal to other collections of the same kind.

* that
  * The object with which this iterable collection should be compared
* returns
  * `true` , if this iterable collection can possibly equal `that` , `false`
    otherwise. The test takes into consideration only the run-time types of
    objects but ignores their elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → Equals

(added by implicit convertion: scala.Option.option2Iterable)


### `def collectFirst[B](pf: PartialFunction[A, B]): Option[B]`              ###

Finds the first element of the iterable collection for which the given partial
function is defined, and applies the partial function to it.

Note: may not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* pf
  * the partial function
* returns
  * an option value containing pf applied to the first value for which it is
    defined, or `None` if none exists.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce

Example:

```scala
Seq("a", 1, 5L).collectFirst({ case x: Int => x*10 }) = Some(10)
```

(added by implicit convertion: scala.Option.option2Iterable)


### `def companion: GenericCompanion[collection.Iterable]`                   ###

The factory companion object that builds instances of class Iterable. (or its
 `Iterable` superclass where class Iterable is not a `Seq` .)

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * Iterable → GenIterable → Traversable → GenTraversable →
    GenericTraversableTemplate

(added by implicit convertion: scala.Option.option2Iterable)


### `def copyToArray[B >: A](xs: Array[B]): Unit`                            ###

[use case]

Copies the elements of this option to an array. Fills the given array `xs` with
values of this option. Copying will stop once either the end of the current
option is reached, or the end of the target array is reached.

* xs
  * the array to fill.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def copyToArray[B >: A](xs: Array[B], start: Int): Unit`                ###

[use case]

Copies the elements of this option to an array. Fills the given array `xs` with
values of this option, beginning at index `start` . Copying will stop once
either the end of the current option is reached, or the end of the target array
is reached.

* xs
  * the array to fill.
* start
  * the starting index.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def copyToArray[B >: A](xs: Array[B], start: Int, len: Int): Unit`      ###

[use case]

Copies the elements of this option to an array. Fills the given array `xs` with
at most `len` elements of this option, starting at position `start` . Copying
will stop once either the end of the current option is reached, or the end of
the target array is reached, or `len` elements have been copied.

* xs
  * the array to fill.
* start
  * the starting index.
* len
  * the maximal number of elements to copy.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def copyToBuffer[B >: A](dest: Buffer[B]): Unit`                        ###

Copies all elements of this iterable collection to a buffer.

Note: will not terminate for infinite-sized collections.

* dest
  * The buffer to which elements are copied.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def count(p: (A) ⇒ Boolean): Int`                                       ###

Counts the number of elements in the iterable collection which satisfy a
predicate.

* p
  * the predicate used to test elements.
* returns
  * the number of elements satisfying the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def drop(n: Int): collection.Iterable[A]`                               ###

Selects all elements except first _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to drop from this iterable collection.
* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the first `n` ones, or else the empty iterable collection, if this
    iterable collection has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def dropRight(n: Int): collection.Iterable[A]`                          ###

Selects all elements except last _n_ ones.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * The number of elements to take
* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the last `n` ones, or else the empty iterable collection, if this
    iterable collection has less than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def dropWhile(p: (A) ⇒ Boolean): collection.Iterable[A]`                ###

Drops longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest suffix of this iterable collection whose first element does not
    satisfy the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def foldLeft[B](z: B)(op: (B, A) ⇒ B): B`                               ###

Applies a binary operator to a start value and all elements of this iterable
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
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going left to right with the start value `z` on the left:

    ```scala
    op(...op(z, x_1), x_2, ..., x_n)
    ```

    where `x1, ..., xn` are the elements of this iterable collection. Returns
     `z` if this iterable collection is empty.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def genericBuilder[B]: Builder[B, collection.Iterable[B]]`              ###

The generic builder that builds instances of Iterable at arbitrary element
types.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.Option.option2Iterable)


### `def groupBy[K](f: (A) ⇒ K): Map[K, collection.Iterable[A]]`             ###

Partitions this iterable collection into a map of iterable collections according
to some discriminator function.

Note: this method is not re-implemented by views. This means when applied to a
view it will always force the view and return a new iterable collection.

* K
  * the type of keys returned by the discriminator function.
* f
  * the discriminator function.
* returns
  * A map from keys to iterable collections such that the following invariant
    holds:

    ```scala
    (xs groupBy f)(k) = xs filter (x => f(x) == k)
    ```

    That is, every key `k` is bound to a iterable collection of those elements
     `x` for which `f(x)` equals `k` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def grouped(size: Int): collection.Iterator[collection.Iterable[A]]`    ###

Partitions elements in fixed size iterable collections.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    will be less than size `size` if the elements don't divide evenly.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `grouped`

(added by implicit convertion: scala.Option.option2Iterable)


### `def init: collection.Iterable[A]`                                       ###

Selects all elements except the last.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the last one.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * UnsupportedOperationException if the iterable collection is empty.

(added by implicit convertion: scala.Option.option2Iterable)


### `def inits: collection.Iterator[collection.Iterable[A]]`                 ###

Iterates over the inits of this iterable collection. The first value will be
this iterable collection and the final one will be an empty iterable collection,
with the intervening values the results of successive applications of `init` .

* returns
  * an iterator over all the inits of this iterable collection

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).inits = Iterator(List(1,2,3), List(1,2), List(1), Nil)
```

(added by implicit convertion: scala.Option.option2Iterable)


### `def maxBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

[use case]

Finds the first element which yields the largest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this option with the largest value measured by function
    f.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def minBy[B](f: (A) ⇒ B)(implicit cmp: Ordering[B]): A`                 ###

[use case]

Finds the first element which yields the smallest value measured by function f.

* B
  * The result type of the function f.
* f
  * The measuring function.
* returns
  * the first element of this option with the smallest value measured by
    function f.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def mkString(sep: String): String`                                      ###

Displays all elements of this iterable collection in a string using a separator
string.

* sep
  * the separator string.
* returns
  * a string representation of this iterable collection. In the resulting string
    the string representations (w.r.t. the method `toString` ) of all elements
    of this iterable collection are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("|") = "1|2|3"
```

(added by implicit convertion: scala.Option.option2Iterable)


### `def mkString(start: String, sep: String, end: String): String`          ###

Displays all elements of this iterable collection in a string using start, end,
and separator strings.

* start
  * the starting string.
* sep
  * the separator string.
* end
  * the ending string.
* returns
  * a string representation of this iterable collection. The resulting string
    begins with the string `start` and ends with the string `end` . Inside, the
    string representations (w.r.t. the method `toString` ) of all elements of
    this iterable collection are separated by the string `sep` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

Example:

```scala
List(1, 2, 3).mkString("(", "; ", ")") = "(1; 2; 3)"
```

(added by implicit convertion: scala.Option.option2Iterable)


### `def par: ParIterable[A]`                                                ###

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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * Parallelizable

(added by implicit convertion: scala.Option.option2Iterable)


### `def partition(p: (A) ⇒ Boolean): (collection.Iterable[A], collection.Iterable[A])` ###

Partitions this iterable collection in two iterable collections according to a
predicate.

* p
  * the predicate on which to partition.
* returns
  * a pair of iterable collections: the first iterable collection consists of
    all elements that satisfy the predicate `p` and the second iterable
    collection consists of all elements that don't. The relative order of the
    elements in the resulting iterable collections is the same as in the
    original iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def reduceLeftOption[B >: A](op: (B, A) ⇒ B): Option[B]`                ###

Optionally applies a binary operator to all elements of this iterable
collection, going left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceLeft(op)` if this iterable
    collection is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def reduceLeft[B >: A](op: (B, A) ⇒ B): B`                              ###

Applies a binary operator to all elements of this iterable collection, going
left to right.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * the result of inserting `op` between consecutive elements of this iterable
    collection, going left to right:

    ```scala
    op( op( ... op(x_1, x_2) ..., x_{n-1}), x_n)
    ```

    where `x1, ..., xn` are the elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this iterable collection is empty.

(added by implicit convertion: scala.Option.option2Iterable)


### `def reduceOption[A1 >: A](op: (A1, A1) ⇒ A1): Option[A1]`               ###

Reduces the elements of this iterable collection, if any, using the specified
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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def reduceRightOption[B >: A](op: (A, B) ⇒ B): Option[B]`               ###

Optionally applies a binary operator to all elements of this iterable
collection, going right to left.

Note: will not terminate for infinite-sized collections.

Note: might return different results for different runs, unless the underlying
collection type is ordered. or the operator is associative and commutative.

* B
  * the result type of the binary operator.
* op
  * the binary operator.
* returns
  * an option value containing the result of `reduceRight(op)` if this iterable
    collection is nonempty, `None` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this iterable collection is empty.

(added by implicit convertion: scala.Option.option2Iterable)


### `def reduce[A1 >: A](op: (A1, A1) ⇒ A1): A1`                             ###

Reduces the elements of this iterable collection using the specified associative
binary operator.

The order in which operations are performed on elements is unspecified and may
be nondeterministic.

* A1
  * A type parameter for the binary operator, a supertype of `A` .
* op
  * A binary operator that must be associative.
* returns
  * The result of applying reduce operator `op` between all the elements if the
    iterable collection is nonempty.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce
* Exceptions thrown
  * UnsupportedOperationException if this iterable collection is empty.

(added by implicit convertion: scala.Option.option2Iterable)


### `def repr: collection.Iterable[A]`                                       ###

The collection of type iterable collection underlying this `TraversableLike`
object. By default this is implemented as the `TraversableLike` object itself,
but this can be overridden.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def sameElements[B >: A](that: GenIterable[B]): Boolean`                ###

[use case]

Checks if the other iterable collection contains the same elements in the same
order as this option.

* that
  * the collection to compare with.
* returns
  * `true` , if both collections contain the same elements in the same order,
     `false` otherwise.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → GenIterableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def scanLeft[B, That](z: B)(op: (B, A) ⇒ B)(implicit bf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def scanRight[B, That](z: B)(op: (A, B) ⇒ B)(implicit bf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

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
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_ The behavior of `scanRight` has changed. The
    previous behavior can be reproduced with scanRight.reverse.

(added by implicit convertion: scala.Option.option2Iterable)


### `def scan[B >: A, That](z: B)(op: (B, B) ⇒ B)(implicit cbf: CanBuildFrom[collection.Iterable[A], B, That]): That` ###

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
  * a new iterable collection containing the prefix scan of the elements in this
    iterable collection

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def seq: collection.Iterable[A]`                                        ###

A version of this collection with all of the operations implemented sequentially
(i.e., in a single-threaded manner).

This method returns a reference to this collection. In parallel collections, it
is redefined to return a sequential implementation of this collection. In both
cases, it has O(1) complexity.

* returns
  * a sequential view of the collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * Iterable → GenIterable → Traversable → GenTraversable → Parallelizable →
    TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def slice(from: Int, until: Int): collection.Iterable[A]`               ###

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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def sliding(size: Int): collection.Iterator[collection.Iterable[A]]`    ###

Groups elements in fixed size blocks by passing a "sliding window" over them (as
opposed to partitioning them, as is done in grouped.) "Sliding window" step is 1
by default.

* size
  * the number of elements per group
* returns
  * An iterator producing iterable collections of size `size` , except the last
    and the only element will be truncated if there are fewer elements than
    size.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(added by implicit convertion: scala.Option.option2Iterable)


### `def sliding(size: Int, step: Int): collection.Iterator[collection.Iterable[A]]` ###

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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike
* See also
  * scala.collection.Iterator, method `sliding`

(added by implicit convertion: scala.Option.option2Iterable)


### `def span(p: (A) ⇒ Boolean): (collection.Iterable[A], collection.Iterable[A])` ###

Splits this iterable collection into a prefix/suffix pair according to a
predicate.

Note: `c span p` is equivalent to (but possibly more efficient than)
 `(c takeWhile p, c dropWhile p)` , provided the evaluation of the predicate
 `p` does not cause any side-effects.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a pair consisting of the longest prefix of this iterable collection whose
    elements all satisfy `p` , and the rest of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def splitAt(n: Int): (collection.Iterable[A], collection.Iterable[A])`  ###

Splits this iterable collection into two at a given position. Note:
 `c splitAt n` is equivalent to (but possibly more efficient than)
 `(c take n, c drop n)` .

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the position at which to split.
* returns
  * a pair of iterable collections consisting of the first `n` elements of this
    iterable collection, and the other elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def tail: collection.Iterable[A]`                                       ###

Selects all elements except the first.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * a iterable collection consisting of all elements of this iterable collection
    except the first one.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → GenTraversableLike
* Exceptions thrown
  * ``UnsupportedOperationException`` if the iterable collection is empty.

(added by implicit convertion: scala.Option.option2Iterable)


### `def tails: collection.Iterator[collection.Iterable[A]]`                 ###

Iterates over the tails of this iterable collection. The first value will be
this iterable collection and the final one will be an empty iterable collection,
with the intervening values the results of successive applications of `tail` .

* returns
  * an iterator over all the tails of this iterable collection

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike

Example:

```scala
List(1,2,3).tails = Iterator(List(1,2,3), List(2,3), List(3), Nil)
```

(added by implicit convertion: scala.Option.option2Iterable)


### `def take(n: Int): collection.Iterable[A]`                               ###

Selects first _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take from this iterable collection.
* returns
  * a iterable collection consisting only of the first `n` elements of this
    iterable collection, or else the whole iterable collection, if it has less
    than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def takeRight(n: Int): collection.Iterable[A]`                          ###

Selects last _n_ elements.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* n
  * the number of elements to take
* returns
  * a iterable collection consisting only of the last `n` elements of this
    iterable collection, or else the whole iterable collection, if it has less
    than `n` elements.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def takeWhile(p: (A) ⇒ Boolean): collection.Iterable[A]`                ###

Takes longest prefix of elements that satisfy a predicate.

Note: might return different results for different runs, unless the underlying
collection type is ordered.

* returns
  * the longest prefix of this iterable collection whose elements all satisfy
    the predicate `p` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def toBuffer[B >: A]: Buffer[B]`                                        ###

Uses the contents of this iterable collection to create a new mutable buffer.

Note: will not terminate for infinite-sized collections.

* returns
  * a buffer containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toIndexedSeq: collection.immutable.IndexedSeq[A]`                   ###

Converts this iterable collection to an indexed sequence.

Note: will not terminate for infinite-sized collections.

* returns
  * an indexed sequence containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toIterable: collection.Iterable[A]`                                 ###

Returns this iterable collection as an iterable collection.

A new collection will not be built; lazy collections will stay lazy.

Note: will not terminate for infinite-sized collections.

* returns
  * an `Iterable` containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toIterator: collection.Iterator[A]`                                 ###

Returns an Iterator over the elements in this iterable collection. Produces the
same result as `iterator` .

Note: will not terminate for infinite-sized collections.

* returns
  * an Iterator containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(added by implicit convertion: scala.Option.option2Iterable)


### `def toMap[T, U](implicit ev: <:<[A, (T, U)]): Map[T, U]`                ###

[use case]

Converts this option to a map. This method is unavailable unless the elements
are members of Tuple2, each ((T, U)) becoming a key-value pair in the map.
Duplicate keys will be overwritten by later keys: if this is an unordered
collection, which key is in the resulting map is undefined.

* returns
  * a map of type `immutable.Map[T, U]` containing all key/value pairs of type
     `(T, U)` of this option.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toSeq: collection.Seq[A]`                                           ###

Converts this iterable collection to a sequence. As with `toIterable` , it's
lazy in this default implementation, as this `TraversableOnce` may be lazy and
unevaluated.

Note: will not terminate for infinite-sized collections.

* returns
  * a sequence containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toSet[B >: A]: Set[B]`                                              ###

Converts this iterable collection to a set.

Note: will not terminate for infinite-sized collections.

* returns
  * a set containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableOnce → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toStream: collection.immutable.Stream[A]`                           ###

Converts this iterable collection to a stream.

* returns
  * a stream containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike → GenTraversableOnce

(added by implicit convertion: scala.Option.option2Iterable)


### `def toTraversable: collection.Traversable[A]`                           ###

Converts this iterable collection to an unspecified Traversable. Will return the
same collection if this instance is already Traversable.

Note: will not terminate for infinite-sized collections.

* returns
  * a Traversable containing all elements of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * TraversableLike → TraversableOnce → GenTraversableOnce
* Annotations
  * @ deprecatedOverriding (message =..., since = "2.11.0")

(added by implicit convertion: scala.Option.option2Iterable)


### `def transpose[B](implicit asTraversable: (A) ⇒ GenTraversableOnce[B]): collection.Iterable[collection.Iterable[B]]` ###

Transposes this iterable collection of traversable collections into a iterable
collection of iterable collections.

The resulting collection's type will be guided by the static type of iterable
collection. For example:

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
  * an implicit conversion which asserts that the element type of this iterable
    collection is a `Traversable` .
* returns
  * a two-dimensional iterable collection of iterable collections which has as _
    n_ th row the _n_ th column of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * GenericTraversableTemplate
* Annotations
  * @migration
* Migration
  * _(Changed in version 2.9.0)_  `transpose` throws an
     `IllegalArgumentException` if collections are not uniformly sized.
* Exceptions thrown
  * IllegalArgumentException if all collections in this iterable collection are
    not of the same size.

(added by implicit convertion: scala.Option.option2Iterable)


### `def unzip3[A1, A2, A3](implicit asTriple: (A) ⇒ (A1, A2, A3)): (collection.Iterable[A1], collection.Iterable[A2], collection.Iterable[A3])` ###

Converts this iterable collection of triples into three collections of the
first, second, and third element of each triple.

```scala
val xs = Iterable(
           (1, "one", '1'),
           (2, "two", '2'),
           (3, "three", '3')).unzip3
// xs == (Iterable(1, 2, 3),
//        Iterable(one, two, three),
//        Iterable(1, 2, 3))
```

* A1
  * the type of the first member of the element triples
* A2
  * the type of the second member of the element triples
* A3
  * the type of the third member of the element triples
* asTriple
  * an implicit conversion which asserts that the element type of this iterable
    collection is a triple.
* returns
  * a triple of iterable collections, containing the first, second, respectively
    third member of each element triple of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.Option.option2Iterable)


### `def unzip[A1, A2](implicit asPair: (A) ⇒ (A1, A2)): (collection.Iterable[A1], collection.Iterable[A2])` ###

Converts this iterable collection of pairs into two collections of the first and
second half of each pair.

```scala
val xs = Iterable(
           (1, "one"),
           (2, "two"),
           (3, "three")).unzip
// xs == (Iterable(1, 2, 3),
//        Iterable(one, two, three))
```

* A1
  * the type of the first half of the element pairs
* A2
  * the type of the second half of the element pairs
* asPair
  * an implicit conversion which asserts that the element type of this iterable
    collection is a pair.
* returns
  * a pair of iterable collections, containing the first, respectively second
    half of each element pair of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * GenericTraversableTemplate

(added by implicit convertion: scala.Option.option2Iterable)


### `def view(from: Int, until: Int): IterableView[A, collection.Iterable[A]]` ###

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

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def view: IterableView[A, collection.Iterable[A]]`                      ###

Creates a non-strict view of this iterable collection.

* returns
  * a non-strict view of this iterable collection.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → TraversableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def zipAll[B, A1 >: A, That](that: GenIterable[B], thisElem: A1, thatElem: B)(implicit bf: CanBuildFrom[collection.Iterable[A], (A1, B), That]): That` ###

[use case]

Returns a option formed from this option and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
shorter than the other, placeholder elements are used to extend the shorter
collection to the length of the longer.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* thisElem
  * the element to be used to fill up the result if this option is shorter than
     `that` .
* thatElem
  * the element to be used to fill up the result if `that` is shorter than this
    option.
* returns
  * a new option containing pairs consisting of corresponding elements of this
    option and `that` . The length of the returned collection is the maximum of
    the lengths of this option and `that` . If this option is shorter than
     `that` , `thisElem` values are used to pad the result. If `that` is shorter
    than this option, `thatElem` values are used to pad the result.

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → GenIterableLike

(added by implicit convertion: scala.Option.option2Iterable)


### `def zip[A1 >: A, B, That](that: GenIterable[B])(implicit bf: CanBuildFrom[collection.Iterable[A], (A1, B), That]): That` ###

[use case]

Returns a option formed from this option and another iterable collection by
combining corresponding elements in pairs. If one of the two collections is
longer than the other, its remaining elements are ignored.

* B
  * the type of the second half of the returned pairs
* that
  * The iterable providing the second half of each result pair
* returns
  * a new option containing pairs consisting of corresponding elements of this
    option and `that` . The length of the returned collection is the minimum of
    the lengths of this option and `that` .

* Implicit information
  * This member is added by an implicit conversion from Some [A] to Iterable [A]
    performed by method option2Iterable in scala.Option.
* Definition Classes
  * IterableLike → GenIterableLike
(added by implicit convertion: scala.Option.option2Iterable)
