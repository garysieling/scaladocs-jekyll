
#               scala.collection.parallel.ParSeqLike#ReverseMap               #

```scala
class ReverseMap[S, That] extends Transformer[Combiner[S, That], ReverseMap[S, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParSeqLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[S, That]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[S, That], ReverseMap[S, That]]]`     ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.ParSeqLike.ReverseMap
--------------------------------------------------------------------------------


### `new ReverseMap(f: (T) ⇒ S, pbf: () ⇒ Combiner[S, That], pit: SeqSplitter[T])` ###

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParSeqLike.ReverseMap
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[S, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ReverseMap → Task

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


### `def merge(that: ReverseMap[S, That]): Unit`                             ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * ReverseMap → Task

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


### `def newSubtask(p: SuperParIterator): ReverseMap[S, That]`               ###

* Attributes
  * protected[this]
* Definition Classes
  * ReverseMap → Accessor

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


### `val pit: SeqSplitter[T]`                                                ###

* Attributes
  * protected[this]
* Definition Classes
  * ReverseMap → Accessor → Accessor

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


### `var result: Combiner[S, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * ReverseMap → Task

(defined at scala.collection.parallel.ParSeqLike.ReverseMap)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ReverseMap[S, That]`                                          ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ReverseMap [S, That] to
    CollectionsHaveToParArray [ReverseMap [S, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ReverseMap [S, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
