
#                          scala.collection.Iterator                          #

```scala
object Iterator
```

The `Iterator` object provides various functions for creating specialized
iterators.

* Source
  * [Iterator.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Iterator.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


--------------------------------------------------------------------------------
                  Value Members From scala.collection.Iterator
--------------------------------------------------------------------------------


### `implicit def IteratorCanBuildFrom[A]: BufferedCanBuildFrom[A, Iterator]` ###

With the advent of `TraversableOnce` and `Iterator` , it can be useful to have a
builder which operates on `Iterator` s so they can be treated uniformly along
with the collections. See `scala.util.Random.shuffle` for an example.

(defined at scala.collection.Iterator)


### `def apply[A](elems: A*): Iterator[A]`                                   ###

Creates an iterator with given elements.

* elems
  * The elements returned one-by-one from the iterator
* returns
  * An iterator which produces the given elements on the first calls to `next` ,
    and which has no further elements.

(defined at scala.collection.Iterator)


### `def continually[A](elem: ⇒ A): Iterator[A]`                             ###

Creates an infinite-length iterator returning the results of evaluating an
expression. The expression is recomputed for every element.

* elem
  * the element computation.
* returns
  * the iterator containing an infinite number of results of evaluating `elem` .

(defined at scala.collection.Iterator)


### `def fill[A](len: Int)(elem: ⇒ A): Iterator[A]`                          ###

Creates iterator that produces the results of some element computation a number
of times.

* len
  * the number of elements returned by the iterator.
* elem
  * the element computation
* returns
  * An iterator that produces the results of `n` evaluations of `elem` .

(defined at scala.collection.Iterator)


### `def from(start: Int): Iterator[Int]`                                    ###

Creates an infinite-length iterator which returns successive values from some
start value.

* start
  * the start value of the iterator
* returns
  * the iterator producing the infinite sequence of values
     `start, start + 1, start + 2, ...`

(defined at scala.collection.Iterator)


### `def from(start: Int, step: Int): Iterator[Int]`                         ###

Creates an infinite-length iterator returning values equally spaced apart.

* start
  * the start value of the iterator
* step
  * the increment between successive values
* returns
  * the iterator producing the infinite sequence of values
     `start, start + 1 * step, start + 2 * step, ...`

(defined at scala.collection.Iterator)


### `def iterate[T](start: T)(f: (T) ⇒ T): Iterator[T]`                      ###

Creates an infinite iterator that repeatedly applies a given function to the
previous result.

* start
  * the start value of the iterator
* f
  * the function that's repeatedly applied
* returns
  * the iterator producing the infinite sequence of values
     `start, f(start), f(f(start)), ...`

(defined at scala.collection.Iterator)


### `def range(start: Int, end: Int): Iterator[Int]`                         ###

Creates nn iterator returning successive values in some integer interval.

* start
  * the start value of the iterator
* end
  * the end value of the iterator (the first value NOT returned)
* returns
  * the iterator producing values `start, start + 1, ..., end - 1`

(defined at scala.collection.Iterator)


### `def range(start: Int, end: Int, step: Int): Iterator[Int]`              ###

An iterator producing equally spaced values in some integer interval.

* start
  * the start value of the iterator
* end
  * the end value of the iterator (the first value NOT returned)
* step
  * the increment value of the iterator (must be positive or negative)
* returns
  * the iterator producing values `start, start + step, ...` up to, but
    excluding `end`

(defined at scala.collection.Iterator)


### `def single[A](elem: A): Iterator[A]`                                    ###

Creates an iterator which produces a single element. *Note:* Equivalent, but
more efficient than Iterator(elem)

* elem
  * the element
* returns
  * An iterator which produces `elem` on the first call to `next` , and which
    has no further elements.

(defined at scala.collection.Iterator)


### `def tabulate[A](end: Int)(f: (Int) ⇒ A): Iterator[A]`                   ###

Creates an iterator producing the values of a given function over a range of
integer values starting from 0.

* end
  * The number of elements returned by the iterator
* f
  * The function computing element values
* returns
  * An iterator that produces the values `f(0), ..., f(n -1)` .
(defined at scala.collection.Iterator)
