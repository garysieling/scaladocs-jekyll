
#                    scala.collection.CustomParallelizable                    #

```scala
trait CustomParallelizable[+A, +ParRepr <: Parallel] extends Parallelizable[A, ParRepr]
```

* Source
  * [CustomParallelizable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/CustomParallelizable.scala#L1)


--------------------------------------------------------------------------------
       Concrete Value Members From scala.collection.CustomParallelizable
--------------------------------------------------------------------------------


### `def parCombiner: Combiner[A, ParRepr]`                                  ###

The default `par` implementation uses the combiner provided by this method to
create a new parallel collection.

* returns
  * a combiner for the parallel collection of type `ParRepr`

* Attributes
  * protected[this]
* Definition Classes
  * CustomParallelizable → Parallelizable

(defined at scala.collection.CustomParallelizable)


--------------------------------------------------------------------------------
          Abstract Value Members From scala.collection.Parallelizable
--------------------------------------------------------------------------------


### `abstract def seq: TraversableOnce[A]`                                   ###

* Definition Classes
  * Parallelizable
(defined at scala.collection.Parallelizable)
