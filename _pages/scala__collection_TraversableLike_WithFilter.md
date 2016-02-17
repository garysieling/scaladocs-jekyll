
#                 scala.collection.TraversableLike#WithFilter                 #

```scala
class WithFilter extends FilterMonadic[A, Repr]
```

A class supporting filtered operations. Instances of this class are returned by
method `withFilter` .

* Source
  * [TraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/TraversableLike.scala#L1)


--------------------------------------------------------------------------------
     Instance Constructors From scala.collection.TraversableLike.WithFilter
--------------------------------------------------------------------------------


### `new WithFilter(p: (A) ⇒ Boolean)`                                       ###

(defined at scala.collection.TraversableLike.WithFilter)


--------------------------------------------------------------------------------
         Value Members From scala.collection.TraversableLike.WithFilter
--------------------------------------------------------------------------------


### `def flatMap[B, That](f: (A) ⇒ GenTraversableOnce[B])(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of the outer
traversable collection containing this `WithFilter` instance that satisfy
predicate `p` and concatenating the results.

The type of the resulting collection will be guided by the static type of the
outer traversable collection.

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new traversable collection resulting from applying the given
    collection-valued function `f` to each element of the outer traversable
    collection that satisfies predicate `p` and concatenating the results.

* Definition Classes
  * WithFilter → FilterMonadic

(defined at scala.collection.TraversableLike.WithFilter)


### `def foreach[U](f: (A) ⇒ U): Unit`                                       ###

[use case]

Applies a function `f` to all elements of the outer traversable collection
containing this `WithFilter` instance that satisfy predicate `p` .

* f
  * the function that is applied for its side-effect to every element. The
    result of function `f` is discarded.

* Definition Classes
  * WithFilter → FilterMonadic

(defined at scala.collection.TraversableLike.WithFilter)


### `def map[B, That](f: (A) ⇒ B)(implicit bf: CanBuildFrom[Repr, B, That]): That` ###

[use case]

Builds a new collection by applying a function to all elements of the outer
traversable collection containing this `WithFilter` instance that satisfy
predicate `p` .

* B
  * the element type of the returned collection.
* f
  * the function to apply to each element.
* returns
  * a new traversable collection resulting from applying the given function `f`
    to each element of the outer traversable collection that satisfies predicate
     `p` and collecting the results.

* Definition Classes
  * WithFilter → FilterMonadic

(defined at scala.collection.TraversableLike.WithFilter)


### `def withFilter(q: (A) ⇒ Boolean): WithFilter`                           ###

Further refines the filter for this traversable collection.

* q
  * the predicate used to test elements.
* returns
  * an object of class `WithFilter` , which supports `map` , `flatMap` ,
     `foreach` , and `withFilter` operations. All these operations apply to
    those elements of this traversable collection which satisfy the predicate
     `q` in addition to the predicate `p` .

* Definition Classes
  * WithFilter → FilterMonadic

(defined at scala.collection.TraversableLike.WithFilter)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from WithFilter to
    CollectionsHaveToParArray [WithFilter, T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (WithFilter) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
