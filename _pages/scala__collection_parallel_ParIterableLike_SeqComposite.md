
#            scala.collection.parallel.ParIterableLike#SeqComposite            #

```scala
abstract class SeqComposite[FR, SR, R, First <: StrictSplitterCheckTask[FR, _], Second <: StrictSplitterCheckTask[SR, _]] extends Composite[FR, SR, R, First, Second]
```

Sequentially performs one task after another.

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

* Definition Classes
  * Composite

(defined at scala.collection.parallel.ParIterableLike.Composite)


--------------------------------------------------------------------------------
Concrete Value Members From scala.collection.parallel.ParIterableLike.SeqComposite
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[R]): Unit`                                       ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * SeqComposite → Task

(defined at scala.collection.parallel.ParIterableLike.SeqComposite)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.SeqComposite
--------------------------------------------------------------------------------


### `new SeqComposite(f: First, s: Second)`                                  ###

(defined at scala.collection.parallel.ParIterableLike.SeqComposite)


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
  * This member is added by an implicit conversion from SeqComposite [FR, SR, R,
    First, Second] to CollectionsHaveToParArray [SeqComposite [FR, SR, R, First,
    Second], T] performed by method CollectionsHaveToParArray in
    scala.collection.parallel. This conversion will take place only if an
    implicit value of type (SeqComposite [FR, SR, R, First, Second]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
