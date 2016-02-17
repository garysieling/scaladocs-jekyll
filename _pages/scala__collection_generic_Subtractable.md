
#                    scala.collection.generic.Subtractable                    #

```scala
trait Subtractable[A, +Repr <: Subtractable[A, Repr]] extends AnyRef
```

This trait represents collection-like objects that can be reduced using a '+'
operator. It defines variants of `-` and `--` as convenience methods in terms of
single-element removal `-` .

* A
  * the type of the elements of the collection.
* Repr
  * the type of the collection itself

* Self Type
  * Subtractable [A, Repr]
* Source
  * [Subtractable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Subtractable.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.Subtractable
--------------------------------------------------------------------------------


### `abstract def -(elem: A): Repr`                                          ###

Creates a new collection from this collection with an element removed.

* elem
  * the element to remove
* returns
  * a new collection that contains all elements of the current collection except
    one less occurrence of `elem` .

(defined at scala.collection.generic.Subtractable)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.generic.Subtractable
--------------------------------------------------------------------------------


### `abstract def repr: Repr`                                                ###

The representation object of type `Repr` which contains the collection's
elements

* Attributes
  * protected

(defined at scala.collection.generic.Subtractable)


### `def -(elem1: A, elem2: A, elems: A*): Repr`                             ###

Creates a new collection from this collection with some elements removed.

This method takes two or more elements to be removed. Another overloaded variant
of this method handles the case where a single element is removed.

* elem1
  * the first element to remove.
* elem2
  * the second element to remove.
* elems
  * the remaining elements to remove.
* returns
  * a new collection that contains all elements of the current collection except
    one less occurrence of each of the given elements.

(defined at scala.collection.generic.Subtractable)


### `def --(xs: GenTraversableOnce[A]): Repr`                                ###

Creates a new collection from this collection by removing all elements of
another collection.

* xs
  * the collection containing the removed elements.
* returns
  * a new collection that contains all elements of the current collection except
    one less occurrence of each of the elements of `elems` .
(defined at scala.collection.generic.Subtractable)
