
#                       scala.collection.immutable.Stack                       #

```scala
object Stack extends SeqFactory[Stack] with Serializable
```

This object provides a set of operations to create `immutable.Stack` values.

* Source
  * [Stack.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/Stack.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Coll = Stack[_]`                                                   ###

The underlying collection type with unknown element type

* Attributes
  * protected[this]
* Definition Classes
  * GenericCompanion


### `class GenericCanBuildFrom[A] extends CanBuildFrom[CC[_], A, CC[A]]`     ###

A generic implementation of the `CanBuildFrom` trait, which forwards all calls
to `apply(from)` to the `genericBuilder` method of collection `from` , and which
forwards all calls of `apply()` to the `newBuilder` method of this factory.

* Definition Classes
  * GenTraversableFactory


--------------------------------------------------------------------------------
       Value Members From scala.collection.generic.GenTraversableFactory
--------------------------------------------------------------------------------


### `def ReusableCBF: GenericCanBuildFrom[Nothing]`                          ###

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def concat[A](xss: collection.Traversable[A]*): Stack[A]`               ###

Concatenates all argument collections into a single collection.

* xss
  * the collections that are to be concatenated.
* returns
  * the concatenation of all the collections.

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n: Int)(elem: ⇒ A): Stack[A]`                               ###

Produces a collection containing the results of some element computation a
number of times.

* n
  * the number of elements contained in the collection.
* elem
  * the element computation
* returns
  * A collection that contains the results of `n` evaluations of `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int)(elem: ⇒ A): Stack[Stack[A]]`              ###

Produces a two-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2` evaluations of `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int)(elem: ⇒ A): Stack[Stack[Stack[A]]]` ###

Produces a three-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3` evaluations of
     `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int, n4: Int)(elem: ⇒ A): Stack[Stack[Stack[Stack[A]]]]` ###

Produces a four-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3 x n4` evaluations of
     `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def fill[A](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(elem: ⇒ A): Stack[Stack[Stack[Stack[Stack[A]]]]]` ###

Produces a five-dimensional collection containing the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* n5
  * the number of elements in the 5th dimension
* elem
  * the element computation
* returns
  * A collection that contains the results of `n1 x n2 x n3 x n4 x n5`
    evaluations of `elem` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def iterate[A](start: A, len: Int)(f: (A) ⇒ A): Stack[A]`               ###

Produces a collection containing repeated applications of a function to a start
value.

* start
  * the start value of the collection
* len
  * the number of elements contained inthe collection
* f
  * the function that's repeatedly applied
* returns
  * a collection with `len` values in the sequence
     `start, f(start), f(f(start)), ...`

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def range[T](start: T, end: T)(implicit arg0: Integral[T]): Stack[T]`   ###

Produces a collection containing a sequence of increasing of integers.

* start
  * the first element of the collection
* end
  * the end value of the collection (the first value NOT contained)
* returns
  * a collection with values `start, start + 1, ..., end - 1`

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def range[T](start: T, end: T, step: T)(implicit arg0: Integral[T]): Stack[T]` ###

Produces a collection containing equally spaced values in some integer interval.

* start
  * the start value of the collection
* end
  * the end value of the collection (the first value NOT contained)
* step
  * the difference between successive elements of the collection (must be
    positive or negative)
* returns
  * a collection with values `start, start + step, ...` up to, but excluding
     `end`

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n: Int)(f: (Int) ⇒ A): Stack[A]`                        ###

Produces a collection containing values of a given function over a range of
integer values starting from 0.

* n
  * The number of elements in the collection
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(0), ..., f(n -1)`

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int)(f: (Int, Int) ⇒ A): Stack[Stack[A]]`  ###

Produces a two-dimensional collection containing values of a given function over
ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2)` for `0 <= i1 < n1` and
     `0 <= i2 < n2` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int)(f: (Int, Int, Int) ⇒ A): Stack[Stack[Stack[A]]]` ###

Produces a three-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3)` for `0 <= i1 < n1` ,
     `0 <= i2 < n2` , and `0 <= i3 < n3` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int, n4: Int)(f: (Int, Int, Int, Int) ⇒ A): Stack[Stack[Stack[Stack[A]]]]` ###

Produces a four-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3, i4)` for `0 <= i1 < n1` ,
     `0 <= i2 < n2` , `0 <= i3 < n3` , and `0 <= i4 < n4` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


### `def tabulate[A](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(f: (Int, Int, Int, Int, Int) ⇒ A): Stack[Stack[Stack[Stack[Stack[A]]]]]` ###

Produces a five-dimensional collection containing values of a given function
over ranges of integer values starting from 0.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* n4
  * the number of elements in the 4th dimension
* n5
  * the number of elements in the 5th dimension
* f
  * The function computing element values
* returns
  * A collection consisting of elements `f(i1, i2, i3, i4, i5)` for
     `0 <= i1 < n1` , `0 <= i2 < n2` , `0 <= i3 < n3` , `0 <= i4 < n4` , and
     `0 <= i5 < n5` .

* Definition Classes
  * GenTraversableFactory

(defined at scala.collection.generic.GenTraversableFactory)


--------------------------------------------------------------------------------
          Value Members From scala.collection.generic.GenericCompanion
--------------------------------------------------------------------------------


### `def apply[A](elems: A*): Stack[A]`                                      ###

Creates a collection with the specified elements.

* A
  * the type of the collection's elements
* elems
  * the elements of the created collection
* returns
  * a new collection with elements `elems`

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


### `def empty[A]: Stack[A]`                                                 ###

An empty collection of type `CC[A]`

* A
  * the type of the collection's elements

* Definition Classes
  * GenericCompanion

(defined at scala.collection.generic.GenericCompanion)


--------------------------------------------------------------------------------
             Value Members From scala.collection.generic.SeqFactory
--------------------------------------------------------------------------------


### `def unapplySeq[A](x: Stack[A]): Some[Stack[A]]`                         ###

This method is called in a pattern match { case Seq(...) => }.

* x
  * the selector value
* returns
  * sequence wrapped in an option, if this is a Seq, otherwise none

* Definition Classes
  * SeqFactory

(defined at scala.collection.generic.SeqFactory)


--------------------------------------------------------------------------------
              Value Members From scala.collection.immutable.Stack
--------------------------------------------------------------------------------


### `implicit def canBuildFrom[A]: CanBuildFrom[Coll, A, Stack[A]]`          ###

The standard `CanBuildFrom` instance for `immutable.Stack` objects. The created
value is an instance of class `GenericCanBuildFrom` , which forwards calls to
create a new builder to the `genericBuilder` method of the requesting
collection.

(defined at scala.collection.immutable.Stack)


### `def newBuilder[A]: Builder[A, Stack[A]]`                                ###

The default builder for `immutable.Stack` objects.

* A
  * the type of the immutable stack's elements

* Definition Classes
  * Stack → GenericCompanion
(defined at scala.collection.immutable.Stack)
