
#                           scala.collection.generic                           #

```scala
package generic
```

* Source
  * [package.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/package.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `trait AtomicIndexFlag extends Signalling`                               ###

A mixin trait that implements index flag behaviour using atomic integers. The
 `setIndex` operation is wait-free, while conditional set operations
 `setIndexIfGreater` and `setIndexIfLesser` are lock-free and support only
monotonic changes.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `trait BitSetFactory[Coll <: BitSet with BitSetLike[Coll]] extends AnyRef` ###

* Source
  * [BitSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/BitSetFactory.scala#L1)


### `type CanBuild[-Elem, +To] = CanBuildFrom[Nothing, Elem, To]`            ###


### `trait CanBuildFrom[-From, -Elem, +To] extends AnyRef`                   ###

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


### `trait CanCombineFrom[-From, -Elem, +To] extends CanBuildFrom[From, Elem, To] with Parallel` ###

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


### `type ClassManifestTraversableFactory[CC[X] <: Traversable[X] with GenericClassManifestTraversableTemplate[X, CC]] = ClassTagTraversableFactory[CC]` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use ClassTagTraversableFactory instead


### `abstract class ClassTagTraversableFactory[CC[X] <: Traversable[X] with GenericClassTagTraversableTemplate[X, CC]] extends GenericClassTagCompanion[CC]` ###

A template for companion objects of `ClassTagTraversable` and subclasses
thereof.

* Source
  * [ClassTagTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ClassTagTraversableFactory.scala#L1)


### `trait Clearable extends AnyRef`                                         ###

This trait forms part of collections that can be cleared with a clear() call.

* Source
  * [Clearable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Clearable.scala#L1)
* Version
  * 2.10
* Since
  * 2.10


### `class DefaultSignalling extends Signalling with VolatileAbort`          ###

This signalling implementation returns default values and ignores received
signals.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `class DelegatedContext extends DelegatedSignalling`                     ###

Class implementing delegated signalling.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `trait DelegatedSignalling extends Signalling`                           ###

An implementation of the signalling interface using delegates.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `trait FilterMonadic[+A, +Repr] extends Any`                             ###

A template trait that contains just the `map` , `flatMap` , `foreach` and
 `withFilter` methods of trait `TraversableLike` .

* Source
  * [FilterMonadic.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/FilterMonadic.scala#L1)


### `abstract class GenMapFactory[CC[A, B] <: GenMap[A, B] with GenMapLike[A, B, CC[A, B]]] extends AnyRef` ###

A template for companion objects of `Map` and subclasses thereof.

* Source
  * [GenMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenMapFactory.scala#L1)


### `abstract class GenSeqFactory[CC[X] <: GenSeq[X] with GenericTraversableTemplate[X, CC]] extends GenTraversableFactory[CC]` ###

A template for companion objects of Seq and subclasses thereof.

* Source
  * [GenSeqFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenSeqFactory.scala#L1)
* Since
  * 2.8


### `abstract class GenSetFactory[CC[X] <: GenSet[X] with GenSetLike[X, CC[X]]] extends GenericCompanion[CC]` ###

A template for companion objects of `Set` and subclasses thereof.

* Source
  * [GenSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenSetFactory.scala#L1)


### `abstract class GenTraversableFactory[CC[X] <: GenTraversable[X] with GenericTraversableTemplate[X, CC]] extends GenericCompanion[CC]` ###

A template for companion objects of `Traversable` and subclasses thereof. This
class provides a set of operations to create `Traversable` objects. It is
typically inherited by companion objects of subclasses of `Traversable` .

* Source
  * [GenTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenTraversableFactory.scala#L1)
* Since
  * 2.8


### `type GenericClassManifestCompanion[+CC[X] <: Traversable[X]] = GenericClassTagCompanion[CC]` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use GenericClassTagCompanion instead


### `type GenericClassManifestTraversableTemplate[+A, +CC[X] <: Traversable[X]] = GenericClassTagTraversableTemplate[A, CC]` ###

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.10.0)_ use GenericClassTagTraversableTemplate instead


### `abstract class GenericClassTagCompanion[+CC[X] <: Traversable[X]] extends AnyRef` ###

This class represents companions of classes which require ClassTags for their
element types.

* Source
  * [GenericClassTagCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericClassTagCompanion.scala#L1)


### `trait GenericClassTagTraversableTemplate[+A, +CC[X] <: Traversable[X]] extends HasNewBuilder[A, CC[A]]` ###

This trait represents collections classes which require class tags for their
element types.

* Source
  * [GenericClassTagTraversableTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericClassTagTraversableTemplate.scala#L1)
* Since
  * 2.8


### `abstract class GenericCompanion[+CC[X] <: GenTraversable[X]] extends AnyRef` ###

A template class for companion objects of "regular" collection classes represent
an unconstrained higher-kinded type. Typically such classes inherit from trait
 `GenericTraversableTemplate` .

* CC
  * The type constructor representing the collection class.

* Source
  * [GenericCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericCompanion.scala#L1)
* Since
  * 2.8
* See also
  * scala.collection.generic.GenericTraversableTemplate


### `abstract class GenericOrderedCompanion[+CC[X] <: Traversable[X]] extends AnyRef` ###

This class represents companions of classes which require the ordered trait for
their element types.

* Source
  * [GenericOrderedCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericOrderedCompanion.scala#L1)
* Since
  * 2.8


### `trait GenericOrderedTraversableTemplate[+A, +CC[X] <: Traversable[X]] extends HasNewBuilder[A, CC[A]]` ###

This trait represents collections classes which require ordered element types.

* Source
  * [GenericOrderedTraversableTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericOrderedTraversableTemplate.scala#L1)


### `trait GenericParCompanion[+CC[X] <: ParIterable[X]] extends AnyRef`     ###

A template class for companion objects of parallel collection classes. They
should be mixed in together with `GenericCompanion` type.

* Source
  * [GenericParCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParCompanion.scala#L1)


### `trait GenericParMapCompanion[+CC[P, Q] <: ParMap[P, Q]] extends AnyRef` ###

* Source
  * [GenericParCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParCompanion.scala#L1)


### `trait GenericParMapTemplate[K, +V, +CC[X, Y] <: ParMap[X, Y]] extends GenericParTemplate[(K, V), ParIterable]` ###

* Source
  * [GenericParTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParTemplate.scala#L1)


### `trait GenericParTemplate[+A, +CC[X] <: ParIterable[X]] extends GenericTraversableTemplate[A, CC] with HasNewCombiner[A, CC[A]]` ###

A template trait for collections having a companion.

* A
  * the element type of the collection
* CC
  * the type constructor representing the collection class

* Source
  * [GenericParTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericParTemplate.scala#L1)
* Since
  * 2.8


### `trait GenericSeqCompanion[CC[X] <: Traversable[X]] extends GenericCompanion[CC]` ###

* Source
  * [GenericSeqCompanion.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericSeqCompanion.scala#L1)


### `trait GenericSetTemplate[A, +CC[X] <: GenSet[X]] extends GenericTraversableTemplate[A, CC]` ###

* Source
  * [GenericSetTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericSetTemplate.scala#L1)
* Since
  * 2.8


### `trait GenericTraversableTemplate[+A, +CC[X] <: GenTraversable[X]] extends HasNewBuilder[A, CC[A]]` ###

A template class for companion objects of `regular` collection classes that
represent an unconstrained higher-kinded type.

* A
  * The type of the collection elements.
* CC
  * The type constructor representing the collection class.

* Source
  * [GenericTraversableTemplate.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/GenericTraversableTemplate.scala#L1)
* Since
  * 2.8


### `trait Growable[-A] extends Clearable`                                   ###

This trait forms part of collections that can be augmented using a `+=` operator
and that can be cleared of all elements using a `clear` method.

* Source
  * [Growable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Growable.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait HasNewBuilder[+A, +Repr] extends Any`                             ###

* Source
  * [HasNewBuilder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/HasNewBuilder.scala#L1)


### `trait HasNewCombiner[+T, +Repr] extends AnyRef`                         ###

* Source
  * [HasNewCombiner.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/HasNewCombiner.scala#L1)
* Since
  * 2.8


### `abstract class ImmutableMapFactory[CC[A, +B] <: immutable.Map[A, B] with immutable.MapLike[A, B, CC[A, B]]] extends MapFactory[CC]` ###

A template for companion objects of `immutable.Map` and subclasses thereof.

* Source
  * [ImmutableMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableMapFactory.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `abstract class ImmutableSetFactory[CC[X] <: immutable.Set[X] with SetLike[X, CC[X]]] extends SetFactory[CC]` ###

* Source
  * [ImmutableSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSetFactory.scala#L1)


### `abstract class ImmutableSortedMapFactory[CC[A, B] <: immutable.SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends SortedMapFactory[CC]` ###

A template for companion objects of `SortedMap` and subclasses thereof.

* Source
  * [ImmutableSortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSortedMapFactory.scala#L1)
* Since
  * 2.8


### `abstract class ImmutableSortedSetFactory[CC[A] <: immutable.SortedSet[A] with SortedSetLike[A, CC[A]]] extends SortedSetFactory[CC]` ###

A template for companion objects of `SortedSet` and subclasses thereof.

* Source
  * [ImmutableSortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ImmutableSortedSetFactory.scala#L1)
* Since
  * 2.8


### `abstract class IndexedSeqFactory[CC[X] <: IndexedSeq[X] with GenericTraversableTemplate[X, CC]] extends SeqFactory[CC]` ###

A template for companion objects of IndexedSeq and subclasses thereof.

* Source
  * [IndexedSeqFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IndexedSeqFactory.scala#L1)
* Since
  * 2.11


### `trait IsSeqLike[Repr] extends AnyRef`                                   ###

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


### `trait IsTraversableLike[Repr] extends AnyRef`                           ###

A trait which can be used to avoid code duplication when defining extension
methods that should be applicable both to existing Scala collections (i.e.,
types extending `GenTraversableLike` ) as well as other (potentially
user-defined) types that could be converted to a Scala collection type. This
trait makes it possible to treat Scala collections and types that can be
implicitly converted to a collection type uniformly. For example, one can
provide extension methods that work both on collection types and on `String` s (
 `String` s do not extend `GenTraversableLike` , but can be converted to
 `GenTraversableLike` )

 `IsTraversable` provides two members:

1. type member `A` , which represents the element type of the target
    `GenTraversableLike[A, Repr]`
2. value member `conversion` , which provides a way to convert between the type
   we wish to add extension methods to, `Repr` , and
    `GenTraversableLike[A, Repr]` .

### Usage

One must provide `IsTraversableLike` as an implicit parameter type of an
implicit conversion. Its usage is shown below. Our objective in the following
example is to provide a generic extension method `mapReduce` to any type that
extends or can be converted to `GenTraversableLike` . In our example, this
includes `String` .

```scala
import scala.collection.GenTraversableLike
  import scala.collection.generic.IsTraversableLike

  class ExtensionMethods[A, Repr](coll: GenTraversableLike[A, Repr]) {
    def mapReduce[B](mapper: A => B)(reducer: (B, B) => B): B = {
      val iter = coll.toIterator
      var res = mapper(iter.next())
      while (iter.hasNext)
        res = reducer(res, mapper(iter.next()))
      res
    }
  }

  implicit def withExtensions[Repr](coll: Repr)(implicit traversable: IsTraversableLike[Repr]) =
    new ExtensionMethods(traversable.conversion(coll))

// See it in action!
List(1, 2, 3).mapReduce(_ * 2)(_ + _) // res0: Int = 12
"Yeah, well, you know, that's just, like, your opinion, man.".mapReduce(x => 1)(_ + _) // res1: Int = 59
```

Here, we begin by creating a class `ExtensionMethods` which contains our
 `mapReduce` extension method. Note that `ExtensionMethods` takes a constructor
argument `coll` of type `GenTraversableLike[A, Repr]` , where `A` represents the
element type and `Repr` represents (typically) the collection type. The
implementation of `mapReduce` itself is straightforward.

The interesting bit is the implicit conversion `withExtensions` , which returns
an instance of `ExtensionMethods` . This implicit conversion can only be applied
if there is an implicit value `traversable` of type `IsTraversableLike[Repr]` in
scope. Since `IsTraversableLike` provides value member `conversion` , which
gives us a way to convert between whatever type we wish to add an extension
method to (in this case, `Repr` ) and `GenTraversableLike[A, Repr]` , we can now
convert `coll` from type `Repr` to `GenTraversableLike[A, Repr]` . This allows
us to create an instance of the `ExtensionMethods` class, which we pass our new
 `GenTraversableLike[A, Repr]` to.

When the `mapReduce` method is called on some type of which it is not a member,
implicit search is triggered. Because implicit conversion `withExtensions` is
generic, it will be applied as long as an implicit value of type
 `IsTraversableLike[Repr]` can be found. Given that `IsTraversableLike` contains
implicit members that return values of type `IsTraversableLike` , this
requirement is typically satisfied, and the chain of interactions described in
the previous paragraph is set into action. (See the `IsTraversableLike`
companion object, which contains a precise specification of the available
implicits.)

 _Note_ : Currently, it's not possible to combine the implicit conversion and
the class with the extension methods into an implicit class due to limitations
of type inference.

### Implementing `IsTraversableLike` for New Types

One must simply provide an implicit value of type `IsTraversableLike` specific
to the new type, or an implicit conversion which returns an instance of
 `IsTraversableLike` specific to the new type.

Below is an example of an implementation of the `IsTraversableLike` trait where
the `Repr` type is `String` .

```scala
implicit val stringRepr: IsTraversableLike[String] { type A = Char } =
  new IsTraversableLike[String] {
    type A = Char
    val conversion = implicitly[String => GenTraversableLike[Char, String]]
  }
```

* Source
  * [IsTraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableLike.scala#L1)
* Since
  * 2.10


### `trait IsTraversableOnce[Repr] extends AnyRef`                           ###

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


### `trait IterableForwarder[+A] extends Iterable[A] with TraversableForwarder[A]` ###

This trait implements a forwarder for iterable objects. It forwards all calls to
a different iterable object, except for

*  `toString` , `hashCode` , `equals` , `stringPrefix`
*  `newBuilder` , `view`
* all calls creating a new iterable object of the same kind

The above methods are forwarded by subclass `IterableProxy`.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Forwarding is inherently unreliable since it is not
    automated and methods can be forgotten.
* Source
  * [IterableForwarder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IterableForwarder.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `abstract class MapFactory[CC[A, B] <: Map[A, B] with MapLike[A, B, CC[A, B]]] extends GenMapFactory[CC]` ###

A template for companion objects of `Map` and subclasses thereof.

* Source
  * [MapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MapFactory.scala#L1)


### `abstract class MutableMapFactory[CC[A, B] <: mutable.Map[A, B] with mutable.MapLike[A, B, CC[A, B]]] extends MapFactory[CC]` ###

A template for companion objects of `mutable.Map` and subclasses thereof.

* Source
  * [MutableMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableMapFactory.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `abstract class MutableSetFactory[CC[X] <: mutable.Set[X] with mutable.SetLike[X, CC[X]]] extends SetFactory[CC]` ###

* Source
  * [MutableSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableSetFactory.scala#L1)


### `abstract class MutableSortedMapFactory[CC[A, B] <: mutable.SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends SortedMapFactory[CC]` ###

A template for companion objects of `SortedMap` and subclasses thereof.

* CC
  * the type of the collection.

* Source
  * [MutableSortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableSortedMapFactory.scala#L1)
* Version
  * 2.12
* Since
  * 2.12


### `abstract class MutableSortedSetFactory[CC[A] <: mutable.SortedSet[A] with SortedSetLike[A, CC[A]] with mutable.Set[A] with mutable.SetLike[A, CC[A]]] extends SortedSetFactory[CC]` ###

* Source
  * [MutableSortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/MutableSortedSetFactory.scala#L1)


### `abstract class OrderedTraversableFactory[CC[X] <: Traversable[X] with GenericOrderedTraversableTemplate[X, CC]] extends GenericOrderedCompanion[CC]` ###

* Source
  * [OrderedTraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/OrderedTraversableFactory.scala#L1)


### `abstract class ParFactory[CC[X] <: ParIterable[X] with GenericParTemplate[X, CC]] extends GenTraversableFactory[CC] with GenericParCompanion[CC]` ###

A template class for companion objects of `ParIterable` and subclasses thereof.
This class extends `TraversableFactory` and provides a set of operations to
create `ParIterable` objects.

* Source
  * [ParFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParFactory.scala#L1)


### `abstract class ParMapFactory[CC[X, Y] <: ParMap[X, Y] with ParMapLike[X, Y, CC[X, Y], _]] extends GenMapFactory[CC] with GenericParMapCompanion[CC]` ###

A template class for companion objects of `ParMap` and subclasses thereof. This
class extends `TraversableFactory` and provides a set of operations to create
 `ParMap` objects.

* Source
  * [ParMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParMapFactory.scala#L1)


### `abstract class ParSetFactory[CC[X] <: ParSet[X] with ParSetLike[X, CC[X], _] with GenericParTemplate[X, CC]] extends GenSetFactory[CC] with GenericParCompanion[CC]` ###

* Source
  * [ParSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/ParSetFactory.scala#L1)
* Since
  * 2.8


### `abstract class SeqFactory[CC[X] <: Seq[X] with GenericTraversableTemplate[X, CC]] extends GenSeqFactory[CC] with TraversableFactory[CC]` ###

A template for companion objects of Seq and subclasses thereof.

* Source
  * [SeqFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SeqFactory.scala#L1)
* Since
  * 2.8


### `trait SeqForwarder[+A] extends Seq[A] with IterableForwarder[A]`        ###

This class implements a forwarder for sequences. It forwards all calls to a
different sequence object except for

*  `toString` , `hashCode` , `equals` , `stringPrefix`
*  `newBuilder` , `view` , `toSeq`
* all calls creating a new sequence of the same kind

The above methods are forwarded by subclass `SeqProxy` .

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Forwarding is inherently unreliable since it is not
    automated and new methods can be forgotten.
* Source
  * [SeqForwarder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SeqForwarder.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `abstract class SetFactory[CC[X] <: Set[X] with SetLike[X, CC[X]]] extends GenSetFactory[CC] with GenericSeqCompanion[CC]` ###

* Source
  * [SetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SetFactory.scala#L1)


### `trait Shrinkable[-A] extends AnyRef`                                    ###

This trait forms part of collections that can be reduced using a `-=` operator.

* Source
  * [Shrinkable.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Shrinkable.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait Signalling extends AnyRef`                                        ###

A message interface serves as a unique interface to the part of the collection
capable of receiving messages from a different task.

One example of use of this is the `find` method, which can use the signalling
interface to inform worker threads that an element has been found and no further
search is necessary.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `trait Sizing extends AnyRef`                                            ###

A trait for objects which have a size.

* Source
  * [Sizing.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Sizing.scala#L1)


### `trait Sorted[K, +This <: Sorted[K, This]] extends AnyRef`               ###

Any collection (including maps) whose keys (or elements) are ordered.

* Source
  * [Sorted.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Sorted.scala#L1)
* Since
  * 2.8


### `abstract class SortedMapFactory[CC[A, B] <: SortedMap[A, B] with SortedMapLike[A, B, CC[A, B]]] extends AnyRef` ###

A template for companion objects of mutable.Map and subclasses thereof.

* Source
  * [SortedMapFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedMapFactory.scala#L1)
* Since
  * 2.8


### `abstract class SortedSetFactory[CC[A] <: SortedSet[A] with SortedSetLike[A, CC[A]]] extends AnyRef` ###

A template for companion objects of Set and subclasses thereof.

* Source
  * [SortedSetFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SortedSetFactory.scala#L1)
* Since
  * 2.8


### `trait Subtractable[A, +Repr <: Subtractable[A, Repr]] extends AnyRef`   ###

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


### `class TaggedDelegatedContext extends DelegatedContext`                  ###

Class implementing delegated signalling, but having its own distinct `tag` .

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `trait TraversableFactory[CC[X] <: Traversable[X] with GenericTraversableTemplate[X, CC]] extends GenTraversableFactory[CC] with GenericSeqCompanion[CC]` ###

A template for companion objects of `Traversable` and subclasses thereof. This
class provides a set of operations to create `Traversable` objects. It is
typically inherited by companion objects of subclasses of `Traversable` .

* Source
  * [TraversableFactory.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/TraversableFactory.scala#L1)
* Since
  * 2.8


### `trait TraversableForwarder[+A] extends Traversable[A]`                  ###

This trait implements a forwarder for traversable objects. It forwards all calls
to a different traversable, except for:

*  `toString` , `hashCode` , `equals` , `stringPrefix`
*  `newBuilder` , `view`

All calls creating a new traversable of the same kind.

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.0)_ Forwarding is inherently unreliable since it is not
    automated and new methods can be forgotten.
* Source
  * [TraversableForwarder.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/TraversableForwarder.scala#L1)
* Version
  * 2.8
* Since
  * 2.8


### `trait VolatileAbort extends Signalling`                                 ###

A mixin trait that implements abort flag behaviour using volatile variables.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


--------------------------------------------------------------------------------
                                 Value Members
--------------------------------------------------------------------------------


### `object IdleSignalling extends DefaultSignalling`                        ###

An object that returns default values and ignores received signals.

* Source
  * [Signalling.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/Signalling.scala#L1)


### `object IsSeqLike`                                                       ###

* Source
  * [IsSeqLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsSeqLike.scala#L1)


### `object IsTraversableLike`                                               ###

* Source
  * [IsTraversableLike.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableLike.scala#L1)


### `object IsTraversableOnce`                                               ###

* Source
  * [IsTraversableOnce.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/IsTraversableOnce.scala#L1)


### `object SliceInterval`                                                   ###

* Source
  * [SliceInterval.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/generic/SliceInterval.scala#L1)

