
#                      scala.collection.generic.Growable                      #

```scala
trait Growable[-A] extends Clearable
```

This trait forms part of collections that can be augmented using a `+=` operator
and that can be cleared of all elements using a `clear` method.

* Source
  * [Growable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Growable.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


--------------------------------------------------------------------------------
         Abstract Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `abstract def +=(elem: A): Growable.this.type`                           ###

adds a single element to this growable collection.

* elem
  * the element to add.
* returns
  * the growable collection itself

(defined at scala.collection.generic.Growable)


--------------------------------------------------------------------------------
         Concrete Value Members From scala.collection.generic.Growable
--------------------------------------------------------------------------------


### `abstract def clear(): Unit`                                             ###

Clears the growable collection's contents. After this operation, the growable
collection is empty.

* Definition Classes
  * Growable → Clearable

(defined at scala.collection.generic.Growable)


### `def ++=(xs: TraversableOnce[A]): Growable.this.type`                    ###

adds all elements produced by a TraversableOnce to this growable collection.

* xs
  * the TraversableOnce producing the elements to add.
* returns
  * the growable collection itself.

(defined at scala.collection.generic.Growable)


### `def +=(elem1: A, elem2: A, elems: A*): Growable.this.type`              ###

adds two or more elements to this growable collection.

* elem1
  * the first element to add.
* elem2
  * the second element to add.
* elems
  * the remaining elements to add.
* returns
  * the growable collection itself
(defined at scala.collection.generic.Growable)
