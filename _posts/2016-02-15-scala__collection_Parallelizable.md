
#                       scala.collection.Parallelizable                       #

```scala
trait Parallelizable[+A, +ParRepr <: Parallel] extends Any
```

This trait describes collections which can be turned into parallel collections
by invoking the method `par` . Parallelizable collections may be parametrized
with a target type different than their own.

* A
  * the type of the elements in the collection
* ParRepr
  * the actual type of the collection, which has to be parallel

* Source
  * [Parallelizable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Parallelizable.scala#L1)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `abstract def parCombiner: Combiner[A, ParRepr]`                         ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]

(defined at scala.collection.Parallelizable)


### `abstract def seq: TraversableOnce[A]`                                   ###
(defined at scala.collection.Parallelizable)
