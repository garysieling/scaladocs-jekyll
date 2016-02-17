
#              scala.collection.parallel.ParIterableLike#Product              #

```scala
class Product[U >: T] extends Accessor[U, Product[U]]
```

* Attributes
  * protected[this]
* Source
  * [ParIterableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/parallel/ParIterableLike.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `type Result = U`                                                        ###

* Definition Classes
  * Task


--------------------------------------------------------------------------------
     Value Members From scala.collection.parallel.ParIterableLike.Accessor
--------------------------------------------------------------------------------


### `def split: scala.Seq[Task[U, Product[U]]]`                              ###

Splits this task into a list of smaller tasks.

* Definition Classes
  * Accessor → Task

(defined at scala.collection.parallel.ParIterableLike.Accessor)


--------------------------------------------------------------------------------
  Instance Constructors From scala.collection.parallel.ParIterableLike.Product
--------------------------------------------------------------------------------


### `new Product(num: Numeric[U], pit: IterableSplitter[T])`                 ###

(defined at scala.collection.parallel.ParIterableLike.Product)


--------------------------------------------------------------------------------
      Value Members From scala.collection.parallel.ParIterableLike.Product
--------------------------------------------------------------------------------


### `def leaf(prevr: Option[U]): Unit`                                       ###

Body of the task - non-divisible unit of work done by this task. Optionally is
provided with the result from the previous completed task or `None` if there was
no previous task (or the previous task is uncompleted or unknown).

* Definition Classes
  * Product → Task

(defined at scala.collection.parallel.ParIterableLike.Product)


### `def merge(that: Product[U]): Unit`                                      ###

Read of results of `that` task and merge them into results of this one.

* Definition Classes
  * Product → Task

(defined at scala.collection.parallel.ParIterableLike.Product)


### `def newSubtask(p: IterableSplitter[T]): Product[U]`                     ###

* Attributes
  * protected[this]
* Definition Classes
  * Product → Accessor

(defined at scala.collection.parallel.ParIterableLike.Product)


### `val pit: IterableSplitter[T]`                                           ###

* Attributes
  * protected[this]
* Definition Classes
  * Product → Accessor

(defined at scala.collection.parallel.ParIterableLike.Product)


--------------------------------------------------------------------------------
               Value Members From scala.collection.parallel.Task
--------------------------------------------------------------------------------


### `def repr: Product[U]`                                                   ###

* Definition Classes
  * Task

(defined at scala.collection.parallel.Task)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Product [U] to
    CollectionsHaveToParArray [Product [U], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Product [U]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
