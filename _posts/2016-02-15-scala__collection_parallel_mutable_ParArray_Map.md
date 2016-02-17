
#                scala.collection.parallel.mutable.ParArray#Map                #

```scala
class Map[S] extends Task[Unit, Map[S]]
```

* Source
  * [ParArray.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/mutable/ParArray.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = Unit`                                                     ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Map[S]`                                                       ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
   Instance Constructors From scala.collection.parallel.mutable.ParArray.Map
--------------------------------------------------------------------------------


### `new Map(f: (T) ⇒ S, targetarr: Array[Any], offset: Int, howmany: Int)`  ###

(defined at scala.collection.parallel.mutable.ParArray.Map)


--------------------------------------------------------------------------------
       Value Members From scala.collection.parallel.mutable.ParArray.Map
--------------------------------------------------------------------------------


### `def leaf(prev: Option[Unit]): Unit`                                     ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Map → Task

(defined at scala.collection.parallel.mutable.ParArray.Map)


### `def split: immutable.List[Map[S]]`                                      ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Map → Task

(defined at scala.collection.parallel.mutable.ParArray.Map)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Map [S] to
    CollectionsHaveToParArray [Map [S], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Map [S]) ⇒ GenTraversableOnce
    [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
