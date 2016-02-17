
#             scala.collection.parallel.ParIterableLike#Composite             #

```scala
abstract class Composite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends NonDivisibleTask[R, Composite[FR, SR, R, First, Second]]
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
Abstract Value Members From scala.collection.parallel.ParIterableLike.Composite
--------------------------------------------------------------------------------


### `abstract def combineResults(fr: FR, sr: SR): R`                         ###

(defined at scala.collection.parallel.ParIterableLike.Composite)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.Composite
--------------------------------------------------------------------------------


### `new Composite(ft: First, st: Second)`                                   ###

(defined at scala.collection.parallel.ParIterableLike.Composite)


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


### `def repr: Composite[FR, SR, R, First, Second]`                          ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Concrete Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Composite [FR, SR, R,
    First, Second] to CollectionsHaveToParArray [Composite [FR, SR, R, First,
    Second], T] performed by method CollectionsHaveToParArray in
    scala.collection.parallel. This conversion will take place only if an
    implicit value of type (Composite [FR, SR, R, First, Second]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
