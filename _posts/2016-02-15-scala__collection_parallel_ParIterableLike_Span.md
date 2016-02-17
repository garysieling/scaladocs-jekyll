
#                scala.collection.parallel.ParIterableLike#Span                #

```scala
class Span[U >: T, This >: Repr] extends Transformer[(Combiner[U, This], Combiner[U, This]), Span[U, This]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = (Combiner[U, This], Combiner[U, This])`                   ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.ParIterableLike.Span
--------------------------------------------------------------------------------


### `new Span(pos: Int, pred: (T) ⇒ Boolean, cbfBefore: CombinerFactory[U, This], cbfAfter: CombinerFactory[U, This], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Span)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Span
--------------------------------------------------------------------------------


### `def leaf(prev: Option[(Combiner[U, This], Combiner[U, This])]): Unit`   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Span → Task

(defined at scala.collection.parallel.ParIterableLike.Span)


### `def merge(that: Span[U, This]): Unit`                                   ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Span → Task

(defined at scala.collection.parallel.ParIterableLike.Span)


### `def newSubtask(p: IterableSplitter[T]): Nothing`                        ###

* Attributes
  * protected[this]
* Definition Classes
  * Span → Accessor

(defined at scala.collection.parallel.ParIterableLike.Span)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Span → Accessor

(defined at scala.collection.parallel.ParIterableLike.Span)


### `var result: (Combiner[U, This], Combiner[U, This])`                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Span → Task

(defined at scala.collection.parallel.ParIterableLike.Span)


### `def split: scala.Seq[Task[(Combiner[U, This], Combiner[U, This]), Span[U, This]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Span → Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Span)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Span[U, This]`                                                ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Span [U, This] to
    CollectionsHaveToParArray [Span [U, This], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Span [U, This]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
