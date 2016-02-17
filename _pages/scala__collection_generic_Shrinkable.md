
#                     scala.collection.generic.Shrinkable                     #

```scala
trait Shrinkable[-A] extends AnyRef
```

This trait forms part of collections that can be reduced using a `-=` operator.

* Source
  * [Shrinkable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Shrinkable.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


--------------------------------------------------------------------------------
        Abstract Value Members From scala.collection.generic.Shrinkable
--------------------------------------------------------------------------------


### `abstract def -=(elem: A): Shrinkable.this.type`                         ###

Removes a single element from this shrinkable collection.

* elem
  * the element to remove.
* returns
  * the shrinkable collection itself

(defined at scala.collection.generic.Shrinkable)


--------------------------------------------------------------------------------
        Concrete Value Members From scala.collection.generic.Shrinkable
--------------------------------------------------------------------------------


### `def --=(xs: TraversableOnce[A]): Shrinkable.this.type`                  ###

Removes all elements produced by an iterator from this shrinkable collection.

* xs
  * the iterator producing the elements to remove.
* returns
  * the shrinkable collection itself

(defined at scala.collection.generic.Shrinkable)


### `def -=(elem1: A, elem2: A, elems: A*): Shrinkable.this.type`            ###

Removes two or more elements from this shrinkable collection.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * the shrinkable collection itself
(defined at scala.collection.generic.Shrinkable)
