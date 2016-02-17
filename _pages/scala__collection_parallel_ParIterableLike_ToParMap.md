
#              scala.collection.parallel.ParIterableLike#ToParMap              #

```scala
class ToParMap[K, V, That] extends Transformer[Combiner[(K, V), That], ToParMap[K, V, That]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Combiner[(K, V), That]`                                   ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[Combiner[(K, V), That], ToParMap[K, V, That]]]` ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
 Instance Constructors From scala.collection.parallel.ParIterableLike.ToParMap
--------------------------------------------------------------------------------


### `new ToParMap(cbf: CombinerFactory[(K, V), That], pit: IterableSplitter[T])(implicit ev: <:<[T, (K, V)])` ###

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.ToParMap
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Combiner[(K, V), That]]): Unit`                   ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * ToParMap → Task

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


### `def merge(that: ToParMap[K, V, That]): Unit`                            ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * ToParMap → Task

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


### `def newSubtask(p: IterableSplitter[T]): ToParMap[K, V, That]`           ###

* Attributes
  * protected[this]
* Definition Classes
  * ToParMap → Accessor

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * ToParMap → Accessor

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


### `var result: Result`                                                     ###

A result that can be accessed once the task is completed.

* Definition Classes
  * ToParMap → Task

(defined at scala.collection.parallel.ParIterableLike.ToParMap)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: ToParMap[K, V, That]`                                         ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from ToParMap [K, V, That] to
    CollectionsHaveToParArray [ToParMap [K, V, That], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (ToParMap [K, V, That]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
