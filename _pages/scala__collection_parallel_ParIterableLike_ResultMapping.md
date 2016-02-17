
#           scala.collection.parallel.ParIterableLike#ResultMapping           #

```scala
abstract class ResultMapping[R, Tp, R1] extends NonDivisibleTask[R1, ResultMapping[R, Tp, R1]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = R1`                                                       ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
Abstract Value Members From scala.collection.parallel.ParIterableLike.ResultMapping
--------------------------------------------------------------------------------


### `abstract def map(r: R): R1`                                             ###

(defined at scala.collection.parallel.ParIterableLike.ResultMapping)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.ParIterableLike.ResultMapping
--------------------------------------------------------------------------------


### `val inner: StrictSplitterCheckTask[R, Tp]`                              ###

(defined at scala.collection.parallel.ParIterableLike.ResultMapping)


### `def leaf(prevr: Option[R1]): Unit`                                      ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ResultMapping → Task

(defined at scala.collection.parallel.ParIterableLike.ResultMapping)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.ResultMapping
--------------------------------------------------------------------------------


### `new ResultMapping(inner: StrictSplitterCheckTask[R, Tp])`               ###

(defined at scala.collection.parallel.ParIterableLike.ResultMapping)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ResultMapping[R, Tp, R1]`                                     ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ResultMapping [R, Tp, R1]
    to CollectionsHaveToParArray [ResultMapping [R, Tp, R1], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (ResultMapping
    [R, Tp, R1]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
