
#          scala.collection.parallel.ParIterableLike#ToParCollection          #

```scala
class ToParCollection[U >: T, That] extends Transformer[Combiner[U, That], ToParCollection[U, That]]
```

* Attributes
  * protected[this]
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


### `def split: scala.Seq[Task[Combiner[U, That], ToParCollection[U, That]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
Instance Constructors From scala.collection.parallel.ParIterableLike.ToParCollection
--------------------------------------------------------------------------------


### `new ToParCollection(cbf: CombinerFactory[U, That], pit: IterableSplitter[T])` ###

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


--------------------------------------------------------------------------------
  Value Members From scala.collection.parallel.ParIterableLike.ToParCollection
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[U, That]]): Unit`                        ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ToParCollection → Task

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


### `def merge(that: ToParCollection[U, That]): Unit`                        ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * ToParCollection → Task

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


### `def newSubtask(p: IterableSplitter[T]): ToParCollection[U, That]`       ###

* Attributes
  * protected[this]
* Definition Classes
  * ToParCollection → Accessor

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * ToParCollection → Accessor

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


### `var result: Result`                                                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * ToParCollection → Task

(defined at scala.collection.parallel.ParIterableLike.ToParCollection)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ToParCollection[U, That]`                                     ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ToParCollection [U, That]
    to CollectionsHaveToParArray [ToParCollection [U, That], T] performed by
    method CollectionsHaveToParArray in scala.collection.parallel. This
    conversion will take place only if an implicit value of type (
    ToParCollection [U, That]) ⇒ GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
