
#                              scala.util.Sorting                              #

```scala
object Sorting
```

The `Sorting` object provides convenience wrappers for `java.util.Arrays.sort` .
Methods that defer to `java.util.Arrays.sort` say that they do or under what
conditions that they do.

 `Sorting` also implements a general-purpose quicksort and stable (merge) sort
for those cases where `java.util.Arrays.sort` could only be used at the cost of
a large memory penalty. If performance rather than memory usage is the primary
concern, one may wish to find alternate strategies to use
 `java.util.Arrays.sort` directly e.g. by boxing primitives to use a custom
ordering on them.

 `Sorting` provides methods where you can provide a comparison function, or can
request a sort of items that are scala.math.Ordered or that otherwise have an
implicit or explicit scala.math.Ordering.

Note also that high-performance non-default sorts for numeric types are not
provided. If this is required, it is advisable to investigate other libraries
that cover this use case.

* Source
  * [Sorting.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/Sorting.scala#L1)
* Version
  * 1.1


--------------------------------------------------------------------------------
                     Value Members From scala.util.Sorting
--------------------------------------------------------------------------------


### `def quickSort(a: Array[Double]): Unit`                                  ###

Sort an array of Doubles using `java.util.Arrays.sort` .

(defined at scala.util.Sorting)


### `def quickSort(a: Array[Float]): Unit`                                   ###

Sort an array of Floats using `java.util.Arrays.sort` .

(defined at scala.util.Sorting)


### `def quickSort(a: Array[Int]): Unit`                                     ###

Sort an array of Ints using `java.util.Arrays.sort` .

(defined at scala.util.Sorting)


### `def quickSort[K](a: Array[K])(implicit arg0: math.Ordering[K]): Unit`   ###

Sort array `a` with quicksort, using the Ordering on its elements. This
algorithm sorts in place, so no additional memory is used aside from what might
be required to box individual elements during comparison.

(defined at scala.util.Sorting)


### `def stableSort[K, M](a: Seq[K], f: (K) ⇒ M)(implicit arg0: ClassTag[K], arg1: math.Ordering[M]): Array[K]` ###

A sorted Array, given an extraction function `f` that returns an ordered key for
each item in the sequence `a` . Uses `java.util.Arrays.sort` unless `K` is a
primitive type.

(defined at scala.util.Sorting)


### `def stableSort[K](a: Array[K])(implicit arg0: ClassTag[K], arg1: math.Ordering[K]): Unit` ###

Sort array `a` using the Ordering on its elements, preserving the original
ordering where possible. Uses `java.util.Arrays.sort` unless `K` is a primitive
type.

(defined at scala.util.Sorting)


### `def stableSort[K](a: Array[K], f: (K, K) ⇒ Boolean)(implicit arg0: ClassTag[K]): Unit` ###

Sort array `a` using function `f` that computes the less-than relation for each
element. Uses `java.util.Arrays.sort` unless `K` is a primitive type.

(defined at scala.util.Sorting)


### `def stableSort[K](a: Seq[K])(implicit arg0: ClassTag[K], arg1: math.Ordering[K]): Array[K]` ###

A sorted Array, using the Ordering for the elements in the sequence `a` . Uses
 `java.util.Arrays.sort` unless `K` is a primitive type.

(defined at scala.util.Sorting)


### `def stableSort[K](a: Seq[K], f: (K, K) ⇒ Boolean)(implicit arg0: ClassTag[K]): Array[K]` ###

A sorted Array, given a function `f` that computes the less-than relation for
each item in the sequence `a` . Uses `java.util.Arrays.sort` unless `K` is a
primitive type.
(defined at scala.util.Sorting)
