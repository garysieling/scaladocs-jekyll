
#                      scala.collection.generic.IsSeqLike                      #

```scala
trait IsSeqLike[Repr] extends AnyRef
```

Type class witnessing that a collection representation type `Repr` has elements
of type `A` and has a conversion to `SeqLike[A, Repr]` .

This type enables simple enrichment of `Seq` s with extension methods which can
make full use of the mechanics of the Scala collections framework in their
implementation.

Example usage:

```scala
class FilterMapImpl[A, Repr](val r: SeqLike[A, Repr]) {
  final def filterMap[B, That](f: A => Option[B])(implicit cbf: CanBuildFrom[Repr, B, That]): That =
    r.flatMap(f(_))
}
implicit def filterMap[Repr, A](r: Repr)(implicit fr: IsSeqLike[Repr]): FilterMapImpl[fr.A,Repr] =
  new FilterMapImpl(fr.conversion(r))

val l = List(1, 2, 3, 4, 5)
List(1, 2, 3, 4, 5) filterMap (i => if(i % 2 == 0) Some(i) else None)
// == List(2, 4)
```

* Source
  * [IsSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsSeqLike.scala#L1)
* See also
  * scala.collection.generic.IsTraversableLike scala.collection.Seq


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `abstract type A`                                                        ###

The type of elements we can traverse over.


--------------------------------------------------------------------------------
         Abstract Value Members From scala.collection.generic.IsSeqLike
--------------------------------------------------------------------------------


### `abstract val conversion: (Repr) ⇒ SeqLike[A, Repr]`                     ###

A conversion from the representation type `Repr` to a `SeqLike[A,Repr]` .
(defined at scala.collection.generic.IsSeqLike)
