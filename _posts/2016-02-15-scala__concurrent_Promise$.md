
#                           scala.concurrent.Promise                           #

```scala
object Promise
```

* Source
  * [Promise.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/concurrent/Promise.scala#L1)


--------------------------------------------------------------------------------
                  Value Members From scala.concurrent.Promise
--------------------------------------------------------------------------------


### `def apply[T](): Promise[T]`                                             ###

Creates a promise object which can be completed with a value.

* T
  * the type of the value in the promise
* returns
  * the newly created `Promise` object

(defined at scala.concurrent.Promise)


### `def failed[T](exception: Throwable): Promise[T]`                        ###

Creates an already completed Promise with the specified exception.

* T
  * the type of the value in the promise
* returns
  * the newly created `Promise` object

(defined at scala.concurrent.Promise)


### `def fromTry[T](result: Try[T]): Promise[T]`                             ###

Creates an already completed Promise with the specified result or exception.

* T
  * the type of the value in the promise
* returns
  * the newly created `Promise` object

(defined at scala.concurrent.Promise)


### `def successful[T](result: T): Promise[T]`                               ###

Creates an already completed Promise with the specified result.

* T
  * the type of the value in the promise
* returns
  * the newly created `Promise` object
(defined at scala.concurrent.Promise)
