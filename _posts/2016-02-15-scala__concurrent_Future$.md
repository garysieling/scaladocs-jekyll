
#                           scala.concurrent.Future                           #

```scala
object Future
```

Future companion object.

* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object never extends Future[Nothing]`                                   ###

A Future which is never completed.

* Source
  * [Future.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Future.scala#L1)


--------------------------------------------------------------------------------
             Deprecated Value Members From scala.concurrent.Future
--------------------------------------------------------------------------------


### `def find[T](futures: TraversableOnce[Future[T]])(p: (T) ⇒ Boolean)(implicit executor: ExecutionContext): Future[Option[T]]` ###

Asynchronously and non-blockingly returns a `Future` that will hold the optional
result of the first `Future` with a result that matches the predicate.

* T
  * the type of the value in the future
* futures
  * the `TraversableOnce` of Futures to search
* p
  * the predicate which indicates if it's a match
* returns
  * the `Future` holding the optional result of the search

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12)_ Use the overloaded version of this method that takes
    a scala.collection.immutable.Iterable instead

(defined at scala.concurrent.Future)


### `def fold[T, R](futures: TraversableOnce[Future[T]])(zero: R)(op: (R, T) ⇒ R)(implicit executor: ExecutionContext): Future[R]` ###

A non-blocking, asynchronous fold over the specified futures, with the start
value of the given zero. The fold is performed on the thread where the last
future is completed, the result will be the first failure of any of the futures,
or any failure in the actual fold, or the result of the fold.

Example:

```scala
val futureSum = Future.fold(futures)(0)(_ + _)
```

* T
  * the type of the value of the input Futures
* R
  * the type of the value of the returned `Future`
* futures
  * the `TraversableOnce` of Futures to be folded
* zero
  * the start value of the fold
* op
  * the fold operation to be applied to the zero and futures
* returns
  * the `Future` holding the result of the fold

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12)_ Use Future.foldLeft instead

(defined at scala.concurrent.Future)


### `def reduce[T, R >: T](futures: TraversableOnce[Future[T]])(op: (R, T) ⇒ R)(implicit executor: ExecutionContext): Future[R]` ###

Initiates a non-blocking, asynchronous, fold over the supplied futures where the
fold-zero is the result value of the `Future` that's completed first.

Example:

```scala
val futureSum = Future.reduce(futures)(_ + _)
```

* T
  * the type of the value of the input Futures
* R
  * the type of the value of the returned `Future`
* futures
  * the `TraversableOnce` of Futures to be reduced
* op
  * the reduce operation which is applied to the results of the futures
* returns
  * the `Future` holding the result of the reduce

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.12)_ Use Future.reduceLeft instead

(defined at scala.concurrent.Future)


--------------------------------------------------------------------------------
                   Value Members From scala.concurrent.Future
--------------------------------------------------------------------------------


### `def apply[T](body: ⇒ T)(implicit executor: ExecutionContext): Future[T]` ###

Starts an asynchronous computation and returns a `Future` instance with the
result of that computation.

The result becomes available once the asynchronous computation is completed.

* T
  * the type of the result
* body
  * the asynchronous computation
* executor
  * the execution context on which the future is run
* returns
  * the `Future` holding the result of the computation

(defined at scala.concurrent.Future)


### `def failed[T](exception: Throwable): Future[T]`                         ###

Creates an already completed Future with the specified exception.

* T
  * the type of the value in the future
* exception
  * the non-null instance of `Throwable`
* returns
  * the newly created `Future` instance

(defined at scala.concurrent.Future)


### `def find[T](futures: collection.immutable.Iterable[Future[T]])(p: (T) ⇒ Boolean)(implicit executor: ExecutionContext): Future[Option[T]]` ###

Asynchronously and non-blockingly returns a `Future` that will hold the optional
result of the first `Future` with a result that matches the predicate, failed
 `Future` s will be ignored.

* T
  * the type of the value in the future
* futures
  * the `scala.collection.immutable.Iterable` of Futures to search
* p
  * the predicate which indicates if it's a match
* returns
  * the `Future` holding the optional result of the search

(defined at scala.concurrent.Future)


### `def firstCompletedOf[T](futures: TraversableOnce[Future[T]])(implicit executor: ExecutionContext): Future[T]` ###

Asynchronously and non-blockingly returns a new `Future` to the result of the
first future in the list that is completed. This means no matter if it is
completed as a success or as a failure.

* T
  * the type of the value in the future
* futures
  * the `TraversableOnce` of Futures in which to find the first completed
* returns
  * the `Future` holding the result of the future that is first to be completed

(defined at scala.concurrent.Future)


### `def foldLeft[T, R](futures: collection.immutable.Iterable[Future[T]])(zero: R)(op: (R, T) ⇒ R)(implicit executor: ExecutionContext): Future[R]` ###

A non-blocking, asynchronous left fold over the specified futures, with the
start value of the given zero. The fold is performed asynchronously in
left-to-right order as the futures become completed. The result will be the
first failure of any of the futures, or any failure in the actual fold, or the
result of the fold.

Example:

```scala
val futureSum = Future.foldLeft(futures)(0)(_ + _)
```

* T
  * the type of the value of the input Futures
* R
  * the type of the value of the returned `Future`
* futures
  * the `scala.collection.immutable.Iterable` of Futures to be folded
* zero
  * the start value of the fold
* op
  * the fold operation to be applied to the zero and futures
* returns
  * the `Future` holding the result of the fold

(defined at scala.concurrent.Future)


### `def fromTry[T](result: Try[T]): Future[T]`                              ###

Creates an already completed Future with the specified result or exception.

* T
  * the type of the value in the `Future`
* result
  * the result of the returned `Future` instance
* returns
  * the newly created `Future` instance

(defined at scala.concurrent.Future)


### `def reduceLeft[T, R >: T](futures: collection.immutable.Iterable[Future[T]])(op: (R, T) ⇒ R)(implicit executor: ExecutionContext): Future[R]` ###

Initiates a non-blocking, asynchronous, left reduction over the supplied futures
where the zero is the result value of the first `Future` .

Example:

```scala
val futureSum = Future.reduceLeft(futures)(_ + _)
```

* T
  * the type of the value of the input Futures
* R
  * the type of the value of the returned `Future`
* futures
  * the `scala.collection.immutable.Iterable` of Futures to be reduced
* op
  * the reduce operation which is applied to the results of the futures
* returns
  * the `Future` holding the result of the reduce

(defined at scala.concurrent.Future)


### `def sequence[A, M[X] <: TraversableOnce[X]](in: M[Future[A]])(implicit cbf: CanBuildFrom[M[Future[A]], A, M[A]], executor: ExecutionContext): Future[M[A]]` ###

Simple version of `Future.traverse` . Asynchronously and non-blockingly
transforms a `TraversableOnce[Future[A]]` into a `Future[TraversableOnce[A]]` .
Useful for reducing many `Future` s into a single `Future` .

* A
  * the type of the value inside the Futures
* M
  * the type of the `TraversableOnce` of Futures
* in
  * the `TraversableOnce` of Futures which will be sequenced
* returns
  * the `Future` of the `TraversableOnce` of results

(defined at scala.concurrent.Future)


### `def successful[T](result: T): Future[T]`                                ###

Creates an already completed Future with the specified result.

* T
  * the type of the value in the future
* result
  * the given successful value
* returns
  * the newly created `Future` instance

(defined at scala.concurrent.Future)


### `def traverse[A, B, M[X] <: TraversableOnce[X]](in: M[A])(fn: (A) ⇒ Future[B])(implicit cbf: CanBuildFrom[M[A], B, M[B]], executor: ExecutionContext): Future[M[B]]` ###

Asynchronously and non-blockingly transforms a `TraversableOnce[A]` into a
 `Future[TraversableOnce[B]]` using the provided function `A => Future[B]` .
This is useful for performing a parallel map. For example, to apply a function
to all items of a list in parallel:

```scala
val myFutureList = Future.traverse(myList)(x => Future(myFunc(x)))
```

* A
  * the type of the value inside the Futures in the `TraversableOnce`
* B
  * the type of the value of the returned `Future`
* M
  * the type of the `TraversableOnce` of Futures
* in
  * the `TraversableOnce` of Futures which will be sequenced
* fn
  * the function to apply to the `TraversableOnce` of Futures to produce the
    results
* returns
  * the `Future` of the `TraversableOnce` of results

(defined at scala.concurrent.Future)


### `val unit: Future[Unit]`                                                 ###

A Future which is always completed with the Unit value.
(defined at scala.concurrent.Future)
