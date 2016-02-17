
#                     scala.collection.immutable.PagedSeq                     #

```scala
object PagedSeq
```

The `PagedSeq` object defines a lazy implementations of a random access
sequence.

Provides utility methods that return instances of `PagedSeq[Char]` .
 `fromIterator` and `fromIterable` provide generalised instances of `PagedSeq`

* Annotations
  * @ deprecated
* Deprecated
  * _(Since version 2.11.8)_ This object will be moved to the
    scala-parser-combinators module
* Source
  * [PagedSeq.scala](https://github.com/scala/scala/tree/6d09a1ba5f/src/library/scala/collection/immutable/PagedSeq.scala#L1)
* Since
  * 2.7


--------------------------------------------------------------------------------
             Value Members From scala.collection.immutable.PagedSeq
--------------------------------------------------------------------------------


### `def fromFile(source: File): PagedSeq[Char]`                             ###

Constructs a paged character sequence from an input file

(defined at scala.collection.immutable.PagedSeq)


### `def fromFile(source: String): PagedSeq[Char]`                           ###

Constructs a paged character sequence from a file with given name

(defined at scala.collection.immutable.PagedSeq)


### `def fromIterable[T](source: Iterable[T])(implicit arg0: ClassTag[T]): PagedSeq[T]` ###

Constructs a paged sequence from an iterable

(defined at scala.collection.immutable.PagedSeq)


### `def fromIterator[T](source: Iterator[T])(implicit arg0: ClassTag[T]): PagedSeq[T]` ###

Constructs a paged sequence from an iterator

(defined at scala.collection.immutable.PagedSeq)


### `def fromLines(source: Iterable[String]): PagedSeq[Char]`                ###

Constructs a paged character sequence from a line iterable Lines do not contain
trailing `\n` characters; The method inserts a line separator `\n` between any
two lines in the sequence.

(defined at scala.collection.immutable.PagedSeq)


### `def fromLines(source: Iterator[String]): PagedSeq[Char]`                ###

Constructs a paged character sequence from a line iterator Lines do not contain
trailing `\n` characters; The method inserts a line separator `\n` between any
two lines in the sequence.

(defined at scala.collection.immutable.PagedSeq)


### `def fromReader(source: Reader): PagedSeq[Char]`                         ###

Constructs a paged character sequence from an input reader

(defined at scala.collection.immutable.PagedSeq)


### `def fromSource(source: Source): PagedSeq[Char]`                         ###

Constructs a paged character sequence from a scala.io.Source value

(defined at scala.collection.immutable.PagedSeq)


### `def fromStrings(source: Iterable[String]): PagedSeq[Char]`              ###

Constructs a paged character sequence from a string iterable

(defined at scala.collection.immutable.PagedSeq)


### `def fromStrings(source: Iterator[String]): PagedSeq[Char]`              ###

Constructs a paged character sequence from a string iterator
(defined at scala.collection.immutable.PagedSeq)
