
#                   scala.collection.generic.CanCombineFrom                   #

```scala
trait CanCombineFrom[-From, -Elem, +To] extends CanBuildFrom[From, Elem, To] with Parallel
```

A base trait for parallel builder factories.

* From
  * the type of the underlying collection that requests a builder to be created.
* Elem
  * the element type of the collection to be created.
* To
  * the type of the collection to be created.

* Source
  * [CanCombineFrom.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/CanCombineFrom.scala#L1)
* Since
  * 2.8


--------------------------------------------------------------------------------
      Abstract Value Members From scala.collection.generic.CanCombineFrom
--------------------------------------------------------------------------------


### `abstract def apply(): Combiner[Elem, To]`                               ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* Definition Classes
  * CanCombineFrom → CanBuildFrom
* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.CanCombineFrom)


### `abstract def apply(from: From): Combiner[Elem, To]`                     ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .

* Definition Classes
  * CanCombineFrom → CanBuildFrom
(defined at scala.collection.generic.CanCombineFrom)
