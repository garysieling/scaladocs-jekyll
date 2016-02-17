
#                  scala.collection.generic.IsTraversableOnce                  #

```scala
trait IsTraversableOnce[Repr] extends AnyRef
```

Type class witnessing that a collection representation type `Repr` has elements
of type `A` and has a conversion to `GenTraversableOnce[A]` .

This type enables simple enrichment of `GenTraversableOnce` s with extension
methods which can make full use of the mechanics of the Scala collections
framework in their implementation.

Example usage,

```scala
class FilterMapImpl[A, Repr](val r: GenTraversableOnce[A]) {
  final def filterMap[B, That](f: A => Option[B])(implicit cbf: CanBuildFrom[Repr, B, That]): That = {
    val b = cbf()
    for(e <- r.seq) f(e) foreach (b +=)
    b.result
  }
}
implicit def filterMap[Repr, A](r: Repr)(implicit fr: IsTraversableOnce[Repr]): FilterMapImpl[fr.A,Repr] =
  new FilterMapImpl[fr.A, Repr](fr.conversion(r))

val l = List(1, 2, 3, 4, 5)
List(1, 2, 3, 4, 5) filterMap (i => if(i % 2 == 0) Some(i) else None)
// == List(2, 4)
```

* Source
  * [IsTraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableOnce.scala#L1)
* Since
  * 2.10


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract type A`                                                        ###

The type of elements we can traverse over.


--------------------------------------------------------------------------------
     Abstract Value Members From scala.collection.generic.IsTraversableOnce
--------------------------------------------------------------------------------


### `abstract val conversion: (Repr) ⇒ GenTraversableOnce[A]`                ###

A conversion from the representation type `Repr` to a `GenTraversableOnce[A]` .
(defined at scala.collection.generic.IsTraversableOnce)
