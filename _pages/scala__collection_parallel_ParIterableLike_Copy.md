
#                scala.collection.parallel.ParIterableLike#Copy                #

```scala
class Copy[U >: T, That] extends Transformer[Combiner[U, That], Copy[U, That]]
```

* Attributes
  * protected
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[U, That]`                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[U, That], Copy[U, That]]]`           ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.ParIterableLike.Copy
--------------------------------------------------------------------------------


### `new Copy(cfactory: CombinerFactory[U, That], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.Copy)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.ParIterableLike.Copy
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Copy → Task

(defined at scala.collection.parallel.ParIterableLike.Copy)


### `def merge(that: Copy[U, That]): Unit`                                   ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Copy → Task

(defined at scala.collection.parallel.ParIterableLike.Copy)


### `def newSubtask(p: IterableSplitter[T]): Copy[U, That]`                  ###

* Attributes
  * protected[this]
* Definition Classes
  * Copy → Accessor

(defined at scala.collection.parallel.ParIterableLike.Copy)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Copy → Accessor

(defined at scala.collection.parallel.ParIterableLike.Copy)


### `var result: Combiner[U, That]`                                          ###

A result that can be accessed once the task is completed.

* Definition Classes
  * Copy → Task

(defined at scala.collection.parallel.ParIterableLike.Copy)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Copy[U, That]`                                                ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Copy [U, That] to
    CollectionsHaveToParArray [Copy [U, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Copy [U, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
