
#            scala.collection.parallel.ParIterableLike#NonDivisible            #

```scala
trait NonDivisible[R] extends NonDivisibleTask[R, NonDivisible[R]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = R`                                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
           Abstract Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `abstract def leaf(result: Option[R]): Unit`                             ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
           Concrete Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `abstract val result: R`                                                 ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


### `def repr: NonDivisible[R]`                                              ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from NonDivisible [R] to
    CollectionsHaveToParArray [NonDivisible [R], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (NonDivisible [R]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
