
#               scala.collection.mutable.UnrolledBuffer.Unrolled               #

```scala
class Unrolled[T] extends AnyRef
```

Unrolled buffer node.

* Source
  * [UnrolledBuffer.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/mutable/UnrolledBuffer.scala#L1)


--------------------------------------------------------------------------------
      Value Members From scala.collection.mutable.UnrolledBuffer.Unrolled
--------------------------------------------------------------------------------


### `final def append(elem: T): Unrolled[T]`                                 ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `final def apply(idx: Int): T`                                           ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `def bind(thathead: Unrolled[T]): Boolean`                               ###

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `val buff: UnrolledBuffer[T]`                                            ###

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `def foreach[U](f: (T) ⇒ U): Unit`                                       ###

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `final def insertAll(idx: Int, t: collection.Traversable[T], buffer: UnrolledBuffer[T]): Unit` ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `final def locate(idx: Int): Unrolled[T]`                                ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `var next: Unrolled[T]`                                                  ###

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `def prepend(elem: T): Unrolled[T]`                                      ###

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `final def remove(idx: Int, buffer: UnrolledBuffer[T]): T`               ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


### `final def update(idx: Int, newelem: T): Unit`                           ###

* Annotations
  * @ tailrec ()

(defined at scala.collection.mutable.UnrolledBuffer.Unrolled)


--------------------------------------------------------------------------------
Value Members From Implicit scala.collection.parallel.CollectionsHaveToParArray
--------------------------------------------------------------------------------


### `def toParArray: ParArray[T]`                                            ###

* Implicit information
  * This member is added by an implicit conversion from Unrolled [T] to
    CollectionsHaveToParArray [Unrolled [T], T] performed by method
    CollectionsHaveToParArray in scala.collection.parallel. This conversion will
    take place only if an implicit value of type (Unrolled [T]) ⇒
    GenTraversableOnce [T] is in scope.
* Definition Classes
  * CollectionsHaveToParArray
(added by implicit convertion: scala.collection.parallel.CollectionsHaveToParArray)
