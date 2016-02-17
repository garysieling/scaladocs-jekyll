
#                    scala.collection.generic.CanBuildFrom                    #

```scala
trait CanBuildFrom[-From, -Elem, +To] extends AnyRef
```

A base trait for builder factories.

* From
  * the type of the underlying collection that requests a builder to be created.
* Elem
  * the element type of the collection to be created.
* To
  * the type of the collection to be created.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [CanBuildFrom.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/CanBuildFrom.scala#L1)
* Since
  * 2.8
* See also
  * scala.collection.mutable.Builder


--------------------------------------------------------------------------------
       Abstract Value Members From scala.collection.generic.CanBuildFrom
--------------------------------------------------------------------------------


### `abstract def apply(): Builder[Elem, To]`                                ###

Creates a new builder from scratch.

* returns
  * a builder for collections of type `To` with element type `Elem` .

* See also
  * scala.collection.breakOut

(defined at scala.collection.generic.CanBuildFrom)


### `abstract def apply(from: From): Builder[Elem, To]`                      ###

Creates a new builder on request of a collection.

* from
  * the collection requesting the builder to be created.
* returns
  * a builder for collections of type `To` with element type `Elem` . The
    collections framework usually arranges things so that the created builder
    will build the same kind of collection as `from` .
(defined at scala.collection.generic.CanBuildFrom)
