
#                                 scala.Array                                 #

```scala
object Array extends FallbackArrayBuilding with Serializable
```

Utility methods for operating on arrays. For example:

```scala
val a = Array(1, 2)
val b = Array.ofDim[Int](2)
val c = Array.concat(a, b)
```

where the array objects `a` , `b` and `c` have respectively the values
 `Array(1, 2)` , `Array(0, 0)` and `Array(1, 2, 0, 0)` .

* Source
  * [Array.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/Array.scala#L1)
* Version
  * 1.0


--------------------------------------------------------------------------------
                         Value Members From scala.Array
--------------------------------------------------------------------------------


### `def apply(x: Boolean, xs: Boolean*): Array[Boolean]`                    ###

Creates an array of `Boolean` objects

(defined at scala.Array)


### `def apply(x: Byte, xs: Byte*): Array[Byte]`                             ###

Creates an array of `Byte` objects

(defined at scala.Array)


### `def apply(x: Char, xs: Char*): Array[Char]`                             ###

Creates an array of `Char` objects

(defined at scala.Array)


### `def apply(x: Double, xs: Double*): Array[Double]`                       ###

Creates an array of `Double` objects

(defined at scala.Array)


### `def apply(x: Float, xs: Float*): Array[Float]`                          ###

Creates an array of `Float` objects

(defined at scala.Array)


### `def apply(x: Int, xs: Int*): Array[Int]`                                ###

Creates an array of `Int` objects

(defined at scala.Array)


### `def apply(x: Long, xs: Long*): Array[Long]`                             ###

Creates an array of `Long` objects

(defined at scala.Array)


### `def apply(x: Short, xs: Short*): Array[Short]`                          ###

Creates an array of `Short` objects

(defined at scala.Array)


### `def apply(x: Unit, xs: Unit*): Array[Unit]`                             ###

Creates an array of `Unit` objects

(defined at scala.Array)


### `def apply[T](xs: T*)(implicit arg0: ClassTag[T]): Array[T]`             ###

Creates an array with given elements.

* xs
  * the elements to put in the array
* returns
  * an array containing all elements from xs.

(defined at scala.Array)


### `implicit def canBuildFrom[T](implicit t: ClassTag[T]): CanBuildFrom[Array[_], T, Array[T]]` ###

(defined at scala.Array)


### `def concat[T](xss: Array[T]*)(implicit arg0: ClassTag[T]): Array[T]`    ###

Concatenates all arrays into a single array.

* xss
  * the given arrays
* returns
  * the array created from concatenating `xss`

(defined at scala.Array)


### `def copy(src: AnyRef, srcPos: Int, dest: AnyRef, destPos: Int, length: Int): Unit` ###

Copy one array to another. Equivalent to Java's
 `System.arraycopy(src, srcPos, dest, destPos, length)` , except that this also
works for polymorphic and boxed arrays.

Note that the passed-in `dest` array will be modified by this call.

* src
  * the source array.
* srcPos
  * starting position in the source array.
* dest
  * destination array.
* destPos
  * starting position in the destination array.
* length
  * the number of array elements to be copied.

* See also
  * `java.lang.System#arraycopy`

(defined at scala.Array)


### `val emptyObjectArray: Array[AnyRef]`                                    ###

(defined at scala.Array)


### `def empty[T](implicit arg0: ClassTag[T]): Array[T]`                     ###

Returns an array of length 0

(defined at scala.Array)


### `def fill[T](n: Int)(elem: ⇒ T)(implicit arg0: ClassTag[T]): Array[T]`   ###

Returns an array that contains the results of some element computation a number
of times.

Note that this means that `elem` is computed a total of n times:

```scala
scala> Array.fill(3){ math.random }
res3: Array[Double] = Array(0.365461167592537, 1.550395944913685E-4, 0.7907242137333306)
```

* n
  * the number of elements desired
* elem
  * the element computation
* returns
  * an Array of size n, where each element contains the result of computing
     `elem` .

(defined at scala.Array)


### `def fill[T](n1: Int, n2: Int)(elem: ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[T]]` ###

Returns a two-dimensional array that contains the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* elem
  * the element computation

(defined at scala.Array)


### `def fill[T](n1: Int, n2: Int, n3: Int)(elem: ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[T]]]` ###

Returns a three-dimensional array that contains the results of some element
computation a number of times.

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3nd dimension
* elem
  * the element computation

(defined at scala.Array)


### `def fill[T](n1: Int, n2: Int, n3: Int, n4: Int)(elem: ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[T]]]]` ###

Returns a four-dimensional array that contains the results of some element
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

(defined at scala.Array)


### `def fill[T](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(elem: ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[Array[T]]]]]` ###

Returns a five-dimensional array that contains the results of some element
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

(defined at scala.Array)


### `def iterate[T](start: T, len: Int)(f: (T) ⇒ T)(implicit arg0: ClassTag[T]): Array[T]` ###

Returns an array containing repeated applications of a function to a start
value.

* start
  * the start value of the array
* len
  * the number of elements returned by the array
* f
  * the function that is repeatedly applied
* returns
  * the array returning `len` values in the sequence
     `start, f(start), f(f(start)), ...`

(defined at scala.Array)


### `def newBuilder[T](implicit t: ClassTag[T]): ArrayBuilder[T]`            ###

Returns a new scala.collection.mutable.ArrayBuilder.

(defined at scala.Array)


### `def ofDim[T](n1: Int)(implicit arg0: ClassTag[T]): Array[T]`            ###

Creates array with given dimensions

(defined at scala.Array)


### `def ofDim[T](n1: Int, n2: Int)(implicit arg0: ClassTag[T]): Array[Array[T]]` ###

Creates a 2-dimensional array

(defined at scala.Array)


### `def ofDim[T](n1: Int, n2: Int, n3: Int)(implicit arg0: ClassTag[T]): Array[Array[Array[T]]]` ###

Creates a 3-dimensional array

(defined at scala.Array)


### `def ofDim[T](n1: Int, n2: Int, n3: Int, n4: Int)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[T]]]]` ###

Creates a 4-dimensional array

(defined at scala.Array)


### `def ofDim[T](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[Array[T]]]]]` ###

Creates a 5-dimensional array

(defined at scala.Array)


### `def range(start: Int, end: Int): Array[Int]`                            ###

Returns an array containing a sequence of increasing integers in a range.

* start
  * the start value of the array
* end
  * the end value of the array, exclusive (in other words, this is the first
    value *not* returned)
* returns
  * the array with values in range `start, start + 1, ..., end - 1` up to, but
    excluding, `end` .

(defined at scala.Array)


### `def range(start: Int, end: Int, step: Int): Array[Int]`                 ###

Returns an array containing equally spaced values in some integer interval.

* start
  * the start value of the array
* end
  * the end value of the array, exclusive (in other words, this is the first
    value *not* returned)
* step
  * the increment value of the array (may not be zero)
* returns
  * the array with values in `start, start + step, ...` up to, but excluding
     `end`

(defined at scala.Array)


### `def tabulate[T](n: Int)(f: (Int) ⇒ T)(implicit arg0: ClassTag[T]): Array[T]` ###

Returns an array containing values of a given function over a range of integer
values starting from 0.

* n
  * The number of elements in the array
* f
  * The function computing element values
* returns
  * A traversable consisting of elements `f(0),f(1), ..., f(n - 1)`

(defined at scala.Array)


### `def tabulate[T](n1: Int, n2: Int)(f: (Int, Int) ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[T]]` ###

Returns a two-dimensional array containing values of a given function over
ranges of integer values starting from `0` .

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* f
  * The function computing element values

(defined at scala.Array)


### `def tabulate[T](n1: Int, n2: Int, n3: Int)(f: (Int, Int, Int) ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[T]]]` ###

Returns a three-dimensional array containing values of a given function over
ranges of integer values starting from `0` .

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3rd dimension
* f
  * The function computing element values

(defined at scala.Array)


### `def tabulate[T](n1: Int, n2: Int, n3: Int, n4: Int)(f: (Int, Int, Int, Int) ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[T]]]]` ###

Returns a four-dimensional array containing values of a given function over
ranges of integer values starting from `0` .

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3rd dimension
* n4
  * the number of elements in the 4th dimension
* f
  * The function computing element values

(defined at scala.Array)


### `def tabulate[T](n1: Int, n2: Int, n3: Int, n4: Int, n5: Int)(f: (Int, Int, Int, Int, Int) ⇒ T)(implicit arg0: ClassTag[T]): Array[Array[Array[Array[Array[T]]]]]` ###

Returns a five-dimensional array containing values of a given function over
ranges of integer values starting from `0` .

* n1
  * the number of elements in the 1st dimension
* n2
  * the number of elements in the 2nd dimension
* n3
  * the number of elements in the 3rd dimension
* n4
  * the number of elements in the 4th dimension
* n5
  * the number of elements in the 5th dimension
* f
  * The function computing element values

(defined at scala.Array)


### `def unapplySeq[T](x: Array[T]): Option[IndexedSeq[T]]`                  ###

Called in a pattern match like `{ case Array(x,y,z) => println('3 elements')}` .

* x
  * the selector value
* returns
  * sequence wrapped in a scala.Some, if `x` is a Seq, otherwise `None`

(defined at scala.Array)


--------------------------------------------------------------------------------
                 Value Members From scala.FallbackArrayBuilding
--------------------------------------------------------------------------------


### `implicit def fallbackCanBuildFrom[T](implicit m: DummyImplicit): CanBuildFrom[Array[_], T, ArraySeq[T]]` ###

A builder factory that generates a generic array. Called instead of
 `Array.newBuilder` if the element type of an array does not have a class tag.
Note that fallbackBuilder factory needs an implicit parameter (otherwise it
would not be dominated in implicit search by `Array.canBuildFrom` ). We make
sure that implicit search is always successful.

* Definition Classes
  * FallbackArrayBuilding
(defined at scala.FallbackArrayBuilding)
