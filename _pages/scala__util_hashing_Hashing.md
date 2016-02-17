
#                          scala.util.hashing.Hashing                          #

```scala
trait Hashing[T] extends Serializable
```

 `Hashing` is a trait whose instances each represent a strategy for hashing
instances of a type.

 `Hashing` 's companion object defines a default hashing strategy for all
objects - it calls their `##` method.

Note: when using a custom `Hashing` , make sure to use it with the `Equiv` such
that if any two objects are equal, then their hash codes must be equal.

* Annotations
  * @ implicitNotFound (msg =...)
* Source
  * [Hashing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/util/hashing/Hashing.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
             Abstract Value Members From scala.util.hashing.Hashing
--------------------------------------------------------------------------------


### `abstract def hash(x: T): Int`                                           ###
(defined at scala.util.hashing.Hashing)
