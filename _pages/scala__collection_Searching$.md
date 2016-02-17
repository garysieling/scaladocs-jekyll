
#                          scala.collection.Searching                          #

```scala
object Searching
```

A collection of wrappers that provide sequence classes with search
functionality.

Example usage:

```scala
import scala.collection.Searching._
val l = List(1, 2, 3, 4, 5)
l.search(3)
// == Found(2)
```

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


--------------------------------------------------------------------------------
                                  Type Members
--------------------------------------------------------------------------------


### `case class Found(foundIndex: Int) extends SearchResult with Product with Serializable` ###

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


### `case class InsertionPoint(insertionPoint: Int) extends SearchResult with Product with Serializable` ###

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


### `class SearchImpl[A, Repr] extends AnyRef`                               ###

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


### `sealed abstract class SearchResult extends AnyRef`                      ###

* Source
  * [Searching.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/Searching.scala#L1)


--------------------------------------------------------------------------------
                 Value Members From scala.collection.Searching
--------------------------------------------------------------------------------


### `implicit def search[Repr, A](coll: Repr)(implicit fr: IsSeqLike[Repr]): SearchImpl[A, Repr]` ###
(defined at scala.collection.Searching)
