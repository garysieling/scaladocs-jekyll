
#                   scala.collection.parallel.ParSeqLike#Zip                   #

```scala
class Zip[U >: T, S, That] extends Transformer[Combiner[(U, S), That], Zip[U, S, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[(U, S), That]`                                   ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
      Instance Constructors From scala.collection.parallel.ParSeqLike.Zip
--------------------------------------------------------------------------------


### `new Zip(len: Int, cf: CombinerFactory[(U, S), That], pit: SeqSplitter[T], otherpit: SeqSplitter[S])` ###

(defined at scala.collection.parallel.ParSeqLike.Zip)


--------------------------------------------------------------------------------
          Value Members From scala.collection.parallel.ParSeqLike.Zip
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Result]): Unit`                                   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `def merge(that: Zip[U, S, That]): Unit`                                 ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `def newSubtask(p: SuperParIterator): Nothing`                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Zip → Accessor

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `val otherpit: SeqSplitter[S]`                                           ###

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * Zip → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `var result: Result`                                                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Zip → Task

(defined at scala.collection.parallel.ParSeqLike.Zip)


### `def split: Seq[Zip[U, S, That]]`                                        ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Zip → Accessor → Task

(defined at scala.collection.parallel.ParSeqLike.Zip)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Zip[U, S, That]`                                              ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Zip [U, S, That] to
    CollectionsHaveToParArray [Zip [U, S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Zip [U, S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
